# TF::AWS::KinesisFirehoseDeliveryStream ExtendedS3ConfigurationDefinition

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
    "<a href="#cloudwatchloggingoptions" title="CloudwatchLoggingOptions">CloudwatchLoggingOptions</a>" : <i>[ <a href="cloudwatchloggingoptionsdefinition.md">CloudwatchLoggingOptionsDefinition</a>, ... ]</i>,
    "<a href="#dataformatconversionconfiguration" title="DataFormatConversionConfiguration">DataFormatConversionConfiguration</a>" : <i>[ <a href="dataformatconversionconfigurationdefinition.md">DataFormatConversionConfigurationDefinition</a>, ... ]</i>,
    "<a href="#processingconfiguration" title="ProcessingConfiguration">ProcessingConfiguration</a>" : <i>[ <a href="processingconfigurationdefinition.md">ProcessingConfigurationDefinition</a>, ... ]</i>,
    "<a href="#s3backupconfiguration" title="S3BackupConfiguration">S3BackupConfiguration</a>" : <i>[ <a href="s3backupconfigurationdefinition.md">S3BackupConfigurationDefinition</a>, ... ]</i>
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
      - <a href="cloudwatchloggingoptionsdefinition.md">CloudwatchLoggingOptionsDefinition</a></i>
<a href="#dataformatconversionconfiguration" title="DataFormatConversionConfiguration">DataFormatConversionConfiguration</a>: <i>
      - <a href="dataformatconversionconfigurationdefinition.md">DataFormatConversionConfigurationDefinition</a></i>
<a href="#processingconfiguration" title="ProcessingConfiguration">ProcessingConfiguration</a>: <i>
      - <a href="processingconfigurationdefinition.md">ProcessingConfigurationDefinition</a></i>
<a href="#s3backupconfiguration" title="S3BackupConfiguration">S3BackupConfiguration</a>: <i>
      - <a href="s3backupconfigurationdefinition.md">S3BackupConfigurationDefinition</a></i>
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

Prefix added to failed records before writing them to S3. This prefix appears immediately following the bucket name.

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

The Amazon S3 backup mode.  Valid values are `Disabled` and `Enabled`.  Default value is `Disabled`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudwatchLoggingOptions

_Required_: No

_Type_: List of <a href="cloudwatchloggingoptionsdefinition.md">CloudwatchLoggingOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataFormatConversionConfiguration

_Required_: No

_Type_: List of <a href="dataformatconversionconfigurationdefinition.md">DataFormatConversionConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessingConfiguration

_Required_: No

_Type_: List of <a href="processingconfigurationdefinition.md">ProcessingConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3BackupConfiguration

_Required_: No

_Type_: List of <a href="s3backupconfigurationdefinition.md">S3BackupConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

