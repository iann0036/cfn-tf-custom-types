# TF::GitHub::ActionsOrganizationSecret

This resource allows you to create and manage GitHub Actions secrets within your GitHub organization.
You must have write access to a repository to use this resource.

Secret values are encrypted using the [Go '/crypto/box' module](https://godoc.org/golang.org/x/crypto/nacl/box) which is
interoperable with [libsodium](https://libsodium.gitbook.io/doc/). Libsodium is used by Github to decrypt secret values. 

For the purposes of security, the contents of the `plaintext_value` field have been marked as `sensitive` to Terraform,
but it is important to note that **this does not hide it from state files**. You should treat state as sensitive always.
It is also advised that you do not store plaintext values in your code but rather populate the `plaintext_value`
using fields from a resource, data source or variable as, while encrypted in state, these will be easily accessible
in your code. See below for an example of this abstraction.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GitHub::ActionsOrganizationSecret",
    "Properties" : {
        "<a href="#encryptedvalue" title="EncryptedValue">EncryptedValue</a>" : <i>String</i>,
        "<a href="#plaintextvalue" title="PlaintextValue">PlaintextValue</a>" : <i>String</i>,
        "<a href="#secretname" title="SecretName">SecretName</a>" : <i>String</i>,
        "<a href="#selectedrepositoryids" title="SelectedRepositoryIds">SelectedRepositoryIds</a>" : <i>[ Double, ... ]</i>,
        "<a href="#visibility" title="Visibility">Visibility</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GitHub::ActionsOrganizationSecret
Properties:
    <a href="#encryptedvalue" title="EncryptedValue">EncryptedValue</a>: <i>String</i>
    <a href="#plaintextvalue" title="PlaintextValue">PlaintextValue</a>: <i>String</i>
    <a href="#secretname" title="SecretName">SecretName</a>: <i>String</i>
    <a href="#selectedrepositoryids" title="SelectedRepositoryIds">SelectedRepositoryIds</a>: <i>
      - Double</i>
    <a href="#visibility" title="Visibility">Visibility</a>: <i>String</i>
</pre>

## Properties

#### EncryptedValue

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlaintextValue

Plaintext value of the secret to be encrypted.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretName

Name of the secret.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SelectedRepositoryIds

An array of repository ids that can access the organization secret.

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Visibility

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

