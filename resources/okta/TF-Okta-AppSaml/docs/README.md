# TF::Okta::AppSaml

Creates an SAML Application.

This resource allows you to create and configure an SAML Application.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Okta::AppSaml",
    "Properties" : {
        "<a href="#accessibilityerrorredirecturl" title="AccessibilityErrorRedirectUrl">AccessibilityErrorRedirectUrl</a>" : <i>String</i>,
        "<a href="#accessibilityloginredirecturl" title="AccessibilityLoginRedirectUrl">AccessibilityLoginRedirectUrl</a>" : <i>String</i>,
        "<a href="#accessibilityselfservice" title="AccessibilitySelfService">AccessibilitySelfService</a>" : <i>Boolean</i>,
        "<a href="#acsendpoints" title="AcsEndpoints">AcsEndpoints</a>" : <i>[ String, ... ]</i>,
        "<a href="#appsettingsjson" title="AppSettingsJson">AppSettingsJson</a>" : <i>String</i>,
        "<a href="#assertionsigned" title="AssertionSigned">AssertionSigned</a>" : <i>Boolean</i>,
        "<a href="#audience" title="Audience">Audience</a>" : <i>String</i>,
        "<a href="#authncontextclassref" title="AuthnContextClassRef">AuthnContextClassRef</a>" : <i>String</i>,
        "<a href="#autosubmittoolbar" title="AutoSubmitToolbar">AutoSubmitToolbar</a>" : <i>Boolean</i>,
        "<a href="#defaultrelaystate" title="DefaultRelayState">DefaultRelayState</a>" : <i>String</i>,
        "<a href="#destination" title="Destination">Destination</a>" : <i>String</i>,
        "<a href="#digestalgorithm" title="DigestAlgorithm">DigestAlgorithm</a>" : <i>String</i>,
        "<a href="#features" title="Features">Features</a>" : <i>[ String, ... ]</i>,
        "<a href="#groups" title="Groups">Groups</a>" : <i>[ String, ... ]</i>,
        "<a href="#hideios" title="HideIos">HideIos</a>" : <i>Boolean</i>,
        "<a href="#hideweb" title="HideWeb">HideWeb</a>" : <i>Boolean</i>,
        "<a href="#honorforceauthn" title="HonorForceAuthn">HonorForceAuthn</a>" : <i>Boolean</i>,
        "<a href="#idpissuer" title="IdpIssuer">IdpIssuer</a>" : <i>String</i>,
        "<a href="#keyname" title="KeyName">KeyName</a>" : <i>String</i>,
        "<a href="#keyyearsvalid" title="KeyYearsValid">KeyYearsValid</a>" : <i>Double</i>,
        "<a href="#label" title="Label">Label</a>" : <i>String</i>,
        "<a href="#preconfiguredapp" title="PreconfiguredApp">PreconfiguredApp</a>" : <i>String</i>,
        "<a href="#recipient" title="Recipient">Recipient</a>" : <i>String</i>,
        "<a href="#requestcompressed" title="RequestCompressed">RequestCompressed</a>" : <i>Boolean</i>,
        "<a href="#responsesigned" title="ResponseSigned">ResponseSigned</a>" : <i>Boolean</i>,
        "<a href="#signaturealgorithm" title="SignatureAlgorithm">SignatureAlgorithm</a>" : <i>String</i>,
        "<a href="#singlelogoutcertificate" title="SingleLogoutCertificate">SingleLogoutCertificate</a>" : <i>String</i>,
        "<a href="#singlelogoutissuer" title="SingleLogoutIssuer">SingleLogoutIssuer</a>" : <i>String</i>,
        "<a href="#singlelogouturl" title="SingleLogoutUrl">SingleLogoutUrl</a>" : <i>String</i>,
        "<a href="#spissuer" title="SpIssuer">SpIssuer</a>" : <i>String</i>,
        "<a href="#ssourl" title="SsoUrl">SsoUrl</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#subjectnameidformat" title="SubjectNameIdFormat">SubjectNameIdFormat</a>" : <i>String</i>,
        "<a href="#subjectnameidtemplate" title="SubjectNameIdTemplate">SubjectNameIdTemplate</a>" : <i>String</i>,
        "<a href="#usernametemplate" title="UserNameTemplate">UserNameTemplate</a>" : <i>String</i>,
        "<a href="#usernametemplatesuffix" title="UserNameTemplateSuffix">UserNameTemplateSuffix</a>" : <i>String</i>,
        "<a href="#usernametemplatetype" title="UserNameTemplateType">UserNameTemplateType</a>" : <i>String</i>,
        "<a href="#attributestatements" title="AttributeStatements">AttributeStatements</a>" : <i>[ <a href="attributestatementsdefinition.md">AttributeStatementsDefinition</a>, ... ]</i>,
        "<a href="#users" title="Users">Users</a>" : <i>[ <a href="usersdefinition.md">UsersDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Okta::AppSaml
Properties:
    <a href="#accessibilityerrorredirecturl" title="AccessibilityErrorRedirectUrl">AccessibilityErrorRedirectUrl</a>: <i>String</i>
    <a href="#accessibilityloginredirecturl" title="AccessibilityLoginRedirectUrl">AccessibilityLoginRedirectUrl</a>: <i>String</i>
    <a href="#accessibilityselfservice" title="AccessibilitySelfService">AccessibilitySelfService</a>: <i>Boolean</i>
    <a href="#acsendpoints" title="AcsEndpoints">AcsEndpoints</a>: <i>
      - String</i>
    <a href="#appsettingsjson" title="AppSettingsJson">AppSettingsJson</a>: <i>String</i>
    <a href="#assertionsigned" title="AssertionSigned">AssertionSigned</a>: <i>Boolean</i>
    <a href="#audience" title="Audience">Audience</a>: <i>String</i>
    <a href="#authncontextclassref" title="AuthnContextClassRef">AuthnContextClassRef</a>: <i>String</i>
    <a href="#autosubmittoolbar" title="AutoSubmitToolbar">AutoSubmitToolbar</a>: <i>Boolean</i>
    <a href="#defaultrelaystate" title="DefaultRelayState">DefaultRelayState</a>: <i>String</i>
    <a href="#destination" title="Destination">Destination</a>: <i>String</i>
    <a href="#digestalgorithm" title="DigestAlgorithm">DigestAlgorithm</a>: <i>String</i>
    <a href="#features" title="Features">Features</a>: <i>
      - String</i>
    <a href="#groups" title="Groups">Groups</a>: <i>
      - String</i>
    <a href="#hideios" title="HideIos">HideIos</a>: <i>Boolean</i>
    <a href="#hideweb" title="HideWeb">HideWeb</a>: <i>Boolean</i>
    <a href="#honorforceauthn" title="HonorForceAuthn">HonorForceAuthn</a>: <i>Boolean</i>
    <a href="#idpissuer" title="IdpIssuer">IdpIssuer</a>: <i>String</i>
    <a href="#keyname" title="KeyName">KeyName</a>: <i>String</i>
    <a href="#keyyearsvalid" title="KeyYearsValid">KeyYearsValid</a>: <i>Double</i>
    <a href="#label" title="Label">Label</a>: <i>String</i>
    <a href="#preconfiguredapp" title="PreconfiguredApp">PreconfiguredApp</a>: <i>String</i>
    <a href="#recipient" title="Recipient">Recipient</a>: <i>String</i>
    <a href="#requestcompressed" title="RequestCompressed">RequestCompressed</a>: <i>Boolean</i>
    <a href="#responsesigned" title="ResponseSigned">ResponseSigned</a>: <i>Boolean</i>
    <a href="#signaturealgorithm" title="SignatureAlgorithm">SignatureAlgorithm</a>: <i>String</i>
    <a href="#singlelogoutcertificate" title="SingleLogoutCertificate">SingleLogoutCertificate</a>: <i>String</i>
    <a href="#singlelogoutissuer" title="SingleLogoutIssuer">SingleLogoutIssuer</a>: <i>String</i>
    <a href="#singlelogouturl" title="SingleLogoutUrl">SingleLogoutUrl</a>: <i>String</i>
    <a href="#spissuer" title="SpIssuer">SpIssuer</a>: <i>String</i>
    <a href="#ssourl" title="SsoUrl">SsoUrl</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#subjectnameidformat" title="SubjectNameIdFormat">SubjectNameIdFormat</a>: <i>String</i>
    <a href="#subjectnameidtemplate" title="SubjectNameIdTemplate">SubjectNameIdTemplate</a>: <i>String</i>
    <a href="#usernametemplate" title="UserNameTemplate">UserNameTemplate</a>: <i>String</i>
    <a href="#usernametemplatesuffix" title="UserNameTemplateSuffix">UserNameTemplateSuffix</a>: <i>String</i>
    <a href="#usernametemplatetype" title="UserNameTemplateType">UserNameTemplateType</a>: <i>String</i>
    <a href="#attributestatements" title="AttributeStatements">AttributeStatements</a>: <i>
      - <a href="attributestatementsdefinition.md">AttributeStatementsDefinition</a></i>
    <a href="#users" title="Users">Users</a>: <i>
      - <a href="usersdefinition.md">UsersDefinition</a></i>
</pre>

## Properties

#### AccessibilityErrorRedirectUrl

Custom error page URL.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessibilityLoginRedirectUrl

Custom login page URL.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessibilitySelfService

Enable self-service.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AcsEndpoints

An array of ACS endpoints. You can configure a maximum of 100 endpoints.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppSettingsJson

Application settings in JSON format.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssertionSigned

Determines whether the SAML assertion is digitally signed.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Audience

Audience restriction.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthnContextClassRef

Identifies the SAML authentication context class for the assertion’s authentication statement.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoSubmitToolbar

Display auto submit toolbar.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultRelayState

Identifies a specific application resource in an IDP initiated SSO scenario.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

Identifies the location where the SAML response is intended to be sent inside the SAML assertion.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DigestAlgorithm

Determines the digest algorithm used to digitally sign the SAML assertion and response.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Features

features enabled. Notice: you can't currently configure provisioning features via the API.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Groups

Groups associated with the application.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HideIos

Do not display application icon on mobile app.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HideWeb

Do not display application icon to users.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HonorForceAuthn

Prompt user to re-authenticate if SP asks for it.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdpIssuer

SAML issuer ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyName

Certificate name. This modulates the rotation of keys. New name == new key. Required to be set with `key_years_valid`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyYearsValid

Number of years the certificate is valid (2 - 10 years).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

label of application.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreconfiguredApp

name of application from the Okta Integration Network, if not included a custom app will be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Recipient

The location where the app may present the SAML assertion.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestCompressed

Denotes whether the request is compressed or not.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseSigned

Determines whether the SAML auth response message is digitally signed.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SignatureAlgorithm

Signature algorithm used ot digitally sign the assertion and response.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SingleLogoutCertificate

x509 encoded certificate that the Service Provider uses to sign Single Logout requests.
Note: should be provided without `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----`, see [official documentation](https://developer.okta.com/docs/reference/api/apps/#service-provider-certificate).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SingleLogoutIssuer

The issuer of the Service Provider that generates the Single Logout request.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SingleLogoutUrl

The location where the logout response is sent.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpIssuer

SAML service provider issuer.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SsoUrl

Single Sign-on Url.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

status of application.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubjectNameIdFormat

Identifies the SAML processing rules.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubjectNameIdTemplate

Template for app user's username when a user is assigned to the app.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserNameTemplate

Username template.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserNameTemplateSuffix

Username template suffix.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserNameTemplateType

Username template type.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AttributeStatements

_Required_: No

_Type_: List of <a href="attributestatementsdefinition.md">AttributeStatementsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Users

_Required_: No

_Type_: List of <a href="usersdefinition.md">UsersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Certificate

Returns the <code>Certificate</code> value.

#### EntityKey

Returns the <code>EntityKey</code> value.

#### EntityUrl

Returns the <code>EntityUrl</code> value.

#### HttpPostBinding

Returns the <code>HttpPostBinding</code> value.

#### HttpRedirectBinding

Returns the <code>HttpRedirectBinding</code> value.

#### Id

Returns the <code>Id</code> value.

#### KeyId

Returns the <code>KeyId</code> value.

#### Metadata

Returns the <code>Metadata</code> value.

#### MetadataUrl

Returns the <code>MetadataUrl</code> value.

#### Name

The name of the attribute statement.
- `filter_type` - (Optional) Type of group attribute filter. Valid values are: `"STARTS_WITH"`, `"EQUALS"`, `"CONTAINS"`, or `"REGEX"`
- `filter_value` - (Optional) Filter value to use.
- `namespace` - (Optional) The attribute namespace. It can be set to `"urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified"`, `"urn:oasis:names:tc:SAML:2.0:attrname-format:uri"`, or `"urn:oasis:names:tc:SAML:2.0:attrname-format:basic"`.
- `type` - (Optional) The type of attribute statement value. Valid values are: `"EXPRESSION"` or `"GROUP"`. Default is `"EXPRESSION"`.
- `values` - (Optional) Array of values to use.

#### SignOnMode

Returns the <code>SignOnMode</code> value.

