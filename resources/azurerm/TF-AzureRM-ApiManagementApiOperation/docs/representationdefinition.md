# TF::AzureRM::ApiManagementApiOperation RepresentationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#contenttype" title="ContentType">ContentType</a>" : <i>String</i>,
    "<a href="#sample" title="Sample">Sample</a>" : <i>String</i>,
    "<a href="#schemaid" title="SchemaId">SchemaId</a>" : <i>String</i>,
    "<a href="#typename" title="TypeName">TypeName</a>" : <i>String</i>,
    "<a href="#formparameter" title="FormParameter">FormParameter</a>" : <i>[ <a href="formparameterdefinition.md">FormParameterDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#contenttype" title="ContentType">ContentType</a>: <i>String</i>
<a href="#sample" title="Sample">Sample</a>: <i>String</i>
<a href="#schemaid" title="SchemaId">SchemaId</a>: <i>String</i>
<a href="#typename" title="TypeName">TypeName</a>: <i>String</i>
<a href="#formparameter" title="FormParameter">FormParameter</a>: <i>
      - <a href="formparameterdefinition.md">FormParameterDefinition</a></i>
</pre>

## Properties

#### ContentType

The Content Type of this representation, such as `application/json`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sample

An example of this representation.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SchemaId

The ID of an API Management Schema which represents this Response.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TypeName

The Type Name defined by the Schema.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FormParameter

_Required_: No

_Type_: List of <a href="formparameterdefinition.md">FormParameterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

