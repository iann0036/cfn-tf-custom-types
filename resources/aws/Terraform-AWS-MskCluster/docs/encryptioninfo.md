# Terraform::AWS::MskCluster EncryptionInfo

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#encryptionatrestkmskeyarn" title="EncryptionAtRestKmsKeyArn">EncryptionAtRestKmsKeyArn</a>" : <i>String</i>,
    "<a href="#encryptionintransit" title="EncryptionInTransit">EncryptionInTransit</a>" : <i>[ <a href="encryptioninfo-encryptionintransit.md">EncryptionInTransit</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#encryptionatrestkmskeyarn" title="EncryptionAtRestKmsKeyArn">EncryptionAtRestKmsKeyArn</a>: <i>String</i>
<a href="#encryptionintransit" title="EncryptionInTransit">EncryptionInTransit</a>: <i>
      - <a href="encryptioninfo-encryptionintransit.md">EncryptionInTransit</a></i>
</pre>

## Properties

#### EncryptionAtRestKmsKeyArn

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionInTransit

_Required_: No
_Type_: List of <a href="encryptioninfo-encryptionintransit.md">EncryptionInTransit</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

