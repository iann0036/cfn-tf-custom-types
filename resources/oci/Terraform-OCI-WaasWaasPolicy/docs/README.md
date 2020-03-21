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
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtags.md">DefinedTags</a>, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtags.md">FreeformTags</a>, ... ]</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#origingroups" title="OriginGroups">OriginGroups</a>" : <i>[ <a href="origingroups.md">OriginGroups</a>, ... ]</i>,
        "<a href="#origins" title="Origins">Origins</a>" : <i>[ <a href="origins.md">Origins</a>, ... ]</i>,
        "<a href="#policyconfig" title="PolicyConfig">PolicyConfig</a>" : <i>[ <a href="policyconfig.md">PolicyConfig</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#wafconfig" title="WafConfig">WafConfig</a>" : <i>[ <a href="wafconfig.md">WafConfig</a>, ... ]</i>,
        "<a href="#origingroup" title="OriginGroup">OriginGroup</a>" : <i>[ <a href="origingroup.md">OriginGroup</a>, ... ]</i>,
        "<a href="#customheaders" title="CustomHeaders">CustomHeaders</a>" : <i>[ <a href="customheaders.md">CustomHeaders</a>, ... ]</i>,
        "<a href="#accessrules" title="AccessRules">AccessRules</a>" : <i>[ <a href="accessrules.md">AccessRules</a>, ... ]</i>,
        "<a href="#addressratelimiting" title="AddressRateLimiting">AddressRateLimiting</a>" : <i>[ <a href="addressratelimiting.md">AddressRateLimiting</a>, ... ]</i>,
        "<a href="#cachingrules" title="CachingRules">CachingRules</a>" : <i>[ <a href="cachingrules.md">CachingRules</a>, ... ]</i>,
        "<a href="#captchas" title="Captchas">Captchas</a>" : <i>[ <a href="captchas.md">Captchas</a>, ... ]</i>,
        "<a href="#customprotectionrules" title="CustomProtectionRules">CustomProtectionRules</a>" : <i>[ <a href="customprotectionrules.md">CustomProtectionRules</a>, ... ]</i>,
        "<a href="#devicefingerprintchallenge" title="DeviceFingerprintChallenge">DeviceFingerprintChallenge</a>" : <i>[ <a href="devicefingerprintchallenge.md">DeviceFingerprintChallenge</a>, ... ]</i>,
        "<a href="#humaninteractionchallenge" title="HumanInteractionChallenge">HumanInteractionChallenge</a>" : <i>[ <a href="humaninteractionchallenge.md">HumanInteractionChallenge</a>, ... ]</i>,
        "<a href="#jschallenge" title="JsChallenge">JsChallenge</a>" : <i>[ <a href="jschallenge.md">JsChallenge</a>, ... ]</i>,
        "<a href="#protectionsettings" title="ProtectionSettings">ProtectionSettings</a>" : <i>[ <a href="protectionsettings.md">ProtectionSettings</a>, ... ]</i>,
        "<a href="#whitelists" title="Whitelists">Whitelists</a>" : <i>[ <a href="whitelists.md">Whitelists</a>, ... ]</i>,
        "<a href="#criteria" title="Criteria">Criteria</a>" : <i>[ <a href="criteria.md">Criteria</a>, ... ]</i>,
        "<a href="#challengesettings" title="ChallengeSettings">ChallengeSettings</a>" : <i>[ <a href="challengesettings.md">ChallengeSettings</a>, ... ]</i>,
        "<a href="#sethttpheader" title="SetHttpHeader">SetHttpHeader</a>" : <i>[ <a href="sethttpheader.md">SetHttpHeader</a>, ... ]</i>
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
      - <a href="definedtags.md">DefinedTags</a></i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtags.md">FreeformTags</a></i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#origingroups" title="OriginGroups">OriginGroups</a>: <i>
      - <a href="origingroups.md">OriginGroups</a></i>
    <a href="#origins" title="Origins">Origins</a>: <i>
      - <a href="origins.md">Origins</a></i>
    <a href="#policyconfig" title="PolicyConfig">PolicyConfig</a>: <i>
      - <a href="policyconfig.md">PolicyConfig</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#wafconfig" title="WafConfig">WafConfig</a>: <i>
      - <a href="wafconfig.md">WafConfig</a></i>
    <a href="#origingroup" title="OriginGroup">OriginGroup</a>: <i>
      - <a href="origingroup.md">OriginGroup</a></i>
    <a href="#customheaders" title="CustomHeaders">CustomHeaders</a>: <i>
      - <a href="customheaders.md">CustomHeaders</a></i>
    <a href="#accessrules" title="AccessRules">AccessRules</a>: <i>
      - <a href="accessrules.md">AccessRules</a></i>
    <a href="#addressratelimiting" title="AddressRateLimiting">AddressRateLimiting</a>: <i>
      - <a href="addressratelimiting.md">AddressRateLimiting</a></i>
    <a href="#cachingrules" title="CachingRules">CachingRules</a>: <i>
      - <a href="cachingrules.md">CachingRules</a></i>
    <a href="#captchas" title="Captchas">Captchas</a>: <i>
      - <a href="captchas.md">Captchas</a></i>
    <a href="#customprotectionrules" title="CustomProtectionRules">CustomProtectionRules</a>: <i>
      - <a href="customprotectionrules.md">CustomProtectionRules</a></i>
    <a href="#devicefingerprintchallenge" title="DeviceFingerprintChallenge">DeviceFingerprintChallenge</a>: <i>
      - <a href="devicefingerprintchallenge.md">DeviceFingerprintChallenge</a></i>
    <a href="#humaninteractionchallenge" title="HumanInteractionChallenge">HumanInteractionChallenge</a>: <i>
      - <a href="humaninteractionchallenge.md">HumanInteractionChallenge</a></i>
    <a href="#jschallenge" title="JsChallenge">JsChallenge</a>: <i>
      - <a href="jschallenge.md">JsChallenge</a></i>
    <a href="#protectionsettings" title="ProtectionSettings">ProtectionSettings</a>: <i>
      - <a href="protectionsettings.md">ProtectionSettings</a></i>
    <a href="#whitelists" title="Whitelists">Whitelists</a>: <i>
      - <a href="whitelists.md">Whitelists</a></i>
    <a href="#criteria" title="Criteria">Criteria</a>: <i>
      - <a href="criteria.md">Criteria</a></i>
    <a href="#challengesettings" title="ChallengeSettings">ChallengeSettings</a>: <i>
      - <a href="challengesettings.md">ChallengeSettings</a></i>
    <a href="#sethttpheader" title="SetHttpHeader">SetHttpHeader</a>: <i>
      - <a href="sethttpheader.md">SetHttpHeader</a></i>
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

