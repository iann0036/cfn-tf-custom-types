# TF::VMC::Sddc

Provides a resource to provision a SingleAZ or MultiAZ SDDC.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::VMC::Sddc",
    "Properties" : {
        "<a href="#delayaccountlink" title="DelayAccountLink">DelayAccountLink</a>" : <i>Boolean</i>,
        "<a href="#deploymenttype" title="DeploymentType">DeploymentType</a>" : <i>String</i>,
        "<a href="#edrspolicytype" title="EdrsPolicyType">EdrsPolicyType</a>" : <i>String</i>,
        "<a href="#enableedrs" title="EnableEdrs">EnableEdrs</a>" : <i>Boolean</i>,
        "<a href="#hostinstancetype" title="HostInstanceType">HostInstanceType</a>" : <i>String</i>,
        "<a href="#intranetmtuuplink" title="IntranetMtuUplink">IntranetMtuUplink</a>" : <i>Double</i>,
        "<a href="#maxhosts" title="MaxHosts">MaxHosts</a>" : <i>Double</i>,
        "<a href="#minhosts" title="MinHosts">MinHosts</a>" : <i>Double</i>,
        "<a href="#numhost" title="NumHost">NumHost</a>" : <i>Double</i>,
        "<a href="#providertype" title="ProviderType">ProviderType</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#sddcname" title="SddcName">SddcName</a>" : <i>String</i>,
        "<a href="#sddctemplateid" title="SddcTemplateId">SddcTemplateId</a>" : <i>String</i>,
        "<a href="#sddctype" title="SddcType">SddcType</a>" : <i>String</i>,
        "<a href="#size" title="Size">Size</a>" : <i>String</i>,
        "<a href="#skipcreatingvxlan" title="SkipCreatingVxlan">SkipCreatingVxlan</a>" : <i>Boolean</i>,
        "<a href="#ssodomain" title="SsoDomain">SsoDomain</a>" : <i>String</i>,
        "<a href="#storagecapacity" title="StorageCapacity">StorageCapacity</a>" : <i>String</i>,
        "<a href="#vpccidr" title="VpcCidr">VpcCidr</a>" : <i>String</i>,
        "<a href="#vxlansubnet" title="VxlanSubnet">VxlanSubnet</a>" : <i>String</i>,
        "<a href="#accountlinksddcconfig" title="AccountLinkSddcConfig">AccountLinkSddcConfig</a>" : <i>[ <a href="accountlinksddcconfigdefinition.md">AccountLinkSddcConfigDefinition</a>, ... ]</i>,
        "<a href="#microsoftlicensingconfig" title="MicrosoftLicensingConfig">MicrosoftLicensingConfig</a>" : <i>[ <a href="microsoftlicensingconfigdefinition.md">MicrosoftLicensingConfigDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::VMC::Sddc
Properties:
    <a href="#delayaccountlink" title="DelayAccountLink">DelayAccountLink</a>: <i>Boolean</i>
    <a href="#deploymenttype" title="DeploymentType">DeploymentType</a>: <i>String</i>
    <a href="#edrspolicytype" title="EdrsPolicyType">EdrsPolicyType</a>: <i>String</i>
    <a href="#enableedrs" title="EnableEdrs">EnableEdrs</a>: <i>Boolean</i>
    <a href="#hostinstancetype" title="HostInstanceType">HostInstanceType</a>: <i>String</i>
    <a href="#intranetmtuuplink" title="IntranetMtuUplink">IntranetMtuUplink</a>: <i>Double</i>
    <a href="#maxhosts" title="MaxHosts">MaxHosts</a>: <i>Double</i>
    <a href="#minhosts" title="MinHosts">MinHosts</a>: <i>Double</i>
    <a href="#numhost" title="NumHost">NumHost</a>: <i>Double</i>
    <a href="#providertype" title="ProviderType">ProviderType</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#sddcname" title="SddcName">SddcName</a>: <i>String</i>
    <a href="#sddctemplateid" title="SddcTemplateId">SddcTemplateId</a>: <i>String</i>
    <a href="#sddctype" title="SddcType">SddcType</a>: <i>String</i>
    <a href="#size" title="Size">Size</a>: <i>String</i>
    <a href="#skipcreatingvxlan" title="SkipCreatingVxlan">SkipCreatingVxlan</a>: <i>Boolean</i>
    <a href="#ssodomain" title="SsoDomain">SsoDomain</a>: <i>String</i>
    <a href="#storagecapacity" title="StorageCapacity">StorageCapacity</a>: <i>String</i>
    <a href="#vpccidr" title="VpcCidr">VpcCidr</a>: <i>String</i>
    <a href="#vxlansubnet" title="VxlanSubnet">VxlanSubnet</a>: <i>String</i>
    <a href="#accountlinksddcconfig" title="AccountLinkSddcConfig">AccountLinkSddcConfig</a>: <i>
      - <a href="accountlinksddcconfigdefinition.md">AccountLinkSddcConfigDefinition</a></i>
    <a href="#microsoftlicensingconfig" title="MicrosoftLicensingConfig">MicrosoftLicensingConfig</a>: <i>
      - <a href="microsoftlicensingconfigdefinition.md">MicrosoftLicensingConfigDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### DelayAccountLink

Boolean flag identifying whether account linking should be delayed
or not for the SDDC.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentType

Denotes if request is for a SingleAZ or a MultiAZ SDDC. Default : SingleAZ.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EdrsPolicyType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableEdrs

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostInstanceType

The instance type for the esx hosts in the primary cluster of the SDDC. Possible values : I3_METAL, I3EN_METAL and R5_METAL. Default value : I3_METAL. Currently I3EN_METAL host_instance_type does not support 1NODE and 2 node SDDC deployment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntranetMtuUplink

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxHosts

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinHosts

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumHost

The number of hosts.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderType

Determines what additional properties are available based on cloud
provider. Default value : AWS.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The AWS specific (e.g us-west-2) or VMC specific region (e.g US_WEST_2) of the cloud resources to work in.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SddcName

Name of the SDDC.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SddcTemplateId

If provided, configuration from the template will applied to the provisioned SDDC.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SddcType

Denotes the sddc type , if the value is null or empty, the type is considered
as default.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

The size of the vCenter and NSX appliances. 'large' or 'LARGE' SDDC size corresponds to a large vCenter appliance and large NSX appliance. 'medium' or 'MEDIUM' SDDC size corresponds to medium vCenter appliance and medium NSX appliance. Default : 'medium'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipCreatingVxlan

Boolean value to skip creating vxlan for compute gateway for SDDC provisioning.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SsoDomain

The SSO domain name to use for vSphere users. If not specified, vmc.local will be used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageCapacity

The storage capacity value to be requested for the SDDC primary cluster.
This variable is only for R5_METAL. Possible values are 15TB, 20TB, 25TB, 30TB, 35TB per host.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcCidr

SDDC management network CIDR. Only prefix of 16, 20 and 23 are supported. Note : Specify a private subnet range (RFC 1918) to be used for
vCenter Server, NSX Manager, and ESXi hosts. Choose a range that will not conflict with other networks you will connect to this SDDC.
Minimum CIDR sizes : /23 for up to 27 hosts, /20 for up to 251 hosts, /16 for up to 4091 hosts.
Reserved CIDRs : 10.0.0.0/15, 172.31.0.0/16.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VxlanSubnet

A logical network segment that will be created with the SDDC under the compute gateway.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountLinkSddcConfig

_Required_: No

_Type_: List of <a href="accountlinksddcconfigdefinition.md">AccountLinkSddcConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MicrosoftLicensingConfig

_Required_: No

_Type_: List of <a href="microsoftlicensingconfigdefinition.md">MicrosoftLicensingConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AvailabilityZones

Returns the <code>AvailabilityZones</code> value.

#### CloudPassword

Returns the <code>CloudPassword</code> value.

#### CloudUsername

Returns the <code>CloudUsername</code> value.

#### ClusterId

Cluster identifier.

#### ClusterInfo

Returns the <code>ClusterInfo</code> value.

#### Id

Returns the <code>Id</code> value.

#### NsxtReverseProxyUrl

Returns the <code>NsxtReverseProxyUrl</code> value.

#### SddcSize

Returns the <code>SddcSize</code> value.

#### SddcState

Returns the <code>SddcState</code> value.

#### VcUrl

Returns the <code>VcUrl</code> value.

