# TF::AWS::Apigatewayv2Route

Manages an Amazon API Gateway Version 2 route.
More information can be found in the [Amazon API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) for [WebSocket](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-develop-routes.html) and [HTTP](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-routes.html) APIs.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::Apigatewayv2Route",
    "Properties" : {
        "<a href="#apiid" title="ApiId">ApiId</a>" : <i>String</i>,
        "<a href="#apikeyrequired" title="ApiKeyRequired">ApiKeyRequired</a>" : <i>Boolean</i>,
        "<a href="#authorizationscopes" title="AuthorizationScopes">AuthorizationScopes</a>" : <i>[ String, ... ]</i>,
        "<a href="#authorizationtype" title="AuthorizationType">AuthorizationType</a>" : <i>String</i>,
        "<a href="#authorizerid" title="AuthorizerId">AuthorizerId</a>" : <i>String</i>,
        "<a href="#modelselectionexpression" title="ModelSelectionExpression">ModelSelectionExpression</a>" : <i>String</i>,
        "<a href="#operationname" title="OperationName">OperationName</a>" : <i>String</i>,
        "<a href="#requestmodels" title="RequestModels">RequestModels</a>" : <i>[ <a href="requestmodelsdefinition.md">RequestModelsDefinition</a>, ... ]</i>,
        "<a href="#routekey" title="RouteKey">RouteKey</a>" : <i>String</i>,
        "<a href="#routeresponseselectionexpression" title="RouteResponseSelectionExpression">RouteResponseSelectionExpression</a>" : <i>String</i>,
        "<a href="#target" title="Target">Target</a>" : <i>String</i>,
        "<a href="#requestparameter" title="RequestParameter">RequestParameter</a>" : <i>[ <a href="requestparameterdefinition.md">RequestParameterDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::Apigatewayv2Route
Properties:
    <a href="#apiid" title="ApiId">ApiId</a>: <i>String</i>
    <a href="#apikeyrequired" title="ApiKeyRequired">ApiKeyRequired</a>: <i>Boolean</i>
    <a href="#authorizationscopes" title="AuthorizationScopes">AuthorizationScopes</a>: <i>
      - String</i>
    <a href="#authorizationtype" title="AuthorizationType">AuthorizationType</a>: <i>String</i>
    <a href="#authorizerid" title="AuthorizerId">AuthorizerId</a>: <i>String</i>
    <a href="#modelselectionexpression" title="ModelSelectionExpression">ModelSelectionExpression</a>: <i>String</i>
    <a href="#operationname" title="OperationName">OperationName</a>: <i>String</i>
    <a href="#requestmodels" title="RequestModels">RequestModels</a>: <i>
      - <a href="requestmodelsdefinition.md">RequestModelsDefinition</a></i>
    <a href="#routekey" title="RouteKey">RouteKey</a>: <i>String</i>
    <a href="#routeresponseselectionexpression" title="RouteResponseSelectionExpression">RouteResponseSelectionExpression</a>: <i>String</i>
    <a href="#target" title="Target">Target</a>: <i>String</i>
    <a href="#requestparameter" title="RequestParameter">RequestParameter</a>: <i>
      - <a href="requestparameterdefinition.md">RequestParameterDefinition</a></i>
</pre>

## Properties

#### ApiId

The API identifier.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiKeyRequired

Boolean whether an API key is required for the route. Defaults to `false`. Supported only for WebSocket APIs.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthorizationScopes

The authorization scopes supported by this route. The scopes are used with a JWT authorizer to authorize the method invocation.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthorizationType

The authorization type for the route.
For WebSocket APIs, valid values are `NONE` for open access, `AWS_IAM` for using AWS IAM permissions, and `CUSTOM` for using a Lambda authorizer.
For HTTP APIs, valid values are `NONE` for open access, `JWT` for using JSON Web Tokens, `AWS_IAM` for using AWS IAM permissions, and `CUSTOM` for using a Lambda authorizer.
Defaults to `NONE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthorizerId

The identifier of the [`aws_apigatewayv2_authorizer`](apigatewayv2_authorizer.html) resource to be associated with this route.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ModelSelectionExpression

The [model selection expression](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-model-selection-expressions) for the route. Supported only for WebSocket APIs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OperationName

The operation name for the route. Must be between 1 and 64 characters in length.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestModels

The request models for the route. Supported only for WebSocket APIs.

_Required_: No

_Type_: List of <a href="requestmodelsdefinition.md">RequestModelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteKey

The route key for the route. For HTTP APIs, the route key can be either `$default`, or a combination of an HTTP method and resource path, for example, `GET /pets`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteResponseSelectionExpression

The [route response selection expression](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-route-response-selection-expressions) for the route. Supported only for WebSocket APIs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Target

The target for the route, of the form `integrations/`*`IntegrationID`*, where *`IntegrationID`* is the identifier of an [`aws_apigatewayv2_integration`](apigatewayv2_integration.html) resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestParameter

_Required_: No

_Type_: List of <a href="requestparameterdefinition.md">RequestParameterDefinition</a>

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

