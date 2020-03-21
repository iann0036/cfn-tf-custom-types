# Terraform::AWS::SsmMaintenanceWindowTask LoggingInfo

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#s3bucketname" title="S3BucketName">S3BucketName</a>" : <i>String</i>,
    "<a href="#s3bucketprefix" title="S3BucketPrefix">S3BucketPrefix</a>" : <i>String</i>,
    "<a href="#s3region" title="S3Region">S3Region</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#s3bucketname" title="S3BucketName">S3BucketName</a>: <i>String</i>
<a href="#s3bucketprefix" title="S3BucketPrefix">S3BucketPrefix</a>: <i>String</i>
<a href="#s3region" title="S3Region">S3Region</a>: <i>String</i>
</pre>

## Properties

#### S3BucketName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3BucketPrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3Region

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

