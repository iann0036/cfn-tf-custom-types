# TF::AWS::NetworkfirewallRuleGroup StatelessRuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
    "<a href="#ruledefinition" title="RuleDefinition">RuleDefinition</a>" : <i>[ <a href="ruledefinitiondefinition.md">RuleDefinitionDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#priority" title="Priority">Priority</a>: <i>Double</i>
<a href="#ruledefinition" title="RuleDefinition">RuleDefinition</a>: <i>
      - <a href="ruledefinitiondefinition.md">RuleDefinitionDefinition</a></i>
</pre>

## Properties

#### Priority

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleDefinition

_Required_: No

_Type_: List of <a href="ruledefinitiondefinition.md">RuleDefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

