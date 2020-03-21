# Terraform::OCI::KmsGeneratedKey

CloudFormation equivalent of oci_kms_generated_key

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::KmsGeneratedKey",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#associateddata" title="AssociatedData">AssociatedData</a>" : <i>[ &lt;a href=&#34;associateddata.md&#34;&gt;AssociatedData&lt;/a&gt;, ... ]</i>,
        "<a href="#ciphertext" title="Ciphertext">Ciphertext</a>" : <i>String</i>,
        "<a href="#cryptoendpoint" title="CryptoEndpoint">CryptoEndpoint</a>" : <i>String</i>,
        "<a href="#includeplaintextkey" title="IncludePlaintextKey">IncludePlaintextKey</a>" : <i>Boolean</i>,
        "<a href="#keyid" title="KeyId">KeyId</a>" : <i>String</i>,
        "<a href="#loggingcontext" title="LoggingContext">LoggingContext</a>" : <i>[ &lt;a href=&#34;loggingcontext.md&#34;&gt;LoggingContext&lt;/a&gt;, ... ]</i>,
        "<a href="#plaintext" title="Plaintext">Plaintext</a>" : <i>String</i>,
        "<a href="#plaintextchecksum" title="PlaintextChecksum">PlaintextChecksum</a>" : <i>String</i>,
        "<a href="#keyshape" title="KeyShape">KeyShape</a>" : <i>[ &lt;a href=&#34;keyshape.md&#34;&gt;KeyShape&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::KmsGeneratedKey
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#associateddata" title="AssociatedData">AssociatedData</a>: <i>
      - &lt;a href=&#34;associateddata.md&#34;&gt;AssociatedData&lt;/a&gt;</i>
    <a href="#ciphertext" title="Ciphertext">Ciphertext</a>: <i>String</i>
    <a href="#cryptoendpoint" title="CryptoEndpoint">CryptoEndpoint</a>: <i>String</i>
    <a href="#includeplaintextkey" title="IncludePlaintextKey">IncludePlaintextKey</a>: <i>Boolean</i>
    <a href="#keyid" title="KeyId">KeyId</a>: <i>String</i>
    <a href="#loggingcontext" title="LoggingContext">LoggingContext</a>: <i>
      - &lt;a href=&#34;loggingcontext.md&#34;&gt;LoggingContext&lt;/a&gt;</i>
    <a href="#plaintext" title="Plaintext">Plaintext</a>: <i>String</i>
    <a href="#plaintextchecksum" title="PlaintextChecksum">PlaintextChecksum</a>: <i>String</i>
    <a href="#keyshape" title="KeyShape">KeyShape</a>: <i>
      - &lt;a href=&#34;keyshape.md&#34;&gt;KeyShape&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssociatedData

_Required_: No

_Type_: List of &lt;a href=&#34;associateddata.md&#34;&gt;AssociatedData&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ciphertext

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CryptoEndpoint

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludePlaintextKey

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingContext

_Required_: No

_Type_: List of &lt;a href=&#34;loggingcontext.md&#34;&gt;LoggingContext&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Plaintext

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlaintextChecksum

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyShape

_Required_: No

_Type_: List of &lt;a href=&#34;keyshape.md&#34;&gt;KeyShape&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

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

Returns the &lt;code&gt;Ciphertext&lt;/code&gt; value.

#### Plaintext

Returns the &lt;code&gt;Plaintext&lt;/code&gt; value.

#### PlaintextChecksum

Returns the &lt;code&gt;PlaintextChecksum&lt;/code&gt; value.

