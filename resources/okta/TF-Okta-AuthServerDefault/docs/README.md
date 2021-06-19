# TF::Okta::AuthServerDefault

Configures Default Authorization Server.

This resource allows you to configure Default Authorization Server.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Okta::AuthServerDefault",
    "Properties" : {
        "<a href="#audiences" title="Audiences">Audiences</a>" : <i>[ String, ... ]</i>,
        "<a href="#credentialsrotationmode" title="CredentialsRotationMode">CredentialsRotationMode</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Okta::AuthServerDefault
Properties:
    <a href="#audiences" title="Audiences">Audiences</a>: <i>
      - String</i>
    <a href="#credentialsrotationmode" title="CredentialsRotationMode">CredentialsRotationMode</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
</pre>

## Properties

#### Audiences

The recipients that the tokens are intended for. This becomes the `aud` claim in an access token.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CredentialsRotationMode

The key rotation mode for the authorization server. Can be `"AUTO"` or `"MANUAL"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description of the authorization server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the authorization server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

The status of the auth server.

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

#### CredentialsLastRotated

Returns the <code>CredentialsLastRotated</code> value.

#### CredentialsNextRotation

Returns the <code>CredentialsNextRotation</code> value.

#### Id

Returns the <code>Id</code> value.

#### Issuer

Returns the <code>Issuer</code> value.

#### Kid

Returns the <code>Kid</code> value.

