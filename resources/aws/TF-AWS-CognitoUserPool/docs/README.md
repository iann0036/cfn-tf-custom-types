# TF::AWS::CognitoUserPool

Provides a Cognito User Pool resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::CognitoUserPool",
    "Properties" : {
        "<a href="#aliasattributes" title="AliasAttributes">AliasAttributes</a>" : <i>[ String, ... ]</i>,
        "<a href="#autoverifiedattributes" title="AutoVerifiedAttributes">AutoVerifiedAttributes</a>" : <i>[ String, ... ]</i>,
        "<a href="#emailverificationmessage" title="EmailVerificationMessage">EmailVerificationMessage</a>" : <i>String</i>,
        "<a href="#emailverificationsubject" title="EmailVerificationSubject">EmailVerificationSubject</a>" : <i>String</i>,
        "<a href="#mfaconfiguration" title="MfaConfiguration">MfaConfiguration</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#smsauthenticationmessage" title="SmsAuthenticationMessage">SmsAuthenticationMessage</a>" : <i>String</i>,
        "<a href="#smsverificationmessage" title="SmsVerificationMessage">SmsVerificationMessage</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#usernameattributes" title="UsernameAttributes">UsernameAttributes</a>" : <i>[ String, ... ]</i>,
        "<a href="#accountrecoverysetting" title="AccountRecoverySetting">AccountRecoverySetting</a>" : <i>[ <a href="accountrecoverysettingdefinition.md">AccountRecoverySettingDefinition</a>, ... ]</i>,
        "<a href="#admincreateuserconfig" title="AdminCreateUserConfig">AdminCreateUserConfig</a>" : <i>[ <a href="admincreateuserconfigdefinition.md">AdminCreateUserConfigDefinition</a>, ... ]</i>,
        "<a href="#deviceconfiguration" title="DeviceConfiguration">DeviceConfiguration</a>" : <i>[ <a href="deviceconfigurationdefinition.md">DeviceConfigurationDefinition</a>, ... ]</i>,
        "<a href="#emailconfiguration" title="EmailConfiguration">EmailConfiguration</a>" : <i>[ <a href="emailconfigurationdefinition.md">EmailConfigurationDefinition</a>, ... ]</i>,
        "<a href="#lambdaconfig" title="LambdaConfig">LambdaConfig</a>" : <i>[ <a href="lambdaconfigdefinition.md">LambdaConfigDefinition</a>, ... ]</i>,
        "<a href="#passwordpolicy" title="PasswordPolicy">PasswordPolicy</a>" : <i>[ <a href="passwordpolicydefinition.md">PasswordPolicyDefinition</a>, ... ]</i>,
        "<a href="#schema" title="Schema">Schema</a>" : <i>[ <a href="schemadefinition.md">SchemaDefinition</a>, ... ]</i>,
        "<a href="#smsconfiguration" title="SmsConfiguration">SmsConfiguration</a>" : <i>[ <a href="smsconfigurationdefinition.md">SmsConfigurationDefinition</a>, ... ]</i>,
        "<a href="#softwaretokenmfaconfiguration" title="SoftwareTokenMfaConfiguration">SoftwareTokenMfaConfiguration</a>" : <i>[ <a href="softwaretokenmfaconfigurationdefinition.md">SoftwareTokenMfaConfigurationDefinition</a>, ... ]</i>,
        "<a href="#userpooladdons" title="UserPoolAddOns">UserPoolAddOns</a>" : <i>[ <a href="userpooladdonsdefinition.md">UserPoolAddOnsDefinition</a>, ... ]</i>,
        "<a href="#usernameconfiguration" title="UsernameConfiguration">UsernameConfiguration</a>" : <i>[ <a href="usernameconfigurationdefinition.md">UsernameConfigurationDefinition</a>, ... ]</i>,
        "<a href="#verificationmessagetemplate" title="VerificationMessageTemplate">VerificationMessageTemplate</a>" : <i>[ <a href="verificationmessagetemplatedefinition.md">VerificationMessageTemplateDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::CognitoUserPool
Properties:
    <a href="#aliasattributes" title="AliasAttributes">AliasAttributes</a>: <i>
      - String</i>
    <a href="#autoverifiedattributes" title="AutoVerifiedAttributes">AutoVerifiedAttributes</a>: <i>
      - String</i>
    <a href="#emailverificationmessage" title="EmailVerificationMessage">EmailVerificationMessage</a>: <i>String</i>
    <a href="#emailverificationsubject" title="EmailVerificationSubject">EmailVerificationSubject</a>: <i>String</i>
    <a href="#mfaconfiguration" title="MfaConfiguration">MfaConfiguration</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#smsauthenticationmessage" title="SmsAuthenticationMessage">SmsAuthenticationMessage</a>: <i>String</i>
    <a href="#smsverificationmessage" title="SmsVerificationMessage">SmsVerificationMessage</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#usernameattributes" title="UsernameAttributes">UsernameAttributes</a>: <i>
      - String</i>
    <a href="#accountrecoverysetting" title="AccountRecoverySetting">AccountRecoverySetting</a>: <i>
      - <a href="accountrecoverysettingdefinition.md">AccountRecoverySettingDefinition</a></i>
    <a href="#admincreateuserconfig" title="AdminCreateUserConfig">AdminCreateUserConfig</a>: <i>
      - <a href="admincreateuserconfigdefinition.md">AdminCreateUserConfigDefinition</a></i>
    <a href="#deviceconfiguration" title="DeviceConfiguration">DeviceConfiguration</a>: <i>
      - <a href="deviceconfigurationdefinition.md">DeviceConfigurationDefinition</a></i>
    <a href="#emailconfiguration" title="EmailConfiguration">EmailConfiguration</a>: <i>
      - <a href="emailconfigurationdefinition.md">EmailConfigurationDefinition</a></i>
    <a href="#lambdaconfig" title="LambdaConfig">LambdaConfig</a>: <i>
      - <a href="lambdaconfigdefinition.md">LambdaConfigDefinition</a></i>
    <a href="#passwordpolicy" title="PasswordPolicy">PasswordPolicy</a>: <i>
      - <a href="passwordpolicydefinition.md">PasswordPolicyDefinition</a></i>
    <a href="#schema" title="Schema">Schema</a>: <i>
      - <a href="schemadefinition.md">SchemaDefinition</a></i>
    <a href="#smsconfiguration" title="SmsConfiguration">SmsConfiguration</a>: <i>
      - <a href="smsconfigurationdefinition.md">SmsConfigurationDefinition</a></i>
    <a href="#softwaretokenmfaconfiguration" title="SoftwareTokenMfaConfiguration">SoftwareTokenMfaConfiguration</a>: <i>
      - <a href="softwaretokenmfaconfigurationdefinition.md">SoftwareTokenMfaConfigurationDefinition</a></i>
    <a href="#userpooladdons" title="UserPoolAddOns">UserPoolAddOns</a>: <i>
      - <a href="userpooladdonsdefinition.md">UserPoolAddOnsDefinition</a></i>
    <a href="#usernameconfiguration" title="UsernameConfiguration">UsernameConfiguration</a>: <i>
      - <a href="usernameconfigurationdefinition.md">UsernameConfigurationDefinition</a></i>
    <a href="#verificationmessagetemplate" title="VerificationMessageTemplate">VerificationMessageTemplate</a>: <i>
      - <a href="verificationmessagetemplatedefinition.md">VerificationMessageTemplateDefinition</a></i>
</pre>

## Properties

#### AliasAttributes

Attributes supported as an alias for this user pool. Valid values: `phone_number`, `email`, or `preferred_username`. Conflicts with `username_attributes`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoVerifiedAttributes

Attributes to be auto-verified. Valid values: `email`, `phone_number`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailVerificationMessage

String representing the email verification message. Conflicts with `verification_message_template` configuration block `email_message` argument.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailVerificationSubject

String representing the email verification subject. Conflicts with `verification_message_template` configuration block `email_subject` argument.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MfaConfiguration

Multi-Factor Authentication (MFA) configuration for the User Pool. Defaults of `OFF`. Valid values are `OFF` (MFA Tokens are not required), `ON` (MFA is required for all users to sign in; requires at least one of `sms_configuration` or `software_token_mfa_configuration` to be configured), or `OPTIONAL` (MFA Will be required only for individual users who have MFA Enabled; requires at least one of `sms_configuration` or `software_token_mfa_configuration` to be configured).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the user pool.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmsAuthenticationMessage

String representing the SMS authentication message. The Message must contain the `{####}` placeholder, which will be replaced with the code.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmsVerificationMessage

String representing the SMS verification message. Conflicts with `verification_message_template` configuration block `sms_message` argument.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Map of tags to assign to the User Pool. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsernameAttributes

Whether email addresses or phone numbers can be specified as usernames when a user signs up. Conflicts with `alias_attributes`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountRecoverySetting

_Required_: No

_Type_: List of <a href="accountrecoverysettingdefinition.md">AccountRecoverySettingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminCreateUserConfig

_Required_: No

_Type_: List of <a href="admincreateuserconfigdefinition.md">AdminCreateUserConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceConfiguration

_Required_: No

_Type_: List of <a href="deviceconfigurationdefinition.md">DeviceConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailConfiguration

_Required_: No

_Type_: List of <a href="emailconfigurationdefinition.md">EmailConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LambdaConfig

_Required_: No

_Type_: List of <a href="lambdaconfigdefinition.md">LambdaConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordPolicy

_Required_: No

_Type_: List of <a href="passwordpolicydefinition.md">PasswordPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schema

_Required_: No

_Type_: List of <a href="schemadefinition.md">SchemaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmsConfiguration

_Required_: No

_Type_: List of <a href="smsconfigurationdefinition.md">SmsConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SoftwareTokenMfaConfiguration

_Required_: No

_Type_: List of <a href="softwaretokenmfaconfigurationdefinition.md">SoftwareTokenMfaConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserPoolAddOns

_Required_: No

_Type_: List of <a href="userpooladdonsdefinition.md">UserPoolAddOnsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsernameConfiguration

_Required_: No

_Type_: List of <a href="usernameconfigurationdefinition.md">UsernameConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VerificationMessageTemplate

_Required_: No

_Type_: List of <a href="verificationmessagetemplatedefinition.md">VerificationMessageTemplateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### CreationDate

Returns the <code>CreationDate</code> value.

#### CustomDomain

Returns the <code>CustomDomain</code> value.

#### Domain

Returns the <code>Domain</code> value.

#### Endpoint

Returns the <code>Endpoint</code> value.

#### EstimatedNumberOfUsers

Returns the <code>EstimatedNumberOfUsers</code> value.

#### Id

Returns the <code>Id</code> value.

#### LastModifiedDate

Returns the <code>LastModifiedDate</code> value.

