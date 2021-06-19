# TF::AWS::Apigatewayv2Integration ResponseParametersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#mappings" title="Mappings">Mappings</a>" : <i>[ <a href="mappingsdefinition.md">MappingsDefinition</a>, ... ]</i>,
    "<a href="#statuscode" title="StatusCode">StatusCode</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#mappings" title="Mappings">Mappings</a>: <i>
      - <a href="mappingsdefinition.md">MappingsDefinition</a></i>
<a href="#statuscode" title="StatusCode">StatusCode</a>: <i>String</i>
</pre>

## Properties

#### Mappings

A key-value map. The key of ths map identifies the location of the request parameter to change, and how to change it. The corresponding value specifies the new data for the parameter.
See the [Amazon API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html) for details.

_Required_: Yes

_Type_: List of <a href="mappingsdefinition.md">MappingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatusCode

The HTTP status code in the range 200-599.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

