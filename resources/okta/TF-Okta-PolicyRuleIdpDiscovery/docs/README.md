# TF::Okta::PolicyRuleIdpDiscovery

Creates an IdP Discovery Policy Rule.

This resource allows you to create and configure an IdP Discovery Policy Rule.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Okta::PolicyRuleIdpDiscovery",
    "Properties" : {
        "<a href="#idpid" title="IdpId">IdpId</a>" : <i>String</i>,
        "<a href="#idptype" title="IdpType">IdpType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkconnection" title="NetworkConnection">NetworkConnection</a>" : <i>String</i>,
        "<a href="#networkexcludes" title="NetworkExcludes">NetworkExcludes</a>" : <i>[ String, ... ]</i>,
        "<a href="#networkincludes" title="NetworkIncludes">NetworkIncludes</a>" : <i>[ String, ... ]</i>,
        "<a href="#policyid" title="Policyid">Policyid</a>" : <i>String</i>,
        "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#useridentifierattribute" title="UserIdentifierAttribute">UserIdentifierAttribute</a>" : <i>String</i>,
        "<a href="#useridentifiertype" title="UserIdentifierType">UserIdentifierType</a>" : <i>String</i>,
        "<a href="#appexclude" title="AppExclude">AppExclude</a>" : <i>[ <a href="appexcludedefinition.md">AppExcludeDefinition</a>, ... ]</i>,
        "<a href="#appinclude" title="AppInclude">AppInclude</a>" : <i>[ <a href="appincludedefinition.md">AppIncludeDefinition</a>, ... ]</i>,
        "<a href="#platforminclude" title="PlatformInclude">PlatformInclude</a>" : <i>[ <a href="platformincludedefinition.md">PlatformIncludeDefinition</a>, ... ]</i>,
        "<a href="#useridentifierpatterns" title="UserIdentifierPatterns">UserIdentifierPatterns</a>" : <i>[ <a href="useridentifierpatternsdefinition.md">UserIdentifierPatternsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Okta::PolicyRuleIdpDiscovery
Properties:
    <a href="#idpid" title="IdpId">IdpId</a>: <i>String</i>
    <a href="#idptype" title="IdpType">IdpType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkconnection" title="NetworkConnection">NetworkConnection</a>: <i>String</i>
    <a href="#networkexcludes" title="NetworkExcludes">NetworkExcludes</a>: <i>
      - String</i>
    <a href="#networkincludes" title="NetworkIncludes">NetworkIncludes</a>: <i>
      - String</i>
    <a href="#policyid" title="Policyid">Policyid</a>: <i>String</i>
    <a href="#priority" title="Priority">Priority</a>: <i>Double</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#useridentifierattribute" title="UserIdentifierAttribute">UserIdentifierAttribute</a>: <i>String</i>
    <a href="#useridentifiertype" title="UserIdentifierType">UserIdentifierType</a>: <i>String</i>
    <a href="#appexclude" title="AppExclude">AppExclude</a>: <i>
      - <a href="appexcludedefinition.md">AppExcludeDefinition</a></i>
    <a href="#appinclude" title="AppInclude">AppInclude</a>: <i>
      - <a href="appincludedefinition.md">AppIncludeDefinition</a></i>
    <a href="#platforminclude" title="PlatformInclude">PlatformInclude</a>: <i>
      - <a href="platformincludedefinition.md">PlatformIncludeDefinition</a></i>
    <a href="#useridentifierpatterns" title="UserIdentifierPatterns">UserIdentifierPatterns</a>: <i>
      - <a href="useridentifierpatternsdefinition.md">UserIdentifierPatternsDefinition</a></i>
</pre>

## Properties

#### IdpId

The identifier for the Idp the rule should route to if all conditions are met.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdpType

Type of Idp. One of: `"SAML2"`, `"IWA"`, `"AgentlessDSSO"`, `"X509"`, `"FACEBOOK"`, `"GOOGLE"`, `"LINKEDIN"`, `"MICROSOFT"`, `"OIDC"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Use if the `type` is `"APP_TYPE"` to indicate the type of application(s) to include in instances where an entire group (i.e. `yahoo_mail`) of applications should be included.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkConnection

The network selection mode. One of `"ANYWEHRE"` or `"ZONE"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkExcludes

Required if `network_connection` = `"ZONE"`. Indicates the network zones to exclude.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkIncludes

Required if `network_connection` = `"ZONE"`. Indicates the network zones to include.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policyid

Policy ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

Idp rule priority. This attribute can be set to a valid priority. To avoid an endless diff situation an error is thrown if an invalid property is provided. The Okta API defaults to the last (lowest) if not provided.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Idp rule status: `"ACTIVE"` or `"INACTIVE"`. By default, it is `"ACTIVE"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserIdentifierAttribute

Profile attribute matching can only have a single value that describes the type indicated in `user_identifier_type`. This is the attribute or identifier that the `user_identifier_patterns` are checked against.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserIdentifierType

One of: `"IDENTIFIER"`, `"ATTRIBUTE"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppExclude

_Required_: No

_Type_: List of <a href="appexcludedefinition.md">AppExcludeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppInclude

_Required_: No

_Type_: List of <a href="appincludedefinition.md">AppIncludeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlatformInclude

_Required_: No

_Type_: List of <a href="platformincludedefinition.md">PlatformIncludeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserIdentifierPatterns

_Required_: No

_Type_: List of <a href="useridentifierpatternsdefinition.md">UserIdentifierPatternsDefinition</a>

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

Use if `type` is `"APP"` to indicate the application id to include.

