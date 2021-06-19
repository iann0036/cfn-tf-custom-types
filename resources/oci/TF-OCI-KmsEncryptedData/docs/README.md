# TF::OCI::KmsEncryptedData

This resource provides the Encrypted Data resource in Oracle Cloud Infrastructure Kms service.

Encrypts data using the given [EncryptDataDetails](https://docs.cloud.oracle.com/iaas/api/#/en/key/latest/datatypes/EncryptDataDetails) resource.
Plaintext included in the example request is a base64-encoded value of a UTF-8 string.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::KmsEncryptedData",
    "Properties" : {
        "<a href="#associateddata" title="AssociatedData">AssociatedData</a>" : <i>[ <a href="associateddatadefinition.md">AssociatedDataDefinition</a>, ... ]</i>,
        "<a href="#cryptoendpoint" title="CryptoEndpoint">CryptoEndpoint</a>" : <i>String</i>,
        "<a href="#encryptionalgorithm" title="EncryptionAlgorithm">EncryptionAlgorithm</a>" : <i>String</i>,
        "<a href="#keyid" title="KeyId">KeyId</a>" : <i>String</i>,
        "<a href="#keyversionid" title="KeyVersionId">KeyVersionId</a>" : <i>String</i>,
        "<a href="#loggingcontext" title="LoggingContext">LoggingContext</a>" : <i>[ <a href="loggingcontextdefinition.md">LoggingContextDefinition</a>, ... ]</i>,
        "<a href="#plaintext" title="Plaintext">Plaintext</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::KmsEncryptedData
Properties:
    <a href="#associateddata" title="AssociatedData">AssociatedData</a>: <i>
      - <a href="associateddatadefinition.md">AssociatedDataDefinition</a></i>
    <a href="#cryptoendpoint" title="CryptoEndpoint">CryptoEndpoint</a>: <i>String</i>
    <a href="#encryptionalgorithm" title="EncryptionAlgorithm">EncryptionAlgorithm</a>: <i>String</i>
    <a href="#keyid" title="KeyId">KeyId</a>: <i>String</i>
    <a href="#keyversionid" title="KeyVersionId">KeyVersionId</a>: <i>String</i>
    <a href="#loggingcontext" title="LoggingContext">LoggingContext</a>: <i>
      - <a href="loggingcontextdefinition.md">LoggingContextDefinition</a></i>
    <a href="#plaintext" title="Plaintext">Plaintext</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AssociatedData

Information that can be used to provide an encryption context for the encrypted data. The length of the string representation of the associated data must be fewer than 4096 characters.

_Required_: No

_Type_: List of <a href="associateddatadefinition.md">AssociatedDataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CryptoEndpoint

The service endpoint to perform cryptographic operations against. Cryptographic operations include 'Encrypt,' 'Decrypt,' and 'GenerateDataEncryptionKey' operations. see Vault Crypto endpoint.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionAlgorithm

The encryption algorithm to use to encrypt and decrypt data with a customer-managed key. `AES_256_GCM` indicates that the key is a symmetric key that uses the Advanced Encryption Standard (AES) algorithm and  that the mode of encryption is the Galois/Counter Mode (GCM). `RSA_OAEP_SHA_1` indicates that the  key is an asymmetric key that uses the RSA encryption algorithm and uses Optimal Asymmetric Encryption Padding (OAEP).  `RSA_OAEP_SHA_256` indicates that the key is an asymmetric key that uses the RSA encryption algorithm with a SHA-256 hash  and uses OAEP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyId

The OCID of the key to encrypt with.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyVersionId

The OCID of the key version used to encrypt the ciphertext.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingContext

Information that provides context for audit logging. You can provide this additional data as key-value pairs to include in the audit logs when audit logging is enabled.

_Required_: No

_Type_: List of <a href="loggingcontextdefinition.md">LoggingContextDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Plaintext

The plaintext data to encrypt.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Ciphertext

Returns the <code>Ciphertext</code> value.

#### Id

Returns the <code>Id</code> value.

