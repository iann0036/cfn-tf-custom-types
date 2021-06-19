# TF::AzureRM::HdinsightSparkCluster AutoscaleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#capacity" title="Capacity">Capacity</a>" : <i>[ <a href="capacitydefinition.md">CapacityDefinition</a>, ... ]</i>,
    "<a href="#recurrence" title="Recurrence">Recurrence</a>" : <i>[ <a href="recurrencedefinition.md">RecurrenceDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#capacity" title="Capacity">Capacity</a>: <i>
      - <a href="capacitydefinition.md">CapacityDefinition</a></i>
<a href="#recurrence" title="Recurrence">Recurrence</a>: <i>
      - <a href="recurrencedefinition.md">RecurrenceDefinition</a></i>
</pre>

## Properties

#### Capacity

_Required_: No

_Type_: List of <a href="capacitydefinition.md">CapacityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Recurrence

_Required_: No

_Type_: List of <a href="recurrencedefinition.md">RecurrenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

