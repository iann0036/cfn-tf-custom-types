# TF::AWS::KmsGrant ConstraintsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#encryptioncontextequals" title="EncryptionContextEquals">EncryptionContextEquals</a>" : <i>[ <a href="encryptioncontextequalsdefinition.md">EncryptionContextEqualsDefinition</a>, ... ]</i>,
    "<a href="#encryptioncontextsubset" title="EncryptionContextSubset">EncryptionContextSubset</a>" : <i>[ <a href="encryptioncontextsubsetdefinition.md">EncryptionContextSubsetDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#encryptioncontextequals" title="EncryptionContextEquals">EncryptionContextEquals</a>: <i>
      - <a href="encryptioncontextequalsdefinition.md">EncryptionContextEqualsDefinition</a></i>
<a href="#encryptioncontextsubset" title="EncryptionContextSubset">EncryptionContextSubset</a>: <i>
      - <a href="encryptioncontextsubsetdefinition.md">EncryptionContextSubsetDefinition</a></i>
</pre>

## Properties

#### EncryptionContextEquals

A list of key-value pairs that must match the encryption context in subsequent cryptographic operation requests. The grant allows the operation only when the encryption context in the request is the same as the encryption context specified in this constraint. Conflicts with `encryption_context_subset`.

_Required_: No

_Type_: List of <a href="encryptioncontextequalsdefinition.md">EncryptionContextEqualsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionContextSubset

A list of key-value pairs that must be included in the encryption context of subsequent cryptographic operation requests. The grant allows the cryptographic operation only when the encryption context in the request includes the key-value pairs specified in this constraint, although it can include additional key-value pairs. Conflicts with `encryption_context_equals`.

_Required_: No

_Type_: List of <a href="encryptioncontextsubsetdefinition.md">EncryptionContextSubsetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

