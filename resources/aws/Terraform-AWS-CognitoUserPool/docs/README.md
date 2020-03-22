# Terraform::AWS::CognitoUserPool

CloudFormation equivalent of aws_cognito_user_pool

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::CognitoUserPool",
    "Properties" : {
        "<a href="#aliasattributes" title="AliasAttributes">AliasAttributes</a>" : <i>[ String, ... ]</i>,
        "<a href="#autoverifiedattributes" title="AutoVerifiedAttributes">AutoVerifiedAttributes</a>" : <i>[ String, ... ]</i>,
        "<a href="#emailverificationmessage" title="EmailVerificationMessage">EmailVerificationMessage</a>" : <i>String</i>,
        "<a href="#emailverificationsubject" title="EmailVerificationSubject">EmailVerificationSubject</a>" : <i>String</i>,
        "<a href="#mfaconfiguration" title="MfaConfiguration">MfaConfiguration</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#smsauthenticationmessage" title="SmsAuthenticationMessage">SmsAuthenticationMessage</a>" : <i>String</i>,
        "<a href="#smsverificationmessage" title="SmsVerificationMessage">SmsVerificationMessage</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#usernameattributes" title="UsernameAttributes">UsernameAttributes</a>" : <i>[ String, ... ]</i>,
        "<a href="#admincreateuserconfig" title="AdminCreateUserConfig">AdminCreateUserConfig</a>" : <i>[ <a href="admincreateuserconfig.md">AdminCreateUserConfig</a>, ... ]</i>,
        "<a href="#deviceconfiguration" title="DeviceConfiguration">DeviceConfiguration</a>" : <i>[ <a href="deviceconfiguration.md">DeviceConfiguration</a>, ... ]</i>,
        "<a href="#emailconfiguration" title="EmailConfiguration">EmailConfiguration</a>" : <i>[ <a href="emailconfiguration.md">EmailConfiguration</a>, ... ]</i>,
        "<a href="#lambdaconfig" title="LambdaConfig">LambdaConfig</a>" : <i>[ <a href="lambdaconfig.md">LambdaConfig</a>, ... ]</i>,
        "<a href="#passwordpolicy" title="PasswordPolicy">PasswordPolicy</a>" : <i>[ <a href="passwordpolicy.md">PasswordPolicy</a>, ... ]</i>,
        "<a href="#schema" title="Schema">Schema</a>" : <i>[ <a href="schema.md">Schema</a>, ... ]</i>,
        "<a href="#smsconfiguration" title="SmsConfiguration">SmsConfiguration</a>" : <i>[ <a href="smsconfiguration.md">SmsConfiguration</a>, ... ]</i>,
        "<a href="#softwaretokenmfaconfiguration" title="SoftwareTokenMfaConfiguration">SoftwareTokenMfaConfiguration</a>" : <i>[ <a href="softwaretokenmfaconfiguration.md">SoftwareTokenMfaConfiguration</a>, ... ]</i>,
        "<a href="#userpooladdons" title="UserPoolAddOns">UserPoolAddOns</a>" : <i>[ <a href="userpooladdons.md">UserPoolAddOns</a>, ... ]</i>,
        "<a href="#usernameconfiguration" title="UsernameConfiguration">UsernameConfiguration</a>" : <i>[ <a href="usernameconfiguration.md">UsernameConfiguration</a>, ... ]</i>,
        "<a href="#verificationmessagetemplate" title="VerificationMessageTemplate">VerificationMessageTemplate</a>" : <i>[ <a href="verificationmessagetemplate.md">VerificationMessageTemplate</a>, ... ]</i>,
        "<a href="#invitemessagetemplate" title="InviteMessageTemplate">InviteMessageTemplate</a>" : <i>[ <a href="invitemessagetemplate.md">InviteMessageTemplate</a>, ... ]</i>,
        "<a href="#numberattributeconstraints" title="NumberAttributeConstraints">NumberAttributeConstraints</a>" : <i>[ <a href="numberattributeconstraints.md">NumberAttributeConstraints</a>, ... ]</i>,
        "<a href="#stringattributeconstraints" title="StringAttributeConstraints">StringAttributeConstraints</a>" : <i>[ <a href="stringattributeconstraints.md">StringAttributeConstraints</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::CognitoUserPool
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
      - <a href="tags.md">Tags</a></i>
    <a href="#usernameattributes" title="UsernameAttributes">UsernameAttributes</a>: <i>
      - String</i>
    <a href="#admincreateuserconfig" title="AdminCreateUserConfig">AdminCreateUserConfig</a>: <i>
      - <a href="admincreateuserconfig.md">AdminCreateUserConfig</a></i>
    <a href="#deviceconfiguration" title="DeviceConfiguration">DeviceConfiguration</a>: <i>
      - <a href="deviceconfiguration.md">DeviceConfiguration</a></i>
    <a href="#emailconfiguration" title="EmailConfiguration">EmailConfiguration</a>: <i>
      - <a href="emailconfiguration.md">EmailConfiguration</a></i>
    <a href="#lambdaconfig" title="LambdaConfig">LambdaConfig</a>: <i>
      - <a href="lambdaconfig.md">LambdaConfig</a></i>
    <a href="#passwordpolicy" title="PasswordPolicy">PasswordPolicy</a>: <i>
      - <a href="passwordpolicy.md">PasswordPolicy</a></i>
    <a href="#schema" title="Schema">Schema</a>: <i>
      - <a href="schema.md">Schema</a></i>
    <a href="#smsconfiguration" title="SmsConfiguration">SmsConfiguration</a>: <i>
      - <a href="smsconfiguration.md">SmsConfiguration</a></i>
    <a href="#softwaretokenmfaconfiguration" title="SoftwareTokenMfaConfiguration">SoftwareTokenMfaConfiguration</a>: <i>
      - <a href="softwaretokenmfaconfiguration.md">SoftwareTokenMfaConfiguration</a></i>
    <a href="#userpooladdons" title="UserPoolAddOns">UserPoolAddOns</a>: <i>
      - <a href="userpooladdons.md">UserPoolAddOns</a></i>
    <a href="#usernameconfiguration" title="UsernameConfiguration">UsernameConfiguration</a>: <i>
      - <a href="usernameconfiguration.md">UsernameConfiguration</a></i>
    <a href="#verificationmessagetemplate" title="VerificationMessageTemplate">VerificationMessageTemplate</a>: <i>
      - <a href="verificationmessagetemplate.md">VerificationMessageTemplate</a></i>
    <a href="#invitemessagetemplate" title="InviteMessageTemplate">InviteMessageTemplate</a>: <i>
      - <a href="invitemessagetemplate.md">InviteMessageTemplate</a></i>
    <a href="#numberattributeconstraints" title="NumberAttributeConstraints">NumberAttributeConstraints</a>: <i>
      - <a href="numberattributeconstraints.md">NumberAttributeConstraints</a></i>
    <a href="#stringattributeconstraints" title="StringAttributeConstraints">StringAttributeConstraints</a>: <i>
      - <a href="stringattributeconstraints.md">StringAttributeConstraints</a></i>
</pre>

## Properties

#### AliasAttributes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoVerifiedAttributes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailVerificationMessage

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailVerificationSubject

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MfaConfiguration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmsAuthenticationMessage

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmsVerificationMessage

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsernameAttributes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminCreateUserConfig

_Required_: No

_Type_: List of <a href="admincreateuserconfig.md">AdminCreateUserConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceConfiguration

_Required_: No

_Type_: List of <a href="deviceconfiguration.md">DeviceConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailConfiguration

_Required_: No

_Type_: List of <a href="emailconfiguration.md">EmailConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LambdaConfig

_Required_: No

_Type_: List of <a href="lambdaconfig.md">LambdaConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordPolicy

_Required_: No

_Type_: List of <a href="passwordpolicy.md">PasswordPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schema

_Required_: No

_Type_: List of <a href="schema.md">Schema</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmsConfiguration

_Required_: No

_Type_: List of <a href="smsconfiguration.md">SmsConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SoftwareTokenMfaConfiguration

_Required_: No

_Type_: List of <a href="softwaretokenmfaconfiguration.md">SoftwareTokenMfaConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserPoolAddOns

_Required_: No

_Type_: List of <a href="userpooladdons.md">UserPoolAddOns</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsernameConfiguration

_Required_: No

_Type_: List of <a href="usernameconfiguration.md">UsernameConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VerificationMessageTemplate

_Required_: No

_Type_: List of <a href="verificationmessagetemplate.md">VerificationMessageTemplate</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InviteMessageTemplate

_Required_: No

_Type_: List of <a href="invitemessagetemplate.md">InviteMessageTemplate</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumberAttributeConstraints

_Required_: No

_Type_: List of <a href="numberattributeconstraints.md">NumberAttributeConstraints</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StringAttributeConstraints

_Required_: No

_Type_: List of <a href="stringattributeconstraints.md">StringAttributeConstraints</a>

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

#### Endpoint

Returns the <code>Endpoint</code> value.

#### Id

Returns the <code>Id</code> value.

#### LastModifiedDate

Returns the <code>LastModifiedDate</code> value.

