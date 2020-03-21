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
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#cloudwatchloggingoptions" title="CloudwatchLoggingOptions">CloudwatchLoggingOptions</a>" : <i>[ &lt;a href=&#34;cloudwatchloggingoptions.md&#34;&gt;CloudwatchLoggingOptions&lt;/a&gt;, ... ]</i>,
        "<a href="#inputs" title="Inputs">Inputs</a>" : <i>[ &lt;a href=&#34;inputs.md&#34;&gt;Inputs&lt;/a&gt;, ... ]</i>,
        "<a href="#outputs" title="Outputs">Outputs</a>" : <i>[ &lt;a href=&#34;outputs.md&#34;&gt;Outputs&lt;/a&gt;, ... ]</i>,
        "<a href="#referencedatasources" title="ReferenceDataSources">ReferenceDataSources</a>" : <i>[ &lt;a href=&#34;referencedatasources.md&#34;&gt;ReferenceDataSources&lt;/a&gt;, ... ]</i>,
        "<a href="#kinesisfirehose" title="KinesisFirehose">KinesisFirehose</a>" : <i>[ &lt;a href=&#34;kinesisfirehose.md&#34;&gt;KinesisFirehose&lt;/a&gt;, ... ]</i>,
        "<a href="#kinesisstream" title="KinesisStream">KinesisStream</a>" : <i>[ &lt;a href=&#34;kinesisstream.md&#34;&gt;KinesisStream&lt;/a&gt;, ... ]</i>,
        "<a href="#parallelism" title="Parallelism">Parallelism</a>" : <i>[ &lt;a href=&#34;parallelism.md&#34;&gt;Parallelism&lt;/a&gt;, ... ]</i>,
        "<a href="#processingconfiguration" title="ProcessingConfiguration">ProcessingConfiguration</a>" : <i>[ &lt;a href=&#34;processingconfiguration.md&#34;&gt;ProcessingConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#schema" title="Schema">Schema</a>" : <i>[ &lt;a href=&#34;schema.md&#34;&gt;Schema&lt;/a&gt;, ... ]</i>,
        "<a href="#lambda" title="Lambda">Lambda</a>" : <i>[ &lt;a href=&#34;lambda.md&#34;&gt;Lambda&lt;/a&gt;, ... ]</i>,
        "<a href="#s3" title="S3">S3</a>" : <i>[ &lt;a href=&#34;s3.md&#34;&gt;S3&lt;/a&gt;, ... ]</i>,
        "<a href="#recordcolumns" title="RecordColumns">RecordColumns</a>" : <i>[ &lt;a href=&#34;recordcolumns.md&#34;&gt;RecordColumns&lt;/a&gt;, ... ]</i>,
        "<a href="#recordformat" title="RecordFormat">RecordFormat</a>" : <i>[ &lt;a href=&#34;recordformat.md&#34;&gt;RecordFormat&lt;/a&gt;, ... ]</i>,
        "<a href="#mappingparameters" title="MappingParameters">MappingParameters</a>" : <i>[ &lt;a href=&#34;mappingparameters.md&#34;&gt;MappingParameters&lt;/a&gt;, ... ]</i>,
        "<a href="#csv" title="Csv">Csv</a>" : <i>[ &lt;a href=&#34;csv.md&#34;&gt;Csv&lt;/a&gt;, ... ]</i>,
        "<a href="#json" title="Json">Json</a>" : <i>[ &lt;a href=&#34;json.md&#34;&gt;Json&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::KinesisAnalyticsApplication
