# TF::AWS::Apigatewayv2Api

Manages an Amazon API Gateway Version 2 API.

-> **Note:** Amazon API Gateway Version 2 resources are used for creating and deploying WebSocket and HTTP APIs. To create and deploy REST APIs, use Amazon API Gateway Version 1 [resources](/docs/providers/aws/r/api_gateway_rest_api.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::Apigatewayv2Api",
    "Properties" : {
        "<a href="#apikeyselectionexpression" title="ApiKeySelectionExpression">ApiKeySelectionExpression</a>" : <i>String</i>,
        "<a href="#body" title="Body">Body</a>" : <i>String</i>,
        "<a href="#credentialsarn" title="CredentialsArn">CredentialsArn</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#disableexecuteapiendpoint" title="DisableExecuteApiEndpoint">DisableExecuteApiEndpoint</a>" : <i>Boolean</i>,
        "<a href="#failonwarnings" title="FailOnWarnings">FailOnWarnings</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#protocoltype" title="ProtocolType">ProtocolType</a>" : <i>String</i>,
        "<a href="#routekey" title="RouteKey">RouteKey</a>" : <i>String</i>,
        "<a href="#routeselectionexpression" title="RouteSelectionExpression">RouteSelectionExpression</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#target" title="Target">Target</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>,
        "<a href="#corsconfiguration" title="CorsConfiguration">CorsConfiguration</a>" : <i>[ <a href="corsconfigurationdefinition.md">CorsConfigurationDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::Apigatewayv2Api
Properties:
    <a href="#apikeyselectionexpression" title="ApiKeySelectionExpression">ApiKeySelectionExpression</a>: <i>String</i>
    <a href="#body" title="Body">Body</a>: <i>String</i>
    <a href="#credentialsarn" title="CredentialsArn">CredentialsArn</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#disableexecuteapiendpoint" title="DisableExecuteApiEndpoint">DisableExecuteApiEndpoint</a>: <i>Boolean</i>
    <a href="#failonwarnings" title="FailOnWarnings">FailOnWarnings</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#protocoltype" title="ProtocolType">ProtocolType</a>: <i>String</i>
    <a href="#routekey" title="RouteKey">RouteKey</a>: <i>String</i>
    <a href="#routeselectionexpression" title="RouteSelectionExpression">RouteSelectionExpression</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#target" title="Target">Target</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
    <a href="#corsconfiguration" title="CorsConfiguration">CorsConfiguration</a>: <i>
      - <a href="corsconfigurationdefinition.md">CorsConfigurationDefinition</a></i>
</pre>

## Properties

#### ApiKeySelectionExpression

An [API key selection expression](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions).
Valid values: `$context.authorizer.usageIdentifierKey`, `$request.header.x-api-key`. Defaults to `$request.header.x-api-key`.
Applicable for WebSocket APIs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Body

An OpenAPI specification that defines the set of routes and integrations to create as part of the HTTP APIs. Supported only for HTTP APIs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CredentialsArn

Part of _quick create_. Specifies any credentials required for the integration. Applicable for HTTP APIs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description of the API. Must be less than or equal to 1024 characters in length.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableExecuteApiEndpoint

Whether clients can invoke the API by using the default `execute-api` endpoint.
By default, clients can invoke the API with the default `{api_id}.execute-api.{region}.amazonaws.com endpoint`.
To require that clients use a custom domain name to invoke the API, disable the default endpoint.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailOnWarnings

Whether warnings should return an error while API Gateway is creating or updating the resource using an OpenAPI specification. Defaults to `false`. Applicable for HTTP APIs.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the API. Must be less than or equal to 128 characters in length.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtocolType

The API protocol. Valid values: `HTTP`, `WEBSOCKET`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteKey

Part of _quick create_. Specifies any [route key](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-routes.html). Applicable for HTTP APIs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteSelectionExpression

The [route selection expression](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-route-selection-expressions) for the API.
Defaults to `$request.method $request.path`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A map of tags to assign to the API. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Target

Part of _quick create_. Quick create produces an API with an integration, a default catch-all route, and a default stage which is configured to automatically deploy changes.
For HTTP integrations, specify a fully qualified URL. For Lambda integrations, specify a function ARN.
The type of the integration will be `HTTP_PROXY` or `AWS_PROXY`, respectively. Applicable for HTTP APIs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

A version identifier for the API. Must be between 1 and 64 characters in length.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CorsConfiguration

_Required_: No

_Type_: List of <a href="corsconfigurationdefinition.md">CorsConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ApiEndpoint

Returns the <code>ApiEndpoint</code> value.

#### Arn

Returns the <code>Arn</code> value.

#### ExecutionArn

Returns the <code>ExecutionArn</code> value.

#### Id

Returns the <code>Id</code> value.

