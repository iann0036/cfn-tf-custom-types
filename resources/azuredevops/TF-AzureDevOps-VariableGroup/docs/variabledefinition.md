# TF::AzureDevOps::VariableGroup VariableDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#issecret" title="IsSecret">IsSecret</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#secretvalue" title="SecretValue">SecretValue</a>" : <i>String</i>,
    "<a href="#value" title="Value">Value</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#issecret" title="IsSecret">IsSecret</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#secretvalue" title="SecretValue">SecretValue</a>: <i>String</i>
<a href="#value" title="Value">Value</a>: <i>String</i>
</pre>

## Properties

#### IsSecret

A boolean flag describing if the variable value is sensitive. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The key value used for the variable. Must be unique within the Variable Group.
- `value` - (Optional) The value of the variable. If omitted, it will default to empty string.
- `secret_value` - (Optional) The secret value of the variable. If omitted, it will default to empty string. Used when `is_secret` set to `true`.
- `is_secret` - (Optional) A boolean flag describing if the variable value is sensitive. Defaults to `false`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretValue

The secret value of the variable. If omitted, it will default to empty string. Used when `is_secret` set to `true`.
- `is_secret` - (Optional) A boolean flag describing if the variable value is sensitive. Defaults to `false`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

The value of the variable. If omitted, it will default to empty string.
- `secret_value` - (Optional) The secret value of the variable. If omitted, it will default to empty string. Used when `is_secret` set to `true`.
- `is_secret` - (Optional) A boolean flag describing if the variable value is sensitive. Defaults to `false`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

