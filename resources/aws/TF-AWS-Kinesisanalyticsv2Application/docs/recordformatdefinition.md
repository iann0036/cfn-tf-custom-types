# TF::AWS::Kinesisanalyticsv2Application RecordFormatDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#recordformattype" title="RecordFormatType">RecordFormatType</a>" : <i>String</i>,
    "<a href="#mappingparameters" title="MappingParameters">MappingParameters</a>" : <i>[ <a href="mappingparametersdefinition.md">MappingParametersDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#recordformattype" title="RecordFormatType">RecordFormatType</a>: <i>String</i>
<a href="#mappingparameters" title="MappingParameters">MappingParameters</a>: <i>
      - <a href="mappingparametersdefinition.md">MappingParametersDefinition</a></i>
</pre>

## Properties

#### RecordFormatType

The type of record format. Valid values: `CSV`, `JSON`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MappingParameters

_Required_: No

_Type_: List of <a href="mappingparametersdefinition.md">MappingParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

