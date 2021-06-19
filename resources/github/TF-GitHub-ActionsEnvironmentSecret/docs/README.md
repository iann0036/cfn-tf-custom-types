# TF::GitHub::ActionsEnvironmentSecret

CloudFormation equivalent of github_actions_environment_secret

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GitHub::ActionsEnvironmentSecret",
    "Properties" : {
        "<a href="#encryptedvalue" title="EncryptedValue">EncryptedValue</a>" : <i>String</i>,
        "<a href="#environment" title="Environment">Environment</a>" : <i>String</i>,
        "<a href="#plaintextvalue" title="PlaintextValue">PlaintextValue</a>" : <i>String</i>,
        "<a href="#repository" title="Repository">Repository</a>" : <i>String</i>,
        "<a href="#secretname" title="SecretName">SecretName</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::GitHub::ActionsEnvironmentSecret
Properties:
    <a href="#encryptedvalue" title="EncryptedValue">EncryptedValue</a>: <i>String</i>
    <a href="#environment" title="Environment">Environment</a>: <i>String</i>
    <a href="#plaintextvalue" title="PlaintextValue">PlaintextValue</a>: <i>String</i>
    <a href="#repository" title="Repository">Repository</a>: <i>String</i>
    <a href="#secretname" title="SecretName">SecretName</a>: <i>String</i>
</pre>

## Properties

#### EncryptedValue

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Environment

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlaintextValue

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Repository

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### Id

Returns the <code>Id</code> value.

#### UpdatedAt

Returns the <code>UpdatedAt</code> value.

