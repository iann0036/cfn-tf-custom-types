# TF::PagerDuty::ServiceEventRule ConditionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#operator" title="Operator">Operator</a>" : <i>String</i>,
    "<a href="#subconditions" title="Subconditions">Subconditions</a>" : <i>[ <a href="subconditionsdefinition.md">SubconditionsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#operator" title="Operator">Operator</a>: <i>String</i>
<a href="#subconditions" title="Subconditions">Subconditions</a>: <i>
      - <a href="subconditionsdefinition.md">SubconditionsDefinition</a></i>
</pre>

## Properties

#### Operator

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subconditions

_Required_: No

_Type_: List of <a href="subconditionsdefinition.md">SubconditionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

