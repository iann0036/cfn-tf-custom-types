# TF::OCI::WaasWaasPolicy

This resource provides the Waas Policy resource in Oracle Cloud Infrastructure Web Application Acceleration and Security service.

Creates a new Web Application Acceleration and Security (WAAS) policy in the specified compartment. A WAAS policy must be established before creating Web Application Firewall (WAF) rules. To use WAF rules, your web application's origin servers must defined in the `WaasPolicy` schema.

A domain name must be specified when creating a WAAS policy. The domain name should be different from the origins specified in your `WaasPolicy`. Once domain name is entered and stored, it is unchangeable.

Use the record data returned in the `cname` field of the `WaasPolicy` object to create a CNAME record in your DNS configuration that will direct your domain's traffic through the WAF.

For the purposes of access control, you must provide the OCID of the compartment where you want the service to reside. For information about access control and compartments, see [Overview of the IAM Service](htt...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::WaasWaasPolicy",
    "Properties" : {
        "<a href="#additionaldomains" title="AdditionalDomains">AdditionalDomains</a>" : <i>[ String, ... ]</i>,
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>, ... ]</i>,
        "<a href="#origingroups" title="OriginGroups">OriginGroups</a>" : <i>[ <a href="origingroupsdefinition.md">OriginGroupsDefinition</a>, ... ]</i>,
        "<a href="#origins" title="Origins">Origins</a>" : <i>[ <a href="originsdefinition.md">OriginsDefinition</a>, ... ]</i>,
        "<a href="#policyconfig" title="PolicyConfig">PolicyConfig</a>" : <i>[ <a href="policyconfigdefinition.md">PolicyConfigDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#wafconfig" title="WafConfig">WafConfig</a>" : <i>[ <a href="wafconfigdefinition.md">WafConfigDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::WaasWaasPolicy
Properties:
    <a href="#additionaldomains" title="AdditionalDomains">AdditionalDomains</a>: <i>
      - String</i>
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtagsdefinition.md">DefinedTagsDefinition</a></i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a></i>
    <a href="#origingroups" title="OriginGroups">OriginGroups</a>: <i>
      - <a href="origingroupsdefinition.md">OriginGroupsDefinition</a></i>
    <a href="#origins" title="Origins">Origins</a>: <i>
      - <a href="originsdefinition.md">OriginsDefinition</a></i>
    <a href="#policyconfig" title="PolicyConfig">PolicyConfig</a>: <i>
      - <a href="policyconfigdefinition.md">PolicyConfigDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#wafconfig" title="WafConfig">WafConfig</a>: <i>
      - <a href="wafconfigdefinition.md">WafConfigDefinition</a></i>
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

_Type_: List of <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

(Updatable) A user-friendly name for the WAAS policy. The name can be changed and does not need to be unique.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

(Updatable) The domain for which the cookie is set, defaults to WAAS policy domain.
* `expiration_time_in_seconds` - (Applicable when method=STICKY_COOKIE) (Updatable) The time for which a browser should keep the cookie in seconds. Empty value will cause the cookie to expire at the end of a browser session.
* `method` - (Required) (Updatable) Load balancing methods are algorithms used to efficiently distribute traffic among origin servers.
* **[IP_HASH](/iaas/api/#/en/waas/latest/datatypes/IPHashLoadBalancingMethod):** All the incoming requests from the same client IP address should go to the same content origination server. IP_HASH load balancing method uses origin weights when choosing which origin should the hash be assigned to initially.
* **[ROUND_ROBIN](/iaas/api/#/en/waas/latest/datatypes/RoundRobinLoadBalancingMethod):** Forwards requests sequentially to the available origin servers. The first request - to the first origin server, the second request - to the next origin server, and so on. After it sends a request to the last origin server, it starts again with the first origin server. When using weights on origins, Weighted Round Robin assigns more requests to origins with a greater weight. Over a period of time, origins will receive a number of requests in proportion to their weight.
* **[STICKY_COOKIE](/iaas/api/#/en/waas/latest/datatypes/StickyCookieLoadBalancingMethod):** Adds a session cookie to the first response from the origin server and identifies the server that sent the response. The client's next request contains the cookie value, and nginx routes the request to the origin server that responded to the first request. STICKY_COOKIE load balancing method falls back to Round Robin for the first request.
* `name` - (Applicable when method=STICKY_COOKIE) (Updatable) The name of the cookie used to track the persistence. Can contain any US-ASCII character except separator or control character.
* `tls_protocols` - (Optional) (Updatable) A list of allowed TLS protocols. Only applicable when HTTPS support is enabled. The TLS protocol is negotiated while the request is connecting and the most recent protocol supported by both the edge node and client browser will be selected. If no such version exists, the connection will be aborted.
* **TLS_V1:** corresponds to TLS 1.0 specification.
* **TLS_V1_1:** corresponds to TLS 1.1 specification.
* **TLS_V1_2:** corresponds to TLS 1.2 specification.
* **TLS_V1_3:** corresponds to TLS 1.3 specification.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

(Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

_Required_: No

_Type_: List of <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginGroups

_Required_: No

_Type_: List of <a href="origingroupsdefinition.md">OriginGroupsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Origins

_Required_: No

_Type_: List of <a href="originsdefinition.md">OriginsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyConfig

_Required_: No

_Type_: List of <a href="policyconfigdefinition.md">PolicyConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WafConfig

_Required_: No

_Type_: List of <a href="wafconfigdefinition.md">WafConfigDefinition</a>

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

#### Id

(Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the custom protection rule.
* `device_fingerprint_challenge` - (Optional) (Updatable) The device fingerprint challenge settings. Blocks bots based on unique device fingerprint information.
* `action` - (Optional) (Updatable) The action to take on requests from detected bots. If unspecified, defaults to `DETECT`.
* `action_expiration_in_seconds` - (Optional) (Updatable) The number of seconds between challenges for the same IP address. If unspecified, defaults to `60`.
* `challenge_settings` - (Optional) (Updatable) The challenge settings if `action` is set to `BLOCK`.
* `block_action` - (Optional) (Updatable) The method used to block requests that fail the challenge, if `action` is set to `BLOCK`. If unspecified, defaults to `SHOW_ERROR_PAGE`.
* `block_error_page_code` - (Optional) (Updatable) The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE` and the request is blocked. If unspecified, defaults to `403`.
* `block_error_page_description` - (Optional) (Updatable) The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `Access blocked by website owner. Please contact support.`
* `block_error_page_message` - (Optional) (Updatable) The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `Access to the website is blocked`.
* `block_response_code` - (Optional) (Updatable) The response status code to return when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE` or `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `403`. The list of available response codes: `200`, `201`, `202`, `204`, `206`, `300`, `301`, `302`, `303`, `304`, `307`, `400`, `401`, `403`, `404`, `405`, `408`, `409`, `411`, `412`, `413`, `414`, `415`, `416`, `422`, `444`, `494`, `495`, `496`, `497`, `499`, `500`, `501`, `502`, `503`, `504`, `507`.
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
* `challenge_settings` - (Optional) (Updatable) The challenge settings if `action` is set to `BLOCK`.
* `block_action` - (Optional) (Updatable) The method used to block requests that fail the challenge, if `action` is set to `BLOCK`. If unspecified, defaults to `SHOW_ERROR_PAGE`.
* `block_error_page_code` - (Optional) (Updatable) The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE` and the request is blocked. If unspecified, defaults to `403`.
* `block_error_page_description` - (Optional) (Updatable) The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `Access blocked by website owner. Please contact support.`
* `block_error_page_message` - (Optional) (Updatable) The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `Access to the website is blocked`.
* `block_response_code` - (Optional) (Updatable) The response status code to return when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE` or `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `403`. The list of available response codes: `200`, `201`, `202`, `204`, `206`, `300`, `301`, `302`, `303`, `304`, `307`, `400`, `401`, `403`, `404`, `405`, `408`, `409`, `411`, `412`, `413`, `414`, `415`, `416`, `422`, `444`, `494`, `495`, `496`, `497`, `499`, `500`, `501`, `502`, `503`, `504`, `507`.
* `captcha_footer` - (Optional) (Updatable) The text to show in the footer when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, default to `Enter the letters and numbers as they are shown in image above`.
* `captcha_header` - (Optional) (Updatable) The text to show in the header when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `We have detected an increased number of attempts to access this webapp. To help us keep this webapp secure, please let us know that you are not a robot by entering the text from captcha below.`
* `captcha_submit_label` - (Optional) (Updatable) The text to show on the label of the CAPTCHA challenge submit button when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Yes, I am human`.
* `captcha_title` - (Optional) (Updatable) The title used when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Are you human?`
* `failure_threshold` - (Optional) (Updatable) The number of failed requests before taking action. If unspecified, defaults to `10`.
* `failure_threshold_expiration_in_seconds` - (Optional) (Updatable) The number of seconds before the failure threshold resets. If unspecified, defaults to  `60`.
* `interaction_threshold` - (Optional) (Updatable) The number of interactions required to pass the challenge. If unspecified, defaults to `3`.
* `is_enabled` - (Required) (Updatable) Enables or disables the human interaction challenge Web Application Firewall feature.
* `is_nat_enabled` - (Optional) (Updatable) When enabled, the user is identified not only by the IP address but also by an unique additional hash, which prevents blocking visitors with shared IP addresses.
* `recording_period_in_seconds` - (Optional) (Updatable) The number of seconds to record the interactions from the user. If unspecified, defaults to `15`.
* `set_http_header` - (Optional) (Updatable) Adds an additional HTTP header to requests that fail the challenge before being passed to the origin. Only applicable when the `action` is set to `DETECT`.
* `name` - (Required) (Updatable) The name of the header.
* `value` - (Required) (Updatable) The value of the header.
* `js_challenge` - (Optional) (Updatable) The JavaScript challenge settings. Blocks bots by challenging requests from browsers that have no JavaScript support.
* `action` - (Optional) (Updatable) The action to take against requests from detected bots. If unspecified, defaults to `DETECT`.
* `action_expiration_in_seconds` - (Optional) (Updatable) The number of seconds between challenges from the same IP address. If unspecified, defaults to `60`.
* `are_redirects_challenged` - (Optional) (Updatable) When enabled, redirect responses from the origin will also be challenged. This will change HTTP 301/302 responses from origin to HTTP 200 with an HTML body containing JavaScript page redirection.
* `challenge_settings` - (Optional) (Updatable) The challenge settings if `action` is set to `BLOCK`.
* `block_action` - (Optional) (Updatable) The method used to block requests that fail the challenge, if `action` is set to `BLOCK`. If unspecified, defaults to `SHOW_ERROR_PAGE`.
* `block_error_page_code` - (Optional) (Updatable) The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE` and the request is blocked. If unspecified, defaults to `403`.
* `block_error_page_description` - (Optional) (Updatable) The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `Access blocked by website owner. Please contact support.`
* `block_error_page_message` - (Optional) (Updatable) The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `Access to the website is blocked`.
* `block_response_code` - (Optional) (Updatable) The response status code to return when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE` or `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `403`. The list of available response codes: `200`, `201`, `202`, `204`, `206`, `300`, `301`, `302`, `303`, `304`, `307`, `400`, `401`, `403`, `404`, `405`, `408`, `409`, `411`, `412`, `413`, `414`, `415`, `416`, `422`, `444`, `494`, `495`, `496`, `497`, `499`, `500`, `501`, `502`, `503`, `504`, `507`.
* `captcha_footer` - (Optional) (Updatable) The text to show in the footer when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, default to `Enter the letters and numbers as they are shown in image above`.
* `captcha_header` - (Optional) (Updatable) The text to show in the header when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `We have detected an increased number of attempts to access this webapp. To help us keep this webapp secure, please let us know that you are not a robot by entering the text from captcha below.`
* `captcha_submit_label` - (Optional) (Updatable) The text to show on the label of the CAPTCHA challenge submit button when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Yes, I am human`.
* `captcha_title` - (Optional) (Updatable) The title used when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Are you human?`
* `criteria` - (Optional) (Updatable) When defined, the JavaScript Challenge would be applied only for the requests that matched all the listed conditions.
* `condition` - (Required) (Updatable) The criteria the access rule and JavaScript Challenge uses to determine if action should be taken on a request.
* **URL_IS:** Matches if the concatenation of request URL path and query is identical to the contents of the `value` field. URL must start with a `/`.
* **URL_IS_NOT:** Matches if the concatenation of request URL path and query is not identical to the contents of the `value` field. URL must start with a `/`.
* **URL_STARTS_WITH:** Matches if the concatenation of request URL path and query starts with the contents of the `value` field. URL must start with a `/`.
* **URL_PART_ENDS_WITH:** Matches if the concatenation of request URL path and query ends with the contents of the `value` field.
* **URL_PART_CONTAINS:** Matches if the concatenation of request URL path and query contains the contents of the `value` field.
* **URL_REGEX:** Matches if the concatenation of request URL path and query is described by the regular expression in the value field. The value must be a valid regular expression recognized by the PCRE library in Nginx (https://www.pcre.org).
* **URL_DOES_NOT_MATCH_REGEX:** Matches if the concatenation of request URL path and query is not described by the regular expression in the `value` field. The value must be a valid regular expression recognized by the PCRE library in Nginx (https://www.pcre.org).
* **URL_DOES_NOT_START_WITH:** Matches if the concatenation of request URL path and query does not start with the contents of the `value` field.
* **URL_PART_DOES_NOT_CONTAIN:** Matches if the concatenation of request URL path and query does not contain the contents of the `value` field.
* **URL_PART_DOES_NOT_END_WITH:** Matches if the concatenation of request URL path and query does not end with the contents of the `value` field.
* **IP_IS:** Matches if the request originates from one of the IP addresses contained in the defined address list. The `value` in this case is string with one or multiple IPs or CIDR notations separated by new line symbol \n *Example:* "1.1.1.1\n1.1.1.2\n1.2.2.1/30"
* **IP_IS_NOT:** Matches if the request does not originate from any of the IP addresses contained in the defined address list. The `value` in this case is string with one or multiple IPs or CIDR notations separated by new line symbol \n *Example:* "1.1.1.1\n1.1.1.2\n1.2.2.1/30"
* **IP_IN_LIST:** Matches if the request originates from one of the IP addresses contained in the referenced address list. The `value` in this case is OCID of the address list.
* **IP_NOT_IN_LIST:** Matches if the request does not originate from any IP address contained in the referenced address list. The `value` field in this case is OCID of the address list.
* **HTTP_HEADER_CONTAINS:** The HTTP_HEADER_CONTAINS criteria is defined using a compound value separated by a colon: a header field name and a header field value. `host:test.example.com` is an example of a criteria value where `host` is the header field name and `test.example.com` is the header field value. A request matches when the header field name is a case insensitive match and the header field value is a case insensitive, substring match. *Example:* With a criteria value of `host:test.example.com`, where `host` is the name of the field and `test.example.com` is the value of the host field, a request with the header values, `Host: www.test.example.com` will match, where as a request with header values of `host: www.example.com` or `host: test.sub.example.com` will not match.
* **HTTP_METHOD_IS:** Matches if the request method is identical to one of the values listed in field. The `value` in this case is string with one or multiple HTTP methods separated by new line symbol \n The list of available methods: `GET`, `HEAD`, `POST`, `PUT`, `DELETE`, `CONNECT`, `OPTIONS`, `TRACE`, `PATCH`.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

