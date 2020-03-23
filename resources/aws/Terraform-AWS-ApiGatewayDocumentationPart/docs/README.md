# Terraform::AWS::ApiGatewayDocumentationPart

Provides a settings of an API Gateway Documentation Part.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::ApiGatewayDocumentationPart",
    "Properties" : {
        "<a href="#properties" title="Properties">Properties</a>" : <i>String</i>,
        "<a href="#restapiid" title="RestApiId">RestApiId</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>[ <a href="location.md">Location</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::ApiGatewayDocumentationPart
Properties:
    <a href="#properties" title="Properties">Properties</a>: <i>String</i>
    <a href="#restapiid" title="RestApiId">RestApiId</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>
      - <a href="location.md">Location</a></i>
</pre>

## Properties

#### Properties

A content map of API-specific key-value pairs describing the targeted API entity. The map must be encoded as a JSON string, e.g., "{ \"description\": \"The API does ...\" }". Only Swagger-compliant key-value pairs can be exported and, hence, published.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestApiId

The ID of the associated Rest API.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: No

_Type_: List of <a href="location.md">Location</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

