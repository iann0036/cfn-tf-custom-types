# TF::FortiOS::SystemSdnconnector

Configure connection to SDN Connector.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemSdnconnector",
    "Properties" : {
        "<a href="#accesskey" title="AccessKey">AccessKey</a>" : <i>String</i>,
        "<a href="#apikey" title="ApiKey">ApiKey</a>" : <i>String</i>,
        "<a href="#azureregion" title="AzureRegion">AzureRegion</a>" : <i>String</i>,
        "<a href="#clientid" title="ClientId">ClientId</a>" : <i>String</i>,
        "<a href="#clientsecret" title="ClientSecret">ClientSecret</a>" : <i>String</i>,
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#computegeneration" title="ComputeGeneration">ComputeGeneration</a>" : <i>Double</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#gcpproject" title="GcpProject">GcpProject</a>" : <i>String</i>,
        "<a href="#groupname" title="GroupName">GroupName</a>" : <i>String</i>,
        "<a href="#hastatus" title="HaStatus">HaStatus</a>" : <i>String</i>,
        "<a href="#ibmregion" title="IbmRegion">IbmRegion</a>" : <i>String</i>,
        "<a href="#keypasswd" title="KeyPasswd">KeyPasswd</a>" : <i>String</i>,
        "<a href="#loginendpoint" title="LoginEndpoint">LoginEndpoint</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#ocicert" title="OciCert">OciCert</a>" : <i>String</i>,
        "<a href="#ocifingerprint" title="OciFingerprint">OciFingerprint</a>" : <i>String</i>,
        "<a href="#ociregion" title="OciRegion">OciRegion</a>" : <i>String</i>,
        "<a href="#ociregiontype" title="OciRegionType">OciRegionType</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#privatekey" title="PrivateKey">PrivateKey</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#resourcegroup" title="ResourceGroup">ResourceGroup</a>" : <i>String</i>,
        "<a href="#resourceurl" title="ResourceUrl">ResourceUrl</a>" : <i>String</i>,
        "<a href="#secretkey" title="SecretKey">SecretKey</a>" : <i>String</i>,
        "<a href="#secrettoken" title="SecretToken">SecretToken</a>" : <i>String</i>,
        "<a href="#server" title="Server">Server</a>" : <i>String</i>,
        "<a href="#serverport" title="ServerPort">ServerPort</a>" : <i>Double</i>,
        "<a href="#serviceaccount" title="ServiceAccount">ServiceAccount</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#subscriptionid" title="SubscriptionId">SubscriptionId</a>" : <i>String</i>,
        "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#updateinterval" title="UpdateInterval">UpdateInterval</a>" : <i>Double</i>,
        "<a href="#usemetadataiam" title="UseMetadataIam">UseMetadataIam</a>" : <i>String</i>,
        "<a href="#userid" title="UserId">UserId</a>" : <i>String</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>,
        "<a href="#vcenterpassword" title="VcenterPassword">VcenterPassword</a>" : <i>String</i>,
        "<a href="#vcenterserver" title="VcenterServer">VcenterServer</a>" : <i>String</i>,
        "<a href="#vcenterusername" title="VcenterUsername">VcenterUsername</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#externalip" title="ExternalIp">ExternalIp</a>" : <i>[ <a href="externalipdefinition.md">ExternalIpDefinition</a>, ... ]</i>,
        "<a href="#nic" title="Nic">Nic</a>" : <i>[ <a href="nicdefinition.md">NicDefinition</a>, ... ]</i>,
        "<a href="#route" title="Route">Route</a>" : <i>[ <a href="routedefinition.md">RouteDefinition</a>, ... ]</i>,
        "<a href="#routetable" title="RouteTable">RouteTable</a>" : <i>[ <a href="routetabledefinition.md">RouteTableDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemSdnconnector
Properties:
    <a href="#accesskey" title="AccessKey">AccessKey</a>: <i>String</i>
    <a href="#apikey" title="ApiKey">ApiKey</a>: <i>String</i>
    <a href="#azureregion" title="AzureRegion">AzureRegion</a>: <i>String</i>
    <a href="#clientid" title="ClientId">ClientId</a>: <i>String</i>
    <a href="#clientsecret" title="ClientSecret">ClientSecret</a>: <i>String</i>
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#computegeneration" title="ComputeGeneration">ComputeGeneration</a>: <i>Double</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#gcpproject" title="GcpProject">GcpProject</a>: <i>String</i>
    <a href="#groupname" title="GroupName">GroupName</a>: <i>String</i>
    <a href="#hastatus" title="HaStatus">HaStatus</a>: <i>String</i>
    <a href="#ibmregion" title="IbmRegion">IbmRegion</a>: <i>String</i>
    <a href="#keypasswd" title="KeyPasswd">KeyPasswd</a>: <i>String</i>
    <a href="#loginendpoint" title="LoginEndpoint">LoginEndpoint</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ocicert" title="OciCert">OciCert</a>: <i>String</i>
    <a href="#ocifingerprint" title="OciFingerprint">OciFingerprint</a>: <i>String</i>
    <a href="#ociregion" title="OciRegion">OciRegion</a>: <i>String</i>
    <a href="#ociregiontype" title="OciRegionType">OciRegionType</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#privatekey" title="PrivateKey">PrivateKey</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#resourcegroup" title="ResourceGroup">ResourceGroup</a>: <i>String</i>
    <a href="#resourceurl" title="ResourceUrl">ResourceUrl</a>: <i>String</i>
    <a href="#secretkey" title="SecretKey">SecretKey</a>: <i>String</i>
    <a href="#secrettoken" title="SecretToken">SecretToken</a>: <i>String</i>
    <a href="#server" title="Server">Server</a>: <i>String</i>
    <a href="#serverport" title="ServerPort">ServerPort</a>: <i>Double</i>
    <a href="#serviceaccount" title="ServiceAccount">ServiceAccount</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#subscriptionid" title="SubscriptionId">SubscriptionId</a>: <i>String</i>
    <a href="#tenantid" title="TenantId">TenantId</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#updateinterval" title="UpdateInterval">UpdateInterval</a>: <i>Double</i>
    <a href="#usemetadataiam" title="UseMetadataIam">UseMetadataIam</a>: <i>String</i>
    <a href="#userid" title="UserId">UserId</a>: <i>String</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
    <a href="#vcenterpassword" title="VcenterPassword">VcenterPassword</a>: <i>String</i>
    <a href="#vcenterserver" title="VcenterServer">VcenterServer</a>: <i>String</i>
    <a href="#vcenterusername" title="VcenterUsername">VcenterUsername</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#externalip" title="ExternalIp">ExternalIp</a>: <i>
      - <a href="externalipdefinition.md">ExternalIpDefinition</a></i>
    <a href="#nic" title="Nic">Nic</a>: <i>
      - <a href="nicdefinition.md">NicDefinition</a></i>
    <a href="#route" title="Route">Route</a>: <i>
      - <a href="routedefinition.md">RouteDefinition</a></i>
    <a href="#routetable" title="RouteTable">RouteTable</a>: <i>
      - <a href="routetabledefinition.md">RouteTableDefinition</a></i>
</pre>

## Properties

#### AccessKey

AWS access key ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiKey

IBM cloud API key or service ID API key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureRegion

Azure server region. Valid values: `global`, `china`, `germany`, `usgov`, `local`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientId

Azure client ID (application ID).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientSecret

Azure client secret (application key).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompartmentId

Compartment ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComputeGeneration

Compute generation for IBM cloud infrastructure.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

Domain name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcpProject

GCP project name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupName

Group name of computers.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaStatus

Enable/disable use for FortiGate HA service. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IbmRegion

IBM cloud region name. Valid values: `us-south`, `us-east`, `germany`, `great-britain`, `japan`, `australia`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyPasswd

Private key password.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoginEndpoint

Azure Stack login endpoint.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

SDN connector name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OciCert

OCI certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OciFingerprint

OCI pubkey fingerprint.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OciRegion

OCI server region.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OciRegionType

OCI region type. Valid values: `commercial`, `government`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Password of the remote SDN connector as login credentials.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateKey

Private key of GCP service account.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

AWS region name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroup

Azure resource group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceUrl

Azure Stack resource URL.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretKey

AWS secret access key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretToken

Secret token of Kubernetes service account.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Server

Server address of the remote SDN connector.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerPort

Port number of the remote SDN connector.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccount

GCP service account email.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable connection to the remote SDN connector. Valid values: `disable`, `enable`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubscriptionId

Azure subscription ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

Tenant ID (directory ID).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Type of SDN connector.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateInterval

Dynamic object update interval (0 - 3600 sec, 0 means disabled, default = 60).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseMetadataIam

Enable/disable using IAM role from metadata to call API. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserId

User ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

Username of the remote SDN connector as login credentials.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VcenterPassword

vCenter server password for NSX quarantine.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VcenterServer

vCenter server address for NSX quarantine.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VcenterUsername

vCenter server username for NSX quarantine.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

AWS VPC ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalIp

_Required_: No

_Type_: List of <a href="externalipdefinition.md">ExternalIpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nic

_Required_: No

_Type_: List of <a href="nicdefinition.md">NicDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Route

_Required_: No

_Type_: List of <a href="routedefinition.md">RouteDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteTable

_Required_: No

_Type_: List of <a href="routetabledefinition.md">RouteTableDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

