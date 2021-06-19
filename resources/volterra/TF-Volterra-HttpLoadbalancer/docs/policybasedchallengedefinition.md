# TF::Volterra::HttpLoadbalancer PolicyBasedChallengeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#alwaysenablecaptchachallenge" title="AlwaysEnableCaptchaChallenge">AlwaysEnableCaptchaChallenge</a>" : <i>Boolean</i>,
    "<a href="#alwaysenablejschallenge" title="AlwaysEnableJsChallenge">AlwaysEnableJsChallenge</a>" : <i>Boolean</i>,
    "<a href="#defaultcaptchachallengeparameters" title="DefaultCaptchaChallengeParameters">DefaultCaptchaChallengeParameters</a>" : <i>Boolean</i>,
    "<a href="#defaultjschallengeparameters" title="DefaultJsChallengeParameters">DefaultJsChallengeParameters</a>" : <i>Boolean</i>,
    "<a href="#defaultmitigationsettings" title="DefaultMitigationSettings">DefaultMitigationSettings</a>" : <i>Boolean</i>,
    "<a href="#defaulttemporaryblockingparameters" title="DefaultTemporaryBlockingParameters">DefaultTemporaryBlockingParameters</a>" : <i>Boolean</i>,
    "<a href="#nochallenge" title="NoChallenge">NoChallenge</a>" : <i>Boolean</i>,
    "<a href="#captchachallengeparameters" title="CaptchaChallengeParameters">CaptchaChallengeParameters</a>" : <i>[ <a href="captchachallengeparametersdefinition.md">CaptchaChallengeParametersDefinition</a>, ... ]</i>,
    "<a href="#jschallengeparameters" title="JsChallengeParameters">JsChallengeParameters</a>" : <i>[ <a href="jschallengeparametersdefinition.md">JsChallengeParametersDefinition</a>, ... ]</i>,
    "<a href="#malicioususermitigation" title="MaliciousUserMitigation">MaliciousUserMitigation</a>" : <i>[ <a href="malicioususermitigationdefinition.md">MaliciousUserMitigationDefinition</a>, ... ]</i>,
    "<a href="#rulelist" title="RuleList">RuleList</a>" : <i>[ <a href="rulelistdefinition.md">RuleListDefinition</a>, ... ]</i>,
    "<a href="#temporaryuserblocking" title="TemporaryUserBlocking">TemporaryUserBlocking</a>" : <i>[ <a href="temporaryuserblockingdefinition.md">TemporaryUserBlockingDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#alwaysenablecaptchachallenge" title="AlwaysEnableCaptchaChallenge">AlwaysEnableCaptchaChallenge</a>: <i>Boolean</i>
<a href="#alwaysenablejschallenge" title="AlwaysEnableJsChallenge">AlwaysEnableJsChallenge</a>: <i>Boolean</i>
<a href="#defaultcaptchachallengeparameters" title="DefaultCaptchaChallengeParameters">DefaultCaptchaChallengeParameters</a>: <i>Boolean</i>
<a href="#defaultjschallengeparameters" title="DefaultJsChallengeParameters">DefaultJsChallengeParameters</a>: <i>Boolean</i>
<a href="#defaultmitigationsettings" title="DefaultMitigationSettings">DefaultMitigationSettings</a>: <i>Boolean</i>
<a href="#defaulttemporaryblockingparameters" title="DefaultTemporaryBlockingParameters">DefaultTemporaryBlockingParameters</a>: <i>Boolean</i>
<a href="#nochallenge" title="NoChallenge">NoChallenge</a>: <i>Boolean</i>
<a href="#captchachallengeparameters" title="CaptchaChallengeParameters">CaptchaChallengeParameters</a>: <i>
      - <a href="captchachallengeparametersdefinition.md">CaptchaChallengeParametersDefinition</a></i>
<a href="#jschallengeparameters" title="JsChallengeParameters">JsChallengeParameters</a>: <i>
      - <a href="jschallengeparametersdefinition.md">JsChallengeParametersDefinition</a></i>
<a href="#malicioususermitigation" title="MaliciousUserMitigation">MaliciousUserMitigation</a>: <i>
      - <a href="malicioususermitigationdefinition.md">MaliciousUserMitigationDefinition</a></i>
<a href="#rulelist" title="RuleList">RuleList</a>: <i>
      - <a href="rulelistdefinition.md">RuleListDefinition</a></i>
<a href="#temporaryuserblocking" title="TemporaryUserBlocking">TemporaryUserBlocking</a>: <i>
      - <a href="temporaryuserblockingdefinition.md">TemporaryUserBlockingDefinition</a></i>
</pre>

## Properties

#### AlwaysEnableCaptchaChallenge

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlwaysEnableJsChallenge

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultCaptchaChallengeParameters

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultJsChallengeParameters

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultMitigationSettings

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultTemporaryBlockingParameters

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoChallenge

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaptchaChallengeParameters

_Required_: No

_Type_: List of <a href="captchachallengeparametersdefinition.md">CaptchaChallengeParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JsChallengeParameters

_Required_: No

_Type_: List of <a href="jschallengeparametersdefinition.md">JsChallengeParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaliciousUserMitigation

_Required_: No

_Type_: List of <a href="malicioususermitigationdefinition.md">MaliciousUserMitigationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleList

_Required_: No

_Type_: List of <a href="rulelistdefinition.md">RuleListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemporaryUserBlocking

_Required_: No

_Type_: List of <a href="temporaryuserblockingdefinition.md">TemporaryUserBlockingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

