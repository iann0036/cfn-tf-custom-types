# TF::Okta::SamlApp

CloudFormation equivalent of okta_saml_app

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Okta::SamlApp",
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
Type: TF::Okta::SamlApp
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

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessibilityLoginRedirectUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessibilitySelfService

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AcsEndpoints

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppSettingsJson

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssertionSigned

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Audience

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthnContextClassRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoSubmitToolbar

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultRelayState

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DigestAlgorithm

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Features

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Groups

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HideIos

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HideWeb

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HonorForceAuthn

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdpIssuer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyYearsValid

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreconfiguredApp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Recipient

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestCompressed

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseSigned

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SignatureAlgorithm

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SingleLogoutCertificate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SingleLogoutIssuer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SingleLogoutUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpIssuer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SsoUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubjectNameIdFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubjectNameIdTemplate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserNameTemplate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserNameTemplateSuffix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserNameTemplateType

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

Returns the <code>Name</code> value.

#### SignOnMode

Returns the <code>SignOnMode</code> value.

