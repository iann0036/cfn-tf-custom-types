# TF::AWS::NetworkfirewallRuleGroup RuleDefinitionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#actions" title="Actions">Actions</a>" : <i>[ String, ... ]</i>,
    "<a href="#matchattributes" title="MatchAttributes">MatchAttributes</a>" : <i>[ <a href="matchattributesdefinition.md">MatchAttributesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#actions" title="Actions">Actions</a>: <i>
      - String</i>
<a href="#matchattributes" title="MatchAttributes">MatchAttributes</a>: <i>
      - <a href="matchattributesdefinition.md">MatchAttributesDefinition</a></i>
</pre>

## Properties

#### Actions

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchAttributes

_Required_: No

_Type_: List of <a href="matchattributesdefinition.md">MatchAttributesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

