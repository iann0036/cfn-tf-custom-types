# TF::AVI::Ipamdnsproviderprofile

The IpamDnsProviderProfile resource allows the creation and management of Avi IpamDnsProviderProfile

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Ipamdnsproviderprofile",
    "Properties" : {
        "<a href="#allocateipinvrf" title="AllocateIpInVrf">AllocateIpInVrf</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#awsprofile" title="AwsProfile">AwsProfile</a>" : <i>[ <a href="awsprofiledefinition.md">AwsProfileDefinition</a>, ... ]</i>,
        "<a href="#azureprofile" title="AzureProfile">AzureProfile</a>" : <i>[ <a href="azureprofiledefinition.md">AzureProfileDefinition</a>, ... ]</i>,
        "<a href="#customprofile" title="CustomProfile">CustomProfile</a>" : <i>[ <a href="customprofiledefinition.md">CustomProfileDefinition</a>, ... ]</i>,
        "<a href="#gcpprofile" title="GcpProfile">GcpProfile</a>" : <i>[ <a href="gcpprofiledefinition.md">GcpProfileDefinition</a>, ... ]</i>,
        "<a href="#infobloxprofile" title="InfobloxProfile">InfobloxProfile</a>" : <i>[ <a href="infobloxprofiledefinition.md">InfobloxProfileDefinition</a>, ... ]</i>,
        "<a href="#internalprofile" title="InternalProfile">InternalProfile</a>" : <i>[ <a href="internalprofiledefinition.md">InternalProfileDefinition</a>, ... ]</i>,
        "<a href="#markers" title="Markers">Markers</a>" : <i>[ <a href="markersdefinition.md">MarkersDefinition</a>, ... ]</i>,
        "<a href="#ociprofile" title="OciProfile">OciProfile</a>" : <i>[ <a href="ociprofiledefinition.md">OciProfileDefinition</a>, ... ]</i>,
        "<a href="#openstackprofile" title="OpenstackProfile">OpenstackProfile</a>" : <i>[ <a href="openstackprofiledefinition.md">OpenstackProfileDefinition</a>, ... ]</i>,
        "<a href="#proxyconfiguration" title="ProxyConfiguration">ProxyConfiguration</a>" : <i>[ <a href="proxyconfigurationdefinition.md">ProxyConfigurationDefinition</a>, ... ]</i>,
        "<a href="#tencentprofile" title="TencentProfile">TencentProfile</a>" : <i>[ <a href="tencentprofiledefinition.md">TencentProfileDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Ipamdnsproviderprofile
Properties:
    <a href="#allocateipinvrf" title="AllocateIpInVrf">AllocateIpInVrf</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#awsprofile" title="AwsProfile">AwsProfile</a>: <i>
      - <a href="awsprofiledefinition.md">AwsProfileDefinition</a></i>
    <a href="#azureprofile" title="AzureProfile">AzureProfile</a>: <i>
      - <a href="azureprofiledefinition.md">AzureProfileDefinition</a></i>
    <a href="#customprofile" title="CustomProfile">CustomProfile</a>: <i>
      - <a href="customprofiledefinition.md">CustomProfileDefinition</a></i>
    <a href="#gcpprofile" title="GcpProfile">GcpProfile</a>: <i>
      - <a href="gcpprofiledefinition.md">GcpProfileDefinition</a></i>
    <a href="#infobloxprofile" title="InfobloxProfile">InfobloxProfile</a>: <i>
      - <a href="infobloxprofiledefinition.md">InfobloxProfileDefinition</a></i>
    <a href="#internalprofile" title="InternalProfile">InternalProfile</a>: <i>
      - <a href="internalprofiledefinition.md">InternalProfileDefinition</a></i>
    <a href="#markers" title="Markers">Markers</a>: <i>
      - <a href="markersdefinition.md">MarkersDefinition</a></i>
    <a href="#ociprofile" title="OciProfile">OciProfile</a>: <i>
      - <a href="ociprofiledefinition.md">OciProfileDefinition</a></i>
    <a href="#openstackprofile" title="OpenstackProfile">OpenstackProfile</a>: <i>
      - <a href="openstackprofiledefinition.md">OpenstackProfileDefinition</a></i>
    <a href="#proxyconfiguration" title="ProxyConfiguration">ProxyConfiguration</a>: <i>
      - <a href="proxyconfigurationdefinition.md">ProxyConfigurationDefinition</a></i>
    <a href="#tencentprofile" title="TencentProfile">TencentProfile</a>: <i>
      - <a href="tencentprofiledefinition.md">TencentProfileDefinition</a></i>
</pre>

## Properties

#### AllocateIpInVrf

If this flag is set, only allocate ip from networks in the virtual service vrf. Applicable for avi vantage ipam only. Field introduced in 17.2.4.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name for the ipam/dns provider profile.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

It is a reference to an object of type tenant.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Provider type for the ipam/dns provider profile. Enum options - IPAMDNS_TYPE_INFOBLOX, IPAMDNS_TYPE_AWS, IPAMDNS_TYPE_OPENSTACK, IPAMDNS_TYPE_GCP, IPAMDNS_TYPE_INFOBLOX_DNS, IPAMDNS_TYPE_CUSTOM, IPAMDNS_TYPE_CUSTOM_DNS, IPAMDNS_TYPE_AZURE, IPAMDNS_TYPE_OCI, IPAMDNS_TYPE_TENCENT, IPAMDNS_TYPE_INTERNAL, IPAMDNS_TYPE_INTERNAL_DNS, IPAMDNS_TYPE_AWS_DNS, IPAMDNS_TYPE_AZURE_DNS. Allowed in basic(allowed values- ipamdns_type_internal) edition, essentials(allowed values- ipamdns_type_internal) edition, enterprise edition.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsProfile

_Required_: No

_Type_: List of <a href="awsprofiledefinition.md">AwsProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureProfile

_Required_: No

_Type_: List of <a href="azureprofiledefinition.md">AzureProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomProfile

_Required_: No

_Type_: List of <a href="customprofiledefinition.md">CustomProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcpProfile

_Required_: No

_Type_: List of <a href="gcpprofiledefinition.md">GcpProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InfobloxProfile

_Required_: No

_Type_: List of <a href="infobloxprofiledefinition.md">InfobloxProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternalProfile

_Required_: No

_Type_: List of <a href="internalprofiledefinition.md">InternalProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Markers

_Required_: No

_Type_: List of <a href="markersdefinition.md">MarkersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OciProfile

_Required_: No

_Type_: List of <a href="ociprofiledefinition.md">OciProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenstackProfile

_Required_: No

_Type_: List of <a href="openstackprofiledefinition.md">OpenstackProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyConfiguration

_Required_: No

_Type_: List of <a href="proxyconfigurationdefinition.md">ProxyConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TencentProfile

_Required_: No

_Type_: List of <a href="tencentprofiledefinition.md">TencentProfileDefinition</a>

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

