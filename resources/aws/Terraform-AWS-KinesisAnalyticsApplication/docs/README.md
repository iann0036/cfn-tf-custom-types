# Terraform::AWS::KinesisAnalyticsApplication

CloudFormation equivalent of aws_kinesis_analytics_application

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::KinesisAnalyticsApplication",
    "Properties" : {
        "<a href="#code" title="Code">Code</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#cloudwatchloggingoptions" title="CloudwatchLoggingOptions">CloudwatchLoggingOptions</a>" : <i>[ <a href="cloudwatchloggingoptions.md">CloudwatchLoggingOptions</a>, ... ]</i>,
        "<a href="#inputs" title="Inputs">Inputs</a>" : <i>[ <a href="inputs.md">Inputs</a>, ... ]</i>,
        "<a href="#outputs" title="Outputs">Outputs</a>" : <i>[ <a href="outputs.md">Outputs</a>, ... ]</i>,
        "<a href="#referencedatasources" title="ReferenceDataSources">ReferenceDataSources</a>" : <i>[ <a href="referencedatasources.md">ReferenceDataSources</a>, ... ]</i>,
        "<a href="#kinesisfirehose" title="KinesisFirehose">KinesisFirehose</a>" : <i>[ <a href="kinesisfirehose.md">KinesisFirehose</a>, ... ]</i>,
        "<a href="#kinesisstream" title="KinesisStream">KinesisStream</a>" : <i>[ <a href="kinesisstream.md">KinesisStream</a>, ... ]</i>,
        "<a href="#parallelism" title="Parallelism">Parallelism</a>" : <i>[ <a href="parallelism.md">Parallelism</a>, ... ]</i>,
        "<a href="#processingconfiguration" title="ProcessingConfiguration">ProcessingConfiguration</a>" : <i>[ <a href="processingconfiguration.md">ProcessingConfiguration</a>, ... ]</i>,
        "<a href="#schema" title="Schema">Schema</a>" : <i>[ <a href="schema.md">Schema</a>, ... ]</i>,
        "<a href="#lambda" title="Lambda">Lambda</a>" : <i>[ <a href="lambda.md">Lambda</a>, ... ]</i>,
        "<a href="#s3" title="S3">S3</a>" : <i>[ <a href="s3.md">S3</a>, ... ]</i>,
        "<a href="#recordcolumns" title="RecordColumns">RecordColumns</a>" : <i>[ <a href="recordcolumns.md">RecordColumns</a>, ... ]</i>,
        "<a href="#recordformat" title="RecordFormat">RecordFormat</a>" : <i>[ <a href="recordformat.md">RecordFormat</a>, ... ]</i>,
        "<a href="#mappingparameters" title="MappingParameters">MappingParameters</a>" : <i>[ <a href="mappingparameters.md">MappingParameters</a>, ... ]</i>,
        "<a href="#csv" title="Csv">Csv</a>" : <i>[ <a href="csv.md">Csv</a>, ... ]</i>,
        "<a href="#json" title="Json">Json</a>" : <i>[ <a href="json.md">Json</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::KinesisAnalyticsApplication
Properties:
    <a href="#code" title="Code">Code</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#cloudwatchloggingoptions" title="CloudwatchLoggingOptions">CloudwatchLoggingOptions</a>: <i>
      - <a href="cloudwatchloggingoptions.md">CloudwatchLoggingOptions</a></i>
    <a href="#inputs" title="Inputs">Inputs</a>: <i>
      - <a href="inputs.md">Inputs</a></i>
    <a href="#outputs" title="Outputs">Outputs</a>: <i>
      - <a href="outputs.md">Outputs</a></i>
    <a href="#referencedatasources" title="ReferenceDataSources">ReferenceDataSources</a>: <i>
      - <a href="referencedatasources.md">ReferenceDataSources</a></i>
    <a href="#kinesisfirehose" title="KinesisFirehose">KinesisFirehose</a>: <i>
      - <a href="kinesisfirehose.md">KinesisFirehose</a></i>
    <a href="#kinesisstream" title="KinesisStream">KinesisStream</a>: <i>
      - <a href="kinesisstream.md">KinesisStream</a></i>
    <a href="#parallelism" title="Parallelism">Parallelism</a>: <i>
      - <a href="parallelism.md">Parallelism</a></i>
    <a href="#processingconfiguration" title="ProcessingConfiguration">ProcessingConfiguration</a>: <i>
      - <a href="processingconfiguration.md">ProcessingConfiguration</a></i>
    <a href="#schema" title="Schema">Schema</a>: <i>
      - <a href="schema.md">Schema</a></i>
    <a href="#lambda" title="Lambda">Lambda</a>: <i>
      - <a href="lambda.md">Lambda</a></i>
    <a href="#s3" title="S3">S3</a>: <i>
      - <a href="s3.md">S3</a></i>
    <a href="#recordcolumns" title="RecordColumns">RecordColumns</a>: <i>
      - <a href="recordcolumns.md">RecordColumns</a></i>
    <a href="#recordformat" title="RecordFormat">RecordFormat</a>: <i>
      - <a href="recordformat.md">RecordFormat</a></i>
    <a href="#mappingparameters" title="MappingParameters">MappingParameters</a>: <i>
      - <a href="mappingparameters.md">MappingParameters</a></i>
    <a href="#csv" title="Csv">Csv</a>: <i>
      - <a href="csv.md">Csv</a></i>
    <a href="#json" title="Json">Json</a>: <i>
      - <a href="json.md">Json</a></i>
</pre>

## Properties

#### Code

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

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

#### CloudwatchLoggingOptions

_Required_: No

_Type_: List of <a href="cloudwatchloggingoptions.md">CloudwatchLoggingOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Inputs

_Required_: No

_Type_: List of <a href="inputs.md">Inputs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Outputs

_Required_: No

_Type_: List of <a href="outputs.md">Outputs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReferenceDataSources

_Required_: No

_Type_: List of <a href="referencedatasources.md">ReferenceDataSources</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KinesisFirehose

_Required_: No

_Type_: List of <a href="kinesisfirehose.md">KinesisFirehose</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KinesisStream

_Required_: No

_Type_: List of <a href="kinesisstream.md">KinesisStream</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parallelism

_Required_: No

_Type_: List of <a href="parallelism.md">Parallelism</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessingConfiguration

_Required_: No

_Type_: List of <a href="processingconfiguration.md">ProcessingConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schema

_Required_: No

_Type_: List of <a href="schema.md">Schema</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lambda

_Required_: No

_Type_: List of <a href="lambda.md">Lambda</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3

_Required_: No

_Type_: List of <a href="s3.md">S3</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecordColumns

_Required_: No

_Type_: List of <a href="recordcolumns.md">RecordColumns</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecordFormat

_Required_: No

_Type_: List of <a href="recordformat.md">RecordFormat</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MappingParameters

_Required_: No

_Type_: List of <a href="mappingparameters.md">MappingParameters</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Csv

_Required_: No

_Type_: List of <a href="csv.md">Csv</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Json

_Required_: No

_Type_: List of <a href="json.md">Json</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### CreateTimestamp

Returns the <code>CreateTimestamp</code> value.

#### Id

Returns the <code>Id</code> value.

#### LastUpdateTimestamp

Returns the <code>LastUpdateTimestamp</code> value.

#### Status

Returns the <code>Status</code> value.

#### Version

Returns the <code>Version</code> value.

