# TF::OCI::AutoscalingAutoScalingConfiguration PoliciesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
    "<a href="#isenabled" title="IsEnabled">IsEnabled</a>" : <i>Boolean</i>,
    "<a href="#policytype" title="PolicyType">PolicyType</a>" : <i>String</i>,
    "<a href="#capacity" title="Capacity">Capacity</a>" : <i>[ <a href="capacitydefinition.md">CapacityDefinition</a>, ... ]</i>,
    "<a href="#executionschedule" title="ExecutionSchedule">ExecutionSchedule</a>" : <i>[ <a href="executionscheduledefinition.md">ExecutionScheduleDefinition</a>, ... ]</i>,
    "<a href="#resourceaction" title="ResourceAction">ResourceAction</a>" : <i>[ <a href="resourceactiondefinition.md">ResourceActionDefinition</a>, ... ]</i>,
    "<a href="#rules" title="Rules">Rules</a>" : <i>[ <a href="rulesdefinition.md">RulesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
<a href="#isenabled" title="IsEnabled">IsEnabled</a>: <i>Boolean</i>
<a href="#policytype" title="PolicyType">PolicyType</a>: <i>String</i>
<a href="#capacity" title="Capacity">Capacity</a>: <i>
      - <a href="capacitydefinition.md">CapacityDefinition</a></i>
<a href="#executionschedule" title="ExecutionSchedule">ExecutionSchedule</a>: <i>
      - <a href="executionscheduledefinition.md">ExecutionScheduleDefinition</a></i>
<a href="#resourceaction" title="ResourceAction">ResourceAction</a>: <i>
      - <a href="resourceactiondefinition.md">ResourceActionDefinition</a></i>
<a href="#rules" title="Rules">Rules</a>: <i>
      - <a href="rulesdefinition.md">RulesDefinition</a></i>
</pre>

## Properties

#### DisplayName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Capacity

_Required_: No

_Type_: List of <a href="capacitydefinition.md">CapacityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExecutionSchedule

_Required_: No

_Type_: List of <a href="executionscheduledefinition.md">ExecutionScheduleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceAction

_Required_: No

_Type_: List of <a href="resourceactiondefinition.md">ResourceActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rules

_Required_: No

_Type_: List of <a href="rulesdefinition.md">RulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