Properties:
    <a href="#code" title="Code">Code</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#cloudwatchloggingoptions" title="CloudwatchLoggingOptions">CloudwatchLoggingOptions</a>: <i>
      - &lt;a href=&#34;cloudwatchloggingoptions.md&#34;&gt;CloudwatchLoggingOptions&lt;/a&gt;</i>
    <a href="#inputs" title="Inputs">Inputs</a>: <i>
      - &lt;a href=&#34;inputs.md&#34;&gt;Inputs&lt;/a&gt;</i>
    <a href="#outputs" title="Outputs">Outputs</a>: <i>
      - &lt;a href=&#34;outputs.md&#34;&gt;Outputs&lt;/a&gt;</i>
    <a href="#referencedatasources" title="ReferenceDataSources">ReferenceDataSources</a>: <i>
      - &lt;a href=&#34;referencedatasources.md&#34;&gt;ReferenceDataSources&lt;/a&gt;</i>
    <a href="#kinesisfirehose" title="KinesisFirehose">KinesisFirehose</a>: <i>
      - &lt;a href=&#34;kinesisfirehose.md&#34;&gt;KinesisFirehose&lt;/a&gt;</i>
    <a href="#kinesisstream" title="KinesisStream">KinesisStream</a>: <i>
      - &lt;a href=&#34;kinesisstream.md&#34;&gt;KinesisStream&lt;/a&gt;</i>
    <a href="#parallelism" title="Parallelism">Parallelism</a>: <i>
      - &lt;a href=&#34;parallelism.md&#34;&gt;Parallelism&lt;/a&gt;</i>
    <a href="#processingconfiguration" title="ProcessingConfiguration">ProcessingConfiguration</a>: <i>
      - &lt;a href=&#34;processingconfiguration.md&#34;&gt;ProcessingConfiguration&lt;/a&gt;</i>
    <a href="#schema" title="Schema">Schema</a>: <i>
      - &lt;a href=&#34;schema.md&#34;&gt;Schema&lt;/a&gt;</i>
    <a href="#lambda" title="Lambda">Lambda</a>: <i>
      - &lt;a href=&#34;lambda.md&#34;&gt;Lambda&lt;/a&gt;</i>
    <a href="#s3" title="S3">S3</a>: <i>
      - &lt;a href=&#34;s3.md&#34;&gt;S3&lt;/a&gt;</i>
    <a href="#recordcolumns" title="RecordColumns">RecordColumns</a>: <i>
      - &lt;a href=&#34;recordcolumns.md&#34;&gt;RecordColumns&lt;/a&gt;</i>
    <a href="#recordformat" title="RecordFormat">RecordFormat</a>: <i>
      - &lt;a href=&#34;recordformat.md&#34;&gt;RecordFormat&lt;/a&gt;</i>
    <a href="#mappingparameters" title="MappingParameters">MappingParameters</a>: <i>
      - &lt;a href=&#34;mappingparameters.md&#34;&gt;MappingParameters&lt;/a&gt;</i>
    <a href="#csv" title="Csv">Csv</a>: <i>
      - &lt;a href=&#34;csv.md&#34;&gt;Csv&lt;/a&gt;</i>
    <a href="#json" title="Json">Json</a>: <i>
      - &lt;a href=&#34;json.md&#34;&gt;Json&lt;/a&gt;</i>
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

#### CloudwatchLoggingOptions

_Required_: No

_Type_: List of &lt;a href=&#34;cloudwatchloggingoptions.md&#34;&gt;CloudwatchLoggingOptions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Inputs

_Required_: No

_Type_: List of &lt;a href=&#34;inputs.md&#34;&gt;Inputs&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Outputs

_Required_: No

_Type_: List of &lt;a href=&#34;outputs.md&#34;&gt;Outputs&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReferenceDataSources

_Required_: No

_Type_: List of &lt;a href=&#34;referencedatasources.md&#34;&gt;ReferenceDataSources&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KinesisFirehose

_Required_: No

_Type_: List of &lt;a href=&#34;kinesisfirehose.md&#34;&gt;KinesisFirehose&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KinesisStream

_Required_: No

_Type_: List of &lt;a href=&#34;kinesisstream.md&#34;&gt;KinesisStream&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parallelism

_Required_: No

_Type_: List of &lt;a href=&#34;parallelism.md&#34;&gt;Parallelism&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessingConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;processingconfiguration.md&#34;&gt;ProcessingConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schema

_Required_: No

_Type_: List of &lt;a href=&#34;schema.md&#34;&gt;Schema&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lambda

_Required_: No

_Type_: List of &lt;a href=&#34;lambda.md&#34;&gt;Lambda&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3

_Required_: No

_Type_: List of &lt;a href=&#34;s3.md&#34;&gt;S3&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecordColumns

_Required_: No

_Type_: List of &lt;a href=&#34;recordcolumns.md&#34;&gt;RecordColumns&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecordFormat

_Required_: No

_Type_: List of &lt;a href=&#34;recordformat.md&#34;&gt;RecordFormat&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MappingParameters

_Required_: No

_Type_: List of &lt;a href=&#34;mappingparameters.md&#34;&gt;MappingParameters&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Csv

_Required_: No

_Type_: List of &lt;a href=&#34;csv.md&#34;&gt;Csv&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Json

_Required_: No

_Type_: List of &lt;a href=&#34;json.md&#34;&gt;Json&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the &lt;code&gt;Arn&lt;/code&gt; value.

#### CreateTimestamp

Returns the &lt;code&gt;CreateTimestamp&lt;/code&gt; value.

#### LastUpdateTimestamp

Returns the &lt;code&gt;LastUpdateTimestamp&lt;/code&gt; value.

#### Status

Returns the &lt;code&gt;Status&lt;/code&gt; value.

#### Version

Returns the &lt;code&gt;Version&lt;/code&gt; value.

