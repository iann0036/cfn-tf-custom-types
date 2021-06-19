# TF::FortiOS::WirelesscontrollerIntercontroller

Configure inter wireless controller operation.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::WirelesscontrollerIntercontroller",
    "Properties" : {
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#fastfailovermax" title="FastFailoverMax">FastFailoverMax</a>" : <i>Double</i>,
        "<a href="#fastfailoverwait" title="FastFailoverWait">FastFailoverWait</a>" : <i>Double</i>,
        "<a href="#intercontrollerkey" title="InterControllerKey">InterControllerKey</a>" : <i>String</i>,
        "<a href="#intercontrollermode" title="InterControllerMode">InterControllerMode</a>" : <i>String</i>,
        "<a href="#intercontrollerpri" title="InterControllerPri">InterControllerPri</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#intercontrollerpeer" title="InterControllerPeer">InterControllerPeer</a>" : <i>[ <a href="intercontrollerpeerdefinition.md">InterControllerPeerDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::WirelesscontrollerIntercontroller
Properties:
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#fastfailovermax" title="FastFailoverMax">FastFailoverMax</a>: <i>Double</i>
    <a href="#fastfailoverwait" title="FastFailoverWait">FastFailoverWait</a>: <i>Double</i>
    <a href="#intercontrollerkey" title="InterControllerKey">InterControllerKey</a>: <i>String</i>
    <a href="#intercontrollermode" title="InterControllerMode">InterControllerMode</a>: <i>String</i>
    <a href="#intercontrollerpri" title="InterControllerPri">InterControllerPri</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#intercontrollerpeer" title="InterControllerPeer">InterControllerPeer</a>: <i>
      - <a href="intercontrollerpeerdefinition.md">InterControllerPeerDefinition</a></i>
</pre>

## Properties

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FastFailoverMax

Maximum number of retransmissions for fast failover HA messages between peer wireless controllers (3 - 64, default = 10).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FastFailoverWait

Minimum wait time before an AP transitions from secondary controller to primary controller (10 - 86400 sec, default = 10).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterControllerKey

Secret key for inter-controller communications.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterControllerMode

Configure inter-controller mode (disable, l2-roaming, 1+1, default = disable). Valid values: `disable`, `l2-roaming`, `1+1`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterControllerPri

Configure inter-controller's priority (primary or secondary, default = primary). Valid values: `primary`, `secondary`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterControllerPeer

_Required_: No

_Type_: List of <a href="intercontrollerpeerdefinition.md">InterControllerPeerDefinition</a>

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

