# TF::FortiOS::ExtendercontrollerExtender1 ControllerReportDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#interval" title="Interval">Interval</a>" : <i>Double</i>,
    "<a href="#signalthreshold" title="SignalThreshold">SignalThreshold</a>" : <i>Double</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#interval" title="Interval">Interval</a>: <i>Double</i>
<a href="#signalthreshold" title="SignalThreshold">SignalThreshold</a>: <i>Double</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
</pre>

## Properties

#### Interval

Controller report interval.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SignalThreshold

Controller report signal threshold.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

FortiExtender controller report status. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

