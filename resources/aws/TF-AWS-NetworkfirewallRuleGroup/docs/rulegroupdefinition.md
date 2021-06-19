# TF::AWS::NetworkfirewallRuleGroup RuleGroupDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#rulevariables" title="RuleVariables">RuleVariables</a>" : <i>[ <a href="rulevariablesdefinition.md">RuleVariablesDefinition</a>, ... ]</i>,
    "<a href="#rulessource" title="RulesSource">RulesSource</a>" : <i>[ <a href="rulessourcedefinition.md">RulesSourceDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#rulevariables" title="RuleVariables">RuleVariables</a>: <i>
      - <a href="rulevariablesdefinition.md">RuleVariablesDefinition</a></i>
<a href="#rulessource" title="RulesSource">RulesSource</a>: <i>
      - <a href="rulessourcedefinition.md">RulesSourceDefinition</a></i>
</pre>

## Properties

#### RuleVariables

_Required_: No

_Type_: List of <a href="rulevariablesdefinition.md">RuleVariablesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RulesSource

_Required_: No

_Type_: List of <a href="rulessourcedefinition.md">RulesSourceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