_Type_: List of <a href="definedtags.md">DefinedTags</a>

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

_Type_: List of <a href="freeformtags.md">FreeformTags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginGroups

_Required_: No

_Type_: List of <a href="origingroups.md">OriginGroups</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Origins

_Required_: No

_Type_: List of <a href="origins.md">Origins</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyConfig

_Required_: No

_Type_: List of <a href="policyconfig.md">PolicyConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WafConfig

_Required_: No

_Type_: List of <a href="wafconfig.md">WafConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginGroup

_Required_: No

_Type_: List of <a href="origingroup.md">OriginGroup</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomHeaders

_Required_: No

_Type_: List of <a href="customheaders.md">CustomHeaders</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessRules

_Required_: No

_Type_: List of <a href="accessrules.md">AccessRules</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddressRateLimiting

_Required_: No

_Type_: List of <a href="addressratelimiting.md">AddressRateLimiting</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CachingRules

_Required_: No

_Type_: List of <a href="cachingrules.md">CachingRules</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Captchas

_Required_: No

_Type_: List of <a href="captchas.md">Captchas</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomProtectionRules

_Required_: No

_Type_: List of <a href="customprotectionrules.md">CustomProtectionRules</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceFingerprintChallenge

_Required_: No

_Type_: List of <a href="devicefingerprintchallenge.md">DeviceFingerprintChallenge</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HumanInteractionChallenge

_Required_: No

_Type_: List of <a href="humaninteractionchallenge.md">HumanInteractionChallenge</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JsChallenge

_Required_: No

_Type_: List of <a href="jschallenge.md">JsChallenge</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtectionSettings

_Required_: No

_Type_: List of <a href="protectionsettings.md">ProtectionSettings</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Whitelists

_Required_: No

_Type_: List of <a href="whitelists.md">Whitelists</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Criteria

_Required_: No

_Type_: List of <a href="criteria.md">Criteria</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChallengeSettings

_Required_: No

_Type_: List of <a href="challengesettings.md">ChallengeSettings</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetHttpHeader

_Required_: No

_Type_: List of <a href="sethttpheader.md">SetHttpHeader</a>

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

Returns the <code>Cname</code> value.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

