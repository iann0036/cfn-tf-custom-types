# Terraform::AWS::ApiGatewayIntegration

Provides an HTTP Method Integration for an API Gateway Integration.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::ApiGatewayIntegration",
    "Properties" : {
        "<a href="#cachekeyparameters" title="CacheKeyParameters">CacheKeyParameters</a>" : <i>[ String, ... ]</i>,
        "<a href="#cachenamespace" title="CacheNamespace">CacheNamespace</a>" : <i>String</i>,
        "<a href="#connectionid" title="ConnectionId">ConnectionId</a>" : <i>String</i>,
        "<a href="#connectiontype" title="ConnectionType">ConnectionType</a>" : <i>String</i>,
        "<a href="#contenthandling" title="ContentHandling">ContentHandling</a>" : <i>String</i>,
        "<a href="#credentials" title="Credentials">Credentials</a>" : <i>String</i>,
        "<a href="#httpmethod" title="HttpMethod">HttpMethod</a>" : <i>String</i>,
        "<a href="#integrationhttpmethod" title="IntegrationHttpMethod">IntegrationHttpMethod</a>" : <i>String</i>,
        "<a href="#passthroughbehavior" title="PassthroughBehavior">PassthroughBehavior</a>" : <i>String</i>,
        "<a href="#requestparameters" title="RequestParameters">RequestParameters</a>" : <i>[ <a href="requestparameters.md">RequestParameters</a>, ... ]</i>,
        "<a href="#requestparametersinjson" title="RequestParametersInJson">RequestParametersInJson</a>" : <i>String</i>,
        "<a href="#requesttemplates" title="RequestTemplates">RequestTemplates</a>" : <i>[ <a href="requesttemplates.md">RequestTemplates</a>, ... ]</i>,
        "<a href="#resourceid" title="ResourceId">ResourceId</a>" : <i>String</i>,
        "<a href="#restapiid" title="RestApiId">RestApiId</a>" : <i>String</i>,
        "<a href="#timeoutmilliseconds" title="TimeoutMilliseconds">TimeoutMilliseconds</a>" : <i>Double</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#uri" title="Uri">Uri</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::ApiGatewayIntegration
Properties:
    <a href="#cachekeyparameters" title="CacheKeyParameters">CacheKeyParameters</a>: <i>
      - String</i>
    <a href="#cachenamespace" title="CacheNamespace">CacheNamespace</a>: <i>String</i>
    <a href="#connectionid" title="ConnectionId">ConnectionId</a>: <i>String</i>
    <a href="#connectiontype" title="ConnectionType">ConnectionType</a>: <i>String</i>
    <a href="#contenthandling" title="ContentHandling">ContentHandling</a>: <i>String</i>
    <a href="#credentials" title="Credentials">Credentials</a>: <i>String</i>
    <a href="#httpmethod" title="HttpMethod">HttpMethod</a>: <i>String</i>
    <a href="#integrationhttpmethod" title="IntegrationHttpMethod">IntegrationHttpMethod</a>: <i>String</i>
    <a href="#passthroughbehavior" title="PassthroughBehavior">PassthroughBehavior</a>: <i>String</i>
    <a href="#requestparameters" title="RequestParameters">RequestParameters</a>: <i>
      - <a href="requestparameters.md">RequestParameters</a></i>
    <a href="#requestparametersinjson" title="RequestParametersInJson">RequestParametersInJson</a>: <i>String</i>
    <a href="#requesttemplates" title="RequestTemplates">RequestTemplates</a>: <i>
      - <a href="requesttemplates.md">RequestTemplates</a></i>
    <a href="#resourceid" title="ResourceId">ResourceId</a>: <i>String</i>
    <a href="#restapiid" title="RestApiId">RestApiId</a>: <i>String</i>
    <a href="#timeoutmilliseconds" title="TimeoutMilliseconds">TimeoutMilliseconds</a>: <i>Double</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#uri" title="Uri">Uri</a>: <i>String</i>
</pre>

## Properties

#### CacheKeyParameters

A list of cache key parameters for the integration.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheNamespace

The integration's cache namespace.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionId

The id of the VpcLink used for the integration. **Required** if `connection_type` is `VPC_LINK`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionType

The integration input's [connectionType](https://docs.aws.amazon.com/apigateway/api-reference/resource/integration/#connectionType). Valid values are `INTERNET` (default for connections through the public routable internet), and `VPC_LINK` (for private connections between API Gateway and a network load balancer in a VPC).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentHandling

Specifies how to handle request payload content type conversions. Supported values are `CONVERT_TO_BINARY` and `CONVERT_TO_TEXT`. If this property is not defined, the request payload will be passed through from the method request to integration request without modification, provided that the passthroughBehaviors is configured to support payload pass-through.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Credentials

The credentials required for the integration. For `AWS` integrations, 2 options are available. To specify an IAM Role for Amazon API Gateway to assume, use the role's ARN. To require that the caller's identity be passed through from the request, specify the string `arn:aws:iam::\*:user/\*`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpMethod

The HTTP method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTION`, `ANY`)
when calling the associated resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationHttpMethod

The integration HTTP method
(`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONs`, `ANY`, `PATCH`) specifying how API Gateway will interact with the back end.
**Required** if `type` is `AWS`, `AWS_PROXY`, `HTTP` or `HTTP_PROXY`.
Not all methods are compatible with all `AWS` integrations.
e.g. Lambda function [can only be invoked](https://github.com/awslabs/aws-apigateway-importer/issues/9#issuecomment-129651005) via `POST`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PassthroughBehavior

The integration passthrough behavior (`WHEN_NO_MATCH`, `WHEN_NO_TEMPLATES`, `NEVER`).  **Required** if `request_templates` is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestParameters

A map of request query string parameters and headers that should be passed to the backend responder.
For example: `request_parameters = { "integration.request.header.X-Some-Other-Header" = "method.request.header.X-Some-Header" }`.

_Required_: No

_Type_: List of <a href="requestparameters.md">RequestParameters</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestParametersInJson

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestTemplates

A map of the integration's request templates.

_Required_: No

_Type_: List of <a href="requesttemplates.md">RequestTemplates</a>

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

#### TimeoutMilliseconds

Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The integration input's [type](https://docs.aws.amazon.com/apigateway/api-reference/resource/integration/). Valid values are `HTTP` (for HTTP backends), `MOCK` (not calling any real backend), `AWS` (for AWS services), `AWS_PROXY` (for Lambda proxy integration) and `HTTP_PROXY` (for HTTP proxy integration). An `HTTP` or `HTTP_PROXY` integration with a `connection_type` of `VPC_LINK` is referred to as a private integration and uses a VpcLink to connect API Gateway to a network load balancer of a VPC.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uri

The input's URI. **Required** if `type` is `AWS`, `AWS_PROXY`, `HTTP` or `HTTP_PROXY`.
For HTTP integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the RFC-3986 specification . For AWS integrations, the URI should be of the form `arn:aws:apigateway:{region}:{subdomain.service|service}:{path|action}/{service_api}`. `region`, `subdomain` and `service` are used to determine the right endpoint.
e.g. `arn:aws:apigateway:eu-west-1:lambda:path/2015-03-31/functions/arn:aws:lambda:eu-west-1:012345678901:function:my-func/invocations`.

_Required_: No

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

