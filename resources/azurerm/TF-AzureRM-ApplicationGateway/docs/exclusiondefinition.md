# TF::AzureRM::ApplicationGateway ExclusionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#matchvariable" title="MatchVariable">MatchVariable</a>" : <i>String</i>,
    "<a href="#selector" title="Selector">Selector</a>" : <i>String</i>,
    "<a href="#selectormatchoperator" title="SelectorMatchOperator">SelectorMatchOperator</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#matchvariable" title="MatchVariable">MatchVariable</a>: <i>String</i>
<a href="#selector" title="Selector">Selector</a>: <i>String</i>
<a href="#selectormatchoperator" title="SelectorMatchOperator">SelectorMatchOperator</a>: <i>String</i>
</pre>

## Properties

#### MatchVariable

Match variable of the exclusion rule to exclude header, cookie or GET arguments. Possible values are `RequestHeaderNames`, `RequestArgNames` and `RequestCookieNames`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Selector

String value which will be used for the filter operation. If empty will exclude all traffic on this `match_variable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SelectorMatchOperator

Operator which will be used to search in the variable content. Possible values are `Equals`, `StartsWith`, `EndsWith`, `Contains`. If empty will exclude all traffic on this `match_variable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

