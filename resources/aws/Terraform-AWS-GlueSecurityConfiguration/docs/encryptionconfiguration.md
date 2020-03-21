# Terraform::AWS::GlueSecurityConfiguration EncryptionConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cloudwatchencryption" title="CloudwatchEncryption">CloudwatchEncryption</a>" : <i>[ &lt;a href=&#34;encryptionconfiguration-cloudwatchencryption.md&#34;&gt;CloudwatchEncryption&lt;/a&gt;, ... ]</i>,
    "<a href="#jobbookmarksencryption" title="JobBookmarksEncryption">JobBookmarksEncryption</a>" : <i>[ &lt;a href=&#34;encryptionconfiguration-jobbookmarksencryption.md&#34;&gt;JobBookmarksEncryption&lt;/a&gt;, ... ]</i>,
    "<a href="#s3encryption" title="S3Encryption">S3Encryption</a>" : <i>[ &lt;a href=&#34;encryptionconfiguration-s3encryption.md&#34;&gt;S3Encryption&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cloudwatchencryption" title="CloudwatchEncryption">CloudwatchEncryption</a>: <i>
      - &lt;a href=&#34;encryptionconfiguration-cloudwatchencryption.md&#34;&gt;CloudwatchEncryption&lt;/a&gt;</i>
<a href="#jobbookmarksencryption" title="JobBookmarksEncryption">JobBookmarksEncryption</a>: <i>
      - &lt;a href=&#34;encryptionconfiguration-jobbookmarksencryption.md&#34;&gt;JobBookmarksEncryption&lt;/a&gt;</i>
<a href="#s3encryption" title="S3Encryption">S3Encryption</a>: <i>
      - &lt;a href=&#34;encryptionconfiguration-s3encryption.md&#34;&gt;S3Encryption&lt;/a&gt;</i>
</pre>

## Properties

#### CloudwatchEncryption

_Required_: No
_Type_: List of &lt;a href=&#34;encryptionconfiguration-cloudwatchencryption.md&#34;&gt;CloudwatchEncryption&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JobBookmarksEncryption

_Required_: No
_Type_: List of &lt;a href=&#34;encryptionconfiguration-jobbookmarksencryption.md&#34;&gt;JobBookmarksEncryption&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3Encryption

_Required_: No
_Type_: List of &lt;a href=&#34;encryptionconfiguration-s3encryption.md&#34;&gt;S3Encryption&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

