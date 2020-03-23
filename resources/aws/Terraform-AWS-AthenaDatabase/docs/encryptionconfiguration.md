# Terraform::AWS::AthenaDatabase EncryptionConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#encryptionoption" title="EncryptionOption">EncryptionOption</a>" : <i>String</i>,
    "<a href="#kmskey" title="KmsKey">KmsKey</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#encryptionoption" title="EncryptionOption">EncryptionOption</a>: <i>String</i>
<a href="#kmskey" title="KmsKey">KmsKey</a>: <i>String</i>
</pre>

## Properties

#### EncryptionOption

The type of key; one of `SSE_S3`, `SSE_KMS`, `CSE_KMS`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKey

The KMS key ARN or ID; required for key types `SSE_KMS` and `CSE_KMS`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

