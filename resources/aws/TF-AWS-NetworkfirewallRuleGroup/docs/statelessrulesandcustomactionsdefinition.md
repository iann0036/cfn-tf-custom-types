# TF::AWS::NetworkfirewallRuleGroup StatelessRulesAndCustomActionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#customaction" title="CustomAction">CustomAction</a>" : <i>[ <a href="customactiondefinition.md">CustomActionDefinition</a>, ... ]</i>,
    "<a href="#statelessrule" title="StatelessRule">StatelessRule</a>" : <i>[ <a href="statelessruledefinition.md">StatelessRuleDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#customaction" title="CustomAction">CustomAction</a>: <i>
      - <a href="customactiondefinition.md">CustomActionDefinition</a></i>
<a href="#statelessrule" title="StatelessRule">StatelessRule</a>: <i>
      - <a href="statelessruledefinition.md">StatelessRuleDefinition</a></i>
</pre>

## Properties

#### CustomAction

_Required_: No

_Type_: List of <a href="customactiondefinition.md">CustomActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatelessRule

_Required_: No

_Type_: List of <a href="statelessruledefinition.md">StatelessRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

