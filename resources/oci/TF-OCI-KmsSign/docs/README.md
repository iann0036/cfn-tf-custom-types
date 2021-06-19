# TF::OCI::KmsSign

This resource provides the Sign resource in Oracle Cloud Infrastructure Kms service.

Creates a digital signature for a message or message digest by using the private key of a public-private key pair, 
also known as an asymmetric key. To verify the generated signature, you can use the [Verify](https://docs.cloud.oracle.com/iaas/api/#/en/key/latest/VerifiedData/Verify) 
operation. Or, if you want to validate the signature outside of the service, you can do so by using the public key of the same asymmetric key.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::KmsSign",
    "Properties" : {
        "<a href="#cryptoendpoint" title="CryptoEndpoint">CryptoEndpoint</a>" : <i>String</i>,
        "<a href="#keyid" title="KeyId">KeyId</a>" : <i>String</i>,
        "<a href="#keyversionid" title="KeyVersionId">KeyVersionId</a>" : <i>String</i>,
        "<a href="#message" title="Message">Message</a>" : <i>String</i>,
        "<a href="#messagetype" title="MessageType">MessageType</a>" : <i>String</i>,
        "<a href="#signingalgorithm" title="SigningAlgorithm">SigningAlgorithm</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::KmsSign
Properties:
    <a href="#cryptoendpoint" title="CryptoEndpoint">CryptoEndpoint</a>: <i>String</i>
    <a href="#keyid" title="KeyId">KeyId</a>: <i>String</i>
    <a href="#keyversionid" title="KeyVersionId">KeyVersionId</a>: <i>String</i>
    <a href="#message" title="Message">Message</a>: <i>String</i>
    <a href="#messagetype" title="MessageType">MessageType</a>: <i>String</i>
    <a href="#signingalgorithm" title="SigningAlgorithm">SigningAlgorithm</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### CryptoEndpoint

The service endpoint to perform cryptographic operations against. Cryptographic operations include 'Encrypt,' 'Decrypt,', 'GenerateDataEncryptionKey', 'Sign' and 'Verify' operations. see Vault Crypto endpoint.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyId

The OCID of the key used to sign the message.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyVersionId

The OCID of the key version used to sign the message.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Message

The base64-encoded binary data object denoting the message or message digest to sign. You can have a message up to 4096 bytes in size. To sign a larger message, provide the message digest.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MessageType

Denotes whether the value of the message parameter is a raw message or a message digest.  The default value, `RAW`, indicates a message. To indicate a message digest, use `DIGEST`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SigningAlgorithm

The algorithm to use to sign the message or message digest. For RSA keys, supported signature schemes include PKCS #1 and RSASSA-PSS, along with  different hashing algorithms.  For ECDSA keys, ECDSA is the supported signature scheme with different hashing algorithms. When you pass a message digest for signing, ensure that you specify the same hashing algorithm  as used when creating the message digest.

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

#### Id

Returns the <code>Id</code> value.

#### Signature

Returns the <code>Signature</code> value.

