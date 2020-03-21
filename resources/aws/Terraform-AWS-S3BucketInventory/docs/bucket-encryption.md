# Terraform::AWS::S3BucketInventory Bucket Encryption

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ssekms" title="SseKms">SseKms</a>" : <i>[ &lt;a href=&#34;bucket-encryption-ssekms.md&#34;&gt;SseKms&lt;/a&gt;, ... ]</i>,
    "<a href="#sses3" title="SseS3">SseS3</a>" : <i>[ &lt;a href=&#34;bucket-encryption-sses3.md&#34;&gt;SseS3&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ssekms" title="SseKms">SseKms</a>: <i>
      - &lt;a href=&#34;bucket-encryption-ssekms.md&#34;&gt;SseKms&lt;/a&gt;</i>
<a href="#sses3" title="SseS3">SseS3</a>: <i>
      - &lt;a href=&#34;bucket-encryption-sses3.md&#34;&gt;SseS3&lt;/a&gt;</i>
</pre>

## Properties

#### SseKms

_Required_: No
_Type_: List of &lt;a href=&#34;bucket-encryption-ssekms.md&#34;&gt;SseKms&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SseS3

_Required_: No
_Type_: List of &lt;a href=&#34;bucket-encryption-sses3.md&#34;&gt;SseS3&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

