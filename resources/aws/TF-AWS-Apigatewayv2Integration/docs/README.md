# TF::AWS::Apigatewayv2Integration

Manages an Amazon API Gateway Version 2 integration.
More information can be found in the [Amazon API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::Apigatewayv2Integration",
    "Properties" : {
        "<a href="#apiid" title="ApiId">ApiId</a>" : <i>String</i>,
        "<a href="#connectionid" title="ConnectionId">ConnectionId</a>" : <i>String</i>,
        "<a href="#connectiontype" title="ConnectionType">ConnectionType</a>" : <i>String</i>,
        "<a href="#contenthandlingstrategy" title="ContentHandlingStrategy">ContentHandlingStrategy</a>" : <i>String</i>,
        "<a href="#credentialsarn" title="CredentialsArn">CredentialsArn</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#integrationmethod" title="IntegrationMethod">IntegrationMethod</a>" : <i>String</i>,
        "<a href="#integrationsubtype" title="IntegrationSubtype">IntegrationSubtype</a>" : <i>String</i>,
        "<a href="#integrationtype" title="IntegrationType">IntegrationType</a>" : <i>String</i>,
        "<a href="#integrationuri" title="IntegrationUri">IntegrationUri</a>" : <i>String</i>,
        "<a href="#passthroughbehavior" title="PassthroughBehavior">PassthroughBehavior</a>" : <i>String</i>,
        "<a href="#payloadformatversion" title="PayloadFormatVersion">PayloadFormatVersion</a>" : <i>String</i>,
        "<a href="#requestparameters" title="RequestParameters">RequestParameters</a>" : <i>[ <a href="requestparametersdefinition.md">RequestParametersDefinition</a>, ... ]</i>,
        "<a href="#requesttemplates" title="RequestTemplates">RequestTemplates</a>" : <i>[ <a href="requesttemplatesdefinition.md">RequestTemplatesDefinition</a>, ... ]</i>,
        "<a href="#templateselectionexpression" title="TemplateSelectionExpression">TemplateSelectionExpression</a>" : <i>String</i>,
        "<a href="#timeoutmilliseconds" title="TimeoutMilliseconds">TimeoutMilliseconds</a>" : <i>Double</i>,
        "<a href="#responseparameters" title="ResponseParameters">ResponseParameters</a>" : <i>[ <a href="responseparametersdefinition.md">ResponseParametersDefinition</a>, ... ]</i>,
        "<a href="#tlsconfig" title="TlsConfig">TlsConfig</a>" : <i>[ <a href="tlsconfigdefinition.md">TlsConfigDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::Apigatewayv2Integration
Properties:
    <a href="#apiid" title="ApiId">ApiId</a>: <i>String</i>
    <a href="#connectionid" title="ConnectionId">ConnectionId</a>: <i>String</i>
    <a href="#connectiontype" title="ConnectionType">ConnectionType</a>: <i>String</i>
    <a href="#contenthandlingstrategy" title="ContentHandlingStrategy">ContentHandlingStrategy</a>: <i>String</i>
    <a href="#credentialsarn" title="CredentialsArn">CredentialsArn</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#integrationmethod" title="IntegrationMethod">IntegrationMethod</a>: <i>String</i>
    <a href="#integrationsubtype" title="IntegrationSubtype">IntegrationSubtype</a>: <i>String</i>
    <a href="#integrationtype" title="IntegrationType">IntegrationType</a>: <i>String</i>
    <a href="#integrationuri" title="IntegrationUri">IntegrationUri</a>: <i>String</i>
    <a href="#passthroughbehavior" title="PassthroughBehavior">PassthroughBehavior</a>: <i>String</i>
    <a href="#payloadformatversion" title="PayloadFormatVersion">PayloadFormatVersion</a>: <i>String</i>
    <a href="#requestparameters" title="RequestParameters">RequestParameters</a>: <i>
      - <a href="requestparametersdefinition.md">RequestParametersDefinition</a></i>
    <a href="#requesttemplates" title="RequestTemplates">RequestTemplates</a>: <i>
      - <a href="requesttemplatesdefinition.md">RequestTemplatesDefinition</a></i>
    <a href="#templateselectionexpression" title="TemplateSelectionExpression">TemplateSelectionExpression</a>: <i>String</i>
    <a href="#timeoutmilliseconds" title="TimeoutMilliseconds">TimeoutMilliseconds</a>: <i>Double</i>
    <a href="#responseparameters" title="ResponseParameters">ResponseParameters</a>: <i>
      - <a href="responseparametersdefinition.md">ResponseParametersDefinition</a></i>
    <a href="#tlsconfig" title="TlsConfig">TlsConfig</a>: <i>
      - <a href="tlsconfigdefinition.md">TlsConfigDefinition</a></i>
</pre>

## Properties

#### ApiId

The API identifier.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionId

The ID of the [VPC link](apigatewayv2_vpc_link.html) for a private integration. Supported only for HTTP APIs. Must be between 1 and 1024 characters in length.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionType

The type of the network connection to the integration endpoint. Valid values: `INTERNET`, `VPC_LINK`. Default is `INTERNET`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentHandlingStrategy

How to handle response payload content type conversions. Valid values: `CONVERT_TO_BINARY`, `CONVERT_TO_TEXT`. Supported only for WebSocket APIs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CredentialsArn

The credentials required for the integration, if any.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description of the integration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationMethod

The integration's HTTP method. Must be specified if `integration_type` is not `MOCK`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationSubtype

Specifies the AWS service action to invoke. Supported only for HTTP APIs when `integration_type` is `AWS_PROXY`. See the [AWS service integration reference](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-aws-services-reference.html) documentation for supported values. Must be between 1 and 128 characters in length.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationType

The integration type of an integration.
Valid values: `AWS` (supported only for WebSocket APIs), `AWS_PROXY`, `HTTP` (supported only for WebSocket APIs), `HTTP_PROXY`, `MOCK` (supported only for WebSocket APIs). For an HTTP API private integration, use `HTTP_PROXY`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationUri

The URI of the Lambda function for a Lambda proxy integration, when `integration_type` is `AWS_PROXY`.
For an `HTTP` integration, specify a fully-qualified URL. For an HTTP API private integration, specify the ARN of an Application Load Balancer listener, Network Load Balancer listener, or AWS Cloud Map service.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PassthroughBehavior

The pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the `request_templates` attribute.
Valid values: `WHEN_NO_MATCH`, `WHEN_NO_TEMPLATES`, `NEVER`. Default is `WHEN_NO_MATCH`. Supported only for WebSocket APIs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PayloadFormatVersion

The [format of the payload](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html#http-api-develop-integrations-lambda.proxy-format) sent to an integration. Valid values: `1.0`, `2.0`. Default is `1.0`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestParameters

For WebSocket APIs, a key-value map specifying request parameters that are passed from the method request to the backend.
For HTTP APIs with a specified `integration_subtype`, a key-value map specifying parameters that are passed to `AWS_PROXY` integrations.
For HTTP APIs without a specified `integration_subtype`, a key-value map specifying how to transform HTTP requests before sending them to the backend.
See the [Amazon API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html) for details.

_Required_: No

_Type_: List of <a href="requestparametersdefinition.md">RequestParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestTemplates

A map of [Velocity](https://velocity.apache.org/) templates that are applied on the request payload based on the value of the Content-Type header sent by the client. Supported only for WebSocket APIs.

_Required_: No

_Type_: List of <a href="requesttemplatesdefinition.md">RequestTemplatesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateSelectionExpression

The [template selection expression](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-template-selection-expressions) for the integration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutMilliseconds

Custom timeout between 50 and 29,000 milliseconds for WebSocket APIs and between 50 and 30,000 milliseconds for HTTP APIs.
The default timeout is 29 seconds for WebSocket APIs and 30 seconds for HTTP APIs.
Terraform will only perform drift detection of its value when present in a configuration.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseParameters

_Required_: No

_Type_: List of <a href="responseparametersdefinition.md">ResponseParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsConfig

_Required_: No

_Type_: List of <a href="tlsconfigdefinition.md">TlsConfigDefinition</a>

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

#### IntegrationResponseSelectionExpression

Returns the <code>IntegrationResponseSelectionExpression</code> value.

