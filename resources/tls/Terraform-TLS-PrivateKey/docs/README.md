# Terraform::TLS::PrivateKey

CloudFormation equivalent of tls_private_key

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TLS::PrivateKey",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#algorithm" title="Algorithm">Algorithm</a>" : <i>String</i>,
        "<a href="#ecdsacurve" title="EcdsaCurve">EcdsaCurve</a>" : <i>String</i>,
        "<a href="#privatekeypem" title="PrivateKeyPem">PrivateKeyPem</a>" : <i>String</i>,
        "<a href="#publickeyfingerprintmd5" title="PublicKeyFingerprintMd5">PublicKeyFingerprintMd5</a>" : <i>String</i>,
        "<a href="#publickeyopenssh" title="PublicKeyOpenssh">PublicKeyOpenssh</a>" : <i>String</i>,
        "<a href="#publickeypem" title="PublicKeyPem">PublicKeyPem</a>" : <i>String</i>,
        "<a href="#rsabits" title="RsaBits">RsaBits</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TLS::PrivateKey
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#algorithm" title="Algorithm">Algorithm</a>: <i>String</i>
    <a href="#ecdsacurve" title="EcdsaCurve">EcdsaCurve</a>: <i>String</i>
    <a href="#privatekeypem" title="PrivateKeyPem">PrivateKeyPem</a>: <i>String</i>
    <a href="#publickeyfingerprintmd5" title="PublicKeyFingerprintMd5">PublicKeyFingerprintMd5</a>: <i>String</i>
    <a href="#publickeyopenssh" title="PublicKeyOpenssh">PublicKeyOpenssh</a>: <i>String</i>
    <a href="#publickeypem" title="PublicKeyPem">PublicKeyPem</a>: <i>String</i>
    <a href="#rsabits" title="RsaBits">RsaBits</a>: <i>Double</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Algorithm

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EcdsaCurve

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateKeyPem

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicKeyFingerprintMd5

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicKeyOpenssh

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicKeyPem

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RsaBits

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### PrivateKeyPem

Returns the &lt;code&gt;PrivateKeyPem&lt;/code&gt; value.

#### PublicKeyFingerprintMd5

Returns the &lt;code&gt;PublicKeyFingerprintMd5&lt;/code&gt; value.

#### PublicKeyOpenssh

Returns the &lt;code&gt;PublicKeyOpenssh&lt;/code&gt; value.

#### PublicKeyPem

Returns the &lt;code&gt;PublicKeyPem&lt;/code&gt; value.

