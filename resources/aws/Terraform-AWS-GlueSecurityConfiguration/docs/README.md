# Terraform::AWS::GlueSecurityConfiguration

CloudFormation equivalent of aws_glue_security_configuration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::GlueSecurityConfiguration",
    "Properties" : {
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#encryptionconfiguration" title="EncryptionConfiguration">EncryptionConfiguration</a>" : <i>[ &lt;a href=&#34;encryptionconfiguration.md&#34;&gt;EncryptionConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#cloudwatchencryption" title="CloudwatchEncryption">CloudwatchEncryption</a>" : <i>[ &lt;a href=&#34;cloudwatchencryption.md&#34;&gt;CloudwatchEncryption&lt;/a&gt;, ... ]</i>,
        "<a href="#jobbookmarksencryption" title="JobBookmarksEncryption">JobBookmarksEncryption</a>" : <i>[ &lt;a href=&#34;jobbookmarksencryption.md&#34;&gt;JobBookmarksEncryption&lt;/a&gt;, ... ]</i>,
        "<a href="#s3encryption" title="S3Encryption">S3Encryption</a>" : <i>[ &lt;a href=&#34;s3encryption.md&#34;&gt;S3Encryption&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::GlueSecurityConfiguration
Properties:
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#encryptionconfiguration" title="EncryptionConfiguration">EncryptionConfiguration</a>: <i>
      - &lt;a href=&#34;encryptionconfiguration.md&#34;&gt;EncryptionConfiguration&lt;/a&gt;</i>
    <a href="#cloudwatchencryption" title="CloudwatchEncryption">CloudwatchEncryption</a>: <i>
      - &lt;a href=&#34;cloudwatchencryption.md&#34;&gt;CloudwatchEncryption&lt;/a&gt;</i>
    <a href="#jobbookmarksencryption" title="JobBookmarksEncryption">JobBookmarksEncryption</a>: <i>
      - &lt;a href=&#34;jobbookmarksencryption.md&#34;&gt;JobBookmarksEncryption&lt;/a&gt;</i>
    <a href="#s3encryption" title="S3Encryption">S3Encryption</a>: <i>
      - &lt;a href=&#34;s3encryption.md&#34;&gt;S3Encryption&lt;/a&gt;</i>
</pre>

## Properties

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;encryptionconfiguration.md&#34;&gt;EncryptionConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudwatchEncryption

_Required_: No

_Type_: List of &lt;a href=&#34;cloudwatchencryption.md&#34;&gt;CloudwatchEncryption&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JobBookmarksEncryption

_Required_: No

_Type_: List of &lt;a href=&#34;jobbookmarksencryption.md&#34;&gt;JobBookmarksEncryption&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3Encryption

_Required_: No

_Type_: List of &lt;a href=&#34;s3encryption.md&#34;&gt;S3Encryption&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

