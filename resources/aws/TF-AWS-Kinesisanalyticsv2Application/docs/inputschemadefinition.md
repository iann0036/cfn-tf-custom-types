# TF::AWS::Kinesisanalyticsv2Application InputSchemaDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#recordencoding" title="RecordEncoding">RecordEncoding</a>" : <i>String</i>,
    "<a href="#recordcolumn" title="RecordColumn">RecordColumn</a>" : <i>[ <a href="recordcolumndefinition.md">RecordColumnDefinition</a>, ... ]</i>,
    "<a href="#recordformat" title="RecordFormat">RecordFormat</a>" : <i>[ <a href="recordformatdefinition.md">RecordFormatDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#recordencoding" title="RecordEncoding">RecordEncoding</a>: <i>String</i>
<a href="#recordcolumn" title="RecordColumn">RecordColumn</a>: <i>
      - <a href="recordcolumndefinition.md">RecordColumnDefinition</a></i>
<a href="#recordformat" title="RecordFormat">RecordFormat</a>: <i>
      - <a href="recordformatdefinition.md">RecordFormatDefinition</a></i>
</pre>

## Properties

#### RecordEncoding

Specifies the encoding of the records in the streaming source. For example, `UTF-8`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecordColumn

_Required_: No

_Type_: List of <a href="recordcolumndefinition.md">RecordColumnDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecordFormat

_Required_: No

_Type_: List of <a href="recordformatdefinition.md">RecordFormatDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

