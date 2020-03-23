# Terraform::AWS::ApiGatewayAuthorizer

Provides an API Gateway Authorizer.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::ApiGatewayAuthorizer",
    "Properties" : {
        "<a href="#authorizercredentials" title="AuthorizerCredentials">AuthorizerCredentials</a>" : <i>String</i>,
        "<a href="#authorizerresultttlinseconds" title="AuthorizerResultTtlInSeconds">AuthorizerResultTtlInSeconds</a>" : <i>Double</i>,
        "<a href="#authorizeruri" title="AuthorizerUri">AuthorizerUri</a>" : <i>String</i>,
        "<a href="#identitysource" title="IdentitySource">IdentitySource</a>" : <i>String</i>,
        "<a href="#identityvalidationexpression" title="IdentityValidationExpression">IdentityValidationExpression</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#providerarns" title="ProviderArns">ProviderArns</a>" : <i>[ String, ... ]</i>,
        "<a href="#restapiid" title="RestApiId">RestApiId</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::ApiGatewayAuthorizer
Properties:
    <a href="#authorizercredentials" title="AuthorizerCredentials">AuthorizerCredentials</a>: <i>String</i>
    <a href="#authorizerresultttlinseconds" title="AuthorizerResultTtlInSeconds">AuthorizerResultTtlInSeconds</a>: <i>Double</i>
    <a href="#authorizeruri" title="AuthorizerUri">AuthorizerUri</a>: <i>String</i>
    <a href="#identitysource" title="IdentitySource">IdentitySource</a>: <i>String</i>
    <a href="#identityvalidationexpression" title="IdentityValidationExpression">IdentityValidationExpression</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#providerarns" title="ProviderArns">ProviderArns</a>: <i>
      - String</i>
    <a href="#restapiid" title="RestApiId">RestApiId</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### AuthorizerCredentials

The credentials required for the authorizer.
To specify an IAM Role for API Gateway to assume, use the IAM Role ARN.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthorizerResultTtlInSeconds

The TTL of cached authorizer results in seconds.
Defaults to `300`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthorizerUri

The authorizer's Uniform Resource Identifier (URI).
This must be a well-formed Lambda function URI in the form of `arn:aws:apigateway:{region}:lambda:path/{service_api}`,
e.g. `arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:012345678912:function:my-function/invocations`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdentitySource

The source of the identity in an incoming request.
Defaults to `method.request.header.Authorization`. For `REQUEST` type, this may be a comma-separated list of values, including headers, query string parameters and stage variables - e.g. `"method.request.header.SomeHeaderName,method.request.querystring.SomeQueryStringName,stageVariables.SomeStageVariableName"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdentityValidationExpression

A validation expression for the incoming identity.
For `TOKEN` type, this value should be a regular expression. The incoming token from the client is matched
against this expression, and will proceed if the token matches. If the token doesn't match,
the client receives a 401 Unauthorized response.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the authorizer.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderArns

A list of the Amazon Cognito user pool ARNs.
Each element is of this format: `arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestApiId

The ID of the associated REST API.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of the authorizer. Possible values are `TOKEN` for a Lambda function using a single authorization token submitted in a custom header, `REQUEST` for a Lambda function using incoming request parameters, or `COGNITO_USER_POOLS` for using an Amazon Cognito user pool.
Defaults to `TOKEN`.

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

