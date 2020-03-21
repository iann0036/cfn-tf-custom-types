# Terraform::OCI::WaasWaasPolicy

This resource provides the Waas Policy resource in Oracle Cloud Infrastructure Web Application Acceleration and Security service.

Creates a new Web Application Acceleration and Security (WAAS) policy in the specified compartment. A WAAS policy must be established before creating Web Application Firewall (WAF) rules. To use WAF rules, your web application's origin servers must defined in the `WaasPolicy` schema.

A domain name must be specified when creating a WAAS policy. The domain name should be different from the origins specified in your `WaasPolicy`. Once domain name is entered and stored, it is unchangeable.

Use the record data returned in the `cname` field of the `WaasPolicy` object to create a CNAME record in your DNS configuration that will direct your domain's traffic through the WAF.

For the purposes of access control, you must provide the OCID of the compartment where you want the service to reside. For information about access control and compartments, see [Overview of the IAM Service](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm).

You must specify a display name and domain for the WAAS policy. The display name does not have to be unique and can be changed. The domain name should be different from every origin specified in `WaasPolicy`.

All Oracle Cloud Infrastructure resources, including WAAS policies, receive a unique, Oracle-assigned ID called an Oracle Cloud Identifier (OCID). When a resource is created, you can find its OCID in the response. You can also retrieve a resource's OCID by using a list API operation for that resource type, or by viewing the resource in the Console. Fore more information, see [Resource Identifiers](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

**Note:** After sending the POST request, the new object's state will temporarily be `CREATING`. Ensure that the resource's state has changed to `ACTIVE` before use.

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

(Updatable) An array of additional domains for the specified web application.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompartmentId

(Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment in which to create the WAAS policy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

(Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

_Required_: No

_Type_: List of <a href="definedtags.md">DefinedTags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

(Updatable) A user-friendly name for the WAAS policy. The name can be changed and does not need to be unique.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

The web application domain that the WAAS policy protects.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

(Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

_Required_: No

_Type_: List of <a href="freeformtags.md">FreeformTags</a>

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

