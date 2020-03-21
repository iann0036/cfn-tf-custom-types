# Terraform::AWS::CognitoUserPool

CloudFormation equivalent of aws_cognito_user_pool

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::CognitoUserPool",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#aliasattributes" title="AliasAttributes">AliasAttributes</a>" : <i>[ String, ... ]</i>,
        "<a href="#arn" title="Arn">Arn</a>" : <i>String</i>,
        "<a href="#autoverifiedattributes" title="AutoVerifiedAttributes">AutoVerifiedAttributes</a>" : <i>[ String, ... ]</i>,
        "<a href="#creationdate" title="CreationDate">CreationDate</a>" : <i>String</i>,
        "<a href="#emailverificationmessage" title="EmailVerificationMessage">EmailVerificationMessage</a>" : <i>String</i>,
        "<a href="#emailverificationsubject" title="EmailVerificationSubject">EmailVerificationSubject</a>" : <i>String</i>,
        "<a href="#endpoint" title="Endpoint">Endpoint</a>" : <i>String</i>,
        "<a href="#lastmodifieddate" title="LastModifiedDate">LastModifiedDate</a>" : <i>String</i>,
        "<a href="#mfaconfiguration" title="MfaConfiguration">MfaConfiguration</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#smsauthenticationmessage" title="SmsAuthenticationMessage">SmsAuthenticationMessage</a>" : <i>String</i>,
        "<a href="#smsverificationmessage" title="SmsVerificationMessage">SmsVerificationMessage</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#usernameattributes" title="UsernameAttributes">UsernameAttributes</a>" : <i>[ String, ... ]</i>,
        "<a href="#admincreateuserconfig" title="AdminCreateUserConfig">AdminCreateUserConfig</a>" : <i>[ &lt;a href=&#34;admincreateuserconfig.md&#34;&gt;AdminCreateUserConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#deviceconfiguration" title="DeviceConfiguration">DeviceConfiguration</a>" : <i>[ &lt;a href=&#34;deviceconfiguration.md&#34;&gt;DeviceConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#emailconfiguration" title="EmailConfiguration">EmailConfiguration</a>" : <i>[ &lt;a href=&#34;emailconfiguration.md&#34;&gt;EmailConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#lambdaconfig" title="LambdaConfig">LambdaConfig</a>" : <i>[ &lt;a href=&#34;lambdaconfig.md&#34;&gt;LambdaConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#passwordpolicy" title="PasswordPolicy">PasswordPolicy</a>" : <i>[ &lt;a href=&#34;passwordpolicy.md&#34;&gt;PasswordPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#schema" title="Schema">Schema</a>" : <i>[ &lt;a href=&#34;schema.md&#34;&gt;Schema&lt;/a&gt;, ... ]</i>,
        "<a href="#smsconfiguration" title="SmsConfiguration">SmsConfiguration</a>" : <i>[ &lt;a href=&#34;smsconfiguration.md&#34;&gt;SmsConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#softwaretokenmfaconfiguration" title="SoftwareTokenMfaConfiguration">SoftwareTokenMfaConfiguration</a>" : <i>[ &lt;a href=&#34;softwaretokenmfaconfiguration.md&#34;&gt;SoftwareTokenMfaConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#userpooladdons" title="UserPoolAddOns">UserPoolAddOns</a>" : <i>[ &lt;a href=&#34;userpooladdons.md&#34;&gt;UserPoolAddOns&lt;/a&gt;, ... ]</i>,
        "<a href="#usernameconfiguration" title="UsernameConfiguration">UsernameConfiguration</a>" : <i>[ &lt;a href=&#34;usernameconfiguration.md&#34;&gt;UsernameConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#verificationmessagetemplate" title="VerificationMessageTemplate">VerificationMessageTemplate</a>" : <i>[ &lt;a href=&#34;verificationmessagetemplate.md&#34;&gt;VerificationMessageTemplate&lt;/a&gt;, ... ]</i>,
        "<a href="#invitemessagetemplate" title="InviteMessageTemplate">InviteMessageTemplate</a>" : <i>[ &lt;a href=&#34;invitemessagetemplate.md&#34;&gt;InviteMessageTemplate&lt;/a&gt;, ... ]</i>,
        "<a href="#numberattributeconstraints" title="NumberAttributeConstraints">NumberAttributeConstraints</a>" : <i>[ &lt;a href=&#34;numberattributeconstraints.md&#34;&gt;NumberAttributeConstraints&lt;/a&gt;, ... ]</i>,
        "<a href="#stringattributeconstraints" title="StringAttributeConstraints">StringAttributeConstraints</a>" : <i>[ &lt;a href=&#34;stringattributeconstraints.md&#34;&gt;StringAttributeConstraints&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::CognitoUserPool
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#aliasattributes" title="AliasAttributes">AliasAttributes</a>: <i>
      - String</i>
    <a href="#arn" title="Arn">Arn</a>: <i>String</i>
    <a href="#autoverifiedattributes" title="AutoVerifiedAttributes">AutoVerifiedAttributes</a>: <i>
      - String</i>
    <a href="#creationdate" title="CreationDate">CreationDate</a>: <i>String</i>
    <a href="#emailverificationmessage" title="EmailVerificationMessage">EmailVerificationMessage</a>: <i>String</i>
    <a href="#emailverificationsubject" title="EmailVerificationSubject">EmailVerificationSubject</a>: <i>String</i>
    <a href="#endpoint" title="Endpoint">Endpoint</a>: <i>String</i>
    <a href="#lastmodifieddate" title="LastModifiedDate">LastModifiedDate</a>: <i>String</i>
    <a href="#mfaconfiguration" title="MfaConfiguration">MfaConfiguration</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#smsauthenticationmessage" title="SmsAuthenticationMessage">SmsAuthenticationMessage</a>: <i>String</i>
    <a href="#smsverificationmessage" title="SmsVerificationMessage">SmsVerificationMessage</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#usernameattributes" title="UsernameAttributes">UsernameAttributes</a>: <i>
      - String</i>
    <a href="#admincreateuserconfig" title="AdminCreateUserConfig">AdminCreateUserConfig</a>: <i>
      - &lt;a href=&#34;admincreateuserconfig.md&#34;&gt;AdminCreateUserConfig&lt;/a&gt;</i>
    <a href="#deviceconfiguration" title="DeviceConfiguration">DeviceConfiguration</a>: <i>
      - &lt;a href=&#34;deviceconfiguration.md&#34;&gt;DeviceConfiguration&lt;/a&gt;</i>
    <a href="#emailconfiguration" title="EmailConfiguration">EmailConfiguration</a>: <i>
      - &lt;a href=&#34;emailconfiguration.md&#34;&gt;EmailConfiguration&lt;/a&gt;</i>
    <a href="#lambdaconfig" title="LambdaConfig">LambdaConfig</a>: <i>
      - &lt;a href=&#34;lambdaconfig.md&#34;&gt;LambdaConfig&lt;/a&gt;</i>
    <a href="#passwordpolicy" title="PasswordPolicy">PasswordPolicy</a>: <i>
      - &lt;a href=&#34;passwordpolicy.md&#34;&gt;PasswordPolicy&lt;/a&gt;</i>
    <a href="#schema" title="Schema">Schema</a>: <i>
      - &lt;a href=&#34;schema.md&#34;&gt;Schema&lt;/a&gt;</i>
    <a href="#smsconfiguration" title="SmsConfiguration">SmsConfiguration</a>: <i>
      - &lt;a href=&#34;smsconfiguration.md&#34;&gt;SmsConfiguration&lt;/a&gt;</i>
    <a href="#softwaretokenmfaconfiguration" title="SoftwareTokenMfaConfiguration">SoftwareTokenMfaConfiguration</a>: <i>
      - &lt;a href=&#34;softwaretokenmfaconfiguration.md&#34;&gt;SoftwareTokenMfaConfiguration&lt;/a&gt;</i>
    <a href="#userpooladdons" title="UserPoolAddOns">UserPoolAddOns</a>: <i>
      - &lt;a href=&#34;userpooladdons.md&#34;&gt;UserPoolAddOns&lt;/a&gt;</i>
    <a href="#usernameconfiguration" title="UsernameConfiguration">UsernameConfiguration</a>: <i>
      - &lt;a href=&#34;usernameconfiguration.md&#34;&gt;UsernameConfiguration&lt;/a&gt;</i>
    <a href="#verificationmessagetemplate" title="VerificationMessageTemplate">VerificationMessageTemplate</a>: <i>
      - &lt;a href=&#34;verificationmessagetemplate.md&#34;&gt;VerificationMessageTemplate&lt;/a&gt;</i>
    <a href="#invitemessagetemplate" title="InviteMessageTemplate">InviteMessageTemplate</a>: <i>
      - &lt;a href=&#34;invitemessagetemplate.md&#34;&gt;InviteMessageTemplate&lt;/a&gt;</i>
    <a href="#numberattributeconstraints" title="NumberAttributeConstraints">NumberAttributeConstraints</a>: <i>
      - &lt;a href=&#34;numberattributeconstraints.md&#34;&gt;NumberAttributeConstraints&lt;/a&gt;</i>
    <a href="#stringattributeconstraints" title="StringAttributeConstraints">StringAttributeConstraints</a>: <i>
      - &lt;a href=&#34;stringattributeconstraints.md&#34;&gt;StringAttributeConstraints&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AliasAttributes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Arn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoVerifiedAttributes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreationDate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailVerificationMessage

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailVerificationSubject

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Endpoint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LastModifiedDate

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

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsernameAttributes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminCreateUserConfig

