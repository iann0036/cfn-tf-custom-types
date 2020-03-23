# Terraform::AWS::ApiGatewayMethodResponse

Provides an HTTP Method Response for an API Gateway Resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::ApiGatewayMethodResponse",
    "Properties" : {
        "<a href="#httpmethod" title="HttpMethod">HttpMethod</a>" : <i>String</i>,
        "<a href="#resourceid" title="ResourceId">ResourceId</a>" : <i>String</i>,
        "<a href="#responsemodels" title="ResponseModels">ResponseModels</a>" : <i>[ <a href="responsemodels.md">ResponseModels</a>, ... ]</i>,
        "<a href="#responseparameters" title="ResponseParameters">ResponseParameters</a>" : <i>[ <a href="responseparameters.md">ResponseParameters</a>, ... ]</i>,
        "<a href="#responseparametersinjson" title="ResponseParametersInJson">ResponseParametersInJson</a>" : <i>String</i>,
        "<a href="#restapiid" title="RestApiId">RestApiId</a>" : <i>String</i>,
        "<a href="#statuscode" title="StatusCode">StatusCode</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::ApiGatewayMethodResponse
Properties:
    <a href="#httpmethod" title="HttpMethod">HttpMethod</a>: <i>String</i>
    <a href="#resourceid" title="ResourceId">ResourceId</a>: <i>String</i>
    <a href="#responsemodels" title="ResponseModels">ResponseModels</a>: <i>
      - <a href="responsemodels.md">ResponseModels</a></i>
    <a href="#responseparameters" title="ResponseParameters">ResponseParameters</a>: <i>
      - <a href="responseparameters.md">ResponseParameters</a></i>
    <a href="#responseparametersinjson" title="ResponseParametersInJson">ResponseParametersInJson</a>: <i>String</i>
    <a href="#restapiid" title="RestApiId">RestApiId</a>: <i>String</i>
    <a href="#statuscode" title="StatusCode">StatusCode</a>: <i>String</i>
</pre>

## Properties

#### HttpMethod

The HTTP Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceId

The API resource ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseModels

A map of the API models used for the response's content type.

_Required_: No

_Type_: List of <a href="responsemodels.md">ResponseModels</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseParameters

A map of response parameters that can be sent to the caller.
For example: `response_parameters = { "method.response.header.X-Some-Header" = true }`
would define that the header `X-Some-Header` can be provided on the response.

_Required_: No

_Type_: List of <a href="responseparameters.md">ResponseParameters</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseParametersInJson

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestApiId

The ID of the associated REST API.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatusCode

The HTTP status code.

_Required_: Yes

_Type_: String

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

