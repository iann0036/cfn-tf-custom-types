# Terraform::AWS::KinesisFirehoseDeliveryStream RedshiftConfiguration

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
    "<a href="#cloudwatchloggingoptions" title="CloudwatchLoggingOptions">CloudwatchLoggingOptions</a>" : <i>[ &lt;a href=&#34;redshiftconfiguration-cloudwatchloggingoptions.md&#34;&gt;CloudwatchLoggingOptions&lt;/a&gt;, ... ]</i>,
    "<a href="#processingconfiguration" title="ProcessingConfiguration">ProcessingConfiguration</a>" : <i>[ &lt;a href=&#34;redshiftconfiguration-processingconfiguration.md&#34;&gt;ProcessingConfiguration&lt;/a&gt;, ... ]</i>,
    "<a href="#s3backupconfiguration" title="S3BackupConfiguration">S3BackupConfiguration</a>" : <i>[ &lt;a href=&#34;redshiftconfiguration-s3backupconfiguration.md&#34;&gt;S3BackupConfiguration&lt;/a&gt;, ... ]</i>
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
      - &lt;a href=&#34;redshiftconfiguration-cloudwatchloggingoptions.md&#34;&gt;CloudwatchLoggingOptions&lt;/a&gt;</i>
<a href="#processingconfiguration" title="ProcessingConfiguration">ProcessingConfiguration</a>: <i>
      - &lt;a href=&#34;redshiftconfiguration-processingconfiguration.md&#34;&gt;ProcessingConfiguration&lt;/a&gt;</i>
<a href="#s3backupconfiguration" title="S3BackupConfiguration">S3BackupConfiguration</a>: <i>
      - &lt;a href=&#34;redshiftconfiguration-s3backupconfiguration.md&#34;&gt;S3BackupConfiguration&lt;/a&gt;</i>
</pre>

## Properties

#### ClusterJdbcurl

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CopyOptions

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataTableColumns

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataTableName

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryDuration

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleArn

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3BackupMode

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudwatchLoggingOptions

_Required_: No
_Type_: List of &lt;a href=&#34;redshiftconfiguration-cloudwatchloggingoptions.md&#34;&gt;CloudwatchLoggingOptions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessingConfiguration

_Required_: No
_Type_: List of &lt;a href=&#34;redshiftconfiguration-processingconfiguration.md&#34;&gt;ProcessingConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3BackupConfiguration

_Required_: No
_Type_: List of &lt;a href=&#34;redshiftconfiguration-s3backupconfiguration.md&#34;&gt;S3BackupConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

