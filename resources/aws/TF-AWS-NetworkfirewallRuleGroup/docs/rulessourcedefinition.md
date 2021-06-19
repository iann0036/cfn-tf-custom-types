# TF::AWS::NetworkfirewallRuleGroup RulesSourceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#rulesstring" title="RulesString">RulesString</a>" : <i>String</i>,
    "<a href="#rulessourcelist" title="RulesSourceList">RulesSourceList</a>" : <i>[ <a href="rulessourcelistdefinition.md">RulesSourceListDefinition</a>, ... ]</i>,
    "<a href="#statefulrule" title="StatefulRule">StatefulRule</a>" : <i>[ <a href="statefulruledefinition.md">StatefulRuleDefinition</a>, ... ]</i>,
    "<a href="#statelessrulesandcustomactions" title="StatelessRulesAndCustomActions">StatelessRulesAndCustomActions</a>" : <i>[ <a href="statelessrulesandcustomactionsdefinition.md">StatelessRulesAndCustomActionsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#rulesstring" title="RulesString">RulesString</a>: <i>String</i>
<a href="#rulessourcelist" title="RulesSourceList">RulesSourceList</a>: <i>
      - <a href="rulessourcelistdefinition.md">RulesSourceListDefinition</a></i>
<a href="#statefulrule" title="StatefulRule">StatefulRule</a>: <i>
      - <a href="statefulruledefinition.md">StatefulRuleDefinition</a></i>
<a href="#statelessrulesandcustomactions" title="StatelessRulesAndCustomActions">StatelessRulesAndCustomActions</a>: <i>
      - <a href="statelessrulesandcustomactionsdefinition.md">StatelessRulesAndCustomActionsDefinition</a></i>
</pre>

## Properties

#### RulesString

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RulesSourceList

_Required_: No

_Type_: List of <a href="rulessourcelistdefinition.md">RulesSourceListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatefulRule

_Required_: No

_Type_: List of <a href="statefulruledefinition.md">StatefulRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatelessRulesAndCustomActions

_Required_: No

_Type_: List of <a href="statelessrulesandcustomactionsdefinition.md">StatelessRulesAndCustomActionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

