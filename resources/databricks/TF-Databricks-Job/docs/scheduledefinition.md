# TF::Databricks::Job ScheduleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#pausestatus" title="PauseStatus">PauseStatus</a>" : <i>String</i>,
    "<a href="#quartzcronexpression" title="QuartzCronExpression">QuartzCronExpression</a>" : <i>String</i>,
    "<a href="#timezoneid" title="TimezoneId">TimezoneId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#pausestatus" title="PauseStatus">PauseStatus</a>: <i>String</i>
<a href="#quartzcronexpression" title="QuartzCronExpression">QuartzCronExpression</a>: <i>String</i>
<a href="#timezoneid" title="TimezoneId">TimezoneId</a>: <i>String</i>
</pre>

## Properties

#### PauseStatus

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuartzCronExpression

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimezoneId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

