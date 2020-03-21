# Terraform::AWS::KinesisFirehoseDeliveryStream ExtendedS3Configuration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bucketarn" title="BucketArn">BucketArn</a>" : <i>String</i>,
    "<a href="#bufferinterval" title="BufferInterval">BufferInterval</a>" : <i>Double</i>,
    "<a href="#buffersize" title="BufferSize">BufferSize</a>" : <i>Double</i>,
    "<a href="#compressionformat" title="CompressionFormat">CompressionFormat</a>" : <i>String</i>,
    "<a href="#erroroutputprefix" title="ErrorOutputPrefix">ErrorOutputPrefix</a>" : <i>String</i>,
    "<a href="#kmskeyarn" title="KmsKeyArn">KmsKeyArn</a>" : <i>String</i>,
    "<a href="#prefix" title="Prefix">Prefix</a>" : <i>String</i>,
    "<a href="#rolearn" title="RoleArn">RoleArn</a>" : <i>String</i>,
    "<a href="#s3backupmode" title="S3BackupMode">S3BackupMode</a>" : <i>String</i>,
    "<a href="#cloudwatchloggingoptions" title="CloudwatchLoggingOptions">CloudwatchLoggingOptions</a>" : <i>[ <a href="extendeds3configuration-cloudwatchloggingoptions.md">CloudwatchLoggingOptions</a>, ... ]</i>,
    "<a href="#dataformatconversionconfiguration" title="DataFormatConversionConfiguration">DataFormatConversionConfiguration</a>" : <i>[ <a href="extendeds3configuration-dataformatconversionconfiguration.md">DataFormatConversionConfiguration</a>, ... ]</i>,
    "<a href="#processingconfiguration" title="ProcessingConfiguration">ProcessingConfiguration</a>" : <i>[ <a href="extendeds3configuration-processingconfiguration.md">ProcessingConfiguration</a>, ... ]</i>,
    "<a href="#s3backupconfiguration" title="S3BackupConfiguration">S3BackupConfiguration</a>" : <i>[ <a href="extendeds3configuration-s3backupconfiguration.md">S3BackupConfiguration</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#bucketarn" title="BucketArn">BucketArn</a>: <i>String</i>
<a href="#bufferinterval" title="BufferInterval">BufferInterval</a>: <i>Double</i>
<a href="#buffersize" title="BufferSize">BufferSize</a>: <i>Double</i>
<a href="#compressionformat" title="CompressionFormat">CompressionFormat</a>: <i>String</i>
<a href="#erroroutputprefix" title="ErrorOutputPrefix">ErrorOutputPrefix</a>: <i>String</i>
<a href="#kmskeyarn" title="KmsKeyArn">KmsKeyArn</a>: <i>String</i>
<a href="#prefix" title="Prefix">Prefix</a>: <i>String</i>
<a href="#rolearn" title="RoleArn">RoleArn</a>: <i>String</i>
<a href="#s3backupmode" title="S3BackupMode">S3BackupMode</a>: <i>String</i>
<a href="#cloudwatchloggingoptions" title="CloudwatchLoggingOptions">CloudwatchLoggingOptions</a>: <i>
      - <a href="extendeds3configuration-cloudwatchloggingoptions.md">CloudwatchLoggingOptions</a></i>
<a href="#dataformatconversionconfiguration" title="DataFormatConversionConfiguration">DataFormatConversionConfiguration</a>: <i>
      - <a href="extendeds3configuration-dataformatconversionconfiguration.md">DataFormatConversionConfiguration</a></i>
<a href="#processingconfiguration" title="ProcessingConfiguration">ProcessingConfiguration</a>: <i>
      - <a href="extendeds3configuration-processingconfiguration.md">ProcessingConfiguration</a></i>
<a href="#s3backupconfiguration" title="S3BackupConfiguration">S3BackupConfiguration</a>: <i>
      - <a href="extendeds3configuration-s3backupconfiguration.md">S3BackupConfiguration</a></i>
</pre>

## Properties

#### BucketArn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BufferInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BufferSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompressionFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ErrorOutputPrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleArn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3BackupMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudwatchLoggingOptions

_Required_: No

_Type_: List of <a href="extendeds3configuration-cloudwatchloggingoptions.md">CloudwatchLoggingOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataFormatConversionConfiguration

_Required_: No

_Type_: List of <a href="extendeds3configuration-dataformatconversionconfiguration.md">DataFormatConversionConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessingConfiguration

_Required_: No

_Type_: List of <a href="extendeds3configuration-processingconfiguration.md">ProcessingConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3BackupConfiguration

_Required_: No

_Type_: List of <a href="extendeds3configuration-s3backupconfiguration.md">S3BackupConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

