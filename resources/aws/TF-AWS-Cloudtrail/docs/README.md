# TF::AWS::Cloudtrail

Provides a CloudTrail resource.

-> **Tip:** For a multi-region trail, this resource must be in the home region of the trail.

-> **Tip:** For an organization trail, this resource must be in the master account of the organization.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::Cloudtrail",
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
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#eventselector" title="EventSelector">EventSelector</a>" : <i>[ <a href="eventselectordefinition.md">EventSelectorDefinition</a>, ... ]</i>,
        "<a href="#insightselector" title="InsightSelector">InsightSelector</a>" : <i>[ <a href="insightselectordefinition.md">InsightSelectorDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::Cloudtrail
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
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#eventselector" title="EventSelector">EventSelector</a>: <i>
      - <a href="eventselectordefinition.md">EventSelectorDefinition</a></i>
    <a href="#insightselector" title="InsightSelector">InsightSelector</a>: <i>
      - <a href="insightselectordefinition.md">InsightSelectorDefinition</a></i>
</pre>

## Properties

#### CloudWatchLogsGroupArn

Log group name using an ARN that represents the log group to which CloudTrail logs will be delivered. Note that CloudTrail requires the Log Stream wildcard.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudWatchLogsRoleArn

Role for the CloudWatch Logs endpoint to assume to write to a user’s log group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableLogFileValidation

Whether log file integrity validation is enabled. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableLogging

Enables logging for the trail. Defaults to `true`. Setting this to `false` will pause logging.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeGlobalServiceEvents

Whether the trail is publishing events from global services such as IAM to the log files. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsMultiRegionTrail

Whether the trail is created in the current region or in all regions. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsOrganizationTrail

Whether the trail is an AWS Organizations trail. Organization trails log events for the master account and all member accounts. Can only be created in the organization master account. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyId

KMS key ARN to use to encrypt the logs delivered by CloudTrail.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the trail.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3BucketName

Name of the S3 bucket designated for publishing log files.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3KeyPrefix

S3 key prefix that follows the name of the bucket you have designated for log file delivery.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnsTopicName

Name of the Amazon SNS topic defined for notification of log file delivery.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Map of tags to assign to the trail. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventSelector

_Required_: No

_Type_: List of <a href="eventselectordefinition.md">EventSelectorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsightSelector

_Required_: No

_Type_: List of <a href="insightselectordefinition.md">InsightSelectorDefinition</a>

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

