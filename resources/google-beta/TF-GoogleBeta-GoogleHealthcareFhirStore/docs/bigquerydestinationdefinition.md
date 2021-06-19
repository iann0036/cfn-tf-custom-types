# TF::GoogleBeta::GoogleHealthcareFhirStore BigqueryDestinationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dataseturi" title="DatasetUri">DatasetUri</a>" : <i>String</i>,
    "<a href="#schemaconfig" title="SchemaConfig">SchemaConfig</a>" : <i>[ <a href="schemaconfigdefinition.md">SchemaConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dataseturi" title="DatasetUri">DatasetUri</a>: <i>String</i>
<a href="#schemaconfig" title="SchemaConfig">SchemaConfig</a>: <i>
      - <a href="schemaconfigdefinition.md">SchemaConfigDefinition</a></i>
</pre>

## Properties

#### DatasetUri

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SchemaConfig

_Required_: No

_Type_: List of <a href="schemaconfigdefinition.md">SchemaConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

