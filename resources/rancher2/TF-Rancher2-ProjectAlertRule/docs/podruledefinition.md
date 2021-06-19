# TF::Rancher2::ProjectAlertRule PodRuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#condition" title="Condition">Condition</a>" : <i>String</i>,
    "<a href="#podid" title="PodId">PodId</a>" : <i>String</i>,
    "<a href="#restartintervalseconds" title="RestartIntervalSeconds">RestartIntervalSeconds</a>" : <i>Double</i>,
    "<a href="#restarttimes" title="RestartTimes">RestartTimes</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#condition" title="Condition">Condition</a>: <i>String</i>
<a href="#podid" title="PodId">PodId</a>: <i>String</i>
<a href="#restartintervalseconds" title="RestartIntervalSeconds">RestartIntervalSeconds</a>: <i>Double</i>
<a href="#restarttimes" title="RestartTimes">RestartTimes</a>: <i>Double</i>
</pre>

## Properties

#### Condition

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PodId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestartIntervalSeconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestartTimes

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

