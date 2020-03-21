# Terraform::AWS::KmsGrant Constraints

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#encryptioncontextequals" title="EncryptionContextEquals">EncryptionContextEquals</a>" : <i>[ &lt;a href=&#34;constraints-encryptioncontextequals.md&#34;&gt;EncryptionContextEquals&lt;/a&gt;, ... ]</i>,
    "<a href="#encryptioncontextsubset" title="EncryptionContextSubset">EncryptionContextSubset</a>" : <i>[ &lt;a href=&#34;constraints-encryptioncontextsubset.md&#34;&gt;EncryptionContextSubset&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#encryptioncontextequals" title="EncryptionContextEquals">EncryptionContextEquals</a>: <i>
      - &lt;a href=&#34;constraints-encryptioncontextequals.md&#34;&gt;EncryptionContextEquals&lt;/a&gt;</i>
<a href="#encryptioncontextsubset" title="EncryptionContextSubset">EncryptionContextSubset</a>: <i>
      - &lt;a href=&#34;constraints-encryptioncontextsubset.md&#34;&gt;EncryptionContextSubset&lt;/a&gt;</i>
</pre>

## Properties

#### EncryptionContextEquals

_Required_: No
_Type_: List of &lt;a href=&#34;constraints-encryptioncontextequals.md&#34;&gt;EncryptionContextEquals&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionContextSubset

_Required_: No
_Type_: List of &lt;a href=&#34;constraints-encryptioncontextsubset.md&#34;&gt;EncryptionContextSubset&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

