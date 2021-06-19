# TF::AWS::KinesisFirehoseDeliveryStream RedshiftConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#clusterjdbcurl" title="ClusterJdbcurl">ClusterJdbcurl</a>" : <i>String</i>,
    "<a href="#copyoptions" title="CopyOptions">CopyOptions</a>" : <i>String</i>,
    "<a href="#datatablecolumns" title="DataTableColumns">DataTableColumns</a>" : <i>String</i>,
    "<a href="#datatablename" title="DataTableName">DataTableName</a>" : <i>String</i>,
    "<a href="#password" title="Password">Password</a>" : <i>String</i>,
    "<a href="#retryduration" title="RetryDuration">RetryDuration</a>" : <i>Double</i>,
    "<a href="#rolearn" title="RoleArn">RoleArn</a>" : <i>String</i>,
    "<a href="#s3backupmode" title="S3BackupMode">S3BackupMode</a>" : <i>String</i>,
    "<a href="#username" title="Username">Username</a>" : <i>String</i>,
    "<a href="#cloudwatchloggingoptions" title="CloudwatchLoggingOptions">CloudwatchLoggingOptions</a>" : <i>[ <a href="cloudwatchloggingoptionsdefinition.md">CloudwatchLoggingOptionsDefinition</a>, ... ]</i>,
    "<a href="#processingconfiguration" title="ProcessingConfiguration">ProcessingConfiguration</a>" : <i>[ <a href="processingconfigurationdefinition.md">ProcessingConfigurationDefinition</a>, ... ]</i>,
    "<a href="#s3backupconfiguration" title="S3BackupConfiguration">S3BackupConfiguration</a>" : <i>[ <a href="s3backupconfigurationdefinition.md">S3BackupConfigurationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#clusterjdbcurl" title="ClusterJdbcurl">ClusterJdbcurl</a>: <i>String</i>
<a href="#copyoptions" title="CopyOptions">CopyOptions</a>: <i>String</i>
<a href="#datatablecolumns" title="DataTableColumns">DataTableColumns</a>: <i>String</i>
<a href="#datatablename" title="DataTableName">DataTableName</a>: <i>String</i>
<a href="#password" title="Password">Password</a>: <i>String</i>
<a href="#retryduration" title="RetryDuration">RetryDuration</a>: <i>Double</i>
<a href="#rolearn" title="RoleArn">RoleArn</a>: <i>String</i>
<a href="#s3backupmode" title="S3BackupMode">S3BackupMode</a>: <i>String</i>
<a href="#username" title="Username">Username</a>: <i>String</i>
<a href="#cloudwatchloggingoptions" title="CloudwatchLoggingOptions">CloudwatchLoggingOptions</a>: <i>
      - <a href="cloudwatchloggingoptionsdefinition.md">CloudwatchLoggingOptionsDefinition</a></i>
<a href="#processingconfiguration" title="ProcessingConfiguration">ProcessingConfiguration</a>: <i>
      - <a href="processingconfigurationdefinition.md">ProcessingConfigurationDefinition</a></i>
<a href="#s3backupconfiguration" title="S3BackupConfiguration">S3BackupConfiguration</a>: <i>
      - <a href="s3backupconfigurationdefinition.md">S3BackupConfigurationDefinition</a></i>
</pre>

## Properties

#### ClusterJdbcurl

The jdbcurl of the redshift cluster.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CopyOptions

Copy options for copying the data from the s3 intermediate bucket into redshift, for example to change the default delimiter. For valid values, see the [AWS documentation](http://docs.aws.amazon.com/firehose/latest/APIReference/API_CopyCommand.html).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataTableColumns

The data table columns that will be targeted by the copy command.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataTableName

The name of the table in the redshift cluster that the s3 bucket will copy to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

The password for the username above.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryDuration

The length of time during which Firehose retries delivery after a failure, starting from the initial request and including the first attempt. The default value is 3600 seconds (60 minutes). Firehose does not retry if the value of DurationInSeconds is 0 (zero) or if the first delivery attempt takes longer than the current value.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleArn

The arn of the role the stream assumes.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3BackupMode

The Amazon S3 backup mode.  Valid values are `Disabled` and `Enabled`.  Default value is `Disabled`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

The username that the firehose delivery stream will assume. It is strongly recommended that the username and password provided is used exclusively for Amazon Kinesis Firehose purposes, and that the permissions for the account are restricted for Amazon Redshift INSERT permissions.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudwatchLoggingOptions

_Required_: No

_Type_: List of <a href="cloudwatchloggingoptionsdefinition.md">CloudwatchLoggingOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessingConfiguration

_Required_: No

_Type_: List of <a href="processingconfigurationdefinition.md">ProcessingConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3BackupConfiguration

_Required_: No

_Type_: List of <a href="s3backupconfigurationdefinition.md">S3BackupConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

