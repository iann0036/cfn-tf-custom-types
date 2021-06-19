# TF::Okta::AuthServerPolicyRule

Creates an Authorization Server Policy Rule.

This resource allows you to create and configure an Authorization Server Policy Rule.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Okta::AuthServerPolicyRule",
    "Properties" : {
        "<a href="#accesstokenlifetimeminutes" title="AccessTokenLifetimeMinutes">AccessTokenLifetimeMinutes</a>" : <i>Double</i>,
        "<a href="#authserverid" title="AuthServerId">AuthServerId</a>" : <i>String</i>,
        "<a href="#granttypewhitelist" title="GrantTypeWhitelist">GrantTypeWhitelist</a>" : <i>[ String, ... ]</i>,
        "<a href="#groupblacklist" title="GroupBlacklist">GroupBlacklist</a>" : <i>[ String, ... ]</i>,
        "<a href="#groupwhitelist" title="GroupWhitelist">GroupWhitelist</a>" : <i>[ String, ... ]</i>,
        "<a href="#inlinehookid" title="InlineHookId">InlineHookId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#policyid" title="PolicyId">PolicyId</a>" : <i>String</i>,
        "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
        "<a href="#refreshtokenlifetimeminutes" title="RefreshTokenLifetimeMinutes">RefreshTokenLifetimeMinutes</a>" : <i>Double</i>,
        "<a href="#refreshtokenwindowminutes" title="RefreshTokenWindowMinutes">RefreshTokenWindowMinutes</a>" : <i>Double</i>,
        "<a href="#scopewhitelist" title="ScopeWhitelist">ScopeWhitelist</a>" : <i>[ String, ... ]</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#userblacklist" title="UserBlacklist">UserBlacklist</a>" : <i>[ String, ... ]</i>,
        "<a href="#userwhitelist" title="UserWhitelist">UserWhitelist</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Okta::AuthServerPolicyRule
Properties:
    <a href="#accesstokenlifetimeminutes" title="AccessTokenLifetimeMinutes">AccessTokenLifetimeMinutes</a>: <i>Double</i>
    <a href="#authserverid" title="AuthServerId">AuthServerId</a>: <i>String</i>
    <a href="#granttypewhitelist" title="GrantTypeWhitelist">GrantTypeWhitelist</a>: <i>
      - String</i>
    <a href="#groupblacklist" title="GroupBlacklist">GroupBlacklist</a>: <i>
      - String</i>
    <a href="#groupwhitelist" title="GroupWhitelist">GroupWhitelist</a>: <i>
      - String</i>
    <a href="#inlinehookid" title="InlineHookId">InlineHookId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#policyid" title="PolicyId">PolicyId</a>: <i>String</i>
    <a href="#priority" title="Priority">Priority</a>: <i>Double</i>
    <a href="#refreshtokenlifetimeminutes" title="RefreshTokenLifetimeMinutes">RefreshTokenLifetimeMinutes</a>: <i>Double</i>
    <a href="#refreshtokenwindowminutes" title="RefreshTokenWindowMinutes">RefreshTokenWindowMinutes</a>: <i>Double</i>
    <a href="#scopewhitelist" title="ScopeWhitelist">ScopeWhitelist</a>: <i>
      - String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#userblacklist" title="UserBlacklist">UserBlacklist</a>: <i>
      - String</i>
    <a href="#userwhitelist" title="UserWhitelist">UserWhitelist</a>: <i>
      - String</i>
</pre>

## Properties

#### AccessTokenLifetimeMinutes

Lifetime of access token. Can be set to a value between 5 and 1440 minutes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthServerId

Auth Server ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GrantTypeWhitelist

Accepted grant type values, `"authorization_code"`, `"implicit"`, `"password"` or `"client_credentials"`. For `"implicit"` value either `user_whitelist` or `group_whitelist` should be set.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupBlacklist

Specifies a set of Groups whose Users are to be excluded.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupWhitelist

Specifies a set of Groups whose Users are to be included. Can be set to Group ID or to the following: "EVERYONE".

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InlineHookId

The ID of the inline token to trigger.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Auth Server Policy Rule name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyId

Auth Server Policy ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

Priority of the auth server policy rule.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RefreshTokenLifetimeMinutes

Lifetime of refresh token.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RefreshTokenWindowMinutes

Window in which a refresh token can be used. It can be a value between 5 and 2628000 (5 years) minutes.
`"refresh_token_window_minutes"` must be between `"access_token_lifetime_minutes"` and `"refresh_token_lifetime_minutes"`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScopeWhitelist

Scopes allowed for this policy rule. They can be whitelisted by name or all can be whitelisted with `"*"`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

The status of the Auth Server Policy Rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserBlacklist

Specifies a set of Users to be excluded.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserWhitelist

Specifies a set of Users to be included.

_Required_: No

_Type_: List of String

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

