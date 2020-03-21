# Terraform::Google::StorageTransferJob

CloudFormation equivalent of google_storage_transfer_job

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::StorageTransferJob",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#schedule" title="Schedule">Schedule</a>" : <i>[ <a href="schedule.md">Schedule</a>, ... ]</i>,
        "<a href="#transferspec" title="TransferSpec">TransferSpec</a>" : <i>[ <a href="transferspec.md">TransferSpec</a>, ... ]</i>,
        "<a href="#scheduleenddate" title="ScheduleEndDate">ScheduleEndDate</a>" : <i>[ <a href="scheduleenddate.md">ScheduleEndDate</a>, ... ]</i>,
        "<a href="#schedulestartdate" title="ScheduleStartDate">ScheduleStartDate</a>" : <i>[ <a href="schedulestartdate.md">ScheduleStartDate</a>, ... ]</i>,
        "<a href="#starttimeofday" title="StartTimeOfDay">StartTimeOfDay</a>" : <i>[ <a href="starttimeofday.md">StartTimeOfDay</a>, ... ]</i>,
        "<a href="#awss3datasource" title="AwsS3DataSource">AwsS3DataSource</a>" : <i>[ <a href="awss3datasource.md">AwsS3DataSource</a>, ... ]</i>,
        "<a href="#gcsdatasink" title="GcsDataSink">GcsDataSink</a>" : <i>[ <a href="gcsdatasink.md">GcsDataSink</a>, ... ]</i>,
        "<a href="#gcsdatasource" title="GcsDataSource">GcsDataSource</a>" : <i>[ <a href="gcsdatasource.md">GcsDataSource</a>, ... ]</i>,
        "<a href="#httpdatasource" title="HttpDataSource">HttpDataSource</a>" : <i>[ <a href="httpdatasource.md">HttpDataSource</a>, ... ]</i>,
        "<a href="#objectconditions" title="ObjectConditions">ObjectConditions</a>" : <i>[ <a href="objectconditions.md">ObjectConditions</a>, ... ]</i>,
        "<a href="#transferoptions" title="TransferOptions">TransferOptions</a>" : <i>[ <a href="transferoptions.md">TransferOptions</a>, ... ]</i>,
        "<a href="#awsaccesskey" title="AwsAccessKey">AwsAccessKey</a>" : <i>[ <a href="awsaccesskey.md">AwsAccessKey</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::StorageTransferJob
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#schedule" title="Schedule">Schedule</a>: <i>
      - <a href="schedule.md">Schedule</a></i>
    <a href="#transferspec" title="TransferSpec">TransferSpec</a>: <i>
      - <a href="transferspec.md">TransferSpec</a></i>
    <a href="#scheduleenddate" title="ScheduleEndDate">ScheduleEndDate</a>: <i>
      - <a href="scheduleenddate.md">ScheduleEndDate</a></i>
    <a href="#schedulestartdate" title="ScheduleStartDate">ScheduleStartDate</a>: <i>
      - <a href="schedulestartdate.md">ScheduleStartDate</a></i>
    <a href="#starttimeofday" title="StartTimeOfDay">StartTimeOfDay</a>: <i>
      - <a href="starttimeofday.md">StartTimeOfDay</a></i>
    <a href="#awss3datasource" title="AwsS3DataSource">AwsS3DataSource</a>: <i>
      - <a href="awss3datasource.md">AwsS3DataSource</a></i>
    <a href="#gcsdatasink" title="GcsDataSink">GcsDataSink</a>: <i>
      - <a href="gcsdatasink.md">GcsDataSink</a></i>
    <a href="#gcsdatasource" title="GcsDataSource">GcsDataSource</a>: <i>
      - <a href="gcsdatasource.md">GcsDataSource</a></i>
    <a href="#httpdatasource" title="HttpDataSource">HttpDataSource</a>: <i>
      - <a href="httpdatasource.md">HttpDataSource</a></i>
    <a href="#objectconditions" title="ObjectConditions">ObjectConditions</a>: <i>
      - <a href="objectconditions.md">ObjectConditions</a></i>
    <a href="#transferoptions" title="TransferOptions">TransferOptions</a>: <i>
      - <a href="transferoptions.md">TransferOptions</a></i>
    <a href="#awsaccesskey" title="AwsAccessKey">AwsAccessKey</a>: <i>
      - <a href="awsaccesskey.md">AwsAccessKey</a></i>
</pre>

## Properties

#### Description

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

_Required_: No

_Type_: List of <a href="schedule.md">Schedule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransferSpec

_Required_: No

_Type_: List of <a href="transferspec.md">TransferSpec</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduleEndDate

_Required_: No

_Type_: List of <a href="scheduleenddate.md">ScheduleEndDate</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduleStartDate

_Required_: No

_Type_: List of <a href="schedulestartdate.md">ScheduleStartDate</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTimeOfDay

_Required_: No

_Type_: List of <a href="starttimeofday.md">StartTimeOfDay</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsS3DataSource

_Required_: No

_Type_: List of <a href="awss3datasource.md">AwsS3DataSource</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcsDataSink

_Required_: No

_Type_: List of <a href="gcsdatasink.md">GcsDataSink</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcsDataSource

_Required_: No

_Type_: List of <a href="gcsdatasource.md">GcsDataSource</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpDataSource

_Required_: No

_Type_: List of <a href="httpdatasource.md">HttpDataSource</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectConditions

_Required_: No

_Type_: List of <a href="objectconditions.md">ObjectConditions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransferOptions

_Required_: No

_Type_: List of <a href="transferoptions.md">TransferOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsAccessKey

_Required_: No

_Type_: List of <a href="awsaccesskey.md">AwsAccessKey</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreationTime

Returns the <code>CreationTime</code> value.

#### DeletionTime

Returns the <code>DeletionTime</code> value.

#### LastModificationTime

Returns the <code>LastModificationTime</code> value.

#### Name

Returns the <code>Name</code> value.
