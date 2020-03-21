# Terraform::AWS::CognitoIdentityProvider

CloudFormation equivalent of aws_cognito_identity_provider

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::CognitoIdentityProvider",
    "Properties" : {
        "<a href="#attributemapping" title="AttributeMapping">AttributeMapping</a>" : <i>[ <a href="attributemapping.md">AttributeMapping</a>, ... ]</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#idpidentifiers" title="IdpIdentifiers">IdpIdentifiers</a>" : <i>[ String, ... ]</i>,
        "<a href="#providerdetails" title="ProviderDetails">ProviderDetails</a>" : <i>[ <a href="providerdetails.md">ProviderDetails</a>, ... ]</i>,
        "<a href="#providername" title="ProviderName">ProviderName</a>" : <i>String</i>,
        "<a href="#providertype" title="ProviderType">ProviderType</a>" : <i>String</i>,
        "<a href="#userpoolid" title="UserPoolId">UserPoolId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::CognitoIdentityProvider
Properties:
    <a href="#attributemapping" title="AttributeMapping">AttributeMapping</a>: <i>
      - <a href="attributemapping.md">AttributeMapping</a></i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#idpidentifiers" title="IdpIdentifiers">IdpIdentifiers</a>: <i>
      - String</i>
    <a href="#providerdetails" title="ProviderDetails">ProviderDetails</a>: <i>
      - <a href="providerdetails.md">ProviderDetails</a></i>
    <a href="#providername" title="ProviderName">ProviderName</a>: <i>String</i>
    <a href="#providertype" title="ProviderType">ProviderType</a>: <i>String</i>
    <a href="#userpoolid" title="UserPoolId">UserPoolId</a>: <i>String</i>
</pre>

## Properties

#### AttributeMapping

_Required_: No

_Type_: List of <a href="attributemapping.md">AttributeMapping</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdpIdentifiers

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderDetails

_Required_: Yes

_Type_: List of <a href="providerdetails.md">ProviderDetails</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserPoolId

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

