# Terraform::Google::StorageTransferJob AwsS3DataSource

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bucketname" title="BucketName">BucketName</a>" : <i>String</i>,
    "<a href="#awsaccesskey" title="AwsAccessKey">AwsAccessKey</a>" : <i>[ <a href="awss3datasource-awsaccesskey.md">AwsAccessKey</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#bucketname" title="BucketName">BucketName</a>: <i>String</i>
<a href="#awsaccesskey" title="AwsAccessKey">AwsAccessKey</a>: <i>
      - <a href="awss3datasource-awsaccesskey.md">AwsAccessKey</a></i>
</pre>

## Properties

#### BucketName

S3 Bucket name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsAccessKey

_Required_: No

_Type_: List of <a href="awss3datasource-awsaccesskey.md">AwsAccessKey</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

