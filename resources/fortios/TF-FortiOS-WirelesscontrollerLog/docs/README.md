# TF::FortiOS::WirelesscontrollerLog

Configure wireless controller event log filters.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::WirelesscontrollerLog",
    "Properties" : {
        "<a href="#addrgrplog" title="AddrgrpLog">AddrgrpLog</a>" : <i>String</i>,
        "<a href="#blelog" title="BleLog">BleLog</a>" : <i>String</i>,
        "<a href="#clblog" title="ClbLog">ClbLog</a>" : <i>String</i>,
        "<a href="#dhcpstarvlog" title="DhcpStarvLog">DhcpStarvLog</a>" : <i>String</i>,
        "<a href="#ledschedlog" title="LedSchedLog">LedSchedLog</a>" : <i>String</i>,
        "<a href="#radioeventlog" title="RadioEventLog">RadioEventLog</a>" : <i>String</i>,
        "<a href="#rogueeventlog" title="RogueEventLog">RogueEventLog</a>" : <i>String</i>,
        "<a href="#staeventlog" title="StaEventLog">StaEventLog</a>" : <i>String</i>,
        "<a href="#stalocatelog" title="StaLocateLog">StaLocateLog</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#widslog" title="WidsLog">WidsLog</a>" : <i>String</i>,
        "<a href="#wtpeventlog" title="WtpEventLog">WtpEventLog</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::WirelesscontrollerLog
Properties:
    <a href="#addrgrplog" title="AddrgrpLog">AddrgrpLog</a>: <i>String</i>
    <a href="#blelog" title="BleLog">BleLog</a>: <i>String</i>
    <a href="#clblog" title="ClbLog">ClbLog</a>: <i>String</i>
    <a href="#dhcpstarvlog" title="DhcpStarvLog">DhcpStarvLog</a>: <i>String</i>
    <a href="#ledschedlog" title="LedSchedLog">LedSchedLog</a>: <i>String</i>
    <a href="#radioeventlog" title="RadioEventLog">RadioEventLog</a>: <i>String</i>
    <a href="#rogueeventlog" title="RogueEventLog">RogueEventLog</a>: <i>String</i>
    <a href="#staeventlog" title="StaEventLog">StaEventLog</a>: <i>String</i>
    <a href="#stalocatelog" title="StaLocateLog">StaLocateLog</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#widslog" title="WidsLog">WidsLog</a>: <i>String</i>
    <a href="#wtpeventlog" title="WtpEventLog">WtpEventLog</a>: <i>String</i>
</pre>

## Properties

#### AddrgrpLog

Lowest severity level to log address group message. Valid values: `emergency`, `alert`, `critical`, `error`, `warning`, `notification`, `information`, `debug`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BleLog

Lowest severity level to log BLE detection message. Valid values: `emergency`, `alert`, `critical`, `error`, `warning`, `notification`, `information`, `debug`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClbLog

Lowest severity level to log client load balancing message. Valid values: `emergency`, `alert`, `critical`, `error`, `warning`, `notification`, `information`, `debug`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpStarvLog

Lowest severity level to log DHCP starvation event message. Valid values: `emergency`, `alert`, `critical`, `error`, `warning`, `notification`, `information`, `debug`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LedSchedLog

Lowest severity level to log LED schedule event message. Valid values: `emergency`, `alert`, `critical`, `error`, `warning`, `notification`, `information`, `debug`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RadioEventLog

Lowest severity level to log radio event message. Valid values: `emergency`, `alert`, `critical`, `error`, `warning`, `notification`, `information`, `debug`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RogueEventLog

Lowest severity level to log rogue AP event message. Valid values: `emergency`, `alert`, `critical`, `error`, `warning`, `notification`, `information`, `debug`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaEventLog

Lowest severity level to log station event message. Valid values: `emergency`, `alert`, `critical`, `error`, `warning`, `notification`, `information`, `debug`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaLocateLog

Lowest severity level to log station locate message. Valid values: `emergency`, `alert`, `critical`, `error`, `warning`, `notification`, `information`, `debug`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable wireless event logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WidsLog

Lowest severity level to log WIDS message. Valid values: `emergency`, `alert`, `critical`, `error`, `warning`, `notification`, `information`, `debug`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WtpEventLog

Lowest severity level to log WTP event message. Valid values: `emergency`, `alert`, `critical`, `error`, `warning`, `notification`, `information`, `debug`.

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

