# TF::AWS::KinesisFirehoseDeliveryStream S3ConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bucketarn" title="BucketArn">BucketArn</a>" : <i>String</i>,
    "<a href="#bufferinterval" title="BufferInterval">BufferInterval</a>" : <i>Double</i>,
    "<a href="#buffersize" title="BufferSize">BufferSize</a>" : <i>Double</i>,
    "<a href="#compressionformat" title="CompressionFormat">CompressionFormat</a>" : <i>String</i>,
    "<a href="#kmskeyarn" title="KmsKeyArn">KmsKeyArn</a>" : <i>String</i>,
    "<a href="#prefix" title="Prefix">Prefix</a>" : <i>String</i>,
    "<a href="#rolearn" title="RoleArn">RoleArn</a>" : <i>String</i>,
    "<a href="#cloudwatchloggingoptions" title="CloudwatchLoggingOptions">CloudwatchLoggingOptions</a>" : <i>[ <a href="cloudwatchloggingoptionsdefinition.md">CloudwatchLoggingOptionsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#bucketarn" title="BucketArn">BucketArn</a>: <i>String</i>
<a href="#bufferinterval" title="BufferInterval">BufferInterval</a>: <i>Double</i>
<a href="#buffersize" title="BufferSize">BufferSize</a>: <i>Double</i>
<a href="#compressionformat" title="CompressionFormat">CompressionFormat</a>: <i>String</i>
<a href="#kmskeyarn" title="KmsKeyArn">KmsKeyArn</a>: <i>String</i>
<a href="#prefix" title="Prefix">Prefix</a>: <i>String</i>
<a href="#rolearn" title="RoleArn">RoleArn</a>: <i>String</i>
<a href="#cloudwatchloggingoptions" title="CloudwatchLoggingOptions">CloudwatchLoggingOptions</a>: <i>
      - <a href="cloudwatchloggingoptionsdefinition.md">CloudwatchLoggingOptionsDefinition</a></i>
</pre>

## Properties

#### BucketArn

The ARN of the S3 bucket.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BufferInterval

Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BufferSize

Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec set SizeInMBs to be 10 MB or higher.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompressionFormat

The compression format. If no value is specified, the default is UNCOMPRESSED. Other supported values are GZIP, ZIP & Snappy. If the destination is redshift you cannot use ZIP or Snappy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyArn

Specifies the KMS key ARN the stream will use to encrypt data. If not set, no encryption will
be used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prefix

The "YYYY/MM/DD/HH" time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleArn

The ARN of the AWS credentials.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudwatchLoggingOptions

_Required_: No

_Type_: List of <a href="cloudwatchloggingoptionsdefinition.md">CloudwatchLoggingOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

