# Terraform::AWS::KmsCiphertext

The KMS ciphertext resource allows you to encrypt plaintext into ciphertext
by using an AWS KMS customer master key. The value returned by this resource
is stable across every apply. For a changing ciphertext value each apply, see
the [`aws_kms_ciphertext` data source](/docs/providers/aws/d/kms_ciphertext.html).

~> **Note:** All arguments including the plaintext be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::KmsCiphertext",
    "Properties" : {
        "<a href="#context" title="Context">Context</a>" : <i>[ <a href="context.md">Context</a>, ... ]</i>,
        "<a href="#keyid" title="KeyId">KeyId</a>" : <i>String</i>,
        "<a href="#plaintext" title="Plaintext">Plaintext</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::KmsCiphertext
Properties:
    <a href="#context" title="Context">Context</a>: <i>
      - <a href="context.md">Context</a></i>
    <a href="#keyid" title="KeyId">KeyId</a>: <i>String</i>
    <a href="#plaintext" title="Plaintext">Plaintext</a>: <i>String</i>
</pre>

## Properties

#### Context

An optional mapping that makes up the encryption context.

_Required_: No

_Type_: List of <a href="context.md">Context</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyId

Globally unique key ID for the customer master key.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Plaintext

Data to be encrypted. Note that this may show up in logs, and it will be stored in the state file.

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

#### CiphertextBlob

Returns the <code>CiphertextBlob</code> value.

#### Id

Returns the <code>Id</code> value.

