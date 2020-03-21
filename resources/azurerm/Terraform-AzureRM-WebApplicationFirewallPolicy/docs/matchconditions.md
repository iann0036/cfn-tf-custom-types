# Terraform::AzureRM::WebApplicationFirewallPolicy MatchConditions

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#matchvalues" title="MatchValues">MatchValues</a>" : <i>[ String, ... ]</i>,
    "<a href="#negationcondition" title="NegationCondition">NegationCondition</a>" : <i>Boolean</i>,
    "<a href="#operator" title="Operator">Operator</a>" : <i>String</i>,
    "<a href="#matchvariables" title="MatchVariables">MatchVariables</a>" : <i>[ <a href="matchconditions-matchvariables.md">MatchVariables</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#matchvalues" title="MatchValues">MatchValues</a>: <i>
      - String</i>
<a href="#negationcondition" title="NegationCondition">NegationCondition</a>: <i>Boolean</i>
<a href="#operator" title="Operator">Operator</a>: <i>String</i>
<a href="#matchvariables" title="MatchVariables">MatchVariables</a>: <i>
      - <a href="matchconditions-matchvariables.md">MatchVariables</a></i>
</pre>

## Properties

#### MatchValues

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NegationCondition

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Operator

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchVariables

_Required_: No

_Type_: List of <a href="matchconditions-matchvariables.md">MatchVariables</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

