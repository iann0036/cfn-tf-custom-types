# Terraform::Alicloud::KmsCiphertext

Encrypt a given plaintext with KMS. The produced ciphertext stays stable across applies. If the plaintext should be re-encrypted on each apply use the [`alicloud_kms_ciphertext`](/docs/providers/alicloud/d/kms_ciphertext.html) data source.

~> **NOTE**: Using this data provider will allow you to conceal secret data within your resource definitions but does not take care of protecting that data in all Terraform logging and state output. Please take care to secure your secret data beyond just the Terraform configuration.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::KmsCiphertext",
    "Properties" : {
        "<a href="#encryptioncontext" title="EncryptionContext">EncryptionContext</a>" : <i>[ <a href="encryptioncontext.md">EncryptionContext</a>, ... ]</i>,
        "<a href="#keyid" title="KeyId">KeyId</a>" : <i>String</i>,
        "<a href="#plaintext" title="Plaintext">Plaintext</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::KmsCiphertext
Properties:
    <a href="#encryptioncontext" title="EncryptionContext">EncryptionContext</a>: <i>
      - <a href="encryptioncontext.md">EncryptionContext</a></i>
    <a href="#keyid" title="KeyId">KeyId</a>: <i>String</i>
    <a href="#plaintext" title="Plaintext">Plaintext</a>: <i>String</i>
</pre>

## Properties

#### EncryptionContext

_Required_: No

_Type_: List of <a href="encryptioncontext.md">EncryptionContext</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyId

The globally unique ID of the CMK.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Plaintext

The plaintext to be encrypted which must be encoded in Base64.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CiphertextBlob

Returns the <code>CiphertextBlob</code> value.

#### Id

Returns the <code>Id</code> value.

