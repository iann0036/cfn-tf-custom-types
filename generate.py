import requests
import subprocess
import os
import pprint
import json
import re
import tempfile
import time
import sys, traceback
from pathlib import Path


CASE_MAP = {
    'oci': ['OCI','Oracle Cloud Infrastructure'],
    'aws': ['AWS','AWS'],
    'opsgenie': ['OpsGenie','OpsGenie'],
    'dnsimple': ['DNSimple','DNSimple'],
    'vsphere': ['VSphere','VMware vSphere'],
    'consul': ['Consul','Consul'],
    'cloudstack': ['CloudStack','CloudStack'],
    'tls': ['TLS','TLS'],
    'cobbler': ['Cobbler','Cobbler'],
    'azurerm': ['AzureRM','Azure'],
    'nomad': ['Nomad','Nomad'],
    'ovh': ['OVH','OVH'],
    'scaleway': ['Scaleway','Scaleway'],
    'bitbucket': ['Bitbucket','Bitbucket'],
    'logentries': ['Logentries','Logentries'],
    'datadog': ['Datadog','Datadog'],
    'pagerduty': ['PagerDuty','PagerDuty'],
    'oneandone': ['OneAndOne','1&1'],
    'chef': ['Chef','Chef'],
    'ultradns': ['UltraDNS','UltraDNS'],
    'profitbricks': ['ProfitBricks','ProfitBricks'],
    'postgresql': ['PostgreSQL','PostgreSQL'],
    'google': ['Google','Google Cloud'],
    'dme': ['DME','DNSMadeEasy'],
    'triton': ['Triton','Triton'],
    'circonus': ['Circonus','Circonus'],
    'dyn': ['Dyn','Dyn'],
    'mailgun': ['Mailgun','Mailgun'],
    'influxdb': ['InfluxDB','InfluxDB'],
    'alicloud': ['Alicloud','Alicloud'],
    'rundeck': ['Rundeck','Rundeck'],
    'grafana': ['Grafana','Grafana'],
    'rabbitmq': ['RabbitMQ','RabbitMQ'],
    'digitalocean': ['DigitalOcean','DigitalOcean'],
    'arukas': ['Arukas','Arukas'],
    'vcd': ['VCD','VMware vCloud Director'],
    'powerdns': ['PowerDNS','PowerDNS'],
    'atlas': ['Atlas','Atlas'],
    'dns': ['DNS','DNS'],
    'newrelic': ['NewRelic','NewRelic'],
    'github': ['GitHub','GitHub'],
    'librato': ['Librato','Librato'],
    'openstack': ['OpenStack','OpenStack'],
    'heroku': ['Heroku','Heroku'],
    'packet': ['Packet','Packet'],
    'clc': ['CLC','CenturyLinkCloud'],
    'template': ['Template','Template'],
    'icinga2': ['Icinga2','Icinga2'],
    'softlayer': ['SoftLayer','SoftLayer'],
    'spotinst': ['Spotinst','Spotinst'],
    'cloudflare': ['Cloudflare','Cloudflare'],
    'mysql': ['MySQL','MySQL'],
    'kubernetes': ['Kubernetes','Kubernetes'],
    'opc': ['OPC','Oracle Public Cloud'],
    'vault': ['Vault','Vault'],
    'gitlab': ['Gitlab','Gitlab'],
    'statuscake': ['StatusCake','StatusCake'],
    'random': ['Random','Random'],
    'local': ['Local','Local'],
    'ns1': ['NS1','NS1'],
    'fastly': ['Fastly','Fastly'],
    'docker': ['Docker','Docker'],
    'rancher': ['Rancher','Rancher'],
    'logicmonitor': ['LogicMonitor','LogicMonitor'],
    'cloudscale': ['CloudScale','CloudScale'],
    'netlify': ['Netlify','Netlify'],
    'opentelekomcloud': ['OpenTelekomCloud','OpenTelekomCloud'],
    'panos': ['Panos','Palo Alto Networks'],
    'oraclepaas': ['OraclePaaS','Oracle Cloud Platform'],
    'nsxt': ['NSXT','VMware NSX-T'],
    'runscope': ['RunScope','RunScope'],
    'flexibleengine': ['FlexibleEngine','FlexibleEngine'],
    'hcloud': ['HCloud','Hetzner Cloud'],
    'azurestack': ['AzureStack','Azure Stack'],
    'telefonicaopencloud': ['TelefonicaOpenCloud','TelefonicaOpenCloud'],
    'huaweicloud': ['HuaweiCloud','HuaweiCloud'],
    'brightbox': ['Brightbox','Brightbox'],
    'tfe': ['Tfe','Terraform Enterprise'],
    'acme': ['ACME','ACME'],
    'rightscale': ['RightScale','RightScale'],
    'bigip': ['BIGIP','F5 BIG-IP'],
    'tencentcloud': ['TencentCloud','TencentCloud'],
    'nutanix': ['Nutanix','Nutanix'],
    'linode': ['Linode','Linode'],
    'selvpc': ['SelVPC','Selectel'],
    'skytap': ['Skytap','Skytap'],
    'hedvig': ['Hedvig','Hedvig'],
    'ucloud': ['UCloud','UCloud'],
    'azuread': ['AzureAD','Azure Active Directory']
}

