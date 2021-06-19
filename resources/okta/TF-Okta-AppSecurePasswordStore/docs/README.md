# TF::Okta::AppSecurePasswordStore

Creates a Secure Password Store Application.

This resource allows you to create and configure a Secure Password Store Application.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Okta::AppSecurePasswordStore",
    "Properties" : {
        "<a href="#accessibilityerrorredirecturl" title="AccessibilityErrorRedirectUrl">AccessibilityErrorRedirectUrl</a>" : <i>String</i>,
        "<a href="#accessibilityselfservice" title="AccessibilitySelfService">AccessibilitySelfService</a>" : <i>Boolean</i>,
        "<a href="#autosubmittoolbar" title="AutoSubmitToolbar">AutoSubmitToolbar</a>" : <i>Boolean</i>,
        "<a href="#credentialsscheme" title="CredentialsScheme">CredentialsScheme</a>" : <i>String</i>,
        "<a href="#groups" title="Groups">Groups</a>" : <i>[ String, ... ]</i>,
        "<a href="#hideios" title="HideIos">HideIos</a>" : <i>Boolean</i>,
        "<a href="#hideweb" title="HideWeb">HideWeb</a>" : <i>Boolean</i>,
        "<a href="#label" title="Label">Label</a>" : <i>String</i>,
        "<a href="#optionalfield1" title="OptionalField1">OptionalField1</a>" : <i>String</i>,
        "<a href="#optionalfield1value" title="OptionalField1Value">OptionalField1Value</a>" : <i>String</i>,
        "<a href="#optionalfield2" title="OptionalField2">OptionalField2</a>" : <i>String</i>,
        "<a href="#optionalfield2value" title="OptionalField2Value">OptionalField2Value</a>" : <i>String</i>,
        "<a href="#optionalfield3" title="OptionalField3">OptionalField3</a>" : <i>String</i>,
        "<a href="#optionalfield3value" title="OptionalField3Value">OptionalField3Value</a>" : <i>String</i>,
        "<a href="#passwordfield" title="PasswordField">PasswordField</a>" : <i>String</i>,
        "<a href="#revealpassword" title="RevealPassword">RevealPassword</a>" : <i>Boolean</i>,
        "<a href="#sharedpassword" title="SharedPassword">SharedPassword</a>" : <i>String</i>,
        "<a href="#sharedusername" title="SharedUsername">SharedUsername</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#url" title="Url">Url</a>" : <i>String</i>,
        "<a href="#usernametemplate" title="UserNameTemplate">UserNameTemplate</a>" : <i>String</i>,
        "<a href="#usernametemplatesuffix" title="UserNameTemplateSuffix">UserNameTemplateSuffix</a>" : <i>String</i>,
        "<a href="#usernametemplatetype" title="UserNameTemplateType">UserNameTemplateType</a>" : <i>String</i>,
        "<a href="#usernamefield" title="UsernameField">UsernameField</a>" : <i>String</i>,
        "<a href="#users" title="Users">Users</a>" : <i>[ <a href="usersdefinition.md">UsersDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Okta::AppSecurePasswordStore
Properties:
    <a href="#accessibilityerrorredirecturl" title="AccessibilityErrorRedirectUrl">AccessibilityErrorRedirectUrl</a>: <i>String</i>
    <a href="#accessibilityselfservice" title="AccessibilitySelfService">AccessibilitySelfService</a>: <i>Boolean</i>
    <a href="#autosubmittoolbar" title="AutoSubmitToolbar">AutoSubmitToolbar</a>: <i>Boolean</i>
    <a href="#credentialsscheme" title="CredentialsScheme">CredentialsScheme</a>: <i>String</i>
    <a href="#groups" title="Groups">Groups</a>: <i>
      - String</i>
    <a href="#hideios" title="HideIos">HideIos</a>: <i>Boolean</i>
    <a href="#hideweb" title="HideWeb">HideWeb</a>: <i>Boolean</i>
    <a href="#label" title="Label">Label</a>: <i>String</i>
    <a href="#optionalfield1" title="OptionalField1">OptionalField1</a>: <i>String</i>
    <a href="#optionalfield1value" title="OptionalField1Value">OptionalField1Value</a>: <i>String</i>
    <a href="#optionalfield2" title="OptionalField2">OptionalField2</a>: <i>String</i>
    <a href="#optionalfield2value" title="OptionalField2Value">OptionalField2Value</a>: <i>String</i>
    <a href="#optionalfield3" title="OptionalField3">OptionalField3</a>: <i>String</i>
    <a href="#optionalfield3value" title="OptionalField3Value">OptionalField3Value</a>: <i>String</i>
    <a href="#passwordfield" title="PasswordField">PasswordField</a>: <i>String</i>
    <a href="#revealpassword" title="RevealPassword">RevealPassword</a>: <i>Boolean</i>
    <a href="#sharedpassword" title="SharedPassword">SharedPassword</a>: <i>String</i>
    <a href="#sharedusername" title="SharedUsername">SharedUsername</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#url" title="Url">Url</a>: <i>String</i>
    <a href="#usernametemplate" title="UserNameTemplate">UserNameTemplate</a>: <i>String</i>
    <a href="#usernametemplatesuffix" title="UserNameTemplateSuffix">UserNameTemplateSuffix</a>: <i>String</i>
    <a href="#usernametemplatetype" title="UserNameTemplateType">UserNameTemplateType</a>: <i>String</i>
    <a href="#usernamefield" title="UsernameField">UsernameField</a>: <i>String</i>
    <a href="#users" title="Users">Users</a>: <i>
      - <a href="usersdefinition.md">UsersDefinition</a></i>
</pre>

## Properties

#### AccessibilityErrorRedirectUrl

Custom error page URL.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessibilitySelfService

Enable self-service. By default, it is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoSubmitToolbar

Display auto submit toolbar.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CredentialsScheme

Application credentials scheme. Can be set to `"EDIT_USERNAME_AND_PASSWORD"`, `"ADMIN_SETS_CREDENTIALS"`, `"EDIT_PASSWORD_ONLY"`, `"EXTERNAL_PASSWORD_SYNC"`, or `"SHARED_USERNAME_AND_PASSWORD"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Groups

Groups associated with the application. See `okta_app_group_assignment` for a more flexible approach.

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

#### Label

The display name of the Application.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OptionalField1

Name of optional param in the login form.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OptionalField1Value

Name of optional value in the login form.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OptionalField2

Name of optional param in the login form.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OptionalField2Value

Name of optional value in the login form.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OptionalField3

Name of optional param in the login form.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OptionalField3Value

Name of optional value in the login form.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordField

Login password field.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RevealPassword

Allow user to reveal password.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPassword

Shared password, required for certain schemes.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedUsername

Shared username, required for certain schemes.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Status of application. By default, it is `"ACTIVE"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

Login URL.

_Required_: Yes

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

#### UsernameField

Login username field.

_Required_: Yes

_Type_: String

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

#### Id

Returns the <code>Id</code> value.

#### Name

Returns the <code>Name</code> value.

#### SignOnMode

Returns the <code>SignOnMode</code> value.

