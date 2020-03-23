# Terraform::AWS::S3BucketInventory Destination Bucket Encryption SseKms

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#keyid" title="KeyId">KeyId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#keyid" title="KeyId">KeyId</a>: <i>String</i>
</pre>

## Properties

#### KeyId

The ARN of the KMS customer master key (CMK) used to encrypt the inventory file.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

