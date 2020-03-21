# Terraform::AWS::KinesisFirehoseDeliveryStream SplunkConfiguration

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
    "<a href="#cloudwatchloggingoptions" title="CloudwatchLoggingOptions">CloudwatchLoggingOptions</a>" : <i>[ <a href="splunkconfiguration-cloudwatchloggingoptions.md">CloudwatchLoggingOptions</a>, ... ]</i>,
    "<a href="#processingconfiguration" title="ProcessingConfiguration">ProcessingConfiguration</a>" : <i>[ <a href="splunkconfiguration-processingconfiguration.md">ProcessingConfiguration</a>, ... ]</i>
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
      - <a href="splunkconfiguration-cloudwatchloggingoptions.md">CloudwatchLoggingOptions</a></i>
<a href="#processingconfiguration" title="ProcessingConfiguration">ProcessingConfiguration</a>: <i>
      - <a href="splunkconfiguration-processingconfiguration.md">ProcessingConfiguration</a></i>
</pre>

## Properties

#### HecAcknowledgmentTimeout

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HecEndpoint

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HecEndpointType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HecToken

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryDuration

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3BackupMode

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudwatchLoggingOptions

_Required_: No
_Type_: List of <a href="splunkconfiguration-cloudwatchloggingoptions.md">CloudwatchLoggingOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessingConfiguration

_Required_: No
_Type_: List of <a href="splunkconfiguration-processingconfiguration.md">ProcessingConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