PROVIDER_TYPE = sys.argv[1]

def tf_to_cfn_str(obj):
    return re.sub(r'(?:^|_)(\w)', lambda x: x.group(1).upper(), obj)

def check_call(args, cwd, inputstr):
    proc = subprocess.Popen(args,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=cwd)
    if inputstr:
        proc.stdin.write(inputstr)
    stdout, stderr = proc.communicate()
    if proc.returncode != 0:
        raise subprocess.CalledProcessError(
            returncode=proc.returncode,
            cmd=args)
    
    return stdout

def jsonschema_type(attrtype):
    if attrtype == "string":
        return {
            'type': 'string'
        }
    elif attrtype == "number":
        return {
            'type': 'number'
        }
    elif attrtype == "bool":
        return {
            'type': 'boolean'
        }
    elif len(attrtype) == 2 and attrtype[0] == "list":
        return {
            'type': 'array',
            'insertionOrder': False,
            'items': jsonschema_type(attrtype[1])
        }
    elif len(attrtype) == 2 and attrtype[0] == "set":
        return {
            'type': 'array',
            'insertionOrder': True,
            'items': jsonschema_type(attrtype[1])
        }
    elif len(attrtype) == 2 and attrtype[0] == "object":
        properties = {}
        for k,v in attrtype[1].items():
            cfnattrname = tf_to_cfn_str(k)
            properties[cfnattrname] = jsonschema_type(v)

        return {
            'type': 'object',
            'additionalProperties': False,
            'properties': properties
        }
    elif len(attrtype) == 2 and attrtype[0] == "map":
        return {
            'type': 'array',
            'insertionOrder': True,
            'items': {
                'type': 'object',
                'additionalProperties': False,
                'properties': {
                    'Key': {
                        'type': 'string'
                    },
                    'Value': jsonschema_type(attrtype[1])
                },
                'required': [
                    'Key',
                    'Value'
                ]
            }
        } # TODO: Reverse this in the Lambda
    else:
        print("ERROR: Unknown attribute type")
        print(attrtype)
        return {
            'type': 'string'
        }

def checkout(url, provider_name):
    try:
        check_call(['git', 'clone', url, '/tmp/' + provider_name + '/'], '/tmp', None)
    except:
        check_call(['git', 'pull', url], '/tmp/' + provider_name, None)

tmpdir = tempfile.TemporaryDirectory()
tempdir = Path(tmpdir.name)

with open(tempdir / "base.tf", "w") as f:
    f.write('''
provider "{provider}" {{}}
    '''.format(provider=PROVIDER_TYPE))

