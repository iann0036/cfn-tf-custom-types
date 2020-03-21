# Terraform::Google::MonitoringAlertPolicy Conditions ConditionAbsent

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#duration" title="Duration">Duration</a>" : <i>String</i>,
    "<a href="#filter" title="Filter">Filter</a>" : <i>String</i>,
    "<a href="#aggregations" title="Aggregations">Aggregations</a>" : <i>[ <a href="conditions-conditionabsent-aggregations.md">Aggregations</a>, ... ]</i>,
    "<a href="#trigger" title="Trigger">Trigger</a>" : <i>[ <a href="conditions-conditionabsent-trigger.md">Trigger</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#duration" title="Duration">Duration</a>: <i>String</i>
<a href="#filter" title="Filter">Filter</a>: <i>String</i>
<a href="#aggregations" title="Aggregations">Aggregations</a>: <i>
      - <a href="conditions-conditionabsent-aggregations.md">Aggregations</a></i>
<a href="#trigger" title="Trigger">Trigger</a>: <i>
      - <a href="conditions-conditionabsent-trigger.md">Trigger</a></i>
</pre>

## Properties

#### Duration

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Aggregations

_Required_: No
_Type_: List of <a href="conditions-conditionabsent-aggregations.md">Aggregations</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trigger

_Required_: No
_Type_: List of <a href="conditions-conditionabsent-trigger.md">Trigger</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

