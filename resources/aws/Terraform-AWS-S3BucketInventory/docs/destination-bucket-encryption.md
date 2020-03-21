# Terraform::AWS::S3BucketInventory Destination Bucket Encryption

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ssekms" title="SseKms">SseKms</a>" : <i>[ <a href="destination-bucket-encryption-ssekms.md">SseKms</a>, ... ]</i>,
    "<a href="#sses3" title="SseS3">SseS3</a>" : <i>[ <a href="destination-bucket-encryption-sses3.md">SseS3</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ssekms" title="SseKms">SseKms</a>: <i>
      - <a href="destination-bucket-encryption-ssekms.md">SseKms</a></i>
<a href="#sses3" title="SseS3">SseS3</a>: <i>
      - <a href="destination-bucket-encryption-sses3.md">SseS3</a></i>
</pre>

## Properties

#### SseKms

_Required_: No
_Type_: List of <a href="destination-bucket-encryption-ssekms.md">SseKms</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SseS3

_Required_: No
_Type_: List of <a href="destination-bucket-encryption-sses3.md">SseS3</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

