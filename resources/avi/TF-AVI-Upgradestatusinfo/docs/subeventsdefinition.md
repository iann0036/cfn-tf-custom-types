# TF::AVI::Upgradestatusinfo SubEventsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#duration" title="Duration">Duration</a>" : <i>Double</i>,
    "<a href="#endtime" title="EndTime">EndTime</a>" : <i>String</i>,
    "<a href="#message" title="Message">Message</a>" : <i>String</i>,
    "<a href="#starttime" title="StartTime">StartTime</a>" : <i>String</i>,
    "<a href="#status" title="Status">Status</a>" : <i>Boolean</i>,
    "<a href="#subtasks" title="SubTasks">SubTasks</a>" : <i>[ String, ... ]</i>,
    "<a href="#ip" title="Ip">Ip</a>" : <i>[ <a href="ipdefinition.md">IpDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#duration" title="Duration">Duration</a>: <i>Double</i>
<a href="#endtime" title="EndTime">EndTime</a>: <i>String</i>
<a href="#message" title="Message">Message</a>: <i>String</i>
<a href="#starttime" title="StartTime">StartTime</a>: <i>String</i>
<a href="#status" title="Status">Status</a>: <i>Boolean</i>
<a href="#subtasks" title="SubTasks">SubTasks</a>: <i>
      - String</i>
<a href="#ip" title="Ip">Ip</a>: <i>
      - <a href="ipdefinition.md">IpDefinition</a></i>
</pre>

## Properties

#### Duration

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Message

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubTasks

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

_Required_: No

_Type_: List of <a href="ipdefinition.md">IpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

