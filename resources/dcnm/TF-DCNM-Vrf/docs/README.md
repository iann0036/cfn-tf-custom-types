# TF::DCNM::Vrf

CloudFormation equivalent of dcnm_vrf

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::DCNM::Vrf",
    "Properties" : {
        "<a href="#advertisedefaultroute" title="AdvertiseDefaultRoute">AdvertiseDefaultRoute</a>" : <i>String</i>,
        "<a href="#advertisehostroute" title="AdvertiseHostRoute">AdvertiseHostRoute</a>" : <i>String</i>,
        "<a href="#deploy" title="Deploy">Deploy</a>" : <i>Boolean</i>,
        "<a href="#deploytimeout" title="DeployTimeout">DeployTimeout</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#extensiontemplate" title="ExtensionTemplate">ExtensionTemplate</a>" : <i>String</i>,
        "<a href="#fabricname" title="FabricName">FabricName</a>" : <i>String</i>,
        "<a href="#intfdescription" title="IntfDescription">IntfDescription</a>" : <i>String</i>,
        "<a href="#ipv6linklocalflag" title="Ipv6LinkLocalFlag">Ipv6LinkLocalFlag</a>" : <i>String</i>,
        "<a href="#loopbackid" title="LoopbackId">LoopbackId</a>" : <i>Double</i>,
        "<a href="#maxbgppath" title="MaxBgpPath">MaxBgpPath</a>" : <i>Double</i>,
        "<a href="#maxibgppath" title="MaxIbgpPath">MaxIbgpPath</a>" : <i>Double</i>,
        "<a href="#mtu" title="Mtu">Mtu</a>" : <i>Double</i>,
        "<a href="#mutlicastaddress" title="MutlicastAddress">MutlicastAddress</a>" : <i>String</i>,
        "<a href="#mutlicastgroup" title="MutlicastGroup">MutlicastGroup</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#rpaddress" title="RpAddress">RpAddress</a>" : <i>String</i>,
        "<a href="#rpexternalflag" title="RpExternalFlag">RpExternalFlag</a>" : <i>String</i>,
        "<a href="#segmentid" title="SegmentId">SegmentId</a>" : <i>String</i>,
        "<a href="#servicetemplate" title="ServiceTemplate">ServiceTemplate</a>" : <i>String</i>,
        "<a href="#source" title="Source">Source</a>" : <i>String</i>,
        "<a href="#staticdefaultroute" title="StaticDefaultRoute">StaticDefaultRoute</a>" : <i>String</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>String</i>,
        "<a href="#template" title="Template">Template</a>" : <i>String</i>,
        "<a href="#trmbgwmsiteflag" title="TrmBgwMsiteFlag">TrmBgwMsiteFlag</a>" : <i>String</i>,
        "<a href="#trmenable" title="TrmEnable">TrmEnable</a>" : <i>String</i>,
        "<a href="#vlanid" title="VlanId">VlanId</a>" : <i>Double</i>,
        "<a href="#vlanname" title="VlanName">VlanName</a>" : <i>String</i>,
        "<a href="#attachments" title="Attachments">Attachments</a>" : <i>[ <a href="attachmentsdefinition.md">AttachmentsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::DCNM::Vrf
Properties:
    <a href="#advertisedefaultroute" title="AdvertiseDefaultRoute">AdvertiseDefaultRoute</a>: <i>String</i>
    <a href="#advertisehostroute" title="AdvertiseHostRoute">AdvertiseHostRoute</a>: <i>String</i>
    <a href="#deploy" title="Deploy">Deploy</a>: <i>Boolean</i>
    <a href="#deploytimeout" title="DeployTimeout">DeployTimeout</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#extensiontemplate" title="ExtensionTemplate">ExtensionTemplate</a>: <i>String</i>
    <a href="#fabricname" title="FabricName">FabricName</a>: <i>String</i>
    <a href="#intfdescription" title="IntfDescription">IntfDescription</a>: <i>String</i>
    <a href="#ipv6linklocalflag" title="Ipv6LinkLocalFlag">Ipv6LinkLocalFlag</a>: <i>String</i>
    <a href="#loopbackid" title="LoopbackId">LoopbackId</a>: <i>Double</i>
    <a href="#maxbgppath" title="MaxBgpPath">MaxBgpPath</a>: <i>Double</i>
    <a href="#maxibgppath" title="MaxIbgpPath">MaxIbgpPath</a>: <i>Double</i>
    <a href="#mtu" title="Mtu">Mtu</a>: <i>Double</i>
    <a href="#mutlicastaddress" title="MutlicastAddress">MutlicastAddress</a>: <i>String</i>
    <a href="#mutlicastgroup" title="MutlicastGroup">MutlicastGroup</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#rpaddress" title="RpAddress">RpAddress</a>: <i>String</i>
    <a href="#rpexternalflag" title="RpExternalFlag">RpExternalFlag</a>: <i>String</i>
    <a href="#segmentid" title="SegmentId">SegmentId</a>: <i>String</i>
    <a href="#servicetemplate" title="ServiceTemplate">ServiceTemplate</a>: <i>String</i>
    <a href="#source" title="Source">Source</a>: <i>String</i>
    <a href="#staticdefaultroute" title="StaticDefaultRoute">StaticDefaultRoute</a>: <i>String</i>
    <a href="#tag" title="Tag">Tag</a>: <i>String</i>
    <a href="#template" title="Template">Template</a>: <i>String</i>
    <a href="#trmbgwmsiteflag" title="TrmBgwMsiteFlag">TrmBgwMsiteFlag</a>: <i>String</i>
    <a href="#trmenable" title="TrmEnable">TrmEnable</a>: <i>String</i>
    <a href="#vlanid" title="VlanId">VlanId</a>: <i>Double</i>
    <a href="#vlanname" title="VlanName">VlanName</a>: <i>String</i>
    <a href="#attachments" title="Attachments">Attachments</a>: <i>
      - <a href="attachmentsdefinition.md">AttachmentsDefinition</a></i>
</pre>

## Properties

#### AdvertiseDefaultRoute

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvertiseHostRoute

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Deploy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeployTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtensionTemplate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FabricName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntfDescription

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6LinkLocalFlag

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoopbackId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxBgpPath

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxIbgpPath

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mtu

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MutlicastAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MutlicastGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RpAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RpExternalFlag

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SegmentId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceTemplate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticDefaultRoute

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrmBgwMsiteFlag

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrmEnable

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Attachments

_Required_: No

_Type_: List of <a href="attachmentsdefinition.md">AttachmentsDefinition</a>

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

