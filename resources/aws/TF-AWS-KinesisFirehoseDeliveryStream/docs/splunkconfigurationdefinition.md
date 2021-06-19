# TF::AWS::KinesisFirehoseDeliveryStream SplunkConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#hecacknowledgmenttimeout" title="HecAcknowledgmentTimeout">HecAcknowledgmentTimeout</a>" : <i>Double</i>,
    "<a href="#hecendpoint" title="HecEndpoint">HecEndpoint</a>" : <i>String</i>,
    "<a href="#hecendpointtype" title="HecEndpointType">HecEndpointType</a>" : <i>String</i>,
    "<a href="#hectoken" title="HecToken">HecToken</a>" : <i>String</i>,
    "<a href="#retryduration" title="RetryDuration">RetryDuration</a>" : <i>Double</i>,
    "<a href="#s3backupmode" title="S3BackupMode">S3BackupMode</a>" : <i>String</i>,
    "<a href="#cloudwatchloggingoptions" title="CloudwatchLoggingOptions">CloudwatchLoggingOptions</a>" : <i>[ <a href="cloudwatchloggingoptionsdefinition.md">CloudwatchLoggingOptionsDefinition</a>, ... ]</i>,
    "<a href="#processingconfiguration" title="ProcessingConfiguration">ProcessingConfiguration</a>" : <i>[ <a href="processingconfigurationdefinition.md">ProcessingConfigurationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#hecacknowledgmenttimeout" title="HecAcknowledgmentTimeout">HecAcknowledgmentTimeout</a>: <i>Double</i>
<a href="#hecendpoint" title="HecEndpoint">HecEndpoint</a>: <i>String</i>
<a href="#hecendpointtype" title="HecEndpointType">HecEndpointType</a>: <i>String</i>
<a href="#hectoken" title="HecToken">HecToken</a>: <i>String</i>
<a href="#retryduration" title="RetryDuration">RetryDuration</a>: <i>Double</i>
<a href="#s3backupmode" title="S3BackupMode">S3BackupMode</a>: <i>String</i>
<a href="#cloudwatchloggingoptions" title="CloudwatchLoggingOptions">CloudwatchLoggingOptions</a>: <i>
      - <a href="cloudwatchloggingoptionsdefinition.md">CloudwatchLoggingOptionsDefinition</a></i>
<a href="#processingconfiguration" title="ProcessingConfiguration">ProcessingConfiguration</a>: <i>
      - <a href="processingconfigurationdefinition.md">ProcessingConfigurationDefinition</a></i>
</pre>

## Properties

#### HecAcknowledgmentTimeout

The amount of time, in seconds between 180 and 600, that Kinesis Firehose waits to receive an acknowledgment from Splunk after it sends it data.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HecEndpoint

The HTTP Event Collector (HEC) endpoint to which Kinesis Firehose sends your data.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HecEndpointType

The HEC endpoint type. Valid values are `Raw` or `Event`. The default value is `Raw`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HecToken

The GUID that you obtain from your Splunk cluster when you create a new HEC endpoint.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryDuration

After an initial failure to deliver to Splunk, the total amount of time, in seconds between 0 to 7200, during which Firehose re-attempts delivery (including the first attempt).  After this time has elapsed, the failed documents are written to Amazon S3.  The default value is 300s.  There will be no retry if the value is 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3BackupMode

Defines how documents should be delivered to Amazon S3.  Valid values are `FailedEventsOnly` and `AllEvents`.  Default value is `FailedEventsOnly`.

_Required_: No

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

