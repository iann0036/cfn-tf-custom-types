# Terraform::OCI::WaasWaasPolicy WafConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#origin" title="Origin">Origin</a>" : <i>String</i>,
    "<a href="#origingroups" title="OriginGroups">OriginGroups</a>" : <i>[ String, ... ]</i>,
    "<a href="#accessrules" title="AccessRules">AccessRules</a>" : <i>[ <a href="wafconfig-accessrules.md">AccessRules</a>, ... ]</i>,
    "<a href="#addressratelimiting" title="AddressRateLimiting">AddressRateLimiting</a>" : <i>[ <a href="wafconfig-addressratelimiting.md">AddressRateLimiting</a>, ... ]</i>,
    "<a href="#cachingrules" title="CachingRules">CachingRules</a>" : <i>[ <a href="wafconfig-cachingrules.md">CachingRules</a>, ... ]</i>,
    "<a href="#captchas" title="Captchas">Captchas</a>" : <i>[ <a href="wafconfig-captchas.md">Captchas</a>, ... ]</i>,
    "<a href="#customprotectionrules" title="CustomProtectionRules">CustomProtectionRules</a>" : <i>[ <a href="wafconfig-customprotectionrules.md">CustomProtectionRules</a>, ... ]</i>,
    "<a href="#devicefingerprintchallenge" title="DeviceFingerprintChallenge">DeviceFingerprintChallenge</a>" : <i>[ <a href="wafconfig-devicefingerprintchallenge.md">DeviceFingerprintChallenge</a>, ... ]</i>,
    "<a href="#humaninteractionchallenge" title="HumanInteractionChallenge">HumanInteractionChallenge</a>" : <i>[ <a href="wafconfig-humaninteractionchallenge.md">HumanInteractionChallenge</a>, ... ]</i>,
    "<a href="#jschallenge" title="JsChallenge">JsChallenge</a>" : <i>[ <a href="wafconfig-jschallenge.md">JsChallenge</a>, ... ]</i>,
    "<a href="#protectionsettings" title="ProtectionSettings">ProtectionSettings</a>" : <i>[ <a href="wafconfig-protectionsettings.md">ProtectionSettings</a>, ... ]</i>,
    "<a href="#whitelists" title="Whitelists">Whitelists</a>" : <i>[ <a href="wafconfig-whitelists.md">Whitelists</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#origin" title="Origin">Origin</a>: <i>String</i>
<a href="#origingroups" title="OriginGroups">OriginGroups</a>: <i>
      - String</i>
<a href="#accessrules" title="AccessRules">AccessRules</a>: <i>
      - <a href="wafconfig-accessrules.md">AccessRules</a></i>
<a href="#addressratelimiting" title="AddressRateLimiting">AddressRateLimiting</a>: <i>
      - <a href="wafconfig-addressratelimiting.md">AddressRateLimiting</a></i>
<a href="#cachingrules" title="CachingRules">CachingRules</a>: <i>
      - <a href="wafconfig-cachingrules.md">CachingRules</a></i>
<a href="#captchas" title="Captchas">Captchas</a>: <i>
      - <a href="wafconfig-captchas.md">Captchas</a></i>
<a href="#customprotectionrules" title="CustomProtectionRules">CustomProtectionRules</a>: <i>
      - <a href="wafconfig-customprotectionrules.md">CustomProtectionRules</a></i>
<a href="#devicefingerprintchallenge" title="DeviceFingerprintChallenge">DeviceFingerprintChallenge</a>: <i>
      - <a href="wafconfig-devicefingerprintchallenge.md">DeviceFingerprintChallenge</a></i>
<a href="#humaninteractionchallenge" title="HumanInteractionChallenge">HumanInteractionChallenge</a>: <i>
      - <a href="wafconfig-humaninteractionchallenge.md">HumanInteractionChallenge</a></i>
<a href="#jschallenge" title="JsChallenge">JsChallenge</a>: <i>
      - <a href="wafconfig-jschallenge.md">JsChallenge</a></i>
<a href="#protectionsettings" title="ProtectionSettings">ProtectionSettings</a>: <i>
      - <a href="wafconfig-protectionsettings.md">ProtectionSettings</a></i>
<a href="#whitelists" title="Whitelists">Whitelists</a>: <i>
      - <a href="wafconfig-whitelists.md">Whitelists</a></i>
</pre>

## Properties

#### Origin

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginGroups

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessRules

_Required_: No

_Type_: List of <a href="wafconfig-accessrules.md">AccessRules</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddressRateLimiting

_Required_: No

_Type_: List of <a href="wafconfig-addressratelimiting.md">AddressRateLimiting</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CachingRules

_Required_: No

_Type_: List of <a href="wafconfig-cachingrules.md">CachingRules</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Captchas

_Required_: No

_Type_: List of <a href="wafconfig-captchas.md">Captchas</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomProtectionRules

_Required_: No

_Type_: List of <a href="wafconfig-customprotectionrules.md">CustomProtectionRules</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceFingerprintChallenge

_Required_: No

_Type_: List of <a href="wafconfig-devicefingerprintchallenge.md">DeviceFingerprintChallenge</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HumanInteractionChallenge

_Required_: No

_Type_: List of <a href="wafconfig-humaninteractionchallenge.md">HumanInteractionChallenge</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JsChallenge

_Required_: No

_Type_: List of <a href="wafconfig-jschallenge.md">JsChallenge</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtectionSettings

_Required_: No

_Type_: List of <a href="wafconfig-protectionsettings.md">ProtectionSettings</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Whitelists

_Required_: No

_Type_: List of <a href="wafconfig-whitelists.md">Whitelists</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

