# Terraform::Vault::OktaAuthBackend

Provides a resource for managing an
[Okta auth backend within Vault](https://www.vaultproject.io/docs/auth/okta.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Vault::OktaAuthBackend",
    "Properties" : {
        "<a href="#baseurl" title="BaseUrl">BaseUrl</a>" : <i>String</i>,
        "<a href="#bypassoktamfa" title="BypassOktaMfa">BypassOktaMfa</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#group" title="Group">Group</a>" : <i>[ <a href="group.md">Group</a>, ... ]</i>,
        "<a href="#maxttl" title="MaxTtl">MaxTtl</a>" : <i>String</i>,
        "<a href="#organization" title="Organization">Organization</a>" : <i>String</i>,
        "<a href="#path" title="Path">Path</a>" : <i>String</i>,
        "<a href="#token" title="Token">Token</a>" : <i>String</i>,
        "<a href="#ttl" title="Ttl">Ttl</a>" : <i>String</i>,
        "<a href="#user" title="User">User</a>" : <i>[ <a href="user.md">User</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Vault::OktaAuthBackend
Properties:
    <a href="#baseurl" title="BaseUrl">BaseUrl</a>: <i>String</i>
    <a href="#bypassoktamfa" title="BypassOktaMfa">BypassOktaMfa</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#group" title="Group">Group</a>: <i>
      - <a href="group.md">Group</a></i>
    <a href="#maxttl" title="MaxTtl">MaxTtl</a>: <i>String</i>
    <a href="#organization" title="Organization">Organization</a>: <i>String</i>
    <a href="#path" title="Path">Path</a>: <i>String</i>
    <a href="#token" title="Token">Token</a>: <i>String</i>
    <a href="#ttl" title="Ttl">Ttl</a>: <i>String</i>
    <a href="#user" title="User">User</a>: <i>
      - <a href="user.md">User</a></i>
</pre>

## Properties

#### BaseUrl

The Okta url. Examples: oktapreview.com, okta.com.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BypassOktaMfa

When true, requests by Okta for a MFA check will be bypassed. This also disallows certain status checks on the account, such as whether the password is expired.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description of the auth backend.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Group

Associate Okta groups with policies within Vault.
[See below for more details](#okta-group).

_Required_: No

_Type_: List of <a href="group.md">Group</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxTtl

Maximum duration after which authentication will be expired
[See the documentation for info on valid duration formats](https://golang.org/pkg/time/#ParseDuration).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Organization

The Okta organization. This will be the first part of the url `https://XXX.okta.com`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

Path to mount the Okta auth backend.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Token

The Okta API token. This is required to query Okta for user group membership.
If this is not supplied only locally configured groups will be enabled.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

Duration after which authentication will be expired.
[See the documentation for info on valid duration formats](https://golang.org/pkg/time/#ParseDuration).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### User

Associate Okta users with groups or policies within Vault.
[See below for more details](#okta-user).

_Required_: No

_Type_: List of <a href="user.md">User</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Accessor

Returns the <code>Accessor</code> value.

