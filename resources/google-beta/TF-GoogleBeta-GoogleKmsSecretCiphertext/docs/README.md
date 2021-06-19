# TF::GoogleBeta::GoogleKmsSecretCiphertext

CloudFormation equivalent of google_kms_secret_ciphertext

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GoogleBeta::GoogleKmsSecretCiphertext",
    "Properties" : {
        "<a href="#additionalauthenticateddata" title="AdditionalAuthenticatedData">AdditionalAuthenticatedData</a>" : <i>String</i>,
        "<a href="#cryptokey" title="CryptoKey">CryptoKey</a>" : <i>String</i>,
        "<a href="#plaintext" title="Plaintext">Plaintext</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GoogleBeta::GoogleKmsSecretCiphertext
Properties:
    <a href="#additionalauthenticateddata" title="AdditionalAuthenticatedData">AdditionalAuthenticatedData</a>: <i>String</i>
    <a href="#cryptokey" title="CryptoKey">CryptoKey</a>: <i>String</i>
    <a href="#plaintext" title="Plaintext">Plaintext</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AdditionalAuthenticatedData

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CryptoKey

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Plaintext

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