print("Downloading latest provider version...")
check_call(['terraform', 'init'], tempdir.absolute(), None)
tfschema = json.loads(check_call(['terraform', 'providers', 'schema', '-json'], tempdir.absolute(), None))

outstandingblocks = {}
schema = {}

for k,v in tfschema['provider_schemas'][PROVIDER_TYPE]['resource_schemas'].items():
    endnaming = tf_to_cfn_str(k)
    if k.startswith(PROVIDER_TYPE + "_"):
        endnaming = tf_to_cfn_str(k[(len(PROVIDER_TYPE)+1):])
    
    cfntypename = "Terraform::" + CASE_MAP[PROVIDER_TYPE][0] + "::" + endnaming
    cfndirname = "Terraform-" + CASE_MAP[PROVIDER_TYPE][0] + "-" + endnaming

    try:
        providerdir = Path('.') / 'resources' / PROVIDER_TYPE / cfndirname

        if not providerdir.exists():
            providerdir.mkdir(parents=True, exist_ok=True)
            check_call(['cfn', 'init'], providerdir.absolute(), "{}\n4\nY\n".format(cfntypename).encode('utf-8'))

        schema = {
            "typeName": cfntypename,
            "description": "CloudFormation equivalent of {}".format(k),
            "sourceUrl": "https://github.com/iann0036/cfn-tf-custom-types.git",
            "definitions": {},
            "properties": {
                "tfcfnid": {
                    "description": "Internal identifier for tracking resource changes. Do not use.",
                    "type": "string"
                }
            },
            "additionalProperties": False,
            "required": [],
            "readOnlyProperties": [
                "/properties/tfcfnid"
            ],
            "primaryIdentifier": [
                "/properties/tfcfnid"
            ],
            "handlers": {
                "create": {
                    "permissions": [
                        "s3:PutObject",
                        "secretsmanager:GetSecretValue"
                    ]
                },
                "read": {
                    "permissions": []
                },
                "update": {
                    "permissions": [
                        "s3:GetObject",
                        "s3:PutObject",
                        "secretsmanager:GetSecretValue"
                    ]
                },
                "delete": {
                    "permissions": [
                        "s3:GetObject",
                        "s3:DeleteObject",
                        "secretsmanager:GetSecretValue"
                    ]
                },
                "list": {
                    "permissions": []
                }
            }
        }

        if PROVIDER_TYPE == "aws":
            schema['handlers'] = {
                "create": {"permissions": ["*"]},
                "read": {"permissions": ["*"]},
                "update": {"permissions": ["*"]},
                "delete": {"permissions": ["*"]},
                "list": {"permissions": ["*"]}
            }

        if 'attributes' in v['block']:
            for attrname,attr in v['block']['attributes'].items():
                cfnattrname = tf_to_cfn_str(attrname)
                attrtype = attr['type']

                computed = False
                optional = None
                if 'optional' in attr:
                    if not attr['optional']:
                        schema['required'].append(cfnattrname)
                        optional = False
                    else:
                        optional = True
                elif 'required' in attr:
                    if attr['required']:
                        schema['required'].append(cfnattrname)
                if 'computed' in attr:
                    if attr['computed']:
                        computed = True
                        if not optional:
                            schema['readOnlyProperties'].append("/properties/" + cfnattrname)

                schema['properties'][cfnattrname] = jsonschema_type(attrtype)

        if 'block_types' in v['block']:
            outstandingblocks.update(v['block']['block_types'])
        
        while len(outstandingblocks):
            blockname = next(iter(outstandingblocks))
            block = outstandingblocks.pop(blockname)
            cfnblockname = tf_to_cfn_str(blockname)

            schema['definitions'][cfnblockname] = {
                'type': 'object',
                'additionalProperties': False,
                'properties': {},
                'required': []
            }

            if 'attributes' in block['block']:
                for attrname,attr in block['block']['attributes'].items():
                    cfnattrname = tf_to_cfn_str(attrname)
                    attrtype = attr['type']

                    computed = False
                    optional = None
                    if 'optional' in attr:
                        if not attr['optional']:
                            schema['definitions'][cfnblockname]['required'].append(cfnattrname)
                            optional = False
                        else:
                            optional = True
                    elif 'required' in attr:
                        if attr['required']:
                            schema['definitions'][cfnblockname]['required'].append(cfnattrname)
                    if 'computed' in attr:
                        if attr['computed']:
                            computed = True
                            if not optional:
                                continue # read-only props in subdefs are skipped from model

                    schema['definitions'][cfnblockname]['properties'][cfnattrname] = jsonschema_type(attrtype)
            
            if 'block_types' in block['block']:
                outstandingblocks.update(block['block']['block_types'])
                for subblockname,subblock in block['block']['block_types'].items():
                    cfnsubblockname = tf_to_cfn_str(subblockname)
                    if subblock['nesting_mode'] == "list":
                        schema['definitions'][cfnblockname]['properties'][cfnsubblockname] = {
                            'type': 'array',
                            'insertionOrder': True,
                            'items': {
                                '$ref': '#/definitions/' + cfnsubblockname
                            }
                        }
                    elif subblock['nesting_mode'] == "set":
                        schema['definitions'][cfnblockname]['properties'][cfnsubblockname] = {
                            'type': 'array',
                            'insertionOrder': False,
                            'items': {
                                '$ref': '#/definitions/' + cfnsubblockname
                            }
                        }
                    elif subblock['nesting_mode'] == "single":
                        schema['definitions'][cfnblockname]['properties'][cfnsubblockname] = {
                            '$ref': '#/definitions/' + cfnsubblockname
                        }
                    else:
                        print("Unknown subblock nesting_mode: " + subblock['nesting_mode'])

            if not bool(schema['definitions'][cfnblockname]['properties']):
                if bool(block['block']):
                    del schema['definitions'][cfnblockname] # no properties found
                    print("Skipped propertyless block: " + cfnblockname)
                    continue
                else:
                    schema['definitions'][cfnblockname]['properties']['IsPropertyDefined'] = {
                        'type': 'boolean'
                    }
                    print("Retained propertyless block: " + cfnblockname)

            if block['nesting_mode'] == "list":
                schema['properties'][cfnblockname] = {
                    'type': 'array',
                    'insertionOrder': False,
                    'items': {
                        '$ref': '#/definitions/' + cfnblockname
                    }
                }
            elif block['nesting_mode'] == "set":
                schema['properties'][cfnblockname] = {
                    'type': 'array',
                    'insertionOrder': True,
                    'items': {
                        '$ref': '#/definitions/' + cfnblockname
                    }
                }
            elif block['nesting_mode'] == "single":
                schema['properties'][cfnblockname] = {
                    '$ref': '#/definitions/' + cfnblockname
                }
            else:
                print("Unknown nesting_mode: " + block['nesting_mode'])

            if 'max_items' in block:
                schema['properties'][cfnblockname]['maxItems'] = block['max_items']
            if 'min_items' in block:
                schema['properties'][cfnblockname]['minItems'] = block['min_items']

        with open(providerdir / (cfndirname.lower() + ".json"), "w") as f:
            f.write(json.dumps(schema, indent=4))
        
        check_call(['cfn', 'generate'], providerdir.absolute(), None)

        # update handlers.py
        with open("handlers.py.template", "r") as handlerstemplate:
            with open(providerdir / "src" / cfndirname.lower().replace("-","_") / "handlers.py", "w") as f:
                template = handlerstemplate.read().replace("###CFNTYPENAME###",cfntypename).replace("###TFTYPENAME###",k).replace("###PROVIDERTYPENAME###",PROVIDER_TYPE)
                f.write(template)

        print("Generated " + cfntypename)
    except KeyboardInterrupt:
        quit()
    except:
        traceback.print_exc(file=sys.stdout)
        print("Failed to generate " + cfntypename)
