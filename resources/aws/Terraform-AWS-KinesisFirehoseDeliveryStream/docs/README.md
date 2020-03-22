# Terraform::AWS::KinesisFirehoseDeliveryStream

CloudFormation equivalent of aws_kinesis_firehose_delivery_stream

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::KinesisFirehoseDeliveryStream",
    "Properties" : {
        "<a href="#arn" title="Arn">Arn</a>" : <i>String</i>,
        "<a href="#destination" title="Destination">Destination</a>" : <i>String</i>,
        "<a href="#destinationid" title="DestinationId">DestinationId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#versionid" title="VersionId">VersionId</a>" : <i>String</i>,
        "<a href="#elasticsearchconfiguration" title="ElasticsearchConfiguration">ElasticsearchConfiguration</a>" : <i>[ <a href="elasticsearchconfiguration.md">ElasticsearchConfiguration</a>, ... ]</i>,
        "<a href="#extendeds3configuration" title="ExtendedS3Configuration">ExtendedS3Configuration</a>" : <i>[ <a href="extendeds3configuration.md">ExtendedS3Configuration</a>, ... ]</i>,
        "<a href="#kinesissourceconfiguration" title="KinesisSourceConfiguration">KinesisSourceConfiguration</a>" : <i>[ <a href="kinesissourceconfiguration.md">KinesisSourceConfiguration</a>, ... ]</i>,
        "<a href="#redshiftconfiguration" title="RedshiftConfiguration">RedshiftConfiguration</a>" : <i>[ <a href="redshiftconfiguration.md">RedshiftConfiguration</a>, ... ]</i>,
        "<a href="#s3configuration" title="S3Configuration">S3Configuration</a>" : <i>[ <a href="s3configuration.md">S3Configuration</a>, ... ]</i>,
        "<a href="#serversideencryption" title="ServerSideEncryption">ServerSideEncryption</a>" : <i>[ <a href="serversideencryption.md">ServerSideEncryption</a>, ... ]</i>,
        "<a href="#splunkconfiguration" title="SplunkConfiguration">SplunkConfiguration</a>" : <i>[ <a href="splunkconfiguration.md">SplunkConfiguration</a>, ... ]</i>,
        "<a href="#cloudwatchloggingoptions" title="CloudwatchLoggingOptions">CloudwatchLoggingOptions</a>" : <i>[ <a href="cloudwatchloggingoptions.md">CloudwatchLoggingOptions</a>, ... ]</i>,
        "<a href="#processingconfiguration" title="ProcessingConfiguration">ProcessingConfiguration</a>" : <i>[ <a href="processingconfiguration.md">ProcessingConfiguration</a>, ... ]</i>,
        "<a href="#dataformatconversionconfiguration" title="DataFormatConversionConfiguration">DataFormatConversionConfiguration</a>" : <i>[ <a href="dataformatconversionconfiguration.md">DataFormatConversionConfiguration</a>, ... ]</i>,
        "<a href="#s3backupconfiguration" title="S3BackupConfiguration">S3BackupConfiguration</a>" : <i>[ <a href="s3backupconfiguration.md">S3BackupConfiguration</a>, ... ]</i>,
        "<a href="#processors" title="Processors">Processors</a>" : <i>[ <a href="processors.md">Processors</a>, ... ]</i>,
        "<a href="#inputformatconfiguration" title="InputFormatConfiguration">InputFormatConfiguration</a>" : <i>[ <a href="inputformatconfiguration.md">InputFormatConfiguration</a>, ... ]</i>,
        "<a href="#outputformatconfiguration" title="OutputFormatConfiguration">OutputFormatConfiguration</a>" : <i>[ <a href="outputformatconfiguration.md">OutputFormatConfiguration</a>, ... ]</i>,
        "<a href="#schemaconfiguration" title="SchemaConfiguration">SchemaConfiguration</a>" : <i>[ <a href="schemaconfiguration.md">SchemaConfiguration</a>, ... ]</i>,
        "<a href="#parameters" title="Parameters">Parameters</a>" : <i>[ <a href="parameters.md">Parameters</a>, ... ]</i>,
        "<a href="#deserializer" title="Deserializer">Deserializer</a>" : <i>[ <a href="deserializer.md">Deserializer</a>, ... ]</i>,
        "<a href="#serializer" title="Serializer">Serializer</a>" : <i>[ <a href="serializer.md">Serializer</a>, ... ]</i>,
        "<a href="#hivejsonserde" title="HiveJsonSerDe">HiveJsonSerDe</a>" : <i>[ <a href="hivejsonserde.md">HiveJsonSerDe</a>, ... ]</i>,
        "<a href="#openxjsonserde" title="OpenXJsonSerDe">OpenXJsonSerDe</a>" : <i>[ <a href="openxjsonserde.md">OpenXJsonSerDe</a>, ... ]</i>,
        "<a href="#orcserde" title="OrcSerDe">OrcSerDe</a>" : <i>[ <a href="orcserde.md">OrcSerDe</a>, ... ]</i>,
        "<a href="#parquetserde" title="ParquetSerDe">ParquetSerDe</a>" : <i>[ <a href="parquetserde.md">ParquetSerDe</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::KinesisFirehoseDeliveryStream
Properties:
    <a href="#arn" title="Arn">Arn</a>: <i>String</i>
    <a href="#destination" title="Destination">Destination</a>: <i>String</i>
    <a href="#destinationid" title="DestinationId">DestinationId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#versionid" title="VersionId">VersionId</a>: <i>String</i>
    <a href="#elasticsearchconfiguration" title="ElasticsearchConfiguration">ElasticsearchConfiguration</a>: <i>
      - <a href="elasticsearchconfiguration.md">ElasticsearchConfiguration</a></i>
    <a href="#extendeds3configuration" title="ExtendedS3Configuration">ExtendedS3Configuration</a>: <i>
      - <a href="extendeds3configuration.md">ExtendedS3Configuration</a></i>
    <a href="#kinesissourceconfiguration" title="KinesisSourceConfiguration">KinesisSourceConfiguration</a>: <i>
      - <a href="kinesissourceconfiguration.md">KinesisSourceConfiguration</a></i>
    <a href="#redshiftconfiguration" title="RedshiftConfiguration">RedshiftConfiguration</a>: <i>
      - <a href="redshiftconfiguration.md">RedshiftConfiguration</a></i>
    <a href="#s3configuration" title="S3Configuration">S3Configuration</a>: <i>
      - <a href="s3configuration.md">S3Configuration</a></i>
    <a href="#serversideencryption" title="ServerSideEncryption">ServerSideEncryption</a>: <i>
      - <a href="serversideencryption.md">ServerSideEncryption</a></i>
    <a href="#splunkconfiguration" title="SplunkConfiguration">SplunkConfiguration</a>: <i>
      - <a href="splunkconfiguration.md">SplunkConfiguration</a></i>
    <a href="#cloudwatchloggingoptions" title="CloudwatchLoggingOptions">CloudwatchLoggingOptions</a>: <i>
      - <a href="cloudwatchloggingoptions.md">CloudwatchLoggingOptions</a></i>
    <a href="#processingconfiguration" title="ProcessingConfiguration">ProcessingConfiguration</a>: <i>
      - <a href="processingconfiguration.md">ProcessingConfiguration</a></i>
    <a href="#dataformatconversionconfiguration" title="DataFormatConversionConfiguration">DataFormatConversionConfiguration</a>: <i>
      - <a href="dataformatconversionconfiguration.md">DataFormatConversionConfiguration</a></i>
    <a href="#s3backupconfiguration" title="S3BackupConfiguration">S3BackupConfiguration</a>: <i>
      - <a href="s3backupconfiguration.md">S3BackupConfiguration</a></i>
    <a href="#processors" title="Processors">Processors</a>: <i>
      - <a href="processors.md">Processors</a></i>
    <a href="#inputformatconfiguration" title="InputFormatConfiguration">InputFormatConfiguration</a>: <i>
      - <a href="inputformatconfiguration.md">InputFormatConfiguration</a></i>
    <a href="#outputformatconfiguration" title="OutputFormatConfiguration">OutputFormatConfiguration</a>: <i>
      - <a href="outputformatconfiguration.md">OutputFormatConfiguration</a></i>
    <a href="#schemaconfiguration" title="SchemaConfiguration">SchemaConfiguration</a>: <i>
      - <a href="schemaconfiguration.md">SchemaConfiguration</a></i>
    <a href="#parameters" title="Parameters">Parameters</a>: <i>
      - <a href="parameters.md">Parameters</a></i>
    <a href="#deserializer" title="Deserializer">Deserializer</a>: <i>
      - <a href="deserializer.md">Deserializer</a></i>
    <a href="#serializer" title="Serializer">Serializer</a>: <i>
      - <a href="serializer.md">Serializer</a></i>
    <a href="#hivejsonserde" title="HiveJsonSerDe">HiveJsonSerDe</a>: <i>
      - <a href="hivejsonserde.md">HiveJsonSerDe</a></i>
    <a href="#openxjsonserde" title="OpenXJsonSerDe">OpenXJsonSerDe</a>: <i>
      - <a href="openxjsonserde.md">OpenXJsonSerDe</a></i>
    <a href="#orcserde" title="OrcSerDe">OrcSerDe</a>: <i>
      - <a href="orcserde.md">OrcSerDe</a></i>
    <a href="#parquetserde" title="ParquetSerDe">ParquetSerDe</a>: <i>
      - <a href="parquetserde.md">ParquetSerDe</a></i>
</pre>

## Properties

#### Arn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ElasticsearchConfiguration

_Required_: No

_Type_: List of <a href="elasticsearchconfiguration.md">ElasticsearchConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtendedS3Configuration

_Required_: No

_Type_: List of <a href="extendeds3configuration.md">ExtendedS3Configuration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KinesisSourceConfiguration

_Required_: No

_Type_: List of <a href="kinesissourceconfiguration.md">KinesisSourceConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedshiftConfiguration

_Required_: No

_Type_: List of <a href="redshiftconfiguration.md">RedshiftConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3Configuration

_Required_: No

_Type_: List of <a href="s3configuration.md">S3Configuration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerSideEncryption

_Required_: No

_Type_: List of <a href="serversideencryption.md">ServerSideEncryption</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SplunkConfiguration

_Required_: No

_Type_: List of <a href="splunkconfiguration.md">SplunkConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudwatchLoggingOptions

_Required_: No

_Type_: List of <a href="cloudwatchloggingoptions.md">CloudwatchLoggingOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessingConfiguration

_Required_: No

_Type_: List of <a href="processingconfiguration.md">ProcessingConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataFormatConversionConfiguration

_Required_: No

_Type_: List of <a href="dataformatconversionconfiguration.md">DataFormatConversionConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3BackupConfiguration

_Required_: No

_Type_: List of <a href="s3backupconfiguration.md">S3BackupConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Processors

_Required_: No

_Type_: List of <a href="processors.md">Processors</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InputFormatConfiguration

_Required_: No

_Type_: List of <a href="inputformatconfiguration.md">InputFormatConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutputFormatConfiguration

_Required_: No

_Type_: List of <a href="outputformatconfiguration.md">OutputFormatConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SchemaConfiguration

_Required_: No

_Type_: List of <a href="schemaconfiguration.md">SchemaConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameters

_Required_: No

_Type_: List of <a href="parameters.md">Parameters</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Deserializer

_Required_: No

_Type_: List of <a href="deserializer.md">Deserializer</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Serializer

_Required_: No

_Type_: List of <a href="serializer.md">Serializer</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HiveJsonSerDe

_Required_: No

_Type_: List of <a href="hivejsonserde.md">HiveJsonSerDe</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenXJsonSerDe

_Required_: No

_Type_: List of <a href="openxjsonserde.md">OpenXJsonSerDe</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrcSerDe

_Required_: No

_Type_: List of <a href="orcserde.md">OrcSerDe</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParquetSerDe

_Required_: No

_Type_: List of <a href="parquetserde.md">ParquetSerDe</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

