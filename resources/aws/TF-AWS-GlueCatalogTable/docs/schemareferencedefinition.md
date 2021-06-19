# TF::AWS::GlueCatalogTable SchemaReferenceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#schemaversionid" title="SchemaVersionId">SchemaVersionId</a>" : <i>String</i>,
    "<a href="#schemaversionnumber" title="SchemaVersionNumber">SchemaVersionNumber</a>" : <i>Double</i>,
    "<a href="#schemaid" title="SchemaId">SchemaId</a>" : <i>[ <a href="schemaiddefinition.md">SchemaIdDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#schemaversionid" title="SchemaVersionId">SchemaVersionId</a>: <i>String</i>
<a href="#schemaversionnumber" title="SchemaVersionNumber">SchemaVersionNumber</a>: <i>Double</i>
<a href="#schemaid" title="SchemaId">SchemaId</a>: <i>
      - <a href="schemaiddefinition.md">SchemaIdDefinition</a></i>
</pre>

## Properties

#### SchemaVersionId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SchemaVersionNumber

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SchemaId

_Required_: No

_Type_: List of <a href="schemaiddefinition.md">SchemaIdDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

