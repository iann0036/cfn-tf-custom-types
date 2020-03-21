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
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#versionid" title="VersionId">VersionId</a>" : <i>String</i>,
        "<a href="#elasticsearchconfiguration" title="ElasticsearchConfiguration">ElasticsearchConfiguration</a>" : <i>[ &lt;a href=&#34;elasticsearchconfiguration.md&#34;&gt;ElasticsearchConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#extendeds3configuration" title="ExtendedS3Configuration">ExtendedS3Configuration</a>" : <i>[ &lt;a href=&#34;extendeds3configuration.md&#34;&gt;ExtendedS3Configuration&lt;/a&gt;, ... ]</i>,
        "<a href="#kinesissourceconfiguration" title="KinesisSourceConfiguration">KinesisSourceConfiguration</a>" : <i>[ &lt;a href=&#34;kinesissourceconfiguration.md&#34;&gt;KinesisSourceConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#redshiftconfiguration" title="RedshiftConfiguration">RedshiftConfiguration</a>" : <i>[ &lt;a href=&#34;redshiftconfiguration.md&#34;&gt;RedshiftConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#s3configuration" title="S3Configuration">S3Configuration</a>" : <i>[ &lt;a href=&#34;s3configuration.md&#34;&gt;S3Configuration&lt;/a&gt;, ... ]</i>,
        "<a href="#serversideencryption" title="ServerSideEncryption">ServerSideEncryption</a>" : <i>[ &lt;a href=&#34;serversideencryption.md&#34;&gt;ServerSideEncryption&lt;/a&gt;, ... ]</i>,
        "<a href="#splunkconfiguration" title="SplunkConfiguration">SplunkConfiguration</a>" : <i>[ &lt;a href=&#34;splunkconfiguration.md&#34;&gt;SplunkConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#cloudwatchloggingoptions" title="CloudwatchLoggingOptions">CloudwatchLoggingOptions</a>" : <i>[ &lt;a href=&#34;cloudwatchloggingoptions.md&#34;&gt;CloudwatchLoggingOptions&lt;/a&gt;, ... ]</i>,
        "<a href="#processingconfiguration" title="ProcessingConfiguration">ProcessingConfiguration</a>" : <i>[ &lt;a href=&#34;processingconfiguration.md&#34;&gt;ProcessingConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#dataformatconversionconfiguration" title="DataFormatConversionConfiguration">DataFormatConversionConfiguration</a>" : <i>[ &lt;a href=&#34;dataformatconversionconfiguration.md&#34;&gt;DataFormatConversionConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#s3backupconfiguration" title="S3BackupConfiguration">S3BackupConfiguration</a>" : <i>[ &lt;a href=&#34;s3backupconfiguration.md&#34;&gt;S3BackupConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#processors" title="Processors">Processors</a>" : <i>[ &lt;a href=&#34;processors.md&#34;&gt;Processors&lt;/a&gt;, ... ]</i>,
        "<a href="#inputformatconfiguration" title="InputFormatConfiguration">InputFormatConfiguration</a>" : <i>[ &lt;a href=&#34;inputformatconfiguration.md&#34;&gt;InputFormatConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#outputformatconfiguration" title="OutputFormatConfiguration">OutputFormatConfiguration</a>" : <i>[ &lt;a href=&#34;outputformatconfiguration.md&#34;&gt;OutputFormatConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#schemaconfiguration" title="SchemaConfiguration">SchemaConfiguration</a>" : <i>[ &lt;a href=&#34;schemaconfiguration.md&#34;&gt;SchemaConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#parameters" title="Parameters">Parameters</a>" : <i>[ &lt;a href=&#34;parameters.md&#34;&gt;Parameters&lt;/a&gt;, ... ]</i>,
        "<a href="#deserializer" title="Deserializer">Deserializer</a>" : <i>[ &lt;a href=&#34;deserializer.md&#34;&gt;Deserializer&lt;/a&gt;, ... ]</i>,
        "<a href="#serializer" title="Serializer">Serializer</a>" : <i>[ &lt;a href=&#34;serializer.md&#34;&gt;Serializer&lt;/a&gt;, ... ]</i>,
        "<a href="#hivejsonserde" title="HiveJsonSerDe">HiveJsonSerDe</a>" : <i>[ &lt;a href=&#34;hivejsonserde.md&#34;&gt;HiveJsonSerDe&lt;/a&gt;, ... ]</i>,
        "<a href="#openxjsonserde" title="OpenXJsonSerDe">OpenXJsonSerDe</a>" : <i>[ &lt;a href=&#34;openxjsonserde.md&#34;&gt;OpenXJsonSerDe&lt;/a&gt;, ... ]</i>,
        "<a href="#orcserde" title="OrcSerDe">OrcSerDe</a>" : <i>[ &lt;a href=&#34;orcserde.md&#34;&gt;OrcSerDe&lt;/a&gt;, ... ]</i>,
        "<a href="#parquetserde" title="ParquetSerDe">ParquetSerDe</a>" : <i>[ &lt;a href=&#34;parquetserde.md&#34;&gt;ParquetSerDe&lt;/a&gt;, ... ]</i>
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
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#versionid" title="VersionId">VersionId</a>: <i>String</i>
    <a href="#elasticsearchconfiguration" title="ElasticsearchConfiguration">ElasticsearchConfiguration</a>: <i>
      - &lt;a href=&#34;elasticsearchconfiguration.md&#34;&gt;ElasticsearchConfiguration&lt;/a&gt;</i>
    <a href="#extendeds3configuration" title="ExtendedS3Configuration">ExtendedS3Configuration</a>: <i>
      - &lt;a href=&#34;extendeds3configuration.md&#34;&gt;ExtendedS3Configuration&lt;/a&gt;</i>
    <a href="#kinesissourceconfiguration" title="KinesisSourceConfiguration">KinesisSourceConfiguration</a>: <i>
      - &lt;a href=&#34;kinesissourceconfiguration.md&#34;&gt;KinesisSourceConfiguration&lt;/a&gt;</i>
    <a href="#redshiftconfiguration" title="RedshiftConfiguration">RedshiftConfiguration</a>: <i>
      - &lt;a href=&#34;redshiftconfiguration.md&#34;&gt;RedshiftConfiguration&lt;/a&gt;</i>
    <a href="#s3configuration" title="S3Configuration">S3Configuration</a>: <i>
      - &lt;a href=&#34;s3configuration.md&#34;&gt;S3Configuration&lt;/a&gt;</i>
    <a href="#serversideencryption" title="ServerSideEncryption">ServerSideEncryption</a>: <i>
      - &lt;a href=&#34;serversideencryption.md&#34;&gt;ServerSideEncryption&lt;/a&gt;</i>
    <a href="#splunkconfiguration" title="SplunkConfiguration">SplunkConfiguration</a>: <i>
      - &lt;a href=&#34;splunkconfiguration.md&#34;&gt;SplunkConfiguration&lt;/a&gt;</i>
    <a href="#cloudwatchloggingoptions" title="CloudwatchLoggingOptions">CloudwatchLoggingOptions</a>: <i>
      - &lt;a href=&#34;cloudwatchloggingoptions.md&#34;&gt;CloudwatchLoggingOptions&lt;/a&gt;</i>
    <a href="#processingconfiguration" title="ProcessingConfiguration">ProcessingConfiguration</a>: <i>
      - &lt;a href=&#34;processingconfiguration.md&#34;&gt;ProcessingConfiguration&lt;/a&gt;</i>
    <a href="#dataformatconversionconfiguration" title="DataFormatConversionConfiguration">DataFormatConversionConfiguration</a>: <i>
      - &lt;a href=&#34;dataformatconversionconfiguration.md&#34;&gt;DataFormatConversionConfiguration&lt;/a&gt;</i>
    <a href="#s3backupconfiguration" title="S3BackupConfiguration">S3BackupConfiguration</a>: <i>
      - &lt;a href=&#34;s3backupconfiguration.md&#34;&gt;S3BackupConfiguration&lt;/a&gt;</i>
    <a href="#processors" title="Processors">Processors</a>: <i>
      - &lt;a href=&#34;processors.md&#34;&gt;Processors&lt;/a&gt;</i>
    <a href="#inputformatconfiguration" title="InputFormatConfiguration">InputFormatConfiguration</a>: <i>
      - &lt;a href=&#34;inputformatconfiguration.md&#34;&gt;InputFormatConfiguration&lt;/a&gt;</i>
    <a href="#outputformatconfiguration" title="OutputFormatConfiguration">OutputFormatConfiguration</a>: <i>
      - &lt;a href=&#34;outputformatconfiguration.md&#34;&gt;OutputFormatConfiguration&lt;/a&gt;</i>
    <a href="#schemaconfiguration" title="SchemaConfiguration">SchemaConfiguration</a>: <i>
      - &lt;a href=&#34;schemaconfiguration.md&#34;&gt;SchemaConfiguration&lt;/a&gt;</i>
    <a href="#parameters" title="Parameters">Parameters</a>: <i>
      - &lt;a href=&#34;parameters.md&#34;&gt;Parameters&lt;/a&gt;</i>
    <a href="#deserializer" title="Deserializer">Deserializer</a>: <i>
      - &lt;a href=&#34;deserializer.md&#34;&gt;Deserializer&lt;/a&gt;</i>
    <a href="#serializer" title="Serializer">Serializer</a>: <i>
      - &lt;a href=&#34;serializer.md&#34;&gt;Serializer&lt;/a&gt;</i>
    <a href="#hivejsonserde" title="HiveJsonSerDe">HiveJsonSerDe</a>: <i>
      - &lt;a href=&#34;hivejsonserde.md&#34;&gt;HiveJsonSerDe&lt;/a&gt;</i>
    <a href="#openxjsonserde" title="OpenXJsonSerDe">OpenXJsonSerDe</a>: <i>
      - &lt;a href=&#34;openxjsonserde.md&#34;&gt;OpenXJsonSerDe&lt;/a&gt;</i>
    <a href="#orcserde" title="OrcSerDe">OrcSerDe</a>: <i>
      - &lt;a href=&#34;orcserde.md&#34;&gt;OrcSerDe&lt;/a&gt;</i>
    <a href="#parquetserde" title="ParquetSerDe">ParquetSerDe</a>: <i>
      - &lt;a href=&#34;parquetserde.md&#34;&gt;ParquetSerDe&lt;/a&gt;</i>
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

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ElasticsearchConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;elasticsearchconfiguration.md&#34;&gt;ElasticsearchConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtendedS3Configuration

