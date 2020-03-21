# Terraform::AzureRM::ApplicationGateway RewriteRule Condition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ignorecase" title="IgnoreCase">IgnoreCase</a>" : <i>Boolean</i>,
    "<a href="#negate" title="Negate">Negate</a>" : <i>Boolean</i>,
    "<a href="#pattern" title="Pattern">Pattern</a>" : <i>String</i>,
    "<a href="#variable" title="Variable">Variable</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#ignorecase" title="IgnoreCase">IgnoreCase</a>: <i>Boolean</i>
<a href="#negate" title="Negate">Negate</a>: <i>Boolean</i>
<a href="#pattern" title="Pattern">Pattern</a>: <i>String</i>
<a href="#variable" title="Variable">Variable</a>: <i>String</i>
</pre>

## Properties

#### IgnoreCase

Perform a case in-sensitive comparison. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Negate

Negate the result of the condition evaluation. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pattern

The pattern, either fixed string or regular expression, that evaluates the truthfulness of the condition.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Variable

The [variable](https://docs.microsoft.com/en-us/azure/application-gateway/rewrite-http-headers#server-variables) of the condition.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

