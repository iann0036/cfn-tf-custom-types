# TF::AWS::S3Bucket ApplyServerSideEncryptionByDefaultDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#kmsmasterkeyid" title="KmsMasterKeyId">KmsMasterKeyId</a>" : <i>String</i>,
    "<a href="#ssealgorithm" title="SseAlgorithm">SseAlgorithm</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#kmsmasterkeyid" title="KmsMasterKeyId">KmsMasterKeyId</a>: <i>String</i>
<a href="#ssealgorithm" title="SseAlgorithm">SseAlgorithm</a>: <i>String</i>
</pre>

## Properties

#### KmsMasterKeyId

The AWS KMS master key ID used for the SSE-KMS encryption. This can only be used when you set the value of `sse_algorithm` as `aws:kms`. The default `aws/s3` AWS KMS master key is used if this element is absent while the `sse_algorithm` is `aws:kms`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SseAlgorithm

The server-side encryption algorithm to use. Valid values are `AES256` and `aws:kms`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

