# TF::OpsGenie::NotificationPolicy DeDuplicationActionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#count" title="Count">Count</a>" : <i>Double</i>,
    "<a href="#deduplicationactiontype" title="DeDuplicationActionType">DeDuplicationActionType</a>" : <i>String</i>,
    "<a href="#duration" title="Duration">Duration</a>" : <i>[ <a href="durationdefinition.md">DurationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#count" title="Count">Count</a>: <i>Double</i>
<a href="#deduplicationactiontype" title="DeDuplicationActionType">DeDuplicationActionType</a>: <i>String</i>
<a href="#duration" title="Duration">Duration</a>: <i>
      - <a href="durationdefinition.md">DurationDefinition</a></i>
</pre>

## Properties

#### Count

- Count.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeDuplicationActionType

Deduplication type. Possible values are: "value-based", "frequency-based".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Duration

_Required_: No

_Type_: List of <a href="durationdefinition.md">DurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

