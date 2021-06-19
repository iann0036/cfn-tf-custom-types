# TF::AWS::NetworkfirewallRuleGroup CustomActionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#actionname" title="ActionName">ActionName</a>" : <i>String</i>,
    "<a href="#actiondefinition" title="ActionDefinition">ActionDefinition</a>" : <i>[ <a href="actiondefinitiondefinition.md">ActionDefinitionDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#actionname" title="ActionName">ActionName</a>: <i>String</i>
<a href="#actiondefinition" title="ActionDefinition">ActionDefinition</a>: <i>
      - <a href="actiondefinitiondefinition.md">ActionDefinitionDefinition</a></i>
</pre>

## Properties

#### ActionName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionDefinition

_Required_: No

_Type_: List of <a href="actiondefinitiondefinition.md">ActionDefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

