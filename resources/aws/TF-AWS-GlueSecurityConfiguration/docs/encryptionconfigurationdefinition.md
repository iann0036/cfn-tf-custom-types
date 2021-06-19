# TF::AWS::GlueSecurityConfiguration EncryptionConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cloudwatchencryption" title="CloudwatchEncryption">CloudwatchEncryption</a>" : <i>[ <a href="cloudwatchencryptiondefinition.md">CloudwatchEncryptionDefinition</a>, ... ]</i>,
    "<a href="#jobbookmarksencryption" title="JobBookmarksEncryption">JobBookmarksEncryption</a>" : <i>[ <a href="jobbookmarksencryptiondefinition.md">JobBookmarksEncryptionDefinition</a>, ... ]</i>,
    "<a href="#s3encryption" title="S3Encryption">S3Encryption</a>" : <i>[ <a href="s3encryptiondefinition.md">S3EncryptionDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cloudwatchencryption" title="CloudwatchEncryption">CloudwatchEncryption</a>: <i>
      - <a href="cloudwatchencryptiondefinition.md">CloudwatchEncryptionDefinition</a></i>
<a href="#jobbookmarksencryption" title="JobBookmarksEncryption">JobBookmarksEncryption</a>: <i>
      - <a href="jobbookmarksencryptiondefinition.md">JobBookmarksEncryptionDefinition</a></i>
<a href="#s3encryption" title="S3Encryption">S3Encryption</a>: <i>
      - <a href="s3encryptiondefinition.md">S3EncryptionDefinition</a></i>
</pre>

## Properties

#### CloudwatchEncryption

_Required_: No

_Type_: List of <a href="cloudwatchencryptiondefinition.md">CloudwatchEncryptionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JobBookmarksEncryption

_Required_: No

_Type_: List of <a href="jobbookmarksencryptiondefinition.md">JobBookmarksEncryptionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3Encryption

_Required_: No

_Type_: List of <a href="s3encryptiondefinition.md">S3EncryptionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

