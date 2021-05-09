import requests
import pprint
import json
import collections


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
    'azurerm': ['AzureRM','Azure'],
    'nomad': ['Nomad','Nomad'],
    'ovh': ['OVH','OVH'],
    'scaleway': ['Scaleway','Scaleway'],
    'bitbucket': ['Bitbucket','Bitbucket'],
    'logentries': ['Logentries','Logentries'],
    'datadog': ['Datadog','Datadog'],
    'pagerduty': ['PagerDuty','PagerDuty'],
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
    'akamai': ['Akamai','Akamai'],
    'azuread': ['AzureAD','Azure Active Directory'],
    'ad': ['AD','Active Directory'],
    'archive': ['Archive','Archive'],
    'boundary': ['Boundary','Boundary'],
    'ciscoasa': ['CiscoASA','Cisco ASA'],
    'cloudinit': ['Cloudinit','Cloudinit'],
    'external': ['External','External'],
    'google-beta': ['GoogleBeta','Google Beta'],
    'hcp': ['HCP','HashiCorp Cloud Platform'],
    'hcs': ['HCS','HashiCorp Consul Service'],
    'helm': ['Helm','Helm'],
    'http': ['HTTP','HTTP'],
    'kubernetes-alpha': ['KubernetesAlpha','Kubernetes (Alpha)'],
    'null': ['Null','Null'],
    'terraform': ['Terraform','Terraform'],
    'time': ['Time','Time'],
    'aci': ['ACI','Cisco ACI'],
    'ah': ['AH','AdvancedHosting Cloud'],
    'aiven': ['Aiven','Aiven'],
    'alkira': ['Alkira','Alkira'],
    'amixr': ['Amixr','Amixr'],
    'anxcloud': ['Anxcloud','Anexia Cloud'],
    'artifactory': ['Artifactory','Artifactory'],
    'avi': ['AVI','AVI Networks'],
    'aviatrix': ['Aviatrix','Aviatrix'],
    'azurecaf': ['AzureCAF','Azure Cloud Adoption Framework'],
    'azuredevops': ['AzureDevOps','Azure DevOps'],
    'b2': ['B2','B2'],
    'buildkite': ['Buildkite','Buildkite'],
    'checkly': ['Checkly','Checkly'],
    'checkpoint': ['CheckPoint','Check Point'],
    'civo': ['Civo','Civo'],
    'cloudeos': ['CloudEOS','Arista CloudEOS'],
    'cloudsigma': ['CloudSigma','CloudSigma'],
    'cloudsmith': ['Cloudsmith','Cloudsmith'],
    'cloudtamerio': ['Cloudtamerio','cloudtamer.io'],
    'configcat': ['ConfigCat','ConfigCat'],
    'constellix': ['Constellix','Constellix'],
    'databricks': ['Databricks','Databricks'],
    'dcnm': ['DCNM','Cisco DCNM'],
    'dome9': ['Dome9','Dome9'],
    'dynatrace': ['Dynatrace','Dynatrace'],
    'ecl': ['ECL','NTT Enterprise Cloud 2.0'],
    'equinix': ['Equinix','Equinix'],
    'exoscale': ['Exoscale','Exoscale'],
    'fortios': ['FortiOS','FortiOS'],
    'gridscale': ['Gridscale','Gridscale'],
    'ilert': ['ILert','iLert'],
    'intersight': ['Intersight','Cisco Intersight'],
    'ionoscloud': ['IONOSCloud','IONOS Cloud'],
    'lacework': ['Lacework','Lacework'],
    'launchdarkly': ['LaunchDarkly','LaunchDarkly'],
    'limelight': ['Limelight','Limelight'],
    'logzio': ['Logzio','Logz.io'],
    'metal': ['Metal','Equinix Metal'],
    'mongodbatlas': ['MongoDBAtlas','MongoDB Atlas'],
    'mso': ['MSO','Cisco MSO'],
    'netapp-cloudmanager': ['NetAppCloudManager','NetApp Cloud Volumes ONTAP'],
    'netapp-elementsw': ['NetAppElementSW','NetApp ElementSW'],
    'netapp-gcp': ['NetAppGCP','NetApp Cloud Volumes Service for Google Cloud'],
    'nutanixkps': ['NutanixKPS','Nutanix KPS'],
    'octopusdeploy': ['OctopusDeploy','Octopus Deploy'],
    'okta': ['Okta','Okta'],
    'oktaasa': ['OktaASA','Okta ASA'],
    'onelogin': ['OneLogin','OneLogin'],
    'onepassword': ['OnePassword','1Password'],
    'oneview': ['OneView','HPE OneView'],
    'opennebula': ['OpenNebula','OpenNebula'],
    'pnap': ['PNAP','phoenixNAP'],
    'prismacloud': ['PrismaCloud','Palo Alto Networks Prisma Cloud'],
    'quorum': ['Quorum','Quorum'],
    'rancher2': ['Rancher2','Rancher v2'],
    'rediscloud': ['RedisCloud','Redis Enterprise Cloud'],
    'rke': ['RKE','Rancher Kubernetes Engine'],
    'rollbar': ['Rollbar','Rollbar'],
    'sdm': ['SDM','strongDM'],
    'sematext': ['Sematext','Sematext'],
    'signalfx': ['SignalFx','SignalFx'],
    'sigsci': ['SigSci','Signal Sciences'],
    'splunk': ['Splunk','Splunk'],
    'stackpath': ['StackPath','StackPath'],
    'sumologic': ['SumoLogic','Sumo Logic'],
    'thunder': ['Thunder','A10 Thunder'],
    'transloadit': ['Transloadit','Transloadit'],
    'turbot': ['Turbot','Turbot'],
    'upcloud': ['UpCloud','UpCloud'],
    'venafi': ['Venafi','Venafi'],
    'victorops': ['VictorOps','VictorOps'],
    'vmc': ['VMC','VMware Cloud'],
    'volterra': ['Volterra','Volterra'],
    'vra': ['VRA','VMware vRealize Automation'],
    'vra7': ['VRA7','VMware vRealize Automation 7'],
    'vultr': ['Vultr','Vultr'],
    'wavefront': ['Wavefront','Wavefront'],
    'zerotier': ['ZeroTier','ZeroTier']
}
PROVIDERS_MAP = collections.OrderedDict(sorted(PROVIDERS_MAP.items(), key=lambda item: item[1][1].lower()))

print("set -e")
for provider in PROVIDERS_MAP.keys():
    print("python3 generate.py {} || true".format(provider))
    print("find resources/{} -name \"terraform-*.zip\" -exec aws s3 cp {{}} s3://cfntf/ --acl public-read --region us-east-1 \\;".format(provider)) 
