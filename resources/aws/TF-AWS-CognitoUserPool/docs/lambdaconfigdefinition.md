# TF::AWS::CognitoUserPool LambdaConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#createauthchallenge" title="CreateAuthChallenge">CreateAuthChallenge</a>" : <i>String</i>,
    "<a href="#custommessage" title="CustomMessage">CustomMessage</a>" : <i>String</i>,
    "<a href="#defineauthchallenge" title="DefineAuthChallenge">DefineAuthChallenge</a>" : <i>String</i>,
    "<a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>" : <i>String</i>,
    "<a href="#postauthentication" title="PostAuthentication">PostAuthentication</a>" : <i>String</i>,
    "<a href="#postconfirmation" title="PostConfirmation">PostConfirmation</a>" : <i>String</i>,
    "<a href="#preauthentication" title="PreAuthentication">PreAuthentication</a>" : <i>String</i>,
    "<a href="#presignup" title="PreSignUp">PreSignUp</a>" : <i>String</i>,
    "<a href="#pretokengeneration" title="PreTokenGeneration">PreTokenGeneration</a>" : <i>String</i>,
    "<a href="#usermigration" title="UserMigration">UserMigration</a>" : <i>String</i>,
    "<a href="#verifyauthchallengeresponse" title="VerifyAuthChallengeResponse">VerifyAuthChallengeResponse</a>" : <i>String</i>,
    "<a href="#customemailsender" title="CustomEmailSender">CustomEmailSender</a>" : <i>[ <a href="customemailsenderdefinition.md">CustomEmailSenderDefinition</a>, ... ]</i>,
    "<a href="#customsmssender" title="CustomSmsSender">CustomSmsSender</a>" : <i>[ <a href="customsmssenderdefinition.md">CustomSmsSenderDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#createauthchallenge" title="CreateAuthChallenge">CreateAuthChallenge</a>: <i>String</i>
<a href="#custommessage" title="CustomMessage">CustomMessage</a>: <i>String</i>
<a href="#defineauthchallenge" title="DefineAuthChallenge">DefineAuthChallenge</a>: <i>String</i>
<a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>: <i>String</i>
<a href="#postauthentication" title="PostAuthentication">PostAuthentication</a>: <i>String</i>
<a href="#postconfirmation" title="PostConfirmation">PostConfirmation</a>: <i>String</i>
<a href="#preauthentication" title="PreAuthentication">PreAuthentication</a>: <i>String</i>
<a href="#presignup" title="PreSignUp">PreSignUp</a>: <i>String</i>
<a href="#pretokengeneration" title="PreTokenGeneration">PreTokenGeneration</a>: <i>String</i>
<a href="#usermigration" title="UserMigration">UserMigration</a>: <i>String</i>
<a href="#verifyauthchallengeresponse" title="VerifyAuthChallengeResponse">VerifyAuthChallengeResponse</a>: <i>String</i>
<a href="#customemailsender" title="CustomEmailSender">CustomEmailSender</a>: <i>
      - <a href="customemailsenderdefinition.md">CustomEmailSenderDefinition</a></i>
<a href="#customsmssender" title="CustomSmsSender">CustomSmsSender</a>: <i>
      - <a href="customsmssenderdefinition.md">CustomSmsSenderDefinition</a></i>
</pre>

## Properties

#### CreateAuthChallenge

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomMessage

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefineAuthChallenge

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PostAuthentication

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PostConfirmation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreAuthentication

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreSignUp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreTokenGeneration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserMigration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VerifyAuthChallengeResponse

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomEmailSender

_Required_: No

_Type_: List of <a href="customemailsenderdefinition.md">CustomEmailSenderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomSmsSender

_Required_: No

_Type_: List of <a href="customsmssenderdefinition.md">CustomSmsSenderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

