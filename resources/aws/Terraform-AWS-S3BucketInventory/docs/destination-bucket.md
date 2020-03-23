# Terraform::AWS::S3BucketInventory Destination Bucket

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accountid" title="AccountId">AccountId</a>" : <i>String</i>,
    "<a href="#bucketarn" title="BucketArn">BucketArn</a>" : <i>String</i>,
    "<a href="#format" title="Format">Format</a>" : <i>String</i>,
    "<a href="#prefix" title="Prefix">Prefix</a>" : <i>String</i>,
    "<a href="#encryption" title="Encryption">Encryption</a>" : <i>[ <a href="destination-bucket-encryption.md">Encryption</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#accountid" title="AccountId">AccountId</a>: <i>String</i>
<a href="#bucketarn" title="BucketArn">BucketArn</a>: <i>String</i>
<a href="#format" title="Format">Format</a>: <i>String</i>
<a href="#prefix" title="Prefix">Prefix</a>: <i>String</i>
<a href="#encryption" title="Encryption">Encryption</a>: <i>
      - <a href="destination-bucket-encryption.md">Encryption</a></i>
</pre>

## Properties

#### AccountId

The ID of the account that owns the destination bucket. Recommended to be set to prevent problems if the destination bucket ownership changes.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BucketArn

The Amazon S3 bucket ARN of the destination.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Format

Specifies the output format of the inventory results. Can be `CSV`, [`ORC`](https://orc.apache.org/) or [`Parquet`](https://parquet.apache.org/).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prefix

The prefix that is prepended to all inventory results.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encryption

_Required_: No

_Type_: List of <a href="destination-bucket-encryption.md">Encryption</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

