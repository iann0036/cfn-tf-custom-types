# TF::Okta::IdpSaml

Creates a SAML Identity Provider.

This resource allows you to create and configure a SAML Identity Provider.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Okta::IdpSaml",
    "Properties" : {
        "<a href="#accountlinkaction" title="AccountLinkAction">AccountLinkAction</a>" : <i>String</i>,
        "<a href="#accountlinkgroupinclude" title="AccountLinkGroupInclude">AccountLinkGroupInclude</a>" : <i>[ String, ... ]</i>,
        "<a href="#acsbinding" title="AcsBinding">AcsBinding</a>" : <i>String</i>,
        "<a href="#acstype" title="AcsType">AcsType</a>" : <i>String</i>,
        "<a href="#deprovisionedaction" title="DeprovisionedAction">DeprovisionedAction</a>" : <i>String</i>,
        "<a href="#groupsaction" title="GroupsAction">GroupsAction</a>" : <i>String</i>,
        "<a href="#groupsassignment" title="GroupsAssignment">GroupsAssignment</a>" : <i>[ String, ... ]</i>,
        "<a href="#groupsattribute" title="GroupsAttribute">GroupsAttribute</a>" : <i>String</i>,
        "<a href="#groupsfilter" title="GroupsFilter">GroupsFilter</a>" : <i>[ String, ... ]</i>,
        "<a href="#issuer" title="Issuer">Issuer</a>" : <i>String</i>,
        "<a href="#issuermode" title="IssuerMode">IssuerMode</a>" : <i>String</i>,
        "<a href="#kid" title="Kid">Kid</a>" : <i>String</i>,
        "<a href="#maxclockskew" title="MaxClockSkew">MaxClockSkew</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nameformat" title="NameFormat">NameFormat</a>" : <i>String</i>,
        "<a href="#profilemaster" title="ProfileMaster">ProfileMaster</a>" : <i>Boolean</i>,
        "<a href="#provisioningaction" title="ProvisioningAction">ProvisioningAction</a>" : <i>String</i>,
        "<a href="#requestsignaturealgorithm" title="RequestSignatureAlgorithm">RequestSignatureAlgorithm</a>" : <i>String</i>,
        "<a href="#requestsignaturescope" title="RequestSignatureScope">RequestSignatureScope</a>" : <i>String</i>,
        "<a href="#responsesignaturealgorithm" title="ResponseSignatureAlgorithm">ResponseSignatureAlgorithm</a>" : <i>String</i>,
        "<a href="#responsesignaturescope" title="ResponseSignatureScope">ResponseSignatureScope</a>" : <i>String</i>,
        "<a href="#ssobinding" title="SsoBinding">SsoBinding</a>" : <i>String</i>,
        "<a href="#ssodestination" title="SsoDestination">SsoDestination</a>" : <i>String</i>,
        "<a href="#ssourl" title="SsoUrl">SsoUrl</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#subjectfilter" title="SubjectFilter">SubjectFilter</a>" : <i>String</i>,
        "<a href="#subjectformat" title="SubjectFormat">SubjectFormat</a>" : <i>[ String, ... ]</i>,
        "<a href="#subjectmatchattribute" title="SubjectMatchAttribute">SubjectMatchAttribute</a>" : <i>String</i>,
        "<a href="#subjectmatchtype" title="SubjectMatchType">SubjectMatchType</a>" : <i>String</i>,
        "<a href="#suspendedaction" title="SuspendedAction">SuspendedAction</a>" : <i>String</i>,
        "<a href="#usernametemplate" title="UsernameTemplate">UsernameTemplate</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Okta::IdpSaml
Properties:
    <a href="#accountlinkaction" title="AccountLinkAction">AccountLinkAction</a>: <i>String</i>
    <a href="#accountlinkgroupinclude" title="AccountLinkGroupInclude">AccountLinkGroupInclude</a>: <i>
      - String</i>
    <a href="#acsbinding" title="AcsBinding">AcsBinding</a>: <i>String</i>
    <a href="#acstype" title="AcsType">AcsType</a>: <i>String</i>
    <a href="#deprovisionedaction" title="DeprovisionedAction">DeprovisionedAction</a>: <i>String</i>
    <a href="#groupsaction" title="GroupsAction">GroupsAction</a>: <i>String</i>
    <a href="#groupsassignment" title="GroupsAssignment">GroupsAssignment</a>: <i>
      - String</i>
    <a href="#groupsattribute" title="GroupsAttribute">GroupsAttribute</a>: <i>String</i>
    <a href="#groupsfilter" title="GroupsFilter">GroupsFilter</a>: <i>
      - String</i>
    <a href="#issuer" title="Issuer">Issuer</a>: <i>String</i>
    <a href="#issuermode" title="IssuerMode">IssuerMode</a>: <i>String</i>
    <a href="#kid" title="Kid">Kid</a>: <i>String</i>
    <a href="#maxclockskew" title="MaxClockSkew">MaxClockSkew</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nameformat" title="NameFormat">NameFormat</a>: <i>String</i>
    <a href="#profilemaster" title="ProfileMaster">ProfileMaster</a>: <i>Boolean</i>
    <a href="#provisioningaction" title="ProvisioningAction">ProvisioningAction</a>: <i>String</i>
    <a href="#requestsignaturealgorithm" title="RequestSignatureAlgorithm">RequestSignatureAlgorithm</a>: <i>String</i>
    <a href="#requestsignaturescope" title="RequestSignatureScope">RequestSignatureScope</a>: <i>String</i>
    <a href="#responsesignaturealgorithm" title="ResponseSignatureAlgorithm">ResponseSignatureAlgorithm</a>: <i>String</i>
    <a href="#responsesignaturescope" title="ResponseSignatureScope">ResponseSignatureScope</a>: <i>String</i>
    <a href="#ssobinding" title="SsoBinding">SsoBinding</a>: <i>String</i>
    <a href="#ssodestination" title="SsoDestination">SsoDestination</a>: <i>String</i>
    <a href="#ssourl" title="SsoUrl">SsoUrl</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#subjectfilter" title="SubjectFilter">SubjectFilter</a>: <i>String</i>
    <a href="#subjectformat" title="SubjectFormat">SubjectFormat</a>: <i>
      - String</i>
    <a href="#subjectmatchattribute" title="SubjectMatchAttribute">SubjectMatchAttribute</a>: <i>String</i>
    <a href="#subjectmatchtype" title="SubjectMatchType">SubjectMatchType</a>: <i>String</i>
    <a href="#suspendedaction" title="SuspendedAction">SuspendedAction</a>: <i>String</i>
    <a href="#usernametemplate" title="UsernameTemplate">UsernameTemplate</a>: <i>String</i>
</pre>

## Properties

#### AccountLinkAction

Specifies the account linking action for an IdP user.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountLinkGroupInclude

Group memberships to determine link candidates.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AcsBinding

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AcsType

The type of ACS. It can be `"INSTANCE"` or `"ORG"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeprovisionedAction

Action for a previously deprovisioned IdP user during authentication. Can be `"NONE"` or `"REACTIVATE"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupsAction

Provisioning action for IdP user's group memberships. It can be `"NONE"`, `"SYNC"`, `"APPEND"`, or `"ASSIGN"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupsAssignment

List of Okta Group IDs to add an IdP user as a member with the `"ASSIGN"` `groups_action`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupsAttribute

IdP user profile attribute name (case-insensitive) for an array value that contains group memberships.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupsFilter

Whitelist of Okta Group identifiers that are allowed for the `"APPEND"` or `"SYNC"` `groups_action`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Issuer

URI that identifies the issuer.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IssuerMode

Indicates whether Okta uses the original Okta org domain URL, or a custom domain URL. It can be `"ORG_URL"` or `"CUSTOM_URL"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Kid

The ID of the signing key.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxClockSkew

Maximum allowable clock-skew when processing messages from the IdP.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The Application's display name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameFormat

The name identifier format to use. By default `"urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProfileMaster

Determines if the IdP should act as a source of truth for user profile attributes.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProvisioningAction

Provisioning action for an IdP user during authentication.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestSignatureAlgorithm

The XML digital signature algorithm used when signing an AuthnRequest message.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestSignatureScope

Specifies whether to digitally sign an AuthnRequest messages to the IdP. It can be `"REQUEST"` or `"NONE"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseSignatureAlgorithm

The minimum XML digital signature algorithm allowed when verifying a SAMLResponse message or Assertion element.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseSignatureScope

Specifies whether to verify a SAMLResponse message or Assertion element XML digital signature. It can be `"RESPONSE"`, `"ASSERTION"`, or `"ANY"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SsoBinding

The method of making an SSO request. It can be set to `"HTTP-POST"` or `"HTTP-REDIRECT"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SsoDestination

URI reference indicating the address to which the AuthnRequest message is sent.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SsoUrl

URL of binding-specific endpoint to send an AuthnRequest message to IdP.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Status of the IdP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubjectFilter

Optional regular expression pattern used to filter untrusted IdP usernames.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubjectFormat

The name format. By default `"urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified"`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubjectMatchAttribute

Okta user profile attribute for matching transformed IdP username. Only for matchType `"CUSTOM_ATTRIBUTE"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubjectMatchType

Determines the Okta user profile attribute match conditions for account linking and authentication of the transformed IdP username. By default, it is set to `"USERNAME"`. It can be set to `"USERNAME"`, `"EMAIL"`, `"USERNAME_OR_EMAIL"` or `"CUSTOM_ATTRIBUTE"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SuspendedAction

Action for a previously suspended IdP user during authentication. Can be set to `"NONE"` or `"UNSUSPEND"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsernameTemplate

Okta EL Expression to generate or transform a unique username for the IdP user.

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

#### Audience

Returns the <code>Audience</code> value.

#### Id

Returns the <code>Id</code> value.

#### Type

Returns the <code>Type</code> value.

