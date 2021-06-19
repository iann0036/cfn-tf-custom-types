# TF::FortiOS::FirewallIppool

Configure IPv4 IP pools.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::FirewallIppool",
    "Properties" : {
        "<a href="#arpintf" title="ArpIntf">ArpIntf</a>" : <i>String</i>,
        "<a href="#arpreply" title="ArpReply">ArpReply</a>" : <i>String</i>,
        "<a href="#associatedinterface" title="AssociatedInterface">AssociatedInterface</a>" : <i>String</i>,
        "<a href="#blocksize" title="BlockSize">BlockSize</a>" : <i>Double</i>,
        "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
        "<a href="#endip" title="Endip">Endip</a>" : <i>String</i>,
        "<a href="#endport" title="Endport">Endport</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#numblocksperuser" title="NumBlocksPerUser">NumBlocksPerUser</a>" : <i>Double</i>,
        "<a href="#pbatimeout" title="PbaTimeout">PbaTimeout</a>" : <i>Double</i>,
        "<a href="#permitanyhost" title="PermitAnyHost">PermitAnyHost</a>" : <i>String</i>,
        "<a href="#portperuser" title="PortPerUser">PortPerUser</a>" : <i>Double</i>,
        "<a href="#sourceendip" title="SourceEndip">SourceEndip</a>" : <i>String</i>,
        "<a href="#sourcestartip" title="SourceStartip">SourceStartip</a>" : <i>String</i>,
        "<a href="#startip" title="Startip">Startip</a>" : <i>String</i>,
        "<a href="#startport" title="Startport">Startport</a>" : <i>Double</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::FirewallIppool
Properties:
    <a href="#arpintf" title="ArpIntf">ArpIntf</a>: <i>String</i>
    <a href="#arpreply" title="ArpReply">ArpReply</a>: <i>String</i>
    <a href="#associatedinterface" title="AssociatedInterface">AssociatedInterface</a>: <i>String</i>
    <a href="#blocksize" title="BlockSize">BlockSize</a>: <i>Double</i>
    <a href="#comments" title="Comments">Comments</a>: <i>String</i>
    <a href="#endip" title="Endip">Endip</a>: <i>String</i>
    <a href="#endport" title="Endport">Endport</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#numblocksperuser" title="NumBlocksPerUser">NumBlocksPerUser</a>: <i>Double</i>
    <a href="#pbatimeout" title="PbaTimeout">PbaTimeout</a>: <i>Double</i>
    <a href="#permitanyhost" title="PermitAnyHost">PermitAnyHost</a>: <i>String</i>
    <a href="#portperuser" title="PortPerUser">PortPerUser</a>: <i>Double</i>
    <a href="#sourceendip" title="SourceEndip">SourceEndip</a>: <i>String</i>
    <a href="#sourcestartip" title="SourceStartip">SourceStartip</a>: <i>String</i>
    <a href="#startip" title="Startip">Startip</a>: <i>String</i>
    <a href="#startport" title="Startport">Startport</a>: <i>Double</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### ArpIntf

Select an interface from available options that will reply to ARP requests. (If blank, any is selected).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ArpReply

Enable/disable replying to ARP requests when an IP Pool is added to a policy (default = enable). Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssociatedInterface

Associated interface name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockSize

Number of addresses in a block (64 to 4096, default = 128).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comments

Comment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Endip

Final IPv4 address (inclusive) in the range for the address pool (format xxx.xxx.xxx.xxx, Default: 0.0.0.0).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Endport

Final port number (inclusive) in the range for the address pool (Default: 65533).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

IP pool name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumBlocksPerUser

Number of addresses blocks that can be used by a user (1 to 128, default = 8).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PbaTimeout

Port block allocation timeout (seconds).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermitAnyHost

Enable/disable full cone NAT. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortPerUser

Number of port for each user (32 to 60416, default = 0, auto).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceEndip

Final IPv4 address (inclusive) in the range of the source addresses to be translated (format xxx.xxx.xxx.xxx, Default: 0.0.0.0).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceStartip

First IPv4 address (inclusive) in the range of the source addresses to be translated (format xxx.xxx.xxx.xxx, Default: 0.0.0.0).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Startip

First IPv4 address (inclusive) in the range for the address pool (format xxx.xxx.xxx.xxx, Default: 0.0.0.0).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Startport

First port number (inclusive) in the range for the address pool (Default: 5117).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

IP pool type (overload, one-to-one, fixed port range, or port block allocation). Valid values: `overload`, `one-to-one`, `fixed-port-range`, `port-block-allocation`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

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

