# Terraform::AWS::ApiGatewayMethod

Provides a HTTP Method for an API Gateway Resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::ApiGatewayMethod",
    "Properties" : {
        "<a href="#apikeyrequired" title="ApiKeyRequired">ApiKeyRequired</a>" : <i>Boolean</i>,
        "<a href="#authorization" title="Authorization">Authorization</a>" : <i>String</i>,
        "<a href="#authorizationscopes" title="AuthorizationScopes">AuthorizationScopes</a>" : <i>[ String, ... ]</i>,
        "<a href="#authorizerid" title="AuthorizerId">AuthorizerId</a>" : <i>String</i>,
        "<a href="#httpmethod" title="HttpMethod">HttpMethod</a>" : <i>String</i>,
        "<a href="#requestmodels" title="RequestModels">RequestModels</a>" : <i>[ <a href="requestmodels.md">RequestModels</a>, ... ]</i>,
        "<a href="#requestparameters" title="RequestParameters">RequestParameters</a>" : <i>[ <a href="requestparameters.md">RequestParameters</a>, ... ]</i>,
        "<a href="#requestparametersinjson" title="RequestParametersInJson">RequestParametersInJson</a>" : <i>String</i>,
        "<a href="#requestvalidatorid" title="RequestValidatorId">RequestValidatorId</a>" : <i>String</i>,
        "<a href="#resourceid" title="ResourceId">ResourceId</a>" : <i>String</i>,
        "<a href="#restapiid" title="RestApiId">RestApiId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::ApiGatewayMethod
Properties:
    <a href="#apikeyrequired" title="ApiKeyRequired">ApiKeyRequired</a>: <i>Boolean</i>
    <a href="#authorization" title="Authorization">Authorization</a>: <i>String</i>
    <a href="#authorizationscopes" title="AuthorizationScopes">AuthorizationScopes</a>: <i>
      - String</i>
    <a href="#authorizerid" title="AuthorizerId">AuthorizerId</a>: <i>String</i>
    <a href="#httpmethod" title="HttpMethod">HttpMethod</a>: <i>String</i>
    <a href="#requestmodels" title="RequestModels">RequestModels</a>: <i>
      - <a href="requestmodels.md">RequestModels</a></i>
    <a href="#requestparameters" title="RequestParameters">RequestParameters</a>: <i>
      - <a href="requestparameters.md">RequestParameters</a></i>
    <a href="#requestparametersinjson" title="RequestParametersInJson">RequestParametersInJson</a>: <i>String</i>
    <a href="#requestvalidatorid" title="RequestValidatorId">RequestValidatorId</a>: <i>String</i>
    <a href="#resourceid" title="ResourceId">ResourceId</a>: <i>String</i>
    <a href="#restapiid" title="RestApiId">RestApiId</a>: <i>String</i>
</pre>

## Properties

#### ApiKeyRequired

Specify if the method requires an API key.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authorization

The type of authorization used for the method (`NONE`, `CUSTOM`, `AWS_IAM`, `COGNITO_USER_POOLS`).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthorizationScopes

The authorization scopes used when the authorization is `COGNITO_USER_POOLS`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthorizerId

The authorizer id to be used when the authorization is `CUSTOM` or `COGNITO_USER_POOLS`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpMethod

The HTTP Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestModels

A map of the API models used for the request's content type
where key is the content type (e.g. `application/json`)
and value is either `Error`, `Empty` (built-in models) or `aws_api_gateway_model`'s `name`.

_Required_: No

_Type_: List of <a href="requestmodels.md">RequestModels</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestParameters

A map of request parameters (from the path, query string and headers) that should be passed to the integration. The boolean value indicates whether the parameter is required (`true`) or optional (`false`).
For example: `request_parameters = {"method.request.header.X-Some-Header" = true "method.request.querystring.some-query-param" = true}` would define that the header `X-Some-Header` and the query string `some-query-param` must be provided in the request.

_Required_: No

_Type_: List of <a href="requestparameters.md">RequestParameters</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestParametersInJson

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestValidatorId

The ID of a `aws_api_gateway_request_validator`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceId

The API resource ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestApiId

The ID of the associated REST API.

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

