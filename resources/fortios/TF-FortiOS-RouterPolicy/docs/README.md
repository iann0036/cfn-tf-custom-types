# TF::FortiOS::RouterPolicy

Configure IPv4 routing policies.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::RouterPolicy",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
        "<a href="#dstnegate" title="DstNegate">DstNegate</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#endport" title="EndPort">EndPort</a>" : <i>Double</i>,
        "<a href="#endsourceport" title="EndSourcePort">EndSourcePort</a>" : <i>Double</i>,
        "<a href="#gateway" title="Gateway">Gateway</a>" : <i>String</i>,
        "<a href="#inputdevicenegate" title="InputDeviceNegate">InputDeviceNegate</a>" : <i>String</i>,
        "<a href="#outputdevice" title="OutputDevice">OutputDevice</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>Double</i>,
        "<a href="#seqnum" title="SeqNum">SeqNum</a>" : <i>Double</i>,
        "<a href="#srcnegate" title="SrcNegate">SrcNegate</a>" : <i>String</i>,
        "<a href="#startport" title="StartPort">StartPort</a>" : <i>Double</i>,
        "<a href="#startsourceport" title="StartSourcePort">StartSourcePort</a>" : <i>Double</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#tos" title="Tos">Tos</a>" : <i>String</i>,
        "<a href="#tosmask" title="TosMask">TosMask</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#dst" title="Dst">Dst</a>" : <i>[ <a href="dstdefinition.md">DstDefinition</a>, ... ]</i>,
        "<a href="#dstaddr" title="Dstaddr">Dstaddr</a>" : <i>[ <a href="dstaddrdefinition.md">DstaddrDefinition</a>, ... ]</i>,
        "<a href="#inputdevice" title="InputDevice">InputDevice</a>" : <i>[ <a href="inputdevicedefinition.md">InputDeviceDefinition</a>, ... ]</i>,
        "<a href="#internetservicecustom" title="InternetServiceCustom">InternetServiceCustom</a>" : <i>[ <a href="internetservicecustomdefinition.md">InternetServiceCustomDefinition</a>, ... ]</i>,
        "<a href="#internetserviceid" title="InternetServiceId">InternetServiceId</a>" : <i>[ <a href="internetserviceiddefinition.md">InternetServiceIdDefinition</a>, ... ]</i>,
        "<a href="#src" title="Src">Src</a>" : <i>[ <a href="srcdefinition.md">SrcDefinition</a>, ... ]</i>,
        "<a href="#srcaddr" title="Srcaddr">Srcaddr</a>" : <i>[ <a href="srcaddrdefinition.md">SrcaddrDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::RouterPolicy
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#comments" title="Comments">Comments</a>: <i>String</i>
    <a href="#dstnegate" title="DstNegate">DstNegate</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#endport" title="EndPort">EndPort</a>: <i>Double</i>
    <a href="#endsourceport" title="EndSourcePort">EndSourcePort</a>: <i>Double</i>
    <a href="#gateway" title="Gateway">Gateway</a>: <i>String</i>
    <a href="#inputdevicenegate" title="InputDeviceNegate">InputDeviceNegate</a>: <i>String</i>
    <a href="#outputdevice" title="OutputDevice">OutputDevice</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>Double</i>
    <a href="#seqnum" title="SeqNum">SeqNum</a>: <i>Double</i>
    <a href="#srcnegate" title="SrcNegate">SrcNegate</a>: <i>String</i>
    <a href="#startport" title="StartPort">StartPort</a>: <i>Double</i>
    <a href="#startsourceport" title="StartSourcePort">StartSourcePort</a>: <i>Double</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#tos" title="Tos">Tos</a>: <i>String</i>
    <a href="#tosmask" title="TosMask">TosMask</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#dst" title="Dst">Dst</a>: <i>
      - <a href="dstdefinition.md">DstDefinition</a></i>
    <a href="#dstaddr" title="Dstaddr">Dstaddr</a>: <i>
      - <a href="dstaddrdefinition.md">DstaddrDefinition</a></i>
    <a href="#inputdevice" title="InputDevice">InputDevice</a>: <i>
      - <a href="inputdevicedefinition.md">InputDeviceDefinition</a></i>
    <a href="#internetservicecustom" title="InternetServiceCustom">InternetServiceCustom</a>: <i>
      - <a href="internetservicecustomdefinition.md">InternetServiceCustomDefinition</a></i>
    <a href="#internetserviceid" title="InternetServiceId">InternetServiceId</a>: <i>
      - <a href="internetserviceiddefinition.md">InternetServiceIdDefinition</a></i>
    <a href="#src" title="Src">Src</a>: <i>
      - <a href="srcdefinition.md">SrcDefinition</a></i>
    <a href="#srcaddr" title="Srcaddr">Srcaddr</a>: <i>
      - <a href="srcaddrdefinition.md">SrcaddrDefinition</a></i>
</pre>

## Properties

#### Action

Action of the policy route. Valid values: `deny`, `permit`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comments

Optional comments.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DstNegate

Enable/disable negating destination address match. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndPort

End destination port number (0 - 65535).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndSourcePort

End source port number (0 - 65535).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gateway

IP address of the gateway.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InputDeviceNegate

Enable/disable negation of input device match. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutputDevice

Outgoing interface name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Protocol number (0 - 255).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeqNum

Sequence number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcNegate

Enable/disable negating source address match. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartPort

Start destination port number (0 - 65535).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartSourcePort

Start source port number (0 - 65535).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable this policy route. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tos

Type of service bit pattern.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TosMask

Type of service evaluated bits.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dst

_Required_: No

_Type_: List of <a href="dstdefinition.md">DstDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dstaddr

_Required_: No

_Type_: List of <a href="dstaddrdefinition.md">DstaddrDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InputDevice

_Required_: No

_Type_: List of <a href="inputdevicedefinition.md">InputDeviceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceCustom

_Required_: No

_Type_: List of <a href="internetservicecustomdefinition.md">InternetServiceCustomDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceId

_Required_: No

_Type_: List of <a href="internetserviceiddefinition.md">InternetServiceIdDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Src

_Required_: No

_Type_: List of <a href="srcdefinition.md">SrcDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Srcaddr

_Required_: No

_Type_: List of <a href="srcaddrdefinition.md">SrcaddrDefinition</a>

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

