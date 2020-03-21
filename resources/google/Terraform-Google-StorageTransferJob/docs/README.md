# Terraform::Google::StorageTransferJob

CloudFormation equivalent of google_storage_transfer_job

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::StorageTransferJob",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#creationtime" title="CreationTime">CreationTime</a>" : <i>String</i>,
        "<a href="#deletiontime" title="DeletionTime">DeletionTime</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#lastmodificationtime" title="LastModificationTime">LastModificationTime</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#schedule" title="Schedule">Schedule</a>" : <i>[ &lt;a href=&#34;schedule.md&#34;&gt;Schedule&lt;/a&gt;, ... ]</i>,
        "<a href="#transferspec" title="TransferSpec">TransferSpec</a>" : <i>[ &lt;a href=&#34;transferspec.md&#34;&gt;TransferSpec&lt;/a&gt;, ... ]</i>,
        "<a href="#scheduleenddate" title="ScheduleEndDate">ScheduleEndDate</a>" : <i>[ &lt;a href=&#34;scheduleenddate.md&#34;&gt;ScheduleEndDate&lt;/a&gt;, ... ]</i>,
        "<a href="#schedulestartdate" title="ScheduleStartDate">ScheduleStartDate</a>" : <i>[ &lt;a href=&#34;schedulestartdate.md&#34;&gt;ScheduleStartDate&lt;/a&gt;, ... ]</i>,
        "<a href="#starttimeofday" title="StartTimeOfDay">StartTimeOfDay</a>" : <i>[ &lt;a href=&#34;starttimeofday.md&#34;&gt;StartTimeOfDay&lt;/a&gt;, ... ]</i>,
        "<a href="#awss3datasource" title="AwsS3DataSource">AwsS3DataSource</a>" : <i>[ &lt;a href=&#34;awss3datasource.md&#34;&gt;AwsS3DataSource&lt;/a&gt;, ... ]</i>,
        "<a href="#gcsdatasink" title="GcsDataSink">GcsDataSink</a>" : <i>[ &lt;a href=&#34;gcsdatasink.md&#34;&gt;GcsDataSink&lt;/a&gt;, ... ]</i>,
        "<a href="#gcsdatasource" title="GcsDataSource">GcsDataSource</a>" : <i>[ &lt;a href=&#34;gcsdatasource.md&#34;&gt;GcsDataSource&lt;/a&gt;, ... ]</i>,
        "<a href="#httpdatasource" title="HttpDataSource">HttpDataSource</a>" : <i>[ &lt;a href=&#34;httpdatasource.md&#34;&gt;HttpDataSource&lt;/a&gt;, ... ]</i>,
        "<a href="#objectconditions" title="ObjectConditions">ObjectConditions</a>" : <i>[ &lt;a href=&#34;objectconditions.md&#34;&gt;ObjectConditions&lt;/a&gt;, ... ]</i>,
        "<a href="#transferoptions" title="TransferOptions">TransferOptions</a>" : <i>[ &lt;a href=&#34;transferoptions.md&#34;&gt;TransferOptions&lt;/a&gt;, ... ]</i>,
        "<a href="#awsaccesskey" title="AwsAccessKey">AwsAccessKey</a>" : <i>[ &lt;a href=&#34;awsaccesskey.md&#34;&gt;AwsAccessKey&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::StorageTransferJob
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#creationtime" title="CreationTime">CreationTime</a>: <i>String</i>
    <a href="#deletiontime" title="DeletionTime">DeletionTime</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#lastmodificationtime" title="LastModificationTime">LastModificationTime</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#schedule" title="Schedule">Schedule</a>: <i>
      - &lt;a href=&#34;schedule.md&#34;&gt;Schedule&lt;/a&gt;</i>
    <a href="#transferspec" title="TransferSpec">TransferSpec</a>: <i>
      - &lt;a href=&#34;transferspec.md&#34;&gt;TransferSpec&lt;/a&gt;</i>
    <a href="#scheduleenddate" title="ScheduleEndDate">ScheduleEndDate</a>: <i>
      - &lt;a href=&#34;scheduleenddate.md&#34;&gt;ScheduleEndDate&lt;/a&gt;</i>
    <a href="#schedulestartdate" title="ScheduleStartDate">ScheduleStartDate</a>: <i>
      - &lt;a href=&#34;schedulestartdate.md&#34;&gt;ScheduleStartDate&lt;/a&gt;</i>
    <a href="#starttimeofday" title="StartTimeOfDay">StartTimeOfDay</a>: <i>
      - &lt;a href=&#34;starttimeofday.md&#34;&gt;StartTimeOfDay&lt;/a&gt;</i>
    <a href="#awss3datasource" title="AwsS3DataSource">AwsS3DataSource</a>: <i>
      - &lt;a href=&#34;awss3datasource.md&#34;&gt;AwsS3DataSource&lt;/a&gt;</i>
    <a href="#gcsdatasink" title="GcsDataSink">GcsDataSink</a>: <i>
      - &lt;a href=&#34;gcsdatasink.md&#34;&gt;GcsDataSink&lt;/a&gt;</i>
    <a href="#gcsdatasource" title="GcsDataSource">GcsDataSource</a>: <i>
      - &lt;a href=&#34;gcsdatasource.md&#34;&gt;GcsDataSource&lt;/a&gt;</i>
    <a href="#httpdatasource" title="HttpDataSource">HttpDataSource</a>: <i>
      - &lt;a href=&#34;httpdatasource.md&#34;&gt;HttpDataSource&lt;/a&gt;</i>
    <a href="#objectconditions" title="ObjectConditions">ObjectConditions</a>: <i>
      - &lt;a href=&#34;objectconditions.md&#34;&gt;ObjectConditions&lt;/a&gt;</i>
    <a href="#transferoptions" title="TransferOptions">TransferOptions</a>: <i>
      - &lt;a href=&#34;transferoptions.md&#34;&gt;TransferOptions&lt;/a&gt;</i>
    <a href="#awsaccesskey" title="AwsAccessKey">AwsAccessKey</a>: <i>
      - &lt;a href=&#34;awsaccesskey.md&#34;&gt;AwsAccessKey&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreationTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeletionTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LastModificationTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

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

