# Terraform::AWS::GlueSecurityConfiguration

CloudFormation equivalent of aws_glue_security_configuration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::GlueSecurityConfiguration",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#encryptionconfiguration" title="EncryptionConfiguration">EncryptionConfiguration</a>" : <i>[ <a href="encryptionconfiguration.md">EncryptionConfiguration</a>, ... ]</i>,
        "<a href="#cloudwatchencryption" title="CloudwatchEncryption">CloudwatchEncryption</a>" : <i>[ <a href="cloudwatchencryption.md">CloudwatchEncryption</a>, ... ]</i>,
        "<a href="#jobbookmarksencryption" title="JobBookmarksEncryption">JobBookmarksEncryption</a>" : <i>[ <a href="jobbookmarksencryption.md">JobBookmarksEncryption</a>, ... ]</i>,
        "<a href="#s3encryption" title="S3Encryption">S3Encryption</a>" : <i>[ <a href="s3encryption.md">S3Encryption</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::GlueSecurityConfiguration
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#encryptionconfiguration" title="EncryptionConfiguration">EncryptionConfiguration</a>: <i>
      - <a href="encryptionconfiguration.md">EncryptionConfiguration</a></i>
    <a href="#cloudwatchencryption" title="CloudwatchEncryption">CloudwatchEncryption</a>: <i>
      - <a href="cloudwatchencryption.md">CloudwatchEncryption</a></i>
    <a href="#jobbookmarksencryption" title="JobBookmarksEncryption">JobBookmarksEncryption</a>: <i>
      - <a href="jobbookmarksencryption.md">JobBookmarksEncryption</a></i>
    <a href="#s3encryption" title="S3Encryption">S3Encryption</a>: <i>
      - <a href="s3encryption.md">S3Encryption</a></i>
</pre>

## Properties

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionConfiguration

_Required_: No

_Type_: List of <a href="encryptionconfiguration.md">EncryptionConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudwatchEncryption

_Required_: No

_Type_: List of <a href="cloudwatchencryption.md">CloudwatchEncryption</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JobBookmarksEncryption

_Required_: No

_Type_: List of <a href="jobbookmarksencryption.md">JobBookmarksEncryption</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3Encryption

_Required_: No

_Type_: List of <a href="s3encryption.md">S3Encryption</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

