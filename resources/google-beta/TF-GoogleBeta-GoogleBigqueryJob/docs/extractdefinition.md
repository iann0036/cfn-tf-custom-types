# TF::GoogleBeta::GoogleBigqueryJob ExtractDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#compression" title="Compression">Compression</a>" : <i>String</i>,
    "<a href="#destinationformat" title="DestinationFormat">DestinationFormat</a>" : <i>String</i>,
    "<a href="#destinationuris" title="DestinationUris">DestinationUris</a>" : <i>[ String, ... ]</i>,
    "<a href="#fielddelimiter" title="FieldDelimiter">FieldDelimiter</a>" : <i>String</i>,
    "<a href="#printheader" title="PrintHeader">PrintHeader</a>" : <i>Boolean</i>,
    "<a href="#useavrologicaltypes" title="UseAvroLogicalTypes">UseAvroLogicalTypes</a>" : <i>Boolean</i>,
    "<a href="#sourcemodel" title="SourceModel">SourceModel</a>" : <i>[ <a href="sourcemodeldefinition.md">SourceModelDefinition</a>, ... ]</i>,
    "<a href="#sourcetable" title="SourceTable">SourceTable</a>" : <i>[ <a href="sourcetabledefinition.md">SourceTableDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#compression" title="Compression">Compression</a>: <i>String</i>
<a href="#destinationformat" title="DestinationFormat">DestinationFormat</a>: <i>String</i>
<a href="#destinationuris" title="DestinationUris">DestinationUris</a>: <i>
      - String</i>
<a href="#fielddelimiter" title="FieldDelimiter">FieldDelimiter</a>: <i>String</i>
<a href="#printheader" title="PrintHeader">PrintHeader</a>: <i>Boolean</i>
<a href="#useavrologicaltypes" title="UseAvroLogicalTypes">UseAvroLogicalTypes</a>: <i>Boolean</i>
<a href="#sourcemodel" title="SourceModel">SourceModel</a>: <i>
      - <a href="sourcemodeldefinition.md">SourceModelDefinition</a></i>
<a href="#sourcetable" title="SourceTable">SourceTable</a>: <i>
      - <a href="sourcetabledefinition.md">SourceTableDefinition</a></i>
</pre>

## Properties

#### Compression

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationUris

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FieldDelimiter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrintHeader

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseAvroLogicalTypes

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceModel

_Required_: No

_Type_: List of <a href="sourcemodeldefinition.md">SourceModelDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceTable

_Required_: No

_Type_: List of <a href="sourcetabledefinition.md">SourceTableDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

