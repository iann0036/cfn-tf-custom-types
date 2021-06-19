# TF::AzureRM::WebApplicationFirewallPolicy ExclusionDefinition

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

The name of the Match Variable. Possible values: `RequestArgNames`, `RequestCookieNames`, `RequestHeaderNames`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Selector

Describes field of the matchVariable collection.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SelectorMatchOperator

Describes operator to be matched. Possible values: `Contains`, `EndsWith`, `Equals`, `EqualsAny`, `StartsWith`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

