# TF::AWS::Macie2ClassificationJob

Provides a resource to manage an [AWS Macie Classification Job](https://docs.aws.amazon.com/macie/latest/APIReference/jobs.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::Macie2ClassificationJob",
    "Properties" : {
        "<a href="#customdataidentifierids" title="CustomDataIdentifierIds">CustomDataIdentifierIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#initialrun" title="InitialRun">InitialRun</a>" : <i>Boolean</i>,
        "<a href="#jobstatus" title="JobStatus">JobStatus</a>" : <i>String</i>,
        "<a href="#jobtype" title="JobType">JobType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nameprefix" title="NamePrefix">NamePrefix</a>" : <i>String</i>,
        "<a href="#samplingpercentage" title="SamplingPercentage">SamplingPercentage</a>" : <i>Double</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#s3jobdefinition" title="S3JobDefinition">S3JobDefinition</a>" : <i>[ <a href="s3jobdefinitiondefinition.md">S3JobDefinitionDefinition</a>, ... ]</i>,
        "<a href="#schedulefrequency" title="ScheduleFrequency">ScheduleFrequency</a>" : <i>[ <a href="schedulefrequencydefinition.md">ScheduleFrequencyDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::Macie2ClassificationJob
Properties:
    <a href="#customdataidentifierids" title="CustomDataIdentifierIds">CustomDataIdentifierIds</a>: <i>
      - String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#initialrun" title="InitialRun">InitialRun</a>: <i>Boolean</i>
    <a href="#jobstatus" title="JobStatus">JobStatus</a>: <i>String</i>
    <a href="#jobtype" title="JobType">JobType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nameprefix" title="NamePrefix">NamePrefix</a>: <i>String</i>
    <a href="#samplingpercentage" title="SamplingPercentage">SamplingPercentage</a>: <i>Double</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#s3jobdefinition" title="S3JobDefinition">S3JobDefinition</a>: <i>
      - <a href="s3jobdefinitiondefinition.md">S3JobDefinitionDefinition</a></i>
    <a href="#schedulefrequency" title="ScheduleFrequency">ScheduleFrequency</a>: <i>
      - <a href="schedulefrequencydefinition.md">ScheduleFrequencyDefinition</a></i>
</pre>

## Properties

#### CustomDataIdentifierIds

The custom data identifiers to use for data analysis and classification.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A custom description of the job. The description can contain as many as 200 characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitialRun

Specifies whether to analyze all existing, eligible objects immediately after the job is created.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JobStatus

The status for the job. Valid values are: `CANCELLED`, `RUNNING` and `USER_PAUSED`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JobType

The schedule for running the job. Valid values are: `ONE_TIME` - Run the job only once. If you specify this value, don't specify a value for the `schedule_frequency` property. `SCHEDULED` - Run the job on a daily, weekly, or monthly basis. If you specify this value, use the `schedule_frequency` property to define the recurrence pattern for the job.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A custom name for the job. The name can contain as many as 500 characters. If omitted, Terraform will assign a random, unique name. Conflicts with `name_prefix`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamePrefix

Creates a unique name beginning with the specified prefix. Conflicts with `name`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SamplingPercentage

The sampling depth, as a percentage, to apply when processing objects. This value determines the percentage of eligible objects that the job analyzes. If this value is less than 100, Amazon Macie selects the objects to analyze at random, up to the specified percentage, and analyzes all the data in those objects.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A map of key-value pairs that specifies the tags to associate with the job. A job can have a maximum of 50 tags. Each tag consists of a tag key and an associated tag value. The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3JobDefinition

_Required_: No

_Type_: List of <a href="s3jobdefinitiondefinition.md">S3JobDefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduleFrequency

_Required_: No

_Type_: List of <a href="schedulefrequencydefinition.md">ScheduleFrequencyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### Id

Returns the <code>Id</code> value.

#### JobArn

Returns the <code>JobArn</code> value.

#### JobId

Returns the <code>JobId</code> value.

#### UserPausedDetails

Returns the <code>UserPausedDetails</code> value.

