# TF::OpsGenie::ServiceIncidentRule IncidentRuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#conditionmatchtype" title="ConditionMatchType">ConditionMatchType</a>" : <i>String</i>,
    "<a href="#conditions" title="Conditions">Conditions</a>" : <i>[ <a href="conditionsdefinition.md">ConditionsDefinition</a>, ... ]</i>,
    "<a href="#incidentproperties" title="IncidentProperties">IncidentProperties</a>" : <i>[ <a href="incidentpropertiesdefinition.md">IncidentPropertiesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#conditionmatchtype" title="ConditionMatchType">ConditionMatchType</a>: <i>String</i>
<a href="#conditions" title="Conditions">Conditions</a>: <i>
      - <a href="conditionsdefinition.md">ConditionsDefinition</a></i>
<a href="#incidentproperties" title="IncidentProperties">IncidentProperties</a>: <i>
      - <a href="incidentpropertiesdefinition.md">IncidentPropertiesDefinition</a></i>
</pre>

## Properties

#### ConditionMatchType

A Condition type, supported types are: `match-all`, `match-any-condition`, `match-all-conditions`. Default: `match-all`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Conditions

_Required_: No

_Type_: List of <a href="conditionsdefinition.md">ConditionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncidentProperties

_Required_: No

_Type_: List of <a href="incidentpropertiesdefinition.md">IncidentPropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

