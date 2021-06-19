# TF::AzureRM::WebApplicationFirewallPolicy MatchConditionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#matchvalues" title="MatchValues">MatchValues</a>" : <i>[ String, ... ]</i>,
    "<a href="#negationcondition" title="NegationCondition">NegationCondition</a>" : <i>Boolean</i>,
    "<a href="#operator" title="Operator">Operator</a>" : <i>String</i>,
    "<a href="#transforms" title="Transforms">Transforms</a>" : <i>[ String, ... ]</i>,
    "<a href="#matchvariables" title="MatchVariables">MatchVariables</a>" : <i>[ <a href="matchvariablesdefinition.md">MatchVariablesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#matchvalues" title="MatchValues">MatchValues</a>: <i>
      - String</i>
<a href="#negationcondition" title="NegationCondition">NegationCondition</a>: <i>Boolean</i>
<a href="#operator" title="Operator">Operator</a>: <i>String</i>
<a href="#transforms" title="Transforms">Transforms</a>: <i>
      - String</i>
<a href="#matchvariables" title="MatchVariables">MatchVariables</a>: <i>
      - <a href="matchvariablesdefinition.md">MatchVariablesDefinition</a></i>
</pre>

## Properties

#### MatchValues

A list of match values.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NegationCondition

Describes if this is negate condition or not.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Operator

Describes operator to be matched.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Transforms

A list of transformations to do before the match is attempted.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchVariables

_Required_: No

_Type_: List of <a href="matchvariablesdefinition.md">MatchVariablesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

