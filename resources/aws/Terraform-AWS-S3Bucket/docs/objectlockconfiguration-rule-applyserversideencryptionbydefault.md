# Terraform::AWS::S3Bucket ObjectLockConfiguration Rule ApplyServerSideEncryptionByDefault

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

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SseAlgorithm

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

