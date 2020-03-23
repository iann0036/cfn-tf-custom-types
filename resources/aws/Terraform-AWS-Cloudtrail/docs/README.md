# Terraform::AWS::Cloudtrail

Provides a CloudTrail resource.

~> *NOTE:* For a multi-region trail, this resource must be in the home region of the trail.

~> *NOTE:* For an organization trail, this resource must be in the master account of the organization.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::Cloudtrail",
    "Properties" : {
        "<a href="#cloudwatchlogsgrouparn" title="CloudWatchLogsGroupArn">CloudWatchLogsGroupArn</a>" : <i>String</i>,
        "<a href="#cloudwatchlogsrolearn" title="CloudWatchLogsRoleArn">CloudWatchLogsRoleArn</a>" : <i>String</i>,
        "<a href="#enablelogfilevalidation" title="EnableLogFileValidation">EnableLogFileValidation</a>" : <i>Boolean</i>,
        "<a href="#enablelogging" title="EnableLogging">EnableLogging</a>" : <i>Boolean</i>,
        "<a href="#includeglobalserviceevents" title="IncludeGlobalServiceEvents">IncludeGlobalServiceEvents</a>" : <i>Boolean</i>,
        "<a href="#ismultiregiontrail" title="IsMultiRegionTrail">IsMultiRegionTrail</a>" : <i>Boolean</i>,
        "<a href="#isorganizationtrail" title="IsOrganizationTrail">IsOrganizationTrail</a>" : <i>Boolean</i>,
        "<a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#s3bucketname" title="S3BucketName">S3BucketName</a>" : <i>String</i>,
        "<a href="#s3keyprefix" title="S3KeyPrefix">S3KeyPrefix</a>" : <i>String</i>,
        "<a href="#snstopicname" title="SnsTopicName">SnsTopicName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#eventselector" title="EventSelector">EventSelector</a>" : <i>[ <a href="eventselector.md">EventSelector</a>, ... ]</i>,
        "<a href="#dataresource" title="DataResource">DataResource</a>" : <i>[ <a href="dataresource.md">DataResource</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::Cloudtrail
Properties:
    <a href="#cloudwatchlogsgrouparn" title="CloudWatchLogsGroupArn">CloudWatchLogsGroupArn</a>: <i>String</i>
    <a href="#cloudwatchlogsrolearn" title="CloudWatchLogsRoleArn">CloudWatchLogsRoleArn</a>: <i>String</i>
    <a href="#enablelogfilevalidation" title="EnableLogFileValidation">EnableLogFileValidation</a>: <i>Boolean</i>
    <a href="#enablelogging" title="EnableLogging">EnableLogging</a>: <i>Boolean</i>
    <a href="#includeglobalserviceevents" title="IncludeGlobalServiceEvents">IncludeGlobalServiceEvents</a>: <i>Boolean</i>
    <a href="#ismultiregiontrail" title="IsMultiRegionTrail">IsMultiRegionTrail</a>: <i>Boolean</i>
    <a href="#isorganizationtrail" title="IsOrganizationTrail">IsOrganizationTrail</a>: <i>Boolean</i>
    <a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#s3bucketname" title="S3BucketName">S3BucketName</a>: <i>String</i>
    <a href="#s3keyprefix" title="S3KeyPrefix">S3KeyPrefix</a>: <i>String</i>
    <a href="#snstopicname" title="SnsTopicName">SnsTopicName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#eventselector" title="EventSelector">EventSelector</a>: <i>
      - <a href="eventselector.md">EventSelector</a></i>
    <a href="#dataresource" title="DataResource">DataResource</a>: <i>
      - <a href="dataresource.md">DataResource</a></i>
</pre>

## Properties

#### CloudWatchLogsGroupArn

Specifies a log group name using an Amazon Resource Name (ARN),
that represents the log group to which CloudTrail logs will be delivered.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudWatchLogsRoleArn

Specifies the role for the CloudWatch Logs
endpoint to assume to write to a user’s log group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableLogFileValidation

Specifies whether log file integrity validation is enabled.
Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableLogging

Enables logging for the trail. Defaults to `true`.
Setting this to `false` will pause logging.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeGlobalServiceEvents

Specifies whether the trail is publishing events
from global services such as IAM to the log files. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsMultiRegionTrail

Specifies whether the trail is created in the current
region or in all regions. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsOrganizationTrail

Specifies whether the trail is an AWS Organizations trail. Organization trails log events for the master account and all member accounts. Can only be created in the organization master account. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyId

Specifies the KMS key ARN to use to encrypt the logs delivered by CloudTrail.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the trail.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3BucketName

Specifies the name of the S3 bucket designated for publishing log files.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3KeyPrefix

Specifies the S3 key prefix that follows
the name of the bucket you have designated for log file delivery.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnsTopicName

Specifies the name of the Amazon SNS topic
defined for notification of log file delivery.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the trail.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventSelector

_Required_: No

_Type_: List of <a href="eventselector.md">EventSelector</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataResource

_Required_: No

_Type_: List of <a href="dataresource.md">DataResource</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### HomeRegion

Returns the <code>HomeRegion</code> value.

#### Id

Returns the <code>Id</code> value.

