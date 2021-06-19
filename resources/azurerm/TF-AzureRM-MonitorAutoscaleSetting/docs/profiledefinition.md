# TF::AzureRM::MonitorAutoscaleSetting ProfileDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#capacity" title="Capacity">Capacity</a>" : <i>[ <a href="capacitydefinition.md">CapacityDefinition</a>, ... ]</i>,
    "<a href="#fixeddate" title="FixedDate">FixedDate</a>" : <i>[ <a href="fixeddatedefinition.md">FixedDateDefinition</a>, ... ]</i>,
    "<a href="#recurrence" title="Recurrence">Recurrence</a>" : <i>[ <a href="recurrencedefinition.md">RecurrenceDefinition</a>, ... ]</i>,
    "<a href="#rule" title="Rule">Rule</a>" : <i>[ <a href="ruledefinition.md">RuleDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#capacity" title="Capacity">Capacity</a>: <i>
      - <a href="capacitydefinition.md">CapacityDefinition</a></i>
<a href="#fixeddate" title="FixedDate">FixedDate</a>: <i>
      - <a href="fixeddatedefinition.md">FixedDateDefinition</a></i>
<a href="#recurrence" title="Recurrence">Recurrence</a>: <i>
      - <a href="recurrencedefinition.md">RecurrenceDefinition</a></i>
<a href="#rule" title="Rule">Rule</a>: <i>
      - <a href="ruledefinition.md">RuleDefinition</a></i>
</pre>

## Properties

#### Name

Specifies the name of the profile.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Capacity

_Required_: No

_Type_: List of <a href="capacitydefinition.md">CapacityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FixedDate

_Required_: No

_Type_: List of <a href="fixeddatedefinition.md">FixedDateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Recurrence

_Required_: No

_Type_: List of <a href="recurrencedefinition.md">RecurrenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: No

_Type_: List of <a href="ruledefinition.md">RuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

