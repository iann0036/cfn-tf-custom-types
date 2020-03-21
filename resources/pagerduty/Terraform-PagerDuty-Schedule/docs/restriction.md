# Terraform::PagerDuty::Schedule Restriction

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#durationseconds" title="DurationSeconds">DurationSeconds</a>" : <i>Double</i>,
    "<a href="#startdayofweek" title="StartDayOfWeek">StartDayOfWeek</a>" : <i>Double</i>,
    "<a href="#starttimeofday" title="StartTimeOfDay">StartTimeOfDay</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#durationseconds" title="DurationSeconds">DurationSeconds</a>: <i>Double</i>
<a href="#startdayofweek" title="StartDayOfWeek">StartDayOfWeek</a>: <i>Double</i>
<a href="#starttimeofday" title="StartTimeOfDay">StartTimeOfDay</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### DurationSeconds

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartDayOfWeek

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTimeOfDay

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

