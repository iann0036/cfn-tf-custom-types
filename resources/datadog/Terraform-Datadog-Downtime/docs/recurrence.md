# Terraform::Datadog::Downtime Recurrence

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#period" title="Period">Period</a>" : <i>Double</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#untildate" title="UntilDate">UntilDate</a>" : <i>Double</i>,
    "<a href="#untiloccurrences" title="UntilOccurrences">UntilOccurrences</a>" : <i>Double</i>,
    "<a href="#weekdays" title="WeekDays">WeekDays</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#period" title="Period">Period</a>: <i>Double</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#untildate" title="UntilDate">UntilDate</a>: <i>Double</i>
<a href="#untiloccurrences" title="UntilOccurrences">UntilOccurrences</a>: <i>Double</i>
<a href="#weekdays" title="WeekDays">WeekDays</a>: <i>
      - String</i>
</pre>

## Properties

#### Period

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UntilDate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UntilOccurrences

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeekDays

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

