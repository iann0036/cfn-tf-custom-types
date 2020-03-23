import requests
import subprocess
import os
import pprint
import json
import re
import tempfile
import time
import sys, traceback
import multiprocessing
from pathlib import Path


PROVIDERS_MAP = {
    'random': ['Random','Random'],
    'digitalocean': ['DigitalOcean','DigitalOcean'],
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


def tf_to_cfn_str(obj):
    return re.sub(r'(?:^|_)(\w)', lambda x: x.group(1).upper(), obj)


def tf_type_to_cfn_type(tf_name, provider_name):
    split_provider_name = tf_name.split("_")
    split_provider_name.pop(0)
    cfn_provider_name = PROVIDERS_MAP[provider_name][0]
    return "Terraform::" + cfn_provider_name + "::" + tf_to_cfn_str("_".join(split_provider_name))


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
                    'MapKey': {
                        'type': 'string'
                    },
                    'MapValue': jsonschema_type(attrtype[1])
                },
                'required': [
                    'MapKey',
                    'MapValue'
                ]
            }
        } # TODO: Handle this in the handlers
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


def process_provider(provider_type):
    tmpdir = tempfile.TemporaryDirectory()
    tempdir = Path(tmpdir.name)

    with open(tempdir / "base.tf", "w") as f:
        f.write('''
    provider "{provider}" {{}}
        '''.format(provider=provider_type))

    print("Downloading latest provider version...")
    check_call(['terraform', 'init'], tempdir.absolute(), None)
    tfschema = json.loads(check_call(['terraform', 'providers', 'schema', '-json'], tempdir.absolute(), None))

    check_call(['git', 'clone', 'https://github.com/terraform-providers/terraform-provider-{}.git'.format(provider_type), provider_type], tempdir.absolute(), None)

    outstandingblocks = {}
    schema = {}

    doc_resources = generate_docs(tempdir, provider_type, tfschema)

    for k,v in tfschema['provider_schemas'][provider_type]['resource_schemas'].items():
        endnaming = tf_to_cfn_str(k)
        if k.startswith(provider_type + "_"):
            endnaming = tf_to_cfn_str(k[(len(provider_type)+1):])
        
        cfntypename = "Terraform::" + PROVIDERS_MAP[provider_type][0] + "::" + endnaming
        cfndirname = "Terraform-" + PROVIDERS_MAP[provider_type][0] + "-" + endnaming

        try:
            providerdir = Path('.') / 'resources' / provider_type / cfndirname

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

            if k in doc_resources and len(doc_resources[k]['description']) > 10:
                schema['description'] = doc_resources[k]['description']

            if provider_type == "aws":
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

                    if attrname == "id":
                        computed = True
                        #schema['primaryIdentifier'] = ["/properties/Id"]
                        schema['readOnlyProperties'].append("/properties/Id")
                    else:
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

                    if k in doc_resources:
                        for docarg in doc_resources[k]['arguments']:
                            if docarg['name'] == attrname and docarg['property_of'] is None:
                                schema['properties'][cfnattrname]['description'] = docarg['description']

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

                        if k in doc_resources:
                            for docarg in doc_resources[k]['arguments']:
                                if docarg['name'] == attrname and docarg['property_of'] == blockname:
                                    schema['definitions'][cfnblockname]['properties'][cfnattrname]['description'] = docarg['description']
                
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

                        if 'max_items' in subblock:
                            schema['definitions'][cfnblockname]['properties'][cfnsubblockname]['maxItems'] = subblock['max_items']
                        if 'min_items' in subblock:
                            schema['definitions'][cfnblockname]['properties'][cfnsubblockname]['minItems'] = subblock['min_items']

                if not bool(schema['definitions'][cfnblockname]['properties']):
                    if bool(block['block']):
                        del schema['definitions'][cfnblockname] # no properties found
                        print("Skipped propertyless block: " + cfnblockname)
                        continue
                    else:
                        schema['definitions'][cfnblockname]['properties']['IsPropertyDefined'] = {
                            'type': 'boolean'
                        } # TODO: Handle this in handlers
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

                # TODO: Block descriptions

            with open(providerdir / (cfndirname.lower() + ".json"), "w") as f:
                f.write(json.dumps(schema, indent=4))
            
            check_call(['cfn', 'generate'], providerdir.absolute(), None)

            # update handlers.py
            with open("handlers.py.template", "r") as handlerstemplate:
                with open(providerdir / "src" / cfndirname.lower().replace("-","_") / "handlers.py", "w") as f:
                    template = handlerstemplate.read().replace("###CFNTYPENAME###",cfntypename).replace("###TFTYPENAME###",k).replace("###PROVIDERTYPENAME###",provider_type)
                    f.write(template)

            print("Generated " + cfntypename)
        except KeyboardInterrupt:
            quit()
        except:
            traceback.print_exc(file=sys.stdout)
            print("Failed to generate " + cfntypename)


