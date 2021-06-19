# TF::AzureRM::WebApplicationFirewallPolicy CustomRulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
    "<a href="#ruletype" title="RuleType">RuleType</a>" : <i>String</i>,
    "<a href="#matchconditions" title="MatchConditions">MatchConditions</a>" : <i>[ <a href="matchconditionsdefinition.md">MatchConditionsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#priority" title="Priority">Priority</a>: <i>Double</i>
<a href="#ruletype" title="RuleType">RuleType</a>: <i>String</i>
<a href="#matchconditions" title="MatchConditions">MatchConditions</a>: <i>
      - <a href="matchconditionsdefinition.md">MatchConditionsDefinition</a></i>
</pre>

## Properties

#### Action

Type of action.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Gets name of the resource that is unique within a policy. This name can be used to access the resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

Describes priority of the rule. Rules with a lower value will be evaluated before rules with a higher value.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleType

Describes the type of rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchConditions

_Required_: No

_Type_: List of <a href="matchconditionsdefinition.md">MatchConditionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

