# Terraform::OCI::WaasWaasPolicy

CloudFormation equivalent of oci_waas_waas_policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::WaasWaasPolicy",
    "Properties" : {
        "<a href="#additionaldomains" title="AdditionalDomains">AdditionalDomains</a>" : <i>[ String, ... ]</i>,
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ &lt;a href=&#34;definedtags.md&#34;&gt;DefinedTags&lt;/a&gt;, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ &lt;a href=&#34;freeformtags.md&#34;&gt;FreeformTags&lt;/a&gt;, ... ]</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#origingroups" title="OriginGroups">OriginGroups</a>" : <i>[ &lt;a href=&#34;origingroups.md&#34;&gt;OriginGroups&lt;/a&gt;, ... ]</i>,
        "<a href="#origins" title="Origins">Origins</a>" : <i>[ &lt;a href=&#34;origins.md&#34;&gt;Origins&lt;/a&gt;, ... ]</i>,
        "<a href="#policyconfig" title="PolicyConfig">PolicyConfig</a>" : <i>[ &lt;a href=&#34;policyconfig.md&#34;&gt;PolicyConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#wafconfig" title="WafConfig">WafConfig</a>" : <i>[ &lt;a href=&#34;wafconfig.md&#34;&gt;WafConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#origingroup" title="OriginGroup">OriginGroup</a>" : <i>[ &lt;a href=&#34;origingroup.md&#34;&gt;OriginGroup&lt;/a&gt;, ... ]</i>,
        "<a href="#customheaders" title="CustomHeaders">CustomHeaders</a>" : <i>[ &lt;a href=&#34;customheaders.md&#34;&gt;CustomHeaders&lt;/a&gt;, ... ]</i>,
        "<a href="#accessrules" title="AccessRules">AccessRules</a>" : <i>[ &lt;a href=&#34;accessrules.md&#34;&gt;AccessRules&lt;/a&gt;, ... ]</i>,
        "<a href="#addressratelimiting" title="AddressRateLimiting">AddressRateLimiting</a>" : <i>[ &lt;a href=&#34;addressratelimiting.md&#34;&gt;AddressRateLimiting&lt;/a&gt;, ... ]</i>,
        "<a href="#cachingrules" title="CachingRules">CachingRules</a>" : <i>[ &lt;a href=&#34;cachingrules.md&#34;&gt;CachingRules&lt;/a&gt;, ... ]</i>,
        "<a href="#captchas" title="Captchas">Captchas</a>" : <i>[ &lt;a href=&#34;captchas.md&#34;&gt;Captchas&lt;/a&gt;, ... ]</i>,
        "<a href="#customprotectionrules" title="CustomProtectionRules">CustomProtectionRules</a>" : <i>[ &lt;a href=&#34;customprotectionrules.md&#34;&gt;CustomProtectionRules&lt;/a&gt;, ... ]</i>,
        "<a href="#devicefingerprintchallenge" title="DeviceFingerprintChallenge">DeviceFingerprintChallenge</a>" : <i>[ &lt;a href=&#34;devicefingerprintchallenge.md&#34;&gt;DeviceFingerprintChallenge&lt;/a&gt;, ... ]</i>,
        "<a href="#humaninteractionchallenge" title="HumanInteractionChallenge">HumanInteractionChallenge</a>" : <i>[ &lt;a href=&#34;humaninteractionchallenge.md&#34;&gt;HumanInteractionChallenge&lt;/a&gt;, ... ]</i>,
        "<a href="#jschallenge" title="JsChallenge">JsChallenge</a>" : <i>[ &lt;a href=&#34;jschallenge.md&#34;&gt;JsChallenge&lt;/a&gt;, ... ]</i>,
        "<a href="#protectionsettings" title="ProtectionSettings">ProtectionSettings</a>" : <i>[ &lt;a href=&#34;protectionsettings.md&#34;&gt;ProtectionSettings&lt;/a&gt;, ... ]</i>,
        "<a href="#whitelists" title="Whitelists">Whitelists</a>" : <i>[ &lt;a href=&#34;whitelists.md&#34;&gt;Whitelists&lt;/a&gt;, ... ]</i>,
        "<a href="#criteria" title="Criteria">Criteria</a>" : <i>[ &lt;a href=&#34;criteria.md&#34;&gt;Criteria&lt;/a&gt;, ... ]</i>,
        "<a href="#challengesettings" title="ChallengeSettings">ChallengeSettings</a>" : <i>[ &lt;a href=&#34;challengesettings.md&#34;&gt;ChallengeSettings&lt;/a&gt;, ... ]</i>,
        "<a href="#sethttpheader" title="SetHttpHeader">SetHttpHeader</a>" : <i>[ &lt;a href=&#34;sethttpheader.md&#34;&gt;SetHttpHeader&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::WaasWaasPolicy
Properties:
    <a href="#additionaldomains" title="AdditionalDomains">AdditionalDomains</a>: <i>
      - String</i>
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - &lt;a href=&#34;definedtags.md&#34;&gt;DefinedTags&lt;/a&gt;</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - &lt;a href=&#34;freeformtags.md&#34;&gt;FreeformTags&lt;/a&gt;</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#origingroups" title="OriginGroups">OriginGroups</a>: <i>
      - &lt;a href=&#34;origingroups.md&#34;&gt;OriginGroups&lt;/a&gt;</i>
    <a href="#origins" title="Origins">Origins</a>: <i>
      - &lt;a href=&#34;origins.md&#34;&gt;Origins&lt;/a&gt;</i>
    <a href="#policyconfig" title="PolicyConfig">PolicyConfig</a>: <i>
      - &lt;a href=&#34;policyconfig.md&#34;&gt;PolicyConfig&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#wafconfig" title="WafConfig">WafConfig</a>: <i>
      - &lt;a href=&#34;wafconfig.md&#34;&gt;WafConfig&lt;/a&gt;</i>
    <a href="#origingroup" title="OriginGroup">OriginGroup</a>: <i>
      - &lt;a href=&#34;origingroup.md&#34;&gt;OriginGroup&lt;/a&gt;</i>
    <a href="#customheaders" title="CustomHeaders">CustomHeaders</a>: <i>
      - &lt;a href=&#34;customheaders.md&#34;&gt;CustomHeaders&lt;/a&gt;</i>
    <a href="#accessrules" title="AccessRules">AccessRules</a>: <i>
      - &lt;a href=&#34;accessrules.md&#34;&gt;AccessRules&lt;/a&gt;</i>
    <a href="#addressratelimiting" title="AddressRateLimiting">AddressRateLimiting</a>: <i>
      - &lt;a href=&#34;addressratelimiting.md&#34;&gt;AddressRateLimiting&lt;/a&gt;</i>
    <a href="#cachingrules" title="CachingRules">CachingRules</a>: <i>
      - &lt;a href=&#34;cachingrules.md&#34;&gt;CachingRules&lt;/a&gt;</i>
    <a href="#captchas" title="Captchas">Captchas</a>: <i>
      - &lt;a href=&#34;captchas.md&#34;&gt;Captchas&lt;/a&gt;</i>
    <a href="#customprotectionrules" title="CustomProtectionRules">CustomProtectionRules</a>: <i>
      - &lt;a href=&#34;customprotectionrules.md&#34;&gt;CustomProtectionRules&lt;/a&gt;</i>
    <a href="#devicefingerprintchallenge" title="DeviceFingerprintChallenge">DeviceFingerprintChallenge</a>: <i>
      - &lt;a href=&#34;devicefingerprintchallenge.md&#34;&gt;DeviceFingerprintChallenge&lt;/a&gt;</i>
    <a href="#humaninteractionchallenge" title="HumanInteractionChallenge">HumanInteractionChallenge</a>: <i>
      - &lt;a href=&#34;humaninteractionchallenge.md&#34;&gt;HumanInteractionChallenge&lt;/a&gt;</i>
    <a href="#jschallenge" title="JsChallenge">JsChallenge</a>: <i>
      - &lt;a href=&#34;jschallenge.md&#34;&gt;JsChallenge&lt;/a&gt;</i>
    <a href="#protectionsettings" title="ProtectionSettings">ProtectionSettings</a>: <i>
      - &lt;a href=&#34;protectionsettings.md&#34;&gt;ProtectionSettings&lt;/a&gt;</i>
    <a href="#whitelists" title="Whitelists">Whitelists</a>: <i>
      - &lt;a href=&#34;whitelists.md&#34;&gt;Whitelists&lt;/a&gt;</i>
    <a href="#criteria" title="Criteria">Criteria</a>: <i>
      - &lt;a href=&#34;criteria.md&#34;&gt;Criteria&lt;/a&gt;</i>
    <a href="#challengesettings" title="ChallengeSettings">ChallengeSettings</a>: <i>
      - &lt;a href=&#34;challengesettings.md&#34;&gt;ChallengeSettings&lt;/a&gt;</i>
    <a href="#sethttpheader" title="SetHttpHeader">SetHttpHeader</a>: <i>
      - &lt;a href=&#34;sethttpheader.md&#34;&gt;SetHttpHeader&lt;/a&gt;</i>
</pre>

## Properties

#### AdditionalDomains

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompartmentId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

_Required_: No

_Type_: List of &lt;a href=&#34;definedtags.md&#34;&gt;DefinedTags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

_Required_: No

_Type_: List of &lt;a href=&#34;freeformtags.md&#34;&gt;FreeformTags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginGroups

_Required_: No

_Type_: List of &lt;a href=&#34;origingroups.md&#34;&gt;OriginGroups&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Origins

_Required_: No

_Type_: List of &lt;a href=&#34;origins.md&#34;&gt;Origins&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyConfig

_Required_: No

_Type_: List of &lt;a href=&#34;policyconfig.md&#34;&gt;PolicyConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WafConfig

_Required_: No

_Type_: List of &lt;a href=&#34;wafconfig.md&#34;&gt;WafConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginGroup

_Required_: No

_Type_: List of &lt;a href=&#34;origingroup.md&#34;&gt;OriginGroup&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomHeaders

_Required_: No

_Type_: List of &lt;a href=&#34;customheaders.md&#34;&gt;CustomHeaders&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessRules

_Required_: No

_Type_: List of &lt;a href=&#34;accessrules.md&#34;&gt;AccessRules&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddressRateLimiting

_Required_: No

_Type_: List of &lt;a href=&#34;addressratelimiting.md&#34;&gt;AddressRateLimiting&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CachingRules

_Required_: No

_Type_: List of &lt;a href=&#34;cachingrules.md&#34;&gt;CachingRules&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Captchas

_Required_: No

_Type_: List of &lt;a href=&#34;captchas.md&#34;&gt;Captchas&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomProtectionRules

_Required_: No

_Type_: List of &lt;a href=&#34;customprotectionrules.md&#34;&gt;CustomProtectionRules&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceFingerprintChallenge

_Required_: No

_Type_: List of &lt;a href=&#34;devicefingerprintchallenge.md&#34;&gt;DeviceFingerprintChallenge&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HumanInteractionChallenge

_Required_: No

_Type_: List of &lt;a href=&#34;humaninteractionchallenge.md&#34;&gt;HumanInteractionChallenge&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JsChallenge

_Required_: No

_Type_: List of &lt;a href=&#34;jschallenge.md&#34;&gt;JsChallenge&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtectionSettings

_Required_: No

_Type_: List of &lt;a href=&#34;protectionsettings.md&#34;&gt;ProtectionSettings&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Whitelists

_Required_: No

_Type_: List of &lt;a href=&#34;whitelists.md&#34;&gt;Whitelists&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Criteria

_Required_: No

_Type_: List of &lt;a href=&#34;criteria.md&#34;&gt;Criteria&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChallengeSettings

_Required_: No

_Type_: List of &lt;a href=&#34;challengesettings.md&#34;&gt;ChallengeSettings&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetHttpHeader

_Required_: No

_Type_: List of &lt;a href=&#34;sethttpheader.md&#34;&gt;SetHttpHeader&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Cname

Returns the &lt;code&gt;Cname&lt;/code&gt; value.

#### State

Returns the &lt;code&gt;State&lt;/code&gt; value.

#### TimeCreated

Returns the &lt;code&gt;TimeCreated&lt;/code&gt; value.

