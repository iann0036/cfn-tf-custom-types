# TF::AzureDevOps::BuildDefinition VariableDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowoverride" title="AllowOverride">AllowOverride</a>" : <i>Boolean</i>,
    "<a href="#issecret" title="IsSecret">IsSecret</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#secretvalue" title="SecretValue">SecretValue</a>" : <i>String</i>,
    "<a href="#value" title="Value">Value</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#allowoverride" title="AllowOverride">AllowOverride</a>: <i>Boolean</i>
<a href="#issecret" title="IsSecret">IsSecret</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#secretvalue" title="SecretValue">SecretValue</a>: <i>String</i>
<a href="#value" title="Value">Value</a>: <i>String</i>
</pre>

## Properties

#### AllowOverride

True if the variable can be overridden. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsSecret

True if the variable is a secret. Defaults to `false`.
- `allow_override` - (Optional) True if the variable can be overridden. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the variable.
- `value` - (Optional) The value of the variable.
- `secret_value` - (Optional) The secret value of the variable. Used when `is_secret` set to `true`.
- `is_secret` - (Optional) True if the variable is a secret. Defaults to `false`.
- `allow_override` - (Optional) True if the variable can be overridden. Defaults to `true`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretValue

The secret value of the variable. Used when `is_secret` set to `true`.
- `is_secret` - (Optional) True if the variable is a secret. Defaults to `false`.
- `allow_override` - (Optional) True if the variable can be overridden. Defaults to `true`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

The value of the variable.
- `secret_value` - (Optional) The secret value of the variable. Used when `is_secret` set to `true`.
- `is_secret` - (Optional) True if the variable is a secret. Defaults to `false`.
- `allow_override` - (Optional) True if the variable can be overridden. Defaults to `true`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

