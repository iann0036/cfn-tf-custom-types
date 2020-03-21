# Terraform::AWS::KmsGrant Constraints

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#encryptioncontextequals" title="EncryptionContextEquals">EncryptionContextEquals</a>" : <i>[ <a href="constraints-encryptioncontextequals.md">EncryptionContextEquals</a>, ... ]</i>,
    "<a href="#encryptioncontextsubset" title="EncryptionContextSubset">EncryptionContextSubset</a>" : <i>[ <a href="constraints-encryptioncontextsubset.md">EncryptionContextSubset</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#encryptioncontextequals" title="EncryptionContextEquals">EncryptionContextEquals</a>: <i>
      - <a href="constraints-encryptioncontextequals.md">EncryptionContextEquals</a></i>
<a href="#encryptioncontextsubset" title="EncryptionContextSubset">EncryptionContextSubset</a>: <i>
      - <a href="constraints-encryptioncontextsubset.md">EncryptionContextSubset</a></i>
</pre>

## Properties

#### EncryptionContextEquals

_Required_: No
_Type_: List of <a href="constraints-encryptioncontextequals.md">EncryptionContextEquals</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionContextSubset

_Required_: No
_Type_: List of <a href="constraints-encryptioncontextsubset.md">EncryptionContextSubset</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

