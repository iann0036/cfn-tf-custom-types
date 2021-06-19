# TF::OCI::WaasWaasPolicy AccessRulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#blockaction" title="BlockAction">BlockAction</a>" : <i>String</i>,
    "<a href="#blockerrorpagecode" title="BlockErrorPageCode">BlockErrorPageCode</a>" : <i>String</i>,
    "<a href="#blockerrorpagedescription" title="BlockErrorPageDescription">BlockErrorPageDescription</a>" : <i>String</i>,
    "<a href="#blockerrorpagemessage" title="BlockErrorPageMessage">BlockErrorPageMessage</a>" : <i>String</i>,
    "<a href="#blockresponsecode" title="BlockResponseCode">BlockResponseCode</a>" : <i>Double</i>,
    "<a href="#bypasschallenges" title="BypassChallenges">BypassChallenges</a>" : <i>[ String, ... ]</i>,
    "<a href="#captchafooter" title="CaptchaFooter">CaptchaFooter</a>" : <i>String</i>,
    "<a href="#captchaheader" title="CaptchaHeader">CaptchaHeader</a>" : <i>String</i>,
    "<a href="#captchasubmitlabel" title="CaptchaSubmitLabel">CaptchaSubmitLabel</a>" : <i>String</i>,
    "<a href="#captchatitle" title="CaptchaTitle">CaptchaTitle</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#redirectresponsecode" title="RedirectResponseCode">RedirectResponseCode</a>" : <i>String</i>,
    "<a href="#redirecturl" title="RedirectUrl">RedirectUrl</a>" : <i>String</i>,
    "<a href="#criteria" title="Criteria">Criteria</a>" : <i>[ <a href="criteriadefinition.md">CriteriaDefinition</a>, ... ]</i>,
    "<a href="#responseheadermanipulation" title="ResponseHeaderManipulation">ResponseHeaderManipulation</a>" : <i>[ <a href="responseheadermanipulationdefinition.md">ResponseHeaderManipulationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#blockaction" title="BlockAction">BlockAction</a>: <i>String</i>
<a href="#blockerrorpagecode" title="BlockErrorPageCode">BlockErrorPageCode</a>: <i>String</i>
<a href="#blockerrorpagedescription" title="BlockErrorPageDescription">BlockErrorPageDescription</a>: <i>String</i>
<a href="#blockerrorpagemessage" title="BlockErrorPageMessage">BlockErrorPageMessage</a>: <i>String</i>
<a href="#blockresponsecode" title="BlockResponseCode">BlockResponseCode</a>: <i>Double</i>
<a href="#bypasschallenges" title="BypassChallenges">BypassChallenges</a>: <i>
      - String</i>
<a href="#captchafooter" title="CaptchaFooter">CaptchaFooter</a>: <i>String</i>
<a href="#captchaheader" title="CaptchaHeader">CaptchaHeader</a>: <i>String</i>
<a href="#captchasubmitlabel" title="CaptchaSubmitLabel">CaptchaSubmitLabel</a>: <i>String</i>
<a href="#captchatitle" title="CaptchaTitle">CaptchaTitle</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#redirectresponsecode" title="RedirectResponseCode">RedirectResponseCode</a>: <i>String</i>
<a href="#redirecturl" title="RedirectUrl">RedirectUrl</a>: <i>String</i>
<a href="#criteria" title="Criteria">Criteria</a>: <i>
      - <a href="criteriadefinition.md">CriteriaDefinition</a></i>
<a href="#responseheadermanipulation" title="ResponseHeaderManipulation">ResponseHeaderManipulation</a>: <i>
      - <a href="responseheadermanipulationdefinition.md">ResponseHeaderManipulationDefinition</a></i>
</pre>

## Properties

#### Action

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockAction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockErrorPageCode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockErrorPageDescription

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockErrorPageMessage

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockResponseCode

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BypassChallenges

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaptchaFooter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaptchaHeader

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaptchaSubmitLabel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaptchaTitle

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectResponseCode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Criteria

_Required_: No

_Type_: List of <a href="criteriadefinition.md">CriteriaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseHeaderManipulation

_Required_: No

_Type_: List of <a href="responseheadermanipulationdefinition.md">ResponseHeaderManipulationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

