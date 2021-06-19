# TF::AzureRM::FrontdoorFirewallPolicy MatchConditionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#matchvalues" title="MatchValues">MatchValues</a>" : <i>[ String, ... ]</i>,
    "<a href="#matchvariable" title="MatchVariable">MatchVariable</a>" : <i>String</i>,
    "<a href="#negationcondition" title="NegationCondition">NegationCondition</a>" : <i>Boolean</i>,
    "<a href="#operator" title="Operator">Operator</a>" : <i>String</i>,
    "<a href="#selector" title="Selector">Selector</a>" : <i>String</i>,
    "<a href="#transforms" title="Transforms">Transforms</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#matchvalues" title="MatchValues">MatchValues</a>: <i>
      - String</i>
<a href="#matchvariable" title="MatchVariable">MatchVariable</a>: <i>String</i>
<a href="#negationcondition" title="NegationCondition">NegationCondition</a>: <i>Boolean</i>
<a href="#operator" title="Operator">Operator</a>: <i>String</i>
<a href="#selector" title="Selector">Selector</a>: <i>String</i>
<a href="#transforms" title="Transforms">Transforms</a>: <i>
      - String</i>
</pre>

## Properties

#### MatchValues

Up to `600` possible values to match. Limit is in total across all `match_condition` blocks and `match_values` arguments. String value itself can be up to `256` characters long.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchVariable

The request variable to compare with. Possible values are `Cookies`, `PostArgs`, `QueryString`, `RemoteAddr`, `RequestBody`, `RequestHeader`, `RequestMethod`, `RequestUri`, or `SocketAddr`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NegationCondition

Should the result of the condition be negated.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Operator

Comparison type to use for matching with the variable value. Possible values are `Any`, `BeginsWith`, `Contains`, `EndsWith`, `Equal`, `GeoMatch`, `GreaterThan`, `GreaterThanOrEqual`, `IPMatch`, `LessThan`, `LessThanOrEqual` or `RegEx`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Selector

Match against a specific key if the `match_variable` is `QueryString`, `PostArgs`, `RequestHeader` or `Cookies`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Transforms

Up to `5` transforms to apply. Possible values are `Lowercase`, `RemoveNulls`, `Trim`, `Uppercase`, `URLDecode` or`URLEncode`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

