# TF::Okta::AuthServerClaimDefault

Configures Default Authorization Server Claim.

This resource allows you to configure Default Authorization Server Claims.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Okta::AuthServerClaimDefault",
    "Properties" : {
        "<a href="#authserverid" title="AuthServerId">AuthServerId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#value" title="Value">Value</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Okta::AuthServerClaimDefault
Properties:
    <a href="#authserverid" title="AuthServerId">AuthServerId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#value" title="Value">Value</a>: <i>String</i>
</pre>

## Properties

#### AuthServerId

ID of the authorization server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the claim. Can be set to `"sub"`, `"address"`, `"birthdate"`, `"email"`,
`"email_verified"`, `"family_name"`, `"gender"`, `"given_name"`, `"locale"`, `"middle_name"`, `"name"`, `"nickname"`,
`"phone_number"`, `"picture"`, `"preferred_username"`, `"profile"`, `"updated_at"`, `"website"`, `"zoneinfo"`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

The value of the claim. Only required for `"sub"` claim.

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

#### AlwaysIncludeInToken

Returns the <code>AlwaysIncludeInToken</code> value.

#### ClaimType

Returns the <code>ClaimType</code> value.

#### Id

Returns the <code>Id</code> value.

#### Scopes

Returns the <code>Scopes</code> value.

#### Status

Returns the <code>Status</code> value.

#### ValueType

Returns the <code>ValueType</code> value.

