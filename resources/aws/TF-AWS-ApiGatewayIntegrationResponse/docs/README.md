# TF::AWS::ApiGatewayIntegrationResponse

Provides an HTTP Method Integration Response for an API Gateway Resource.

-> **Note:** Depends on having `aws_api_gateway_integration` inside your rest api. To ensure this
you might need to add an explicit `depends_on` for clean runs.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::ApiGatewayIntegrationResponse",
    "Properties" : {
        "<a href="#contenthandling" title="ContentHandling">ContentHandling</a>" : <i>String</i>,
        "<a href="#httpmethod" title="HttpMethod">HttpMethod</a>" : <i>String</i>,
        "<a href="#resourceid" title="ResourceId">ResourceId</a>" : <i>String</i>,
        "<a href="#responseparameters" title="ResponseParameters">ResponseParameters</a>" : <i>[ <a href="responseparametersdefinition.md">ResponseParametersDefinition</a>, ... ]</i>,
        "<a href="#responsetemplates" title="ResponseTemplates">ResponseTemplates</a>" : <i>[ <a href="responsetemplatesdefinition.md">ResponseTemplatesDefinition</a>, ... ]</i>,
        "<a href="#restapiid" title="RestApiId">RestApiId</a>" : <i>String</i>,
        "<a href="#selectionpattern" title="SelectionPattern">SelectionPattern</a>" : <i>String</i>,
        "<a href="#statuscode" title="StatusCode">StatusCode</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::ApiGatewayIntegrationResponse
Properties:
    <a href="#contenthandling" title="ContentHandling">ContentHandling</a>: <i>String</i>
    <a href="#httpmethod" title="HttpMethod">HttpMethod</a>: <i>String</i>
    <a href="#resourceid" title="ResourceId">ResourceId</a>: <i>String</i>
    <a href="#responseparameters" title="ResponseParameters">ResponseParameters</a>: <i>
      - <a href="responseparametersdefinition.md">ResponseParametersDefinition</a></i>
    <a href="#responsetemplates" title="ResponseTemplates">ResponseTemplates</a>: <i>
      - <a href="responsetemplatesdefinition.md">ResponseTemplatesDefinition</a></i>
    <a href="#restapiid" title="RestApiId">RestApiId</a>: <i>String</i>
    <a href="#selectionpattern" title="SelectionPattern">SelectionPattern</a>: <i>String</i>
    <a href="#statuscode" title="StatusCode">StatusCode</a>: <i>String</i>
</pre>

## Properties

#### ContentHandling

Specifies how to handle request payload content type conversions. Supported values are `CONVERT_TO_BINARY` and `CONVERT_TO_TEXT`. If this property is not defined, the response payload will be passed through from the integration response to the method response without modification.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpMethod

The HTTP method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceId

The API resource ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseParameters

A map of response parameters that can be read from the backend response.
For example: `response_parameters = { "method.response.header.X-Some-Header" = "integration.response.header.X-Some-Other-Header" }`.

_Required_: No

_Type_: List of <a href="responseparametersdefinition.md">ResponseParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseTemplates

A map specifying the templates used to transform the integration response body.

_Required_: No

_Type_: List of <a href="responsetemplatesdefinition.md">ResponseTemplatesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestApiId

The ID of the associated REST API.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SelectionPattern

Specifies the regular expression pattern used to choose
an integration response based on the response from the backend. Omit configuring this to make the integration the default one.
If the backend is an `AWS` Lambda function, the AWS Lambda function error header is matched.
For all other `HTTP` and `AWS` backends, the HTTP status code is matched.

_Required_: No

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