_Required_: No

_Type_: List of &lt;a href=&#34;admincreateuserconfig.md&#34;&gt;AdminCreateUserConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;deviceconfiguration.md&#34;&gt;DeviceConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;emailconfiguration.md&#34;&gt;EmailConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LambdaConfig

_Required_: No

_Type_: List of &lt;a href=&#34;lambdaconfig.md&#34;&gt;LambdaConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;passwordpolicy.md&#34;&gt;PasswordPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schema

_Required_: No

_Type_: List of &lt;a href=&#34;schema.md&#34;&gt;Schema&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmsConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;smsconfiguration.md&#34;&gt;SmsConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SoftwareTokenMfaConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;softwaretokenmfaconfiguration.md&#34;&gt;SoftwareTokenMfaConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserPoolAddOns

_Required_: No

_Type_: List of &lt;a href=&#34;userpooladdons.md&#34;&gt;UserPoolAddOns&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsernameConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;usernameconfiguration.md&#34;&gt;UsernameConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VerificationMessageTemplate

_Required_: No

_Type_: List of &lt;a href=&#34;verificationmessagetemplate.md&#34;&gt;VerificationMessageTemplate&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InviteMessageTemplate

_Required_: No

_Type_: List of &lt;a href=&#34;invitemessagetemplate.md&#34;&gt;InviteMessageTemplate&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumberAttributeConstraints

_Required_: No

_Type_: List of &lt;a href=&#34;numberattributeconstraints.md&#34;&gt;NumberAttributeConstraints&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StringAttributeConstraints

_Required_: No

_Type_: List of &lt;a href=&#34;stringattributeconstraints.md&#34;&gt;StringAttributeConstraints&lt;/a&gt;

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

Returns the &lt;code&gt;Arn&lt;/code&gt; value.

#### CreationDate

Returns the &lt;code&gt;CreationDate&lt;/code&gt; value.

#### Endpoint

Returns the &lt;code&gt;Endpoint&lt;/code&gt; value.

#### LastModifiedDate

Returns the &lt;code&gt;LastModifiedDate&lt;/code&gt; value.

