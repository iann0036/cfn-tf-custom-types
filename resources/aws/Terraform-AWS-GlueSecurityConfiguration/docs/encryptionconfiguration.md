# Terraform::AWS::GlueSecurityConfiguration EncryptionConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cloudwatchencryption" title="CloudwatchEncryption">CloudwatchEncryption</a>" : <i>[ <a href="encryptionconfiguration-cloudwatchencryption.md">CloudwatchEncryption</a>, ... ]</i>,
    "<a href="#jobbookmarksencryption" title="JobBookmarksEncryption">JobBookmarksEncryption</a>" : <i>[ <a href="encryptionconfiguration-jobbookmarksencryption.md">JobBookmarksEncryption</a>, ... ]</i>,
    "<a href="#s3encryption" title="S3Encryption">S3Encryption</a>" : <i>[ <a href="encryptionconfiguration-s3encryption.md">S3Encryption</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cloudwatchencryption" title="CloudwatchEncryption">CloudwatchEncryption</a>: <i>
      - <a href="encryptionconfiguration-cloudwatchencryption.md">CloudwatchEncryption</a></i>
<a href="#jobbookmarksencryption" title="JobBookmarksEncryption">JobBookmarksEncryption</a>: <i>
      - <a href="encryptionconfiguration-jobbookmarksencryption.md">JobBookmarksEncryption</a></i>
<a href="#s3encryption" title="S3Encryption">S3Encryption</a>: <i>
      - <a href="encryptionconfiguration-s3encryption.md">S3Encryption</a></i>
</pre>

## Properties

#### CloudwatchEncryption

_Required_: No
_Type_: List of <a href="encryptionconfiguration-cloudwatchencryption.md">CloudwatchEncryption</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JobBookmarksEncryption

_Required_: No
_Type_: List of <a href="encryptionconfiguration-jobbookmarksencryption.md">JobBookmarksEncryption</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3Encryption

_Required_: No
_Type_: List of <a href="encryptionconfiguration-s3encryption.md">S3Encryption</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

