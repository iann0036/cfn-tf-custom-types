# Terraform::OCI::WaasWaasPolicy WafConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#origin" title="Origin">Origin</a>" : <i>String</i>,
    "<a href="#origingroups" title="OriginGroups">OriginGroups</a>" : <i>[ String, ... ]</i>,
    "<a href="#accessrules" title="AccessRules">AccessRules</a>" : <i>[ &lt;a href=&#34;wafconfig-accessrules.md&#34;&gt;AccessRules&lt;/a&gt;, ... ]</i>,
    "<a href="#addressratelimiting" title="AddressRateLimiting">AddressRateLimiting</a>" : <i>[ &lt;a href=&#34;wafconfig-addressratelimiting.md&#34;&gt;AddressRateLimiting&lt;/a&gt;, ... ]</i>,
    "<a href="#cachingrules" title="CachingRules">CachingRules</a>" : <i>[ &lt;a href=&#34;wafconfig-cachingrules.md&#34;&gt;CachingRules&lt;/a&gt;, ... ]</i>,
    "<a href="#captchas" title="Captchas">Captchas</a>" : <i>[ &lt;a href=&#34;wafconfig-captchas.md&#34;&gt;Captchas&lt;/a&gt;, ... ]</i>,
    "<a href="#customprotectionrules" title="CustomProtectionRules">CustomProtectionRules</a>" : <i>[ &lt;a href=&#34;wafconfig-customprotectionrules.md&#34;&gt;CustomProtectionRules&lt;/a&gt;, ... ]</i>,
    "<a href="#devicefingerprintchallenge" title="DeviceFingerprintChallenge">DeviceFingerprintChallenge</a>" : <i>[ &lt;a href=&#34;wafconfig-devicefingerprintchallenge.md&#34;&gt;DeviceFingerprintChallenge&lt;/a&gt;, ... ]</i>,
    "<a href="#humaninteractionchallenge" title="HumanInteractionChallenge">HumanInteractionChallenge</a>" : <i>[ &lt;a href=&#34;wafconfig-humaninteractionchallenge.md&#34;&gt;HumanInteractionChallenge&lt;/a&gt;, ... ]</i>,
    "<a href="#jschallenge" title="JsChallenge">JsChallenge</a>" : <i>[ &lt;a href=&#34;wafconfig-jschallenge.md&#34;&gt;JsChallenge&lt;/a&gt;, ... ]</i>,
    "<a href="#protectionsettings" title="ProtectionSettings">ProtectionSettings</a>" : <i>[ &lt;a href=&#34;wafconfig-protectionsettings.md&#34;&gt;ProtectionSettings&lt;/a&gt;, ... ]</i>,
    "<a href="#whitelists" title="Whitelists">Whitelists</a>" : <i>[ &lt;a href=&#34;wafconfig-whitelists.md&#34;&gt;Whitelists&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#origin" title="Origin">Origin</a>: <i>String</i>
<a href="#origingroups" title="OriginGroups">OriginGroups</a>: <i>
      - String</i>
<a href="#accessrules" title="AccessRules">AccessRules</a>: <i>
      - &lt;a href=&#34;wafconfig-accessrules.md&#34;&gt;AccessRules&lt;/a&gt;</i>
<a href="#addressratelimiting" title="AddressRateLimiting">AddressRateLimiting</a>: <i>
      - &lt;a href=&#34;wafconfig-addressratelimiting.md&#34;&gt;AddressRateLimiting&lt;/a&gt;</i>
<a href="#cachingrules" title="CachingRules">CachingRules</a>: <i>
      - &lt;a href=&#34;wafconfig-cachingrules.md&#34;&gt;CachingRules&lt;/a&gt;</i>
<a href="#captchas" title="Captchas">Captchas</a>: <i>
      - &lt;a href=&#34;wafconfig-captchas.md&#34;&gt;Captchas&lt;/a&gt;</i>
<a href="#customprotectionrules" title="CustomProtectionRules">CustomProtectionRules</a>: <i>
      - &lt;a href=&#34;wafconfig-customprotectionrules.md&#34;&gt;CustomProtectionRules&lt;/a&gt;</i>
<a href="#devicefingerprintchallenge" title="DeviceFingerprintChallenge">DeviceFingerprintChallenge</a>: <i>
      - &lt;a href=&#34;wafconfig-devicefingerprintchallenge.md&#34;&gt;DeviceFingerprintChallenge&lt;/a&gt;</i>
<a href="#humaninteractionchallenge" title="HumanInteractionChallenge">HumanInteractionChallenge</a>: <i>
      - &lt;a href=&#34;wafconfig-humaninteractionchallenge.md&#34;&gt;HumanInteractionChallenge&lt;/a&gt;</i>
<a href="#jschallenge" title="JsChallenge">JsChallenge</a>: <i>
      - &lt;a href=&#34;wafconfig-jschallenge.md&#34;&gt;JsChallenge&lt;/a&gt;</i>
<a href="#protectionsettings" title="ProtectionSettings">ProtectionSettings</a>: <i>
      - &lt;a href=&#34;wafconfig-protectionsettings.md&#34;&gt;ProtectionSettings&lt;/a&gt;</i>
<a href="#whitelists" title="Whitelists">Whitelists</a>: <i>
      - &lt;a href=&#34;wafconfig-whitelists.md&#34;&gt;Whitelists&lt;/a&gt;</i>
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
_Type_: List of &lt;a href=&#34;wafconfig-accessrules.md&#34;&gt;AccessRules&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddressRateLimiting

_Required_: No
_Type_: List of &lt;a href=&#34;wafconfig-addressratelimiting.md&#34;&gt;AddressRateLimiting&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CachingRules

_Required_: No
_Type_: List of &lt;a href=&#34;wafconfig-cachingrules.md&#34;&gt;CachingRules&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Captchas

_Required_: No
_Type_: List of &lt;a href=&#34;wafconfig-captchas.md&#34;&gt;Captchas&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomProtectionRules

_Required_: No
_Type_: List of &lt;a href=&#34;wafconfig-customprotectionrules.md&#34;&gt;CustomProtectionRules&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceFingerprintChallenge

_Required_: No
_Type_: List of &lt;a href=&#34;wafconfig-devicefingerprintchallenge.md&#34;&gt;DeviceFingerprintChallenge&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HumanInteractionChallenge

_Required_: No
_Type_: List of &lt;a href=&#34;wafconfig-humaninteractionchallenge.md&#34;&gt;HumanInteractionChallenge&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JsChallenge

_Required_: No
_Type_: List of &lt;a href=&#34;wafconfig-jschallenge.md&#34;&gt;JsChallenge&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtectionSettings

_Required_: No
_Type_: List of &lt;a href=&#34;wafconfig-protectionsettings.md&#34;&gt;ProtectionSettings&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Whitelists

_Required_: No
_Type_: List of &lt;a href=&#34;wafconfig-whitelists.md&#34;&gt;Whitelists&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

