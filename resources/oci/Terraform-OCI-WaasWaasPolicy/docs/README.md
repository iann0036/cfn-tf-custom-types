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

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Cname

Returns the <code>Cname</code> value.

#### Id

(Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the custom protection rule.
* `device_fingerprint_challenge` - (Optional) (Updatable) The device fingerprint challenge settings. Blocks bots based on unique device fingerprint information.
* `action` - (Optional) (Updatable) The action to take on requests from detected bots. If unspecified, defaults to `DETECT`.
* `action_expiration_in_seconds` - (Optional) (Updatable) The number of seconds between challenges for the same IP address. If unspecified, defaults to `60`.
* `challenge_settings` - (Optional) (Updatable)
* `block_action` - (Optional) (Updatable) The method used to block requests that fail the challenge, if `action` is set to `BLOCK`. If unspecified, defaults to `SHOW_ERROR_PAGE`.
* `block_error_page_code` - (Optional) (Updatable) The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE` and the request is blocked. If unspecified, defaults to `403`.
* `block_error_page_description` - (Optional) (Updatable) The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `Access blocked by website owner. Please contact support.`
* `block_error_page_message` - (Optional) (Updatable) The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `Access to the website is blocked`.
* `block_response_code` - (Optional) (Updatable) The response status code to return when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE` or `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `403`. The list of available response codes: `200`, `201`, `202`, `204`, `206`, `300`, `301`, `302`, `303`, `304`, `307`, `400`, `401`, `403`, `404`, `405`, `408`, `409`, `411`, `412`, `413`, `414`, `415`, `416`, `422`, `444`, `499`, `500`, `501`, `502`, `503`, `504`, `507`.
* `captcha_footer` - (Optional) (Updatable) The text to show in the footer when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, default to `Enter the letters and numbers as they are shown in image above`.
* `captcha_header` - (Optional) (Updatable) The text to show in the header when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `We have detected an increased number of attempts to access this webapp. To help us keep this webapp secure, please let us know that you are not a robot by entering the text from captcha below.`
* `captcha_submit_label` - (Optional) (Updatable) The text to show on the label of the CAPTCHA challenge submit button when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Yes, I am human`.
* `captcha_title` - (Optional) (Updatable) The title used when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Are you human?`
* `failure_threshold` - (Optional) (Updatable) The number of failed requests allowed before taking action. If unspecified, defaults to `10`.
* `failure_threshold_expiration_in_seconds` - (Optional) (Updatable) The number of seconds before the failure threshold resets. If unspecified, defaults to `60`.
* `is_enabled` - (Required) (Updatable) Enables or disables the device fingerprint challenge Web Application Firewall feature.
* `max_address_count` - (Optional) (Updatable) The maximum number of IP addresses permitted with the same device fingerprint. If unspecified, defaults to `20`.
* `max_address_count_expiration_in_seconds` - (Optional) (Updatable) The number of seconds before the maximum addresses count resets. If unspecified, defaults to `60`.
* `human_interaction_challenge` - (Optional) (Updatable) The human interaction challenge settings. Detects natural human interactions such as mouse movements, time on site, and page scrolling to identify bots.
* `action` - (Optional) (Updatable) The action to take against requests from detected bots. If unspecified, defaults to `DETECT`.
* `action_expiration_in_seconds` - (Optional) (Updatable) The number of seconds between challenges for the same IP address. If unspecified, defaults to `60`.
* `challenge_settings` - (Optional) (Updatable)
* `block_action` - (Optional) (Updatable) The method used to block requests that fail the challenge, if `action` is set to `BLOCK`. If unspecified, defaults to `SHOW_ERROR_PAGE`.
* `block_error_page_code` - (Optional) (Updatable) The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE` and the request is blocked. If unspecified, defaults to `403`.
* `block_error_page_description` - (Optional) (Updatable) The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `Access blocked by website owner. Please contact support.`
* `block_error_page_message` - (Optional) (Updatable) The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `Access to the website is blocked`.
* `block_response_code` - (Optional) (Updatable) The response status code to return when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE` or `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `403`. The list of available response codes: `200`, `201`, `202`, `204`, `206`, `300`, `301`, `302`, `303`, `304`, `307`, `400`, `401`, `403`, `404`, `405`, `408`, `409`, `411`, `412`, `413`, `414`, `415`, `416`, `422`, `444`, `499`, `500`, `501`, `502`, `503`, `504`, `507`.
* `captcha_footer` - (Optional) (Updatable) The text to show in the footer when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, default to `Enter the letters and numbers as they are shown in image above`.
* `captcha_header` - (Optional) (Updatable) The text to show in the header when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `We have detected an increased number of attempts to access this webapp. To help us keep this webapp secure, please let us know that you are not a robot by entering the text from captcha below.`
* `captcha_submit_label` - (Optional) (Updatable) The text to show on the label of the CAPTCHA challenge submit button when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Yes, I am human`.
* `captcha_title` - (Optional) (Updatable) The title used when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Are you human?`
* `failure_threshold` - (Optional) (Updatable) The number of failed requests before taking action. If unspecified, defaults to `10`.
* `failure_threshold_expiration_in_seconds` - (Optional) (Updatable) The number of seconds before the failure threshold resets. If unspecified, defaults to  `60`.
* `interaction_threshold` - (Optional) (Updatable) The number of interactions required to pass the challenge. If unspecified, defaults to `3`.
* `is_enabled` - (Required) (Updatable) Enables or disables the human interaction challenge Web Application Firewall feature.
* `recording_period_in_seconds` - (Optional) (Updatable) The number of seconds to record the interactions from the user. If unspecified, defaults to `15`.
* `set_http_header` - (Optional) (Updatable) Adds an additional HTTP header to requests that fail the challenge before being passed to the origin. Only applicable when the `action` is set to `DETECT`.
* `name` - (Required) (Updatable) The name of the header.
* `value` - (Required) (Updatable) The value of the header.
* `js_challenge` - (Optional) (Updatable) The JavaScript challenge settings. Blocks bots by challenging requests from browsers that have no JavaScript support.
* `action` - (Optional) (Updatable) The action to take against requests from detected bots. If unspecified, defaults to `DETECT`.
* `action_expiration_in_seconds` - (Optional) (Updatable) The number of seconds between challenges from the same IP address. If unspecified, defaults to `60`.
* `challenge_settings` - (Optional) (Updatable)
* `block_action` - (Optional) (Updatable) The method used to block requests that fail the challenge, if `action` is set to `BLOCK`. If unspecified, defaults to `SHOW_ERROR_PAGE`.
* `block_error_page_code` - (Optional) (Updatable) The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE` and the request is blocked. If unspecified, defaults to `403`.
* `block_error_page_description` - (Optional) (Updatable) The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `Access blocked by website owner. Please contact support.`
* `block_error_page_message` - (Optional) (Updatable) The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `Access to the website is blocked`.
* `block_response_code` - (Optional) (Updatable) The response status code to return when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE` or `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `403`. The list of available response codes: `200`, `201`, `202`, `204`, `206`, `300`, `301`, `302`, `303`, `304`, `307`, `400`, `401`, `403`, `404`, `405`, `408`, `409`, `411`, `412`, `413`, `414`, `415`, `416`, `422`, `444`, `499`, `500`, `501`, `502`, `503`, `504`, `507`.
* `captcha_footer` - (Optional) (Updatable) The text to show in the footer when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, default to `Enter the letters and numbers as they are shown in image above`.
* `captcha_header` - (Optional) (Updatable) The text to show in the header when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `We have detected an increased number of attempts to access this webapp. To help us keep this webapp secure, please let us know that you are not a robot by entering the text from captcha below.`
* `captcha_submit_label` - (Optional) (Updatable) The text to show on the label of the CAPTCHA challenge submit button when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Yes, I am human`.
* `captcha_title` - (Optional) (Updatable) The title used when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Are you human?`
* `failure_threshold` - (Optional) (Updatable) The number of failed requests before taking action. If unspecified, defaults to `10`.
* `is_enabled` - (Required) (Updatable) Enables or disables the JavaScript challenge Web Application Firewall feature.
* `set_http_header` - (Optional) (Updatable) Adds an additional HTTP header to requests that fail the challenge before being passed to the origin. Only applicable when the `action` is set to `DETECT`.
* `name` - (Required) (Updatable) The name of the header.
* `value` - (Required) (Updatable) The value of the header.
* `origin` - (Optional) (Updatable) The key in the map of origins referencing the origin used for the Web Application Firewall. The origin must already be included in `Origins`. Required when creating the `WafConfig` resource, but is not required upon updating the configuration.
* `origin_groups` - (Optional) (Updatable) The map of origin groups and their keys used to associate origins to the `wafConfig`. Origin groups allow you to apply weights to groups of origins for load balancing purposes. Origins with higher weights will receive larger proportions of client requests. To add additional origins to your WAAS policy, update the `origins` field of a `UpdateWaasPolicy` request.
* `protection_settings` - (Optional) (Updatable) The settings applied to protection rules.
* `allowed_http_methods` - (Optional) (Updatable) The list of allowed HTTP methods. If unspecified, default to `[OPTIONS, GET, HEAD, POST]`. This setting only applies if a corresponding protection rule is enabled, such as the "Restrict HTTP Request Methods" rule (key: 911100).
* `block_action` - (Optional) (Updatable) If `action` is set to `BLOCK`, this specifies how the traffic is blocked when detected as malicious by a protection rule. If unspecified, defaults to `SET_RESPONSE_CODE`.
* `block_error_page_code` - (Optional) (Updatable) The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the traffic is detected as malicious by a protection rule. If unspecified, defaults to `403`.
* `block_error_page_description` - (Optional) (Updatable) The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the traffic is detected as malicious by a protection rule. If unspecified, defaults to `Access blocked by website owner. Please contact support.`
* `block_error_page_message` - (Optional) (Updatable) The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the traffic is detected as malicious by a protection rule. If unspecified, defaults to 'Access to the website is blocked.'
* `block_response_code` - (Optional) (Updatable) The response code returned when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE`, and the traffic is detected as malicious by a protection rule. If unspecified, defaults to `403`. The list of available response codes: `400`, `401`, `403`, `405`, `409`, `411`, `412`, `413`, `414`, `415`, `416`, `500`, `501`, `502`, `503`, `504`, `507`.
* `is_response_inspected` - (Optional) (Updatable) Inspects the response body of origin responses. Can be used to detect leakage of sensitive data. If unspecified, defaults to `false`.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

