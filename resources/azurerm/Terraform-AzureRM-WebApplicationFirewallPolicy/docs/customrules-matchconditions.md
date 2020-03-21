# Terraform::AzureRM::WebApplicationFirewallPolicy CustomRules MatchConditions

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#matchvalues" title="MatchValues">MatchValues</a>" : <i>[ String, ... ]</i>,
    "<a href="#negationcondition" title="NegationCondition">NegationCondition</a>" : <i>Boolean</i>,
    "<a href="#operator" title="Operator">Operator</a>" : <i>String</i>,
    "<a href="#matchvariables" title="MatchVariables">MatchVariables</a>" : <i>[ &lt;a href=&#34;customrules-matchconditions-matchvariables.md&#34;&gt;MatchVariables&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#matchvalues" title="MatchValues">MatchValues</a>: <i>
      - String</i>
<a href="#negationcondition" title="NegationCondition">NegationCondition</a>: <i>Boolean</i>
<a href="#operator" title="Operator">Operator</a>: <i>String</i>
<a href="#matchvariables" title="MatchVariables">MatchVariables</a>: <i>
      - &lt;a href=&#34;customrules-matchconditions-matchvariables.md&#34;&gt;MatchVariables&lt;/a&gt;</i>
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
_Type_: List of &lt;a href=&#34;customrules-matchconditions-matchvariables.md&#34;&gt;MatchVariables&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