_Required_: No

_Type_: List of &lt;a href=&#34;extendeds3configuration.md&#34;&gt;ExtendedS3Configuration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KinesisSourceConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;kinesissourceconfiguration.md&#34;&gt;KinesisSourceConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedshiftConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;redshiftconfiguration.md&#34;&gt;RedshiftConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3Configuration

_Required_: No

_Type_: List of &lt;a href=&#34;s3configuration.md&#34;&gt;S3Configuration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerSideEncryption

_Required_: No

_Type_: List of &lt;a href=&#34;serversideencryption.md&#34;&gt;ServerSideEncryption&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SplunkConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;splunkconfiguration.md&#34;&gt;SplunkConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudwatchLoggingOptions

_Required_: No

_Type_: List of &lt;a href=&#34;cloudwatchloggingoptions.md&#34;&gt;CloudwatchLoggingOptions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessingConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;processingconfiguration.md&#34;&gt;ProcessingConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataFormatConversionConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;dataformatconversionconfiguration.md&#34;&gt;DataFormatConversionConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3BackupConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;s3backupconfiguration.md&#34;&gt;S3BackupConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Processors

_Required_: No

_Type_: List of &lt;a href=&#34;processors.md&#34;&gt;Processors&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InputFormatConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;inputformatconfiguration.md&#34;&gt;InputFormatConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutputFormatConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;outputformatconfiguration.md&#34;&gt;OutputFormatConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SchemaConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;schemaconfiguration.md&#34;&gt;SchemaConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameters

_Required_: No

_Type_: List of &lt;a href=&#34;parameters.md&#34;&gt;Parameters&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Deserializer

_Required_: No

_Type_: List of &lt;a href=&#34;deserializer.md&#34;&gt;Deserializer&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Serializer

_Required_: No

_Type_: List of &lt;a href=&#34;serializer.md&#34;&gt;Serializer&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HiveJsonSerDe

_Required_: No

_Type_: List of &lt;a href=&#34;hivejsonserde.md&#34;&gt;HiveJsonSerDe&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenXJsonSerDe

_Required_: No

_Type_: List of &lt;a href=&#34;openxjsonserde.md&#34;&gt;OpenXJsonSerDe&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrcSerDe

_Required_: No

_Type_: List of &lt;a href=&#34;orcserde.md&#34;&gt;OrcSerDe&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParquetSerDe

_Required_: No

_Type_: List of &lt;a href=&#34;parquetserde.md&#34;&gt;ParquetSerDe&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

