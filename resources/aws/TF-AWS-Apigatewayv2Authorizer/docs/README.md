# TF::AWS::Apigatewayv2Authorizer

Manages an Amazon API Gateway Version 2 authorizer.
More information can be found in the [Amazon API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::Apigatewayv2Authorizer",
    "Properties" : {
        "<a href="#apiid" title="ApiId">ApiId</a>" : <i>String</i>,
        "<a href="#authorizercredentialsarn" title="AuthorizerCredentialsArn">AuthorizerCredentialsArn</a>" : <i>String</i>,
        "<a href="#authorizerpayloadformatversion" title="AuthorizerPayloadFormatVersion">AuthorizerPayloadFormatVersion</a>" : <i>String</i>,
        "<a href="#authorizerresultttlinseconds" title="AuthorizerResultTtlInSeconds">AuthorizerResultTtlInSeconds</a>" : <i>Double</i>,
        "<a href="#authorizertype" title="AuthorizerType">AuthorizerType</a>" : <i>String</i>,
        "<a href="#authorizeruri" title="AuthorizerUri">AuthorizerUri</a>" : <i>String</i>,
        "<a href="#enablesimpleresponses" title="EnableSimpleResponses">EnableSimpleResponses</a>" : <i>Boolean</i>,
        "<a href="#identitysources" title="IdentitySources">IdentitySources</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#jwtconfiguration" title="JwtConfiguration">JwtConfiguration</a>" : <i>[ <a href="jwtconfigurationdefinition.md">JwtConfigurationDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::Apigatewayv2Authorizer
Properties:
    <a href="#apiid" title="ApiId">ApiId</a>: <i>String</i>
    <a href="#authorizercredentialsarn" title="AuthorizerCredentialsArn">AuthorizerCredentialsArn</a>: <i>String</i>
    <a href="#authorizerpayloadformatversion" title="AuthorizerPayloadFormatVersion">AuthorizerPayloadFormatVersion</a>: <i>String</i>
    <a href="#authorizerresultttlinseconds" title="AuthorizerResultTtlInSeconds">AuthorizerResultTtlInSeconds</a>: <i>Double</i>
    <a href="#authorizertype" title="AuthorizerType">AuthorizerType</a>: <i>String</i>
    <a href="#authorizeruri" title="AuthorizerUri">AuthorizerUri</a>: <i>String</i>
    <a href="#enablesimpleresponses" title="EnableSimpleResponses">EnableSimpleResponses</a>: <i>Boolean</i>
    <a href="#identitysources" title="IdentitySources">IdentitySources</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#jwtconfiguration" title="JwtConfiguration">JwtConfiguration</a>: <i>
      - <a href="jwtconfigurationdefinition.md">JwtConfigurationDefinition</a></i>
</pre>

## Properties

#### ApiId

The API identifier.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthorizerCredentialsArn

The required credentials as an IAM role for API Gateway to invoke the authorizer.
Supported only for `REQUEST` authorizers.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthorizerPayloadFormatVersion

The format of the payload sent to an HTTP API Lambda authorizer. Required for HTTP API Lambda authorizers.
Valid values: `1.0`, `2.0`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthorizerResultTtlInSeconds

The time to live (TTL) for cached authorizer results, in seconds. If it equals 0, authorization caching is disabled.
If it is greater than 0, API Gateway caches authorizer responses. The maximum value is 3600, or 1 hour. Defaults to `300`.
Supported only for HTTP API Lambda authorizers.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthorizerType

The authorizer type. Valid values: `JWT`, `REQUEST`.
Specify `REQUEST` for a Lambda function using incoming request parameters.
For HTTP APIs, specify `JWT` to use JSON Web Tokens.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthorizerUri

The authorizer's Uniform Resource Identifier (URI).
For `REQUEST` authorizers this must be a well-formed Lambda function URI, such as the `invoke_arn` attribute of the [`aws_lambda_function`](/docs/providers/aws/r/lambda_function.html) resource.
Supported only for `REQUEST` authorizers. Must be between 1 and 2048 characters in length.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableSimpleResponses

Whether a Lambda authorizer returns a response in a simple format. If enabled, the Lambda authorizer can return a boolean value instead of an IAM policy.
Supported only for HTTP APIs.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdentitySources

The identity sources for which authorization is requested.
For `REQUEST` authorizers the value is a list of one or more mapping expressions of the specified request parameters.
For `JWT` authorizers the single entry specifies where to extract the JSON Web Token (JWT) from inbound requests.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the authorizer. Must be between 1 and 128 characters in length.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JwtConfiguration

_Required_: No

_Type_: List of <a href="jwtconfigurationdefinition.md">JwtConfigurationDefinition</a>

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

