# Terraform::AzureRM::ApplicationGateway RewriteRuleSet RewriteRule Condition

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

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Negate

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pattern

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Variable

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