# Docs
def process_resource_docs(provider_name, file_contents, provider_readme_items):
    section = ""

    resource_type = ""
    description = ""
    example = ""
    arguments = []
    argument_lines = []
    attributes = {}

    lines = file_contents.split("\n")
    for line in lines:
        if line.startswith("# " + provider_name):
            resource_type = line[2:].replace("\\", "")
            section = "description"
        elif line.startswith("# Resource: " + provider_name): # aws docs differences
            resource_type = line[len("# Resource: "):].replace("\\", "")
            section = "description"
        elif line == "## Example Usage":
            section = "example"
        elif line == "## Argument Reference":
            section = "arguments"
        elif line == "## Attributes Reference":
            section = "attributes"
        elif line.startswith("##"):
            section = ""
        elif section == "description":
            description += line + "\n"
        elif section == "example":
            example += line + "\n"
        elif section == "arguments":
            argument_lines.append(line)
        elif section == "attributes":
            if line.strip().startswith("* "):
                startpos = line.strip().find("`")
                endpos = line.strip().find("`", startpos+1)
                if startpos != -1 and endpos != -1:
                    attribute_name = line.strip()[startpos+1:endpos]
                    if line.strip()[endpos+1:].strip().startswith("- ") or line.strip()[endpos+1:].strip().startswith("= "):
                        attribute_description = line.strip()[endpos+1:].strip()[2:]
                        if attribute_description[-1] != ".":
                            attribute_description += "."
                        attributes[attribute_name] = attribute_description
    
    # process arguments
    argument_names = []
    argument_block = None
    for line_number, line in enumerate(argument_lines):
        if line.strip().startswith("* ") or line.strip().startswith("- "):
            startpos = line.strip().find("`")
            endpos = line.strip().find("`", startpos+1)
            if startpos != -1 and endpos != -1:
                argument_name = line.strip()[startpos+1:endpos]
                argument_names.append(argument_name)
                if line.strip()[endpos+1:].strip().startswith("- ") or line.strip()[endpos+1:].strip().startswith("= "):
                    argument_description = line.strip()[endpos+1:].strip()[2:]

                    # concat lines in newlines for description of attribute
                    line_num_iterator = 1
                    while len(argument_lines) > line_number+line_num_iterator and (argument_lines[line_number+line_num_iterator].strip() != "" and not argument_lines[line_number+line_num_iterator].startswith("* ") and not argument_lines[line_number+line_num_iterator].startswith("#")):
                        argument_description += "\n" + argument_lines[line_number+line_num_iterator].strip()
                        line_num_iterator += 1

                    argument_attributes = []
                    argument_description = argument_description.strip()
                    if argument_description[0] == "(":
                        endbracked_index = argument_description.find(')')
                        argument_attributes = map(str.strip, argument_description[1:endbracked_index].split(","))
                        argument_description = argument_description[endbracked_index+1:].strip()

                    if argument_description and len(argument_description) > 2:
                        if argument_description[-1] != ".":
                            argument_description += "."
                    else:
                        argument_description = None
                    
                    arguments.append({
                        'name': argument_name,
                        'description': argument_description,
                        'property_of': argument_block,
                        'attributes': argument_attributes
                    })
        if line.strip().endswith(":") and argument_lines[line_number+1].strip() == "":
            for argument_name in argument_names:
                if "`{}`".format(argument_name) in line:
                    argument_block = argument_name

    if resource_type != "":
        if provider_name not in PROVIDERS_MAP:
            return
        
        description = description.strip()

        return {
            'resource_type': resource_type,
            'description': description,
            'example': example,
            'arguments': arguments,
            'attributes': attributes
        }
    
    return None


