# Terraform::AzureRM::FrontdoorFirewallPolicy ManagedRule Override Exclusion

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#matchvariable" title="MatchVariable">MatchVariable</a>" : <i>String</i>,
    "<a href="#operator" title="Operator">Operator</a>" : <i>String</i>,
    "<a href="#selector" title="Selector">Selector</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#matchvariable" title="MatchVariable">MatchVariable</a>: <i>String</i>
<a href="#operator" title="Operator">Operator</a>: <i>String</i>
<a href="#selector" title="Selector">Selector</a>: <i>String</i>
</pre>

## Properties

#### MatchVariable

The variable type to be excluded. Possible values are `QueryStringArgNames`, `RequestBodyPostArgNames`, `RequestCookieNames`, `RequestHeaderNames`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Operator

Comparison operator to apply to the selector when specifying which elements in the collection this exclusion applies to. Possible values are: `Equals`, `Contains`, `StartsWith`, `EndsWith`, `EqualsAny`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Selector

Selector for the value in the `match_variable` attribute this exclusion applies to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

