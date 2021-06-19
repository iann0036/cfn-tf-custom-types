# TF::Rancher2::Cluster AksConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#aadserverappsecret" title="AadServerAppSecret">AadServerAppSecret</a>" : <i>String</i>,
    "<a href="#aadtenantid" title="AadTenantId">AadTenantId</a>" : <i>String</i>,
    "<a href="#addclientappid" title="AddClientAppId">AddClientAppId</a>" : <i>String</i>,
    "<a href="#addserverappid" title="AddServerAppId">AddServerAppId</a>" : <i>String</i>,
    "<a href="#adminusername" title="AdminUsername">AdminUsername</a>" : <i>String</i>,
    "<a href="#agentdnsprefix" title="AgentDnsPrefix">AgentDnsPrefix</a>" : <i>String</i>,
    "<a href="#agentosdisksize" title="AgentOsDiskSize">AgentOsDiskSize</a>" : <i>Double</i>,
    "<a href="#agentpoolname" title="AgentPoolName">AgentPoolName</a>" : <i>String</i>,
    "<a href="#agentstorageprofile" title="AgentStorageProfile">AgentStorageProfile</a>" : <i>String</i>,
    "<a href="#agentvmsize" title="AgentVmSize">AgentVmSize</a>" : <i>String</i>,
    "<a href="#authbaseurl" title="AuthBaseUrl">AuthBaseUrl</a>" : <i>String</i>,
    "<a href="#baseurl" title="BaseUrl">BaseUrl</a>" : <i>String</i>,
    "<a href="#clientid" title="ClientId">ClientId</a>" : <i>String</i>,
    "<a href="#clientsecret" title="ClientSecret">ClientSecret</a>" : <i>String</i>,
    "<a href="#count" title="Count">Count</a>" : <i>Double</i>,
    "<a href="#dnsserviceip" title="DnsServiceIp">DnsServiceIp</a>" : <i>String</i>,
    "<a href="#dockerbridgecidr" title="DockerBridgeCidr">DockerBridgeCidr</a>" : <i>String</i>,
    "<a href="#enablehttpapplicationrouting" title="EnableHttpApplicationRouting">EnableHttpApplicationRouting</a>" : <i>Boolean</i>,
    "<a href="#enablemonitoring" title="EnableMonitoring">EnableMonitoring</a>" : <i>Boolean</i>,
    "<a href="#kubernetesversion" title="KubernetesVersion">KubernetesVersion</a>" : <i>String</i>,
    "<a href="#loadbalancersku" title="LoadBalancerSku">LoadBalancerSku</a>" : <i>String</i>,
    "<a href="#location" title="Location">Location</a>" : <i>String</i>,
    "<a href="#loganalyticsworkspace" title="LogAnalyticsWorkspace">LogAnalyticsWorkspace</a>" : <i>String</i>,
    "<a href="#loganalyticsworkspaceresourcegroup" title="LogAnalyticsWorkspaceResourceGroup">LogAnalyticsWorkspaceResourceGroup</a>" : <i>String</i>,
    "<a href="#masterdnsprefix" title="MasterDnsPrefix">MasterDnsPrefix</a>" : <i>String</i>,
    "<a href="#maxpods" title="MaxPods">MaxPods</a>" : <i>Double</i>,
    "<a href="#networkplugin" title="NetworkPlugin">NetworkPlugin</a>" : <i>String</i>,
    "<a href="#networkpolicy" title="NetworkPolicy">NetworkPolicy</a>" : <i>String</i>,
    "<a href="#podcidr" title="PodCidr">PodCidr</a>" : <i>String</i>,
    "<a href="#resourcegroup" title="ResourceGroup">ResourceGroup</a>" : <i>String</i>,
    "<a href="#servicecidr" title="ServiceCidr">ServiceCidr</a>" : <i>String</i>,
    "<a href="#sshpublickeycontents" title="SshPublicKeyContents">SshPublicKeyContents</a>" : <i>String</i>,
    "<a href="#subnet" title="Subnet">Subnet</a>" : <i>String</i>,
    "<a href="#subscriptionid" title="SubscriptionId">SubscriptionId</a>" : <i>String</i>,
    "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tagdefinition.md">TagDefinition</a>, ... ]</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
    "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>,
    "<a href="#virtualnetwork" title="VirtualNetwork">VirtualNetwork</a>" : <i>String</i>,
    "<a href="#virtualnetworkresourcegroup" title="VirtualNetworkResourceGroup">VirtualNetworkResourceGroup</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#aadserverappsecret" title="AadServerAppSecret">AadServerAppSecret</a>: <i>String</i>
