# TF::OCI::WaasWaasPolicy WafConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#origin" title="Origin">Origin</a>" : <i>String</i>,
    "<a href="#origingroups" title="OriginGroups">OriginGroups</a>" : <i>[ <a href="origingroupsdefinition.md">OriginGroupsDefinition</a>, ... ]</i>,
    "<a href="#accessrules" title="AccessRules">AccessRules</a>" : <i>[ <a href="accessrulesdefinition.md">AccessRulesDefinition</a>, ... ]</i>,
    "<a href="#addressratelimiting" title="AddressRateLimiting">AddressRateLimiting</a>" : <i>[ <a href="addressratelimitingdefinition.md">AddressRateLimitingDefinition</a>, ... ]</i>,
    "<a href="#cachingrules" title="CachingRules">CachingRules</a>" : <i>[ <a href="cachingrulesdefinition.md">CachingRulesDefinition</a>, ... ]</i>,
    "<a href="#captchas" title="Captchas">Captchas</a>" : <i>[ <a href="captchasdefinition.md">CaptchasDefinition</a>, ... ]</i>,
    "<a href="#customprotectionrules" title="CustomProtectionRules">CustomProtectionRules</a>" : <i>[ <a href="customprotectionrulesdefinition.md">CustomProtectionRulesDefinition</a>, ... ]</i>,
    "<a href="#devicefingerprintchallenge" title="DeviceFingerprintChallenge">DeviceFingerprintChallenge</a>" : <i>[ <a href="devicefingerprintchallengedefinition.md">DeviceFingerprintChallengeDefinition</a>, ... ]</i>,
    "<a href="#humaninteractionchallenge" title="HumanInteractionChallenge">HumanInteractionChallenge</a>" : <i>[ <a href="humaninteractionchallengedefinition.md">HumanInteractionChallengeDefinition</a>, ... ]</i>,
    "<a href="#jschallenge" title="JsChallenge">JsChallenge</a>" : <i>[ <a href="jschallengedefinition.md">JsChallengeDefinition</a>, ... ]</i>,
    "<a href="#protectionsettings" title="ProtectionSettings">ProtectionSettings</a>" : <i>[ <a href="protectionsettingsdefinition.md">ProtectionSettingsDefinition</a>, ... ]</i>,
    "<a href="#whitelists" title="Whitelists">Whitelists</a>" : <i>[ <a href="whitelistsdefinition.md">WhitelistsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#origin" title="Origin">Origin</a>: <i>String</i>
<a href="#origingroups" title="OriginGroups">OriginGroups</a>: <i>
      - <a href="origingroupsdefinition.md">OriginGroupsDefinition</a></i>
<a href="#accessrules" title="AccessRules">AccessRules</a>: <i>
      - <a href="accessrulesdefinition.md">AccessRulesDefinition</a></i>
<a href="#addressratelimiting" title="AddressRateLimiting">AddressRateLimiting</a>: <i>
      - <a href="addressratelimitingdefinition.md">AddressRateLimitingDefinition</a></i>
<a href="#cachingrules" title="CachingRules">CachingRules</a>: <i>
      - <a href="cachingrulesdefinition.md">CachingRulesDefinition</a></i>
<a href="#captchas" title="Captchas">Captchas</a>: <i>
      - <a href="captchasdefinition.md">CaptchasDefinition</a></i>
<a href="#customprotectionrules" title="CustomProtectionRules">CustomProtectionRules</a>: <i>
      - <a href="customprotectionrulesdefinition.md">CustomProtectionRulesDefinition</a></i>
<a href="#devicefingerprintchallenge" title="DeviceFingerprintChallenge">DeviceFingerprintChallenge</a>: <i>
      - <a href="devicefingerprintchallengedefinition.md">DeviceFingerprintChallengeDefinition</a></i>
<a href="#humaninteractionchallenge" title="HumanInteractionChallenge">HumanInteractionChallenge</a>: <i>
      - <a href="humaninteractionchallengedefinition.md">HumanInteractionChallengeDefinition</a></i>
<a href="#jschallenge" title="JsChallenge">JsChallenge</a>: <i>
      - <a href="jschallengedefinition.md">JsChallengeDefinition</a></i>
<a href="#protectionsettings" title="ProtectionSettings">ProtectionSettings</a>: <i>
      - <a href="protectionsettingsdefinition.md">ProtectionSettingsDefinition</a></i>
<a href="#whitelists" title="Whitelists">Whitelists</a>: <i>
      - <a href="whitelistsdefinition.md">WhitelistsDefinition</a></i>
</pre>

## Properties

#### Origin

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginGroups

_Required_: No

_Type_: List of <a href="origingroupsdefinition.md">OriginGroupsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessRules

_Required_: No

_Type_: List of <a href="accessrulesdefinition.md">AccessRulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddressRateLimiting

_Required_: No

_Type_: List of <a href="addressratelimitingdefinition.md">AddressRateLimitingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CachingRules

_Required_: No

_Type_: List of <a href="cachingrulesdefinition.md">CachingRulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Captchas

_Required_: No

_Type_: List of <a href="captchasdefinition.md">CaptchasDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomProtectionRules

_Required_: No

_Type_: List of <a href="customprotectionrulesdefinition.md">CustomProtectionRulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceFingerprintChallenge

_Required_: No

_Type_: List of <a href="devicefingerprintchallengedefinition.md">DeviceFingerprintChallengeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HumanInteractionChallenge

_Required_: No

_Type_: List of <a href="humaninteractionchallengedefinition.md">HumanInteractionChallengeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JsChallenge

_Required_: No

_Type_: List of <a href="jschallengedefinition.md">JsChallengeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtectionSettings

_Required_: No

_Type_: List of <a href="protectionsettingsdefinition.md">ProtectionSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Whitelists

_Required_: No

_Type_: List of <a href="whitelistsdefinition.md">WhitelistsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

