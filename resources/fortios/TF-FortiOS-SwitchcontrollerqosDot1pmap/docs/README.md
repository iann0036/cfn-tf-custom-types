# TF::FortiOS::SwitchcontrollerqosDot1pmap

Configure FortiSwitch QoS 802.1p.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SwitchcontrollerqosDot1pmap",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#egresspritagging" title="EgressPriTagging">EgressPriTagging</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#priority0" title="Priority0">Priority0</a>" : <i>String</i>,
        "<a href="#priority1" title="Priority1">Priority1</a>" : <i>String</i>,
        "<a href="#priority2" title="Priority2">Priority2</a>" : <i>String</i>,
        "<a href="#priority3" title="Priority3">Priority3</a>" : <i>String</i>,
        "<a href="#priority4" title="Priority4">Priority4</a>" : <i>String</i>,
        "<a href="#priority5" title="Priority5">Priority5</a>" : <i>String</i>,
        "<a href="#priority6" title="Priority6">Priority6</a>" : <i>String</i>,
        "<a href="#priority7" title="Priority7">Priority7</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SwitchcontrollerqosDot1pmap
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#egresspritagging" title="EgressPriTagging">EgressPriTagging</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#priority0" title="Priority0">Priority0</a>: <i>String</i>
    <a href="#priority1" title="Priority1">Priority1</a>: <i>String</i>
    <a href="#priority2" title="Priority2">Priority2</a>: <i>String</i>
    <a href="#priority3" title="Priority3">Priority3</a>: <i>String</i>
    <a href="#priority4" title="Priority4">Priority4</a>: <i>String</i>
    <a href="#priority5" title="Priority5">Priority5</a>: <i>String</i>
    <a href="#priority6" title="Priority6">Priority6</a>: <i>String</i>
    <a href="#priority7" title="Priority7">Priority7</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### Description

Description of the 802.1p name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EgressPriTagging

Enable/disable egress priority-tag frame. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Dot1p map name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority0

COS queue mapped to dot1p priority number. Valid values: `queue-0`, `queue-1`, `queue-2`, `queue-3`, `queue-4`, `queue-5`, `queue-6`, `queue-7`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority1

COS queue mapped to dot1p priority number. Valid values: `queue-0`, `queue-1`, `queue-2`, `queue-3`, `queue-4`, `queue-5`, `queue-6`, `queue-7`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority2

COS queue mapped to dot1p priority number. Valid values: `queue-0`, `queue-1`, `queue-2`, `queue-3`, `queue-4`, `queue-5`, `queue-6`, `queue-7`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority3

COS queue mapped to dot1p priority number. Valid values: `queue-0`, `queue-1`, `queue-2`, `queue-3`, `queue-4`, `queue-5`, `queue-6`, `queue-7`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority4

COS queue mapped to dot1p priority number. Valid values: `queue-0`, `queue-1`, `queue-2`, `queue-3`, `queue-4`, `queue-5`, `queue-6`, `queue-7`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority5

COS queue mapped to dot1p priority number. Valid values: `queue-0`, `queue-1`, `queue-2`, `queue-3`, `queue-4`, `queue-5`, `queue-6`, `queue-7`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority6

COS queue mapped to dot1p priority number. Valid values: `queue-0`, `queue-1`, `queue-2`, `queue-3`, `queue-4`, `queue-5`, `queue-6`, `queue-7`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority7

COS queue mapped to dot1p priority number. Valid values: `queue-0`, `queue-1`, `queue-2`, `queue-3`, `queue-4`, `queue-5`, `queue-6`, `queue-7`.

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

