# TF::FortiOS::VoipProfile SccpDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#blockmcast" title="BlockMcast">BlockMcast</a>" : <i>String</i>,
    "<a href="#logcallsummary" title="LogCallSummary">LogCallSummary</a>" : <i>String</i>,
    "<a href="#logviolations" title="LogViolations">LogViolations</a>" : <i>String</i>,
    "<a href="#maxcalls" title="MaxCalls">MaxCalls</a>" : <i>Double</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#verifyheader" title="VerifyHeader">VerifyHeader</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#blockmcast" title="BlockMcast">BlockMcast</a>: <i>String</i>
<a href="#logcallsummary" title="LogCallSummary">LogCallSummary</a>: <i>String</i>
<a href="#logviolations" title="LogViolations">LogViolations</a>: <i>String</i>
<a href="#maxcalls" title="MaxCalls">MaxCalls</a>: <i>Double</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#verifyheader" title="VerifyHeader">VerifyHeader</a>: <i>String</i>
</pre>

## Properties

#### BlockMcast

Enable/disable block multicast RTP connections. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogCallSummary

Enable/disable log summary of SCCP calls. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogViolations

Enable/disable logging of SCCP violations. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxCalls

Maximum calls per minute per SCCP client (max 65535).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable SCCP. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VerifyHeader

Enable/disable verify SCCP header content. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

