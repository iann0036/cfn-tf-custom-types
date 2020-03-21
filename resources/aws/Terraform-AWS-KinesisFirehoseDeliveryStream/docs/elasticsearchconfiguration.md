# Terraform::AWS::KinesisFirehoseDeliveryStream ElasticsearchConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bufferinginterval" title="BufferingInterval">BufferingInterval</a>" : <i>Double</i>,
    "<a href="#bufferingsize" title="BufferingSize">BufferingSize</a>" : <i>Double</i>,
    "<a href="#domainarn" title="DomainArn">DomainArn</a>" : <i>String</i>,
    "<a href="#indexname" title="IndexName">IndexName</a>" : <i>String</i>,
    "<a href="#indexrotationperiod" title="IndexRotationPeriod">IndexRotationPeriod</a>" : <i>String</i>,
    "<a href="#retryduration" title="RetryDuration">RetryDuration</a>" : <i>Double</i>,
    "<a href="#rolearn" title="RoleArn">RoleArn</a>" : <i>String</i>,
    "<a href="#s3backupmode" title="S3BackupMode">S3BackupMode</a>" : <i>String</i>,
    "<a href="#typename" title="TypeName">TypeName</a>" : <i>String</i>,
    "<a href="#cloudwatchloggingoptions" title="CloudwatchLoggingOptions">CloudwatchLoggingOptions</a>" : <i>[ <a href="elasticsearchconfiguration-cloudwatchloggingoptions.md">CloudwatchLoggingOptions</a>, ... ]</i>,
    "<a href="#processingconfiguration" title="ProcessingConfiguration">ProcessingConfiguration</a>" : <i>[ <a href="elasticsearchconfiguration-processingconfiguration.md">ProcessingConfiguration</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#bufferinginterval" title="BufferingInterval">BufferingInterval</a>: <i>Double</i>
<a href="#bufferingsize" title="BufferingSize">BufferingSize</a>: <i>Double</i>
<a href="#domainarn" title="DomainArn">DomainArn</a>: <i>String</i>
<a href="#indexname" title="IndexName">IndexName</a>: <i>String</i>
<a href="#indexrotationperiod" title="IndexRotationPeriod">IndexRotationPeriod</a>: <i>String</i>
<a href="#retryduration" title="RetryDuration">RetryDuration</a>: <i>Double</i>
<a href="#rolearn" title="RoleArn">RoleArn</a>: <i>String</i>
<a href="#s3backupmode" title="S3BackupMode">S3BackupMode</a>: <i>String</i>
<a href="#typename" title="TypeName">TypeName</a>: <i>String</i>
<a href="#cloudwatchloggingoptions" title="CloudwatchLoggingOptions">CloudwatchLoggingOptions</a>: <i>
      - <a href="elasticsearchconfiguration-cloudwatchloggingoptions.md">CloudwatchLoggingOptions</a></i>
<a href="#processingconfiguration" title="ProcessingConfiguration">ProcessingConfiguration</a>: <i>
      - <a href="elasticsearchconfiguration-processingconfiguration.md">ProcessingConfiguration</a></i>
</pre>

## Properties

#### BufferingInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BufferingSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainArn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IndexName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IndexRotationPeriod

_Required_: No

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

#### TypeName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudwatchLoggingOptions

_Required_: No

_Type_: List of <a href="elasticsearchconfiguration-cloudwatchloggingoptions.md">CloudwatchLoggingOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessingConfiguration

_Required_: No

_Type_: List of <a href="elasticsearchconfiguration-processingconfiguration.md">ProcessingConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

