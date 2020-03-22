# Terraform::Scaleway::Token

**DEPRECATED**: This resource is deprecated and will be removed in `v2.0+`.

Provides Tokens for scaleway API access. For additional details please refer to [API documentation](https://developer.scaleway.com/#tokens-tokens-post).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Scaleway::Token",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#email" title="Email">Email</a>" : <i>String</i>,
        "<a href="#expires" title="Expires">Expires</a>" : <i>Boolean</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Scaleway::Token
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#email" title="Email">Email</a>: <i>String</i>
    <a href="#expires" title="Expires">Expires</a>: <i>Boolean</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
</pre>

## Properties

#### Description

Token description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

Scaleway account email. Defaults to registered account.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expires

Define if the token should automatically expire or not.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Scaleway account password. Required for cross-account token management.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AccessKey

Returns the <code>AccessKey</code> value.

#### CreationIp

Returns the <code>CreationIp</code> value.

#### ExpirationDate

Returns the <code>ExpirationDate</code> value.

#### Id

Returns the <code>Id</code> value.

#### SecretKey

Returns the <code>SecretKey</code> value.

#### UserId

Returns the <code>UserId</code> value.