<a href="#aadtenantid" title="AadTenantId">AadTenantId</a>: <i>String</i>
<a href="#addclientappid" title="AddClientAppId">AddClientAppId</a>: <i>String</i>
<a href="#addserverappid" title="AddServerAppId">AddServerAppId</a>: <i>String</i>
<a href="#adminusername" title="AdminUsername">AdminUsername</a>: <i>String</i>
<a href="#agentdnsprefix" title="AgentDnsPrefix">AgentDnsPrefix</a>: <i>String</i>
<a href="#agentosdisksize" title="AgentOsDiskSize">AgentOsDiskSize</a>: <i>Double</i>
<a href="#agentpoolname" title="AgentPoolName">AgentPoolName</a>: <i>String</i>
<a href="#agentstorageprofile" title="AgentStorageProfile">AgentStorageProfile</a>: <i>String</i>
<a href="#agentvmsize" title="AgentVmSize">AgentVmSize</a>: <i>String</i>
<a href="#authbaseurl" title="AuthBaseUrl">AuthBaseUrl</a>: <i>String</i>
<a href="#baseurl" title="BaseUrl">BaseUrl</a>: <i>String</i>
<a href="#clientid" title="ClientId">ClientId</a>: <i>String</i>
<a href="#clientsecret" title="ClientSecret">ClientSecret</a>: <i>String</i>
<a href="#count" title="Count">Count</a>: <i>Double</i>
<a href="#dnsserviceip" title="DnsServiceIp">DnsServiceIp</a>: <i>String</i>
<a href="#dockerbridgecidr" title="DockerBridgeCidr">DockerBridgeCidr</a>: <i>String</i>
<a href="#enablehttpapplicationrouting" title="EnableHttpApplicationRouting">EnableHttpApplicationRouting</a>: <i>Boolean</i>
<a href="#enablemonitoring" title="EnableMonitoring">EnableMonitoring</a>: <i>Boolean</i>
<a href="#kubernetesversion" title="KubernetesVersion">KubernetesVersion</a>: <i>String</i>
<a href="#loadbalancersku" title="LoadBalancerSku">LoadBalancerSku</a>: <i>String</i>
<a href="#location" title="Location">Location</a>: <i>String</i>
<a href="#loganalyticsworkspace" title="LogAnalyticsWorkspace">LogAnalyticsWorkspace</a>: <i>String</i>
<a href="#loganalyticsworkspaceresourcegroup" title="LogAnalyticsWorkspaceResourceGroup">LogAnalyticsWorkspaceResourceGroup</a>: <i>String</i>
<a href="#masterdnsprefix" title="MasterDnsPrefix">MasterDnsPrefix</a>: <i>String</i>
<a href="#maxpods" title="MaxPods">MaxPods</a>: <i>Double</i>
<a href="#networkplugin" title="NetworkPlugin">NetworkPlugin</a>: <i>String</i>
<a href="#networkpolicy" title="NetworkPolicy">NetworkPolicy</a>: <i>String</i>
<a href="#podcidr" title="PodCidr">PodCidr</a>: <i>String</i>
<a href="#resourcegroup" title="ResourceGroup">ResourceGroup</a>: <i>String</i>
<a href="#servicecidr" title="ServiceCidr">ServiceCidr</a>: <i>String</i>
<a href="#sshpublickeycontents" title="SshPublicKeyContents">SshPublicKeyContents</a>: <i>String</i>
<a href="#subnet" title="Subnet">Subnet</a>: <i>String</i>
<a href="#subscriptionid" title="SubscriptionId">SubscriptionId</a>: <i>String</i>
<a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tagdefinition.md">TagDefinition</a></i>
<a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
<a href="#tenantid" title="TenantId">TenantId</a>: <i>String</i>
<a href="#virtualnetwork" title="VirtualNetwork">VirtualNetwork</a>: <i>String</i>
<a href="#virtualnetworkresourcegroup" title="VirtualNetworkResourceGroup">VirtualNetworkResourceGroup</a>: <i>String</i>
</pre>

## Properties

#### AadServerAppSecret

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AadTenantId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddClientAppId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddServerAppId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminUsername

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AgentDnsPrefix

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AgentOsDiskSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AgentPoolName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AgentStorageProfile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AgentVmSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthBaseUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BaseUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientSecret

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Count

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsServiceIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DockerBridgeCidr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableHttpApplicationRouting

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableMonitoring

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesVersion

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerSku

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogAnalyticsWorkspace

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogAnalyticsWorkspaceResourceGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterDnsPrefix

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPods

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkPlugin

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PodCidr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroup

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceCidr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshPublicKeyContents

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubscriptionId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tagdefinition.md">TagDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualNetwork

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualNetworkResourceGroup

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

