# TF::AWS::GlueDataCatalogEncryptionSettings DataCatalogEncryptionSettingsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#connectionpasswordencryption" title="ConnectionPasswordEncryption">ConnectionPasswordEncryption</a>" : <i>[ <a href="connectionpasswordencryptiondefinition.md">ConnectionPasswordEncryptionDefinition</a>, ... ]</i>,
    "<a href="#encryptionatrest" title="EncryptionAtRest">EncryptionAtRest</a>" : <i>[ <a href="encryptionatrestdefinition.md">EncryptionAtRestDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#connectionpasswordencryption" title="ConnectionPasswordEncryption">ConnectionPasswordEncryption</a>: <i>
      - <a href="connectionpasswordencryptiondefinition.md">ConnectionPasswordEncryptionDefinition</a></i>
<a href="#encryptionatrest" title="EncryptionAtRest">EncryptionAtRest</a>: <i>
      - <a href="encryptionatrestdefinition.md">EncryptionAtRestDefinition</a></i>
</pre>

## Properties

#### ConnectionPasswordEncryption

_Required_: No

_Type_: List of <a href="connectionpasswordencryptiondefinition.md">ConnectionPasswordEncryptionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionAtRest

_Required_: No

_Type_: List of <a href="encryptionatrestdefinition.md">EncryptionAtRestDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

