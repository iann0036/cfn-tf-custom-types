# Terraform::Vault::JwtAuthBackendRole

Manages an JWT/OIDC auth backend role in a Vault server. See the [Vault
documentation](https://www.vaultproject.io/docs/auth/jwt.html) for more
information.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Vault::JwtAuthBackendRole",
    "Properties" : {
        "<a href="#allowedredirecturis" title="AllowedRedirectUris">AllowedRedirectUris</a>" : <i>[ String, ... ]</i>,
        "<a href="#backend" title="Backend">Backend</a>" : <i>String</i>,
        "<a href="#boundaudiences" title="BoundAudiences">BoundAudiences</a>" : <i>[ String, ... ]</i>,
        "<a href="#boundcidrs" title="BoundCidrs">BoundCidrs</a>" : <i>[ String, ... ]</i>,
        "<a href="#boundclaims" title="BoundClaims">BoundClaims</a>" : <i>[ <a href="boundclaims.md">BoundClaims</a>, ... ]</i>,
        "<a href="#boundsubject" title="BoundSubject">BoundSubject</a>" : <i>String</i>,
        "<a href="#claimmappings" title="ClaimMappings">ClaimMappings</a>" : <i>[ <a href="claimmappings.md">ClaimMappings</a>, ... ]</i>,
        "<a href="#clockskewleeway" title="ClockSkewLeeway">ClockSkewLeeway</a>" : <i>Double</i>,
        "<a href="#expirationleeway" title="ExpirationLeeway">ExpirationLeeway</a>" : <i>Double</i>,
        "<a href="#groupsclaim" title="GroupsClaim">GroupsClaim</a>" : <i>String</i>,
        "<a href="#groupsclaimdelimiterpattern" title="GroupsClaimDelimiterPattern">GroupsClaimDelimiterPattern</a>" : <i>String</i>,
        "<a href="#maxttl" title="MaxTtl">MaxTtl</a>" : <i>Double</i>,
        "<a href="#notbeforeleeway" title="NotBeforeLeeway">NotBeforeLeeway</a>" : <i>Double</i>,
        "<a href="#numuses" title="NumUses">NumUses</a>" : <i>Double</i>,
        "<a href="#oidcscopes" title="OidcScopes">OidcScopes</a>" : <i>[ String, ... ]</i>,
        "<a href="#period" title="Period">Period</a>" : <i>Double</i>,
        "<a href="#policies" title="Policies">Policies</a>" : <i>[ String, ... ]</i>,
        "<a href="#rolename" title="RoleName">RoleName</a>" : <i>String</i>,
        "<a href="#roletype" title="RoleType">RoleType</a>" : <i>String</i>,
        "<a href="#tokenboundcidrs" title="TokenBoundCidrs">TokenBoundCidrs</a>" : <i>[ String, ... ]</i>,
        "<a href="#tokenexplicitmaxttl" title="TokenExplicitMaxTtl">TokenExplicitMaxTtl</a>" : <i>Double</i>,
        "<a href="#tokenmaxttl" title="TokenMaxTtl">TokenMaxTtl</a>" : <i>Double</i>,
        "<a href="#tokennodefaultpolicy" title="TokenNoDefaultPolicy">TokenNoDefaultPolicy</a>" : <i>Boolean</i>,
        "<a href="#tokennumuses" title="TokenNumUses">TokenNumUses</a>" : <i>Double</i>,
        "<a href="#tokenperiod" title="TokenPeriod">TokenPeriod</a>" : <i>Double</i>,
        "<a href="#tokenpolicies" title="TokenPolicies">TokenPolicies</a>" : <i>[ String, ... ]</i>,
        "<a href="#tokenttl" title="TokenTtl">TokenTtl</a>" : <i>Double</i>,
        "<a href="#tokentype" title="TokenType">TokenType</a>" : <i>String</i>,
        "<a href="#ttl" title="Ttl">Ttl</a>" : <i>Double</i>,
        "<a href="#userclaim" title="UserClaim">UserClaim</a>" : <i>String</i>,
        "<a href="#verboseoidclogging" title="VerboseOidcLogging">VerboseOidcLogging</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Vault::JwtAuthBackendRole
Properties:
    <a href="#allowedredirecturis" title="AllowedRedirectUris">AllowedRedirectUris</a>: <i>
      - String</i>
    <a href="#backend" title="Backend">Backend</a>: <i>String</i>
    <a href="#boundaudiences" title="BoundAudiences">BoundAudiences</a>: <i>
      - String</i>
    <a href="#boundcidrs" title="BoundCidrs">BoundCidrs</a>: <i>
      - String</i>
    <a href="#boundclaims" title="BoundClaims">BoundClaims</a>: <i>
      - <a href="boundclaims.md">BoundClaims</a></i>
    <a href="#boundsubject" title="BoundSubject">BoundSubject</a>: <i>String</i>
    <a href="#claimmappings" title="ClaimMappings">ClaimMappings</a>: <i>
      - <a href="claimmappings.md">ClaimMappings</a></i>
    <a href="#clockskewleeway" title="ClockSkewLeeway">ClockSkewLeeway</a>: <i>Double</i>
    <a href="#expirationleeway" title="ExpirationLeeway">ExpirationLeeway</a>: <i>Double</i>
    <a href="#groupsclaim" title="GroupsClaim">GroupsClaim</a>: <i>String</i>
    <a href="#groupsclaimdelimiterpattern" title="GroupsClaimDelimiterPattern">GroupsClaimDelimiterPattern</a>: <i>String</i>
    <a href="#maxttl" title="MaxTtl">MaxTtl</a>: <i>Double</i>
    <a href="#notbeforeleeway" title="NotBeforeLeeway">NotBeforeLeeway</a>: <i>Double</i>
    <a href="#numuses" title="NumUses">NumUses</a>: <i>Double</i>
    <a href="#oidcscopes" title="OidcScopes">OidcScopes</a>: <i>
      - String</i>
    <a href="#period" title="Period">Period</a>: <i>Double</i>
    <a href="#policies" title="Policies">Policies</a>: <i>
      - String</i>
    <a href="#rolename" title="RoleName">RoleName</a>: <i>String</i>
    <a href="#roletype" title="RoleType">RoleType</a>: <i>String</i>
    <a href="#tokenboundcidrs" title="TokenBoundCidrs">TokenBoundCidrs</a>: <i>
      - String</i>
    <a href="#tokenexplicitmaxttl" title="TokenExplicitMaxTtl">TokenExplicitMaxTtl</a>: <i>Double</i>
    <a href="#tokenmaxttl" title="TokenMaxTtl">TokenMaxTtl</a>: <i>Double</i>
    <a href="#tokennodefaultpolicy" title="TokenNoDefaultPolicy">TokenNoDefaultPolicy</a>: <i>Boolean</i>
    <a href="#tokennumuses" title="TokenNumUses">TokenNumUses</a>: <i>Double</i>
    <a href="#tokenperiod" title="TokenPeriod">TokenPeriod</a>: <i>Double</i>
    <a href="#tokenpolicies" title="TokenPolicies">TokenPolicies</a>: <i>
      - String</i>
    <a href="#tokenttl" title="TokenTtl">TokenTtl</a>: <i>Double</i>
    <a href="#tokentype" title="TokenType">TokenType</a>: <i>String</i>
    <a href="#ttl" title="Ttl">Ttl</a>: <i>Double</i>
    <a href="#userclaim" title="UserClaim">UserClaim</a>: <i>String</i>
    <a href="#verboseoidclogging" title="VerboseOidcLogging">VerboseOidcLogging</a>: <i>Boolean</i>
</pre>

## Properties

#### AllowedRedirectUris

The list of allowed values for redirect_uri during OIDC logins.
Required for OIDC roles.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backend

The unique name of the auth backend to configure.
Defaults to `jwt`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundAudiences

List of `aud` claims to match
against. Any match is sufficient.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundCidrs

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundClaims

If set, a map of claims/values to match against.
The expected value may be a single string or a list of strings.

_Required_: No

_Type_: List of <a href="boundclaims.md">BoundClaims</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundSubject

If set, requires that the `sub` claim matches
this value.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClaimMappings

If set, a map of claims (keys) to be copied
to specified metadata fields (values).

_Required_: No

_Type_: List of <a href="claimmappings.md">ClaimMappings</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClockSkewLeeway

The amount of leeway to add to all claims to account for clock skew, in
seconds. Defaults to `60` seconds if set to `0` and can be disabled if set to `-1`.
Only applicable with "jwt" roles.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpirationLeeway

The amount of leeway to add to expiration (`exp`) claims to account for
clock skew, in seconds. Defaults to `60` seconds if set to `0` and can be disabled if set to `-1`.
Only applicable with "jwt" roles.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupsClaim

The claim to use to uniquely identify
the set of groups to which the user belongs; this will be used as the names
for the Identity group aliases created due to a successful login. The claim
value must be a list of strings.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupsClaimDelimiterPattern

.)
A pattern of delimiters
used to allow the groups_claim to live outside of the top-level JWT structure.
For instance, a groups_claim of meta/user.name/groups with this field
set to // will expect nested structures named meta, user.name, and groups.
If this field was set to /./ the groups information would expect to be
via nested structures of meta, user, name, and groups.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotBeforeLeeway

The amount of leeway to add to not before (`nbf`) claims to account for
clock skew, in seconds. Defaults to `60` seconds if set to `0` and can be disabled if set to `-1`.
Only applicable with "jwt" roles.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumUses

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OidcScopes

If set, a list of OIDC scopes to be used with an OIDC role.
The standard scope "openid" is automatically included and need not be specified.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Period

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policies

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleName

The name of the role.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleType

Type of role, either "oidc" (default) or "jwt".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenBoundCidrs

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenExplicitMaxTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenMaxTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenNoDefaultPolicy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenNumUses

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenPeriod

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenPolicies

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserClaim

The claim to use to uniquely identify
the user; this will be used as the name for the Identity entity alias created
due to a successful login.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VerboseOidcLogging

Log received OIDC tokens and claims when debug-level
logging is active. Not recommended in production since sensitive information may be present
in OIDC responses.

_Required_: No

_Type_: Boolean

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

