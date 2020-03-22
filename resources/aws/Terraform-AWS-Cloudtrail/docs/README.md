# Terraform::AWS::Cloudtrail

CloudFormation equivalent of aws_cloudtrail

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

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudWatchLogsRoleArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableLogFileValidation

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableLogging

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeGlobalServiceEvents

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsMultiRegionTrail

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsOrganizationTrail

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3BucketName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3KeyPrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnsTopicName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

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

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

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

