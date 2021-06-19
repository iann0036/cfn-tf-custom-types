# TF::Google::DataLossPreventionInspectTemplate RuleSetDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#infotypes" title="InfoTypes">InfoTypes</a>" : <i>[ <a href="infotypesdefinition.md">InfoTypesDefinition</a>, ... ]</i>,
    "<a href="#rules" title="Rules">Rules</a>" : <i>[ <a href="rulesdefinition.md">RulesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#infotypes" title="InfoTypes">InfoTypes</a>: <i>
      - <a href="infotypesdefinition.md">InfoTypesDefinition</a></i>
<a href="#rules" title="Rules">Rules</a>: <i>
      - <a href="rulesdefinition.md">RulesDefinition</a></i>
</pre>

## Properties

#### InfoTypes

_Required_: No

_Type_: List of <a href="infotypesdefinition.md">InfoTypesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rules

_Required_: No

_Type_: List of <a href="rulesdefinition.md">RulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

