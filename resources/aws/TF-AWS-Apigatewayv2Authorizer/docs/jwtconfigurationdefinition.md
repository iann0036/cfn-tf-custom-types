# TF::AWS::Apigatewayv2Authorizer JwtConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#audience" title="Audience">Audience</a>" : <i>[ String, ... ]</i>,
    "<a href="#issuer" title="Issuer">Issuer</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#audience" title="Audience">Audience</a>: <i>
      - String</i>
<a href="#issuer" title="Issuer">Issuer</a>: <i>String</i>
</pre>

## Properties

#### Audience

A list of the intended recipients of the JWT. A valid JWT must provide an aud that matches at least one entry in this list.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Issuer

The base domain of the identity provider that issues JSON Web Tokens, such as the `endpoint` attribute of the [`aws_cognito_user_pool`](/docs/providers/aws/r/cognito_user_pool.html) resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

