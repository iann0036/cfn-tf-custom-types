# TF::DCNM::Network

CloudFormation equivalent of dcnm_network

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::DCNM::Network",
    "Properties" : {
        "<a href="#arpsuppflag" title="ArpSuppFlag">ArpSuppFlag</a>" : <i>Boolean</i>,
        "<a href="#deploy" title="Deploy">Deploy</a>" : <i>Boolean</i>,
        "<a href="#deploytimeout" title="DeployTimeout">DeployTimeout</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#dhcp1" title="Dhcp1">Dhcp1</a>" : <i>String</i>,
        "<a href="#dhcp2" title="Dhcp2">Dhcp2</a>" : <i>String</i>,
        "<a href="#dhcpvrf" title="DhcpVrf">DhcpVrf</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#extensiontemplate" title="ExtensionTemplate">ExtensionTemplate</a>" : <i>String</i>,
        "<a href="#fabricname" title="FabricName">FabricName</a>" : <i>String</i>,
        "<a href="#ipv4gateway" title="Ipv4Gateway">Ipv4Gateway</a>" : <i>String</i>,
        "<a href="#ipv6gateway" title="Ipv6Gateway">Ipv6Gateway</a>" : <i>String</i>,
        "<a href="#irenableflag" title="IrEnableFlag">IrEnableFlag</a>" : <i>Boolean</i>,
        "<a href="#l2onlyflag" title="L2OnlyFlag">L2OnlyFlag</a>" : <i>Boolean</i>,
        "<a href="#l3gatewayflag" title="L3GatewayFlag">L3GatewayFlag</a>" : <i>Boolean</i>,
        "<a href="#loopbackid" title="LoopbackId">LoopbackId</a>" : <i>Double</i>,
        "<a href="#mcastgroup" title="McastGroup">McastGroup</a>" : <i>String</i>,
        "<a href="#mtu" title="Mtu">Mtu</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkid" title="NetworkId">NetworkId</a>" : <i>String</i>,
        "<a href="#rtbothflag" title="RtBothFlag">RtBothFlag</a>" : <i>Boolean</i>,
        "<a href="#secondarygw1" title="SecondaryGw1">SecondaryGw1</a>" : <i>String</i>,
        "<a href="#secondarygw2" title="SecondaryGw2">SecondaryGw2</a>" : <i>String</i>,
        "<a href="#servicetemplate" title="ServiceTemplate">ServiceTemplate</a>" : <i>String</i>,
        "<a href="#source" title="Source">Source</a>" : <i>String</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>String</i>,
        "<a href="#template" title="Template">Template</a>" : <i>String</i>,
        "<a href="#trmenableflag" title="TrmEnableFlag">TrmEnableFlag</a>" : <i>Boolean</i>,
        "<a href="#vlanid" title="VlanId">VlanId</a>" : <i>Double</i>,
        "<a href="#vlanname" title="VlanName">VlanName</a>" : <i>String</i>,
        "<a href="#vrfname" title="VrfName">VrfName</a>" : <i>String</i>,
        "<a href="#attachments" title="Attachments">Attachments</a>" : <i>[ <a href="attachmentsdefinition.md">AttachmentsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::DCNM::Network
Properties:
    <a href="#arpsuppflag" title="ArpSuppFlag">ArpSuppFlag</a>: <i>Boolean</i>
    <a href="#deploy" title="Deploy">Deploy</a>: <i>Boolean</i>
    <a href="#deploytimeout" title="DeployTimeout">DeployTimeout</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#dhcp1" title="Dhcp1">Dhcp1</a>: <i>String</i>
    <a href="#dhcp2" title="Dhcp2">Dhcp2</a>: <i>String</i>
    <a href="#dhcpvrf" title="DhcpVrf">DhcpVrf</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#extensiontemplate" title="ExtensionTemplate">ExtensionTemplate</a>: <i>String</i>
    <a href="#fabricname" title="FabricName">FabricName</a>: <i>String</i>
    <a href="#ipv4gateway" title="Ipv4Gateway">Ipv4Gateway</a>: <i>String</i>
    <a href="#ipv6gateway" title="Ipv6Gateway">Ipv6Gateway</a>: <i>String</i>
    <a href="#irenableflag" title="IrEnableFlag">IrEnableFlag</a>: <i>Boolean</i>
    <a href="#l2onlyflag" title="L2OnlyFlag">L2OnlyFlag</a>: <i>Boolean</i>
    <a href="#l3gatewayflag" title="L3GatewayFlag">L3GatewayFlag</a>: <i>Boolean</i>
    <a href="#loopbackid" title="LoopbackId">LoopbackId</a>: <i>Double</i>
    <a href="#mcastgroup" title="McastGroup">McastGroup</a>: <i>String</i>
    <a href="#mtu" title="Mtu">Mtu</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkid" title="NetworkId">NetworkId</a>: <i>String</i>
    <a href="#rtbothflag" title="RtBothFlag">RtBothFlag</a>: <i>Boolean</i>
    <a href="#secondarygw1" title="SecondaryGw1">SecondaryGw1</a>: <i>String</i>
    <a href="#secondarygw2" title="SecondaryGw2">SecondaryGw2</a>: <i>String</i>
    <a href="#servicetemplate" title="ServiceTemplate">ServiceTemplate</a>: <i>String</i>
    <a href="#source" title="Source">Source</a>: <i>String</i>
    <a href="#tag" title="Tag">Tag</a>: <i>String</i>
    <a href="#template" title="Template">Template</a>: <i>String</i>
    <a href="#trmenableflag" title="TrmEnableFlag">TrmEnableFlag</a>: <i>Boolean</i>
    <a href="#vlanid" title="VlanId">VlanId</a>: <i>Double</i>
    <a href="#vlanname" title="VlanName">VlanName</a>: <i>String</i>
    <a href="#vrfname" title="VrfName">VrfName</a>: <i>String</i>
    <a href="#attachments" title="Attachments">Attachments</a>: <i>
      - <a href="attachmentsdefinition.md">AttachmentsDefinition</a></i>
</pre>

## Properties

#### ArpSuppFlag

_Required_: No

_Type_: Boolean

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

#### Dhcp1

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dhcp2

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpVrf

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

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

#### Ipv4Gateway

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6Gateway

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IrEnableFlag

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L2OnlyFlag

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L3GatewayFlag

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoopbackId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### McastGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mtu

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RtBothFlag

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryGw1

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryGw2

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

#### Tag

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrmEnableFlag

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VrfName

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

