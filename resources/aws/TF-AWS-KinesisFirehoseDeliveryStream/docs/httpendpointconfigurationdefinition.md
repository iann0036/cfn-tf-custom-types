# TF::AWS::KinesisFirehoseDeliveryStream HttpEndpointConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accesskey" title="AccessKey">AccessKey</a>" : <i>String</i>,
    "<a href="#bufferinginterval" title="BufferingInterval">BufferingInterval</a>" : <i>Double</i>,
    "<a href="#bufferingsize" title="BufferingSize">BufferingSize</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#retryduration" title="RetryDuration">RetryDuration</a>" : <i>Double</i>,
    "<a href="#rolearn" title="RoleArn">RoleArn</a>" : <i>String</i>,
    "<a href="#s3backupmode" title="S3BackupMode">S3BackupMode</a>" : <i>String</i>,
    "<a href="#url" title="Url">Url</a>" : <i>String</i>,
    "<a href="#cloudwatchloggingoptions" title="CloudwatchLoggingOptions">CloudwatchLoggingOptions</a>" : <i>[ <a href="cloudwatchloggingoptionsdefinition.md">CloudwatchLoggingOptionsDefinition</a>, ... ]</i>,
    "<a href="#processingconfiguration" title="ProcessingConfiguration">ProcessingConfiguration</a>" : <i>[ <a href="processingconfigurationdefinition.md">ProcessingConfigurationDefinition</a>, ... ]</i>,
    "<a href="#requestconfiguration" title="RequestConfiguration">RequestConfiguration</a>" : <i>[ <a href="requestconfigurationdefinition.md">RequestConfigurationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#accesskey" title="AccessKey">AccessKey</a>: <i>String</i>
<a href="#bufferinginterval" title="BufferingInterval">BufferingInterval</a>: <i>Double</i>
<a href="#bufferingsize" title="BufferingSize">BufferingSize</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#retryduration" title="RetryDuration">RetryDuration</a>: <i>Double</i>
<a href="#rolearn" title="RoleArn">RoleArn</a>: <i>String</i>
<a href="#s3backupmode" title="S3BackupMode">S3BackupMode</a>: <i>String</i>
<a href="#url" title="Url">Url</a>: <i>String</i>
<a href="#cloudwatchloggingoptions" title="CloudwatchLoggingOptions">CloudwatchLoggingOptions</a>: <i>
      - <a href="cloudwatchloggingoptionsdefinition.md">CloudwatchLoggingOptionsDefinition</a></i>
<a href="#processingconfiguration" title="ProcessingConfiguration">ProcessingConfiguration</a>: <i>
      - <a href="processingconfigurationdefinition.md">ProcessingConfigurationDefinition</a></i>
<a href="#requestconfiguration" title="RequestConfiguration">RequestConfiguration</a>: <i>
      - <a href="requestconfigurationdefinition.md">RequestConfigurationDefinition</a></i>
</pre>

## Properties

#### AccessKey

The access key required for Kinesis Firehose to authenticate with the HTTP endpoint selected as the destination.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BufferingInterval

Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300 (5 minutes).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BufferingSize

Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The HTTP endpoint name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryDuration

Total amount of seconds Firehose spends on retries. This duration starts after the initial attempt fails, It does not include the time periods during which Firehose waits for acknowledgment from the specified destination after each attempt. Valid values between `0` and `7200`. Default is `300`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleArn

Kinesis Data Firehose uses this IAM role for all the permissions that the delivery stream needs. The pattern needs to be `arn:.*`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3BackupMode

Defines how documents should be delivered to Amazon S3.  Valid values are `FailedDataOnly` and `AllData`.  Default value is `FailedDataOnly`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

The HTTP endpoint URL to which Kinesis Firehose sends your data.

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

#### RequestConfiguration

_Required_: No

_Type_: List of <a href="requestconfigurationdefinition.md">RequestConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

