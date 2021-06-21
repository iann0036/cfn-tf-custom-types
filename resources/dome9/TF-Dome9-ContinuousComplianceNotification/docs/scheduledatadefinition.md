# TF::Dome9::ContinuousComplianceNotification ScheduleDataDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cronexpression" title="CronExpression">CronExpression</a>" : <i>String</i>,
    "<a href="#recipients" title="Recipients">Recipients</a>" : <i>[ String, ... ]</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#cronexpression" title="CronExpression">CronExpression</a>: <i>String</i>
<a href="#recipients" title="Recipients">Recipients</a>: <i>
      - String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### CronExpression

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Recipients

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