def generate_docs(tempdir, provider_type, tfschema):
    resources_path = (tempdir / provider_type / "website" / "docs" / "r").absolute()
    index_path = (tempdir / provider_type / "website" / "docs" / "index.html.markdown").absolute()
    provider_reference_path = (tempdir / provider_type / "website" / "docs" / "provider_reference.html.markdown").absolute()
    provider_readme_items = []
    ret = {}

    if os.path.isdir(resources_path) and provider_type in PROVIDERS_MAP:
        
        with open(Path("docs") / "{}.md".format(provider_type), 'w') as provider_readme:
            readable_provider_name = PROVIDERS_MAP[provider_type][1]
            
            # provider info
            with open(index_path, 'r') as f:
                section = ""
                first_argument_found = False
                arguments = []
                index_file_contents = f.read()
                lines = index_file_contents.split("\n")
                for line in lines:
                    if line.startswith("*") and section == "arguments":
                        first_argument_found = True
                    if line.startswith("## Argument Reference") or line.startswith("## Arguments Reference") or line.startswith("## Configuration Reference") or "the following arguments:" in line or "provide the following credentials:" in line:
                        section = "arguments"
                    elif line.startswith("#"):
                        section = ""
                    elif section == "arguments" and first_argument_found:
                        arguments.append(line)
            
            # try provider reference (eg. google)
            if len(arguments) == 0:
                try:
                    with open(provider_reference_path, 'r') as f:
                        section = ""
                        first_argument_found = False
                        arguments = []
                        index_file_contents = f.read()
                        lines = index_file_contents.split("\n")
                        for line in lines:
                            if (line.startswith("*") or line.startswith("-")) and section == "arguments":
                                first_argument_found = True
                            if line.startswith("## Argument Reference") or line.startswith("## Arguments Reference") or line.startswith("## Configuration Reference") or "the following arguments:" in line or "provide the following credentials:" in line:
                                section = "arguments"
                            elif line.startswith("#"):
                                section = ""
                            elif section == "arguments" and first_argument_found and not "navigation to the left" in line:
                                if line.startswith("-"):
                                    line[0] = "*"
                                arguments.append(line)
                except:
                    pass
            
            # remove environmental variable references
            argument_text = "\n".join(arguments)
            if provider_type not in ['digitalocean', 'fastly', 'flexibleengine', 'google', 'oneandone', 'profitbricks']:
                sentences = argument_text.split(".")
                i = 0
                while len(sentences) > i:
                    if ("environment variable" in sentences[i] or "environmental variable" in sentences[i] or "Can be sourced from" in sentences[i]):
                        del sentences[i]
                    else:
                        i+=1
                argument_text = ".".join(sentences)
            
            # replace tf references
            if provider_type in ['aws']:
                argument_text = re.sub(r"(\`%s\_.+\`)" % provider_type, lambda x: "`" + tf_type_to_cfn_type(x.group(1), provider_type), argument_text) # TODO - why only one backtick used?!?

            has_required_arguments = False
            if "required" in argument_text.lower() and provider_type not in ['aws']:
                has_required_arguments = True
            
            provider_readme.write("# {} Provider\n\n".format(readable_provider_name))
            if provider_type == "aws":
                provider_readme.write("> For the AWS provider, credentials will be inherited from the executor role, meaning you are not required to provide credentials in a configuration secret.\n\n")
            provider_readme.write("## Configuration\n\n")
            if len(arguments) == 0:
                provider_readme.write("No configuration is required for this provider.\n\n")
            elif not has_required_arguments:
                provider_readme.write("To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/{}**. The below arguments may be included as the key/value or JSON properties in the secret:\n\n".format(provider_type))
                provider_readme.write(argument_text + "\n\n")
            else:
                provider_readme.write("To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/{}**. The below arguments may be included as the key/value or JSON properties in the secret:\n\n".format(provider_type))
                provider_readme.write(argument_text + "\n\n")

            # iterate provider resources
            provider_readme.write("## Supported Resources\n\n")
            provider_readme_items = []
            files = [f for f in os.listdir(resources_path) if os.path.isfile(os.path.join(resources_path, f))]
            for filename in files:
                with open(os.path.join(resources_path, filename), 'r') as f:
                    #print(filename)
                    resource_file_contents = f.read()
                    resource_properties = process_resource_docs(provider_type, resource_file_contents, provider_readme_items)
                    if resource_properties:
                        ret[resource_properties['resource_type']] = resource_properties
            
            # provider index
            for k,v in tfschema['provider_schemas'][provider_type]['resource_schemas'].items():
                split_provider_name = k.split("_")
                split_provider_name.pop(0)

                endnaming = tf_to_cfn_str(k)
                if k.startswith(provider_type + "_"):
                    endnaming = tf_to_cfn_str(k[(len(provider_type)+1):])
                
                cfn_type = "Terraform::" + PROVIDERS_MAP[provider_type][0] + "::" + endnaming
                
                provider_readme_items.append("* [{cfn_type}](../resources/{provider_name}/{type_stub}/docs/README.md)".format(
                    cfn_type=cfn_type,
                    provider_name=provider_type,
                    type_stub=tf_type_to_cfn_type(provider_type + "_" + "_".join(split_provider_name), provider_type).replace("::","-")
                ))
            
            provider_readme_items = list(set(provider_readme_items))
            provider_readme_items.sort()
            provider_readme.write("\n".join(provider_readme_items))

    return ret


def main():
    if sys.argv[1] == "all":
        provider_list = PROVIDERS_MAP.keys()
        with multiprocessing.Pool(multiprocessing.cpu_count()) as p: # CPU warmer :S
            list(p.imap_unordered(process_provider, provider_list))
    else:
        process_provider(sys.argv[1])


if __name__ == "__main__":
    main()