_Type_: List of &lt;a href=&#34;schedule.md&#34;&gt;Schedule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransferSpec

_Required_: No

_Type_: List of &lt;a href=&#34;transferspec.md&#34;&gt;TransferSpec&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduleEndDate

_Required_: No

_Type_: List of &lt;a href=&#34;scheduleenddate.md&#34;&gt;ScheduleEndDate&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduleStartDate

_Required_: No

_Type_: List of &lt;a href=&#34;schedulestartdate.md&#34;&gt;ScheduleStartDate&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTimeOfDay

_Required_: No

_Type_: List of &lt;a href=&#34;starttimeofday.md&#34;&gt;StartTimeOfDay&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsS3DataSource

_Required_: No

_Type_: List of &lt;a href=&#34;awss3datasource.md&#34;&gt;AwsS3DataSource&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcsDataSink

_Required_: No

_Type_: List of &lt;a href=&#34;gcsdatasink.md&#34;&gt;GcsDataSink&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcsDataSource

_Required_: No

_Type_: List of &lt;a href=&#34;gcsdatasource.md&#34;&gt;GcsDataSource&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpDataSource

_Required_: No

_Type_: List of &lt;a href=&#34;httpdatasource.md&#34;&gt;HttpDataSource&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectConditions

_Required_: No

_Type_: List of &lt;a href=&#34;objectconditions.md&#34;&gt;ObjectConditions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransferOptions

_Required_: No

_Type_: List of &lt;a href=&#34;transferoptions.md&#34;&gt;TransferOptions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsAccessKey

_Required_: No

_Type_: List of &lt;a href=&#34;awsaccesskey.md&#34;&gt;AwsAccessKey&lt;/a&gt;

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

Returns the &lt;code&gt;CreationTime&lt;/code&gt; value.

#### DeletionTime

Returns the &lt;code&gt;DeletionTime&lt;/code&gt; value.

#### LastModificationTime

Returns the &lt;code&gt;LastModificationTime&lt;/code&gt; value.

#### Name

Returns the &lt;code&gt;Name&lt;/code&gt; value.

