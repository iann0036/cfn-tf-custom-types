# Terraform::AWS::Cloudtrail

CloudFormation equivalent of aws_cloudtrail

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::Cloudtrail",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#arn" title="Arn">Arn</a>" : <i>String</i>,
        "<a href="#cloudwatchlogsgrouparn" title="CloudWatchLogsGroupArn">CloudWatchLogsGroupArn</a>" : <i>String</i>,
        "<a href="#cloudwatchlogsrolearn" title="CloudWatchLogsRoleArn">CloudWatchLogsRoleArn</a>" : <i>String</i>,
        "<a href="#enablelogfilevalidation" title="EnableLogFileValidation">EnableLogFileValidation</a>" : <i>Boolean</i>,
        "<a href="#enablelogging" title="EnableLogging">EnableLogging</a>" : <i>Boolean</i>,
        "<a href="#homeregion" title="HomeRegion">HomeRegion</a>" : <i>String</i>,
        "<a href="#includeglobalserviceevents" title="IncludeGlobalServiceEvents">IncludeGlobalServiceEvents</a>" : <i>Boolean</i>,
        "<a href="#ismultiregiontrail" title="IsMultiRegionTrail">IsMultiRegionTrail</a>" : <i>Boolean</i>,
        "<a href="#isorganizationtrail" title="IsOrganizationTrail">IsOrganizationTrail</a>" : <i>Boolean</i>,
        "<a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#s3bucketname" title="S3BucketName">S3BucketName</a>" : <i>String</i>,
        "<a href="#s3keyprefix" title="S3KeyPrefix">S3KeyPrefix</a>" : <i>String</i>,
        "<a href="#snstopicname" title="SnsTopicName">SnsTopicName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#eventselector" title="EventSelector">EventSelector</a>" : <i>[ &lt;a href=&#34;eventselector.md&#34;&gt;EventSelector&lt;/a&gt;, ... ]</i>,
        "<a href="#dataresource" title="DataResource">DataResource</a>" : <i>[ &lt;a href=&#34;dataresource.md&#34;&gt;DataResource&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::Cloudtrail
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#arn" title="Arn">Arn</a>: <i>String</i>
    <a href="#cloudwatchlogsgrouparn" title="CloudWatchLogsGroupArn">CloudWatchLogsGroupArn</a>: <i>String</i>
    <a href="#cloudwatchlogsrolearn" title="CloudWatchLogsRoleArn">CloudWatchLogsRoleArn</a>: <i>String</i>
    <a href="#enablelogfilevalidation" title="EnableLogFileValidation">EnableLogFileValidation</a>: <i>Boolean</i>
    <a href="#enablelogging" title="EnableLogging">EnableLogging</a>: <i>Boolean</i>
    <a href="#homeregion" title="HomeRegion">HomeRegion</a>: <i>String</i>
    <a href="#includeglobalserviceevents" title="IncludeGlobalServiceEvents">IncludeGlobalServiceEvents</a>: <i>Boolean</i>
    <a href="#ismultiregiontrail" title="IsMultiRegionTrail">IsMultiRegionTrail</a>: <i>Boolean</i>
    <a href="#isorganizationtrail" title="IsOrganizationTrail">IsOrganizationTrail</a>: <i>Boolean</i>
    <a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#s3bucketname" title="S3BucketName">S3BucketName</a>: <i>String</i>
    <a href="#s3keyprefix" title="S3KeyPrefix">S3KeyPrefix</a>: <i>String</i>
    <a href="#snstopicname" title="SnsTopicName">SnsTopicName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#eventselector" title="EventSelector">EventSelector</a>: <i>
      - &lt;a href=&#34;eventselector.md&#34;&gt;EventSelector&lt;/a&gt;</i>
    <a href="#dataresource" title="DataResource">DataResource</a>: <i>
      - &lt;a href=&#34;dataresource.md&#34;&gt;DataResource&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Arn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

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

#### HomeRegion

_Required_: No

_Type_: String

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

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventSelector

_Required_: No

_Type_: List of &lt;a href=&#34;eventselector.md&#34;&gt;EventSelector&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataResource

_Required_: No

_Type_: List of &lt;a href=&#34;dataresource.md&#34;&gt;DataResource&lt;/a&gt;

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

Returns the &lt;code&gt;Arn&lt;/code&gt; value.

#### HomeRegion

Returns the &lt;code&gt;HomeRegion&lt;/code&gt; value.

