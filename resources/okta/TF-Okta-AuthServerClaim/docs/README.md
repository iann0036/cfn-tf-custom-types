# TF::Okta::AuthServerClaim

Creates an Authorization Server Claim.

This resource allows you to create and configure an Authorization Server Claim.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Okta::AuthServerClaim",
    "Properties" : {
        "<a href="#alwaysincludeintoken" title="AlwaysIncludeInToken">AlwaysIncludeInToken</a>" : <i>Boolean</i>,
        "<a href="#authserverid" title="AuthServerId">AuthServerId</a>" : <i>String</i>,
        "<a href="#claimtype" title="ClaimType">ClaimType</a>" : <i>String</i>,
        "<a href="#groupfiltertype" title="GroupFilterType">GroupFilterType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#scopes" title="Scopes">Scopes</a>" : <i>[ String, ... ]</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#value" title="Value">Value</a>" : <i>String</i>,
        "<a href="#valuetype" title="ValueType">ValueType</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Okta::AuthServerClaim
Properties:
    <a href="#alwaysincludeintoken" title="AlwaysIncludeInToken">AlwaysIncludeInToken</a>: <i>Boolean</i>
    <a href="#authserverid" title="AuthServerId">AuthServerId</a>: <i>String</i>
    <a href="#claimtype" title="ClaimType">ClaimType</a>: <i>String</i>
    <a href="#groupfiltertype" title="GroupFilterType">GroupFilterType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#scopes" title="Scopes">Scopes</a>: <i>
      - String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#value" title="Value">Value</a>: <i>String</i>
    <a href="#valuetype" title="ValueType">ValueType</a>: <i>String</i>
</pre>

## Properties

#### AlwaysIncludeInToken

Specifies whether to include claims in token, by default it is set to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthServerId

ID of the authorization server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClaimType

Specifies whether the claim is for an access token `"RESOURCE"` or ID token `"IDENTITY"`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupFilterType

Specifies the type of group filter if `value_type` is `"GROUPS"`. Can be set to one of the following `"STARTS_WITH"`, `"EQUALS"`, `"CONTAINS"`, `"REGEX"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the claim.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scopes

The list of scopes the auth server claim is tied to.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

The status of the application. It defaults to `"ACTIVE"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

The value of the claim.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValueType

The type of value of the claim. It can be set to `"EXPRESSION"` or `"GROUPS"`. It defaults to `"EXPRESSION"`.

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

