# TF::Volterra::HttpLoadbalancer

CloudFormation equivalent of volterra_http_loadbalancer

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Volterra::HttpLoadbalancer",
    "Properties" : {
        "<a href="#addlocation" title="AddLocation">AddLocation</a>" : <i>Boolean</i>,
        "<a href="#advertiseonpublicdefaultvip" title="AdvertiseOnPublicDefaultVip">AdvertiseOnPublicDefaultVip</a>" : <i>Boolean</i>,
        "<a href="#annotations" title="Annotations">Annotations</a>" : <i>[ <a href="annotationsdefinition.md">AnnotationsDefinition</a>, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#disable" title="Disable">Disable</a>" : <i>Boolean</i>,
        "<a href="#disableratelimit" title="DisableRateLimit">DisableRateLimit</a>" : <i>Boolean</i>,
        "<a href="#disablewaf" title="DisableWaf">DisableWaf</a>" : <i>Boolean</i>,
        "<a href="#donotadvertise" title="DoNotAdvertise">DoNotAdvertise</a>" : <i>Boolean</i>,
        "<a href="#domains" title="Domains">Domains</a>" : <i>[ String, ... ]</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#leastactive" title="LeastActive">LeastActive</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
        "<a href="#nochallenge" title="NoChallenge">NoChallenge</a>" : <i>Boolean</i>,
        "<a href="#noservicepolicies" title="NoServicePolicies">NoServicePolicies</a>" : <i>Boolean</i>,
        "<a href="#random" title="Random">Random</a>" : <i>Boolean</i>,
        "<a href="#roundrobin" title="RoundRobin">RoundRobin</a>" : <i>Boolean</i>,
        "<a href="#servicepoliciesfromnamespace" title="ServicePoliciesFromNamespace">ServicePoliciesFromNamespace</a>" : <i>Boolean</i>,
        "<a href="#sourceipstickiness" title="SourceIpStickiness">SourceIpStickiness</a>" : <i>Boolean</i>,
        "<a href="#activeservicepolicies" title="ActiveServicePolicies">ActiveServicePolicies</a>" : <i>[ <a href="activeservicepoliciesdefinition.md">ActiveServicePoliciesDefinition</a>, ... ]</i>,
        "<a href="#advertisecustom" title="AdvertiseCustom">AdvertiseCustom</a>" : <i>[ <a href="advertisecustomdefinition.md">AdvertiseCustomDefinition</a>, ... ]</i>,
        "<a href="#advertiseonpublic" title="AdvertiseOnPublic">AdvertiseOnPublic</a>" : <i>[ <a href="advertiseonpublicdefinition.md">AdvertiseOnPublicDefinition</a>, ... ]</i>,
        "<a href="#blockedclients" title="BlockedClients">BlockedClients</a>" : <i>[ <a href="blockedclientsdefinition.md">BlockedClientsDefinition</a>, ... ]</i>,
        "<a href="#captchachallenge" title="CaptchaChallenge">CaptchaChallenge</a>" : <i>[ <a href="captchachallengedefinition.md">CaptchaChallengeDefinition</a>, ... ]</i>,
        "<a href="#cookiestickiness" title="CookieStickiness">CookieStickiness</a>" : <i>[ <a href="cookiestickinessdefinition.md">CookieStickinessDefinition</a>, ... ]</i>,
        "<a href="#corspolicy" title="CorsPolicy">CorsPolicy</a>" : <i>[ <a href="corspolicydefinition.md">CorsPolicyDefinition</a>, ... ]</i>,
        "<a href="#defaultroutepools" title="DefaultRoutePools">DefaultRoutePools</a>" : <i>[ <a href="defaultroutepoolsdefinition.md">DefaultRoutePoolsDefinition</a>, ... ]</i>,
        "<a href="#http" title="Http">Http</a>" : <i>[ <a href="httpdefinition.md">HttpDefinition</a>, ... ]</i>,
        "<a href="#https" title="Https">Https</a>" : <i>[ <a href="httpsdefinition.md">HttpsDefinition</a>, ... ]</i>,
        "<a href="#httpsautocert" title="HttpsAutoCert">HttpsAutoCert</a>" : <i>[ <a href="httpsautocertdefinition.md">HttpsAutoCertDefinition</a>, ... ]</i>,
        "<a href="#jschallenge" title="JsChallenge">JsChallenge</a>" : <i>[ <a href="jschallengedefinition.md">JsChallengeDefinition</a>, ... ]</i>,
        "<a href="#malicioususermitigation" title="MaliciousUserMitigation">MaliciousUserMitigation</a>" : <i>[ <a href="malicioususermitigationdefinition.md">MaliciousUserMitigationDefinition</a>, ... ]</i>,
        "<a href="#moreoption" title="MoreOption">MoreOption</a>" : <i>[ <a href="moreoptiondefinition.md">MoreOptionDefinition</a>, ... ]</i>,
        "<a href="#policybasedchallenge" title="PolicyBasedChallenge">PolicyBasedChallenge</a>" : <i>[ <a href="policybasedchallengedefinition.md">PolicyBasedChallengeDefinition</a>, ... ]</i>,
        "<a href="#ratelimit" title="RateLimit">RateLimit</a>" : <i>[ <a href="ratelimitdefinition.md">RateLimitDefinition</a>, ... ]</i>,
        "<a href="#ringhash" title="RingHash">RingHash</a>" : <i>[ <a href="ringhashdefinition.md">RingHashDefinition</a>, ... ]</i>,
        "<a href="#routes" title="Routes">Routes</a>" : <i>[ <a href="routesdefinition.md">RoutesDefinition</a>, ... ]</i>,
        "<a href="#trustedclients" title="TrustedClients">TrustedClients</a>" : <i>[ <a href="trustedclientsdefinition.md">TrustedClientsDefinition</a>, ... ]</i>,
        "<a href="#useridentification" title="UserIdentification">UserIdentification</a>" : <i>[ <a href="useridentificationdefinition.md">UserIdentificationDefinition</a>, ... ]</i>,
        "<a href="#waf" title="Waf">Waf</a>" : <i>[ <a href="wafdefinition.md">WafDefinition</a>, ... ]</i>,
        "<a href="#wafexclusionrules" title="WafExclusionRules">WafExclusionRules</a>" : <i>[ <a href="wafexclusionrulesdefinition.md">WafExclusionRulesDefinition</a>, ... ]</i>,
        "<a href="#wafrule" title="WafRule">WafRule</a>" : <i>[ <a href="wafruledefinition.md">WafRuleDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Volterra::HttpLoadbalancer
Properties:
    <a href="#addlocation" title="AddLocation">AddLocation</a>: <i>Boolean</i>
    <a href="#advertiseonpublicdefaultvip" title="AdvertiseOnPublicDefaultVip">AdvertiseOnPublicDefaultVip</a>: <i>Boolean</i>
    <a href="#annotations" title="Annotations">Annotations</a>: <i>
      - <a href="annotationsdefinition.md">AnnotationsDefinition</a></i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#disable" title="Disable">Disable</a>: <i>Boolean</i>
    <a href="#disableratelimit" title="DisableRateLimit">DisableRateLimit</a>: <i>Boolean</i>
    <a href="#disablewaf" title="DisableWaf">DisableWaf</a>: <i>Boolean</i>
    <a href="#donotadvertise" title="DoNotAdvertise">DoNotAdvertise</a>: <i>Boolean</i>
    <a href="#domains" title="Domains">Domains</a>: <i>
      - String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#leastactive" title="LeastActive">LeastActive</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
    <a href="#nochallenge" title="NoChallenge">NoChallenge</a>: <i>Boolean</i>
    <a href="#noservicepolicies" title="NoServicePolicies">NoServicePolicies</a>: <i>Boolean</i>
    <a href="#random" title="Random">Random</a>: <i>Boolean</i>
    <a href="#roundrobin" title="RoundRobin">RoundRobin</a>: <i>Boolean</i>
    <a href="#servicepoliciesfromnamespace" title="ServicePoliciesFromNamespace">ServicePoliciesFromNamespace</a>: <i>Boolean</i>
    <a href="#sourceipstickiness" title="SourceIpStickiness">SourceIpStickiness</a>: <i>Boolean</i>
    <a href="#activeservicepolicies" title="ActiveServicePolicies">ActiveServicePolicies</a>: <i>
      - <a href="activeservicepoliciesdefinition.md">ActiveServicePoliciesDefinition</a></i>
    <a href="#advertisecustom" title="AdvertiseCustom">AdvertiseCustom</a>: <i>
      - <a href="advertisecustomdefinition.md">AdvertiseCustomDefinition</a></i>
    <a href="#advertiseonpublic" title="AdvertiseOnPublic">AdvertiseOnPublic</a>: <i>
      - <a href="advertiseonpublicdefinition.md">AdvertiseOnPublicDefinition</a></i>
    <a href="#blockedclients" title="BlockedClients">BlockedClients</a>: <i>
      - <a href="blockedclientsdefinition.md">BlockedClientsDefinition</a></i>
    <a href="#captchachallenge" title="CaptchaChallenge">CaptchaChallenge</a>: <i>
      - <a href="captchachallengedefinition.md">CaptchaChallengeDefinition</a></i>
    <a href="#cookiestickiness" title="CookieStickiness">CookieStickiness</a>: <i>
      - <a href="cookiestickinessdefinition.md">CookieStickinessDefinition</a></i>
    <a href="#corspolicy" title="CorsPolicy">CorsPolicy</a>: <i>
      - <a href="corspolicydefinition.md">CorsPolicyDefinition</a></i>
    <a href="#defaultroutepools" title="DefaultRoutePools">DefaultRoutePools</a>: <i>
      - <a href="defaultroutepoolsdefinition.md">DefaultRoutePoolsDefinition</a></i>
    <a href="#http" title="Http">Http</a>: <i>
      - <a href="httpdefinition.md">HttpDefinition</a></i>
    <a href="#https" title="Https">Https</a>: <i>
      - <a href="httpsdefinition.md">HttpsDefinition</a></i>
    <a href="#httpsautocert" title="HttpsAutoCert">HttpsAutoCert</a>: <i>
      - <a href="httpsautocertdefinition.md">HttpsAutoCertDefinition</a></i>
    <a href="#jschallenge" title="JsChallenge">JsChallenge</a>: <i>
      - <a href="jschallengedefinition.md">JsChallengeDefinition</a></i>
    <a href="#malicioususermitigation" title="MaliciousUserMitigation">MaliciousUserMitigation</a>: <i>
      - <a href="malicioususermitigationdefinition.md">MaliciousUserMitigationDefinition</a></i>
    <a href="#moreoption" title="MoreOption">MoreOption</a>: <i>
      - <a href="moreoptiondefinition.md">MoreOptionDefinition</a></i>
    <a href="#policybasedchallenge" title="PolicyBasedChallenge">PolicyBasedChallenge</a>: <i>
      - <a href="policybasedchallengedefinition.md">PolicyBasedChallengeDefinition</a></i>
    <a href="#ratelimit" title="RateLimit">RateLimit</a>: <i>
      - <a href="ratelimitdefinition.md">RateLimitDefinition</a></i>
    <a href="#ringhash" title="RingHash">RingHash</a>: <i>
      - <a href="ringhashdefinition.md">RingHashDefinition</a></i>
    <a href="#routes" title="Routes">Routes</a>: <i>
      - <a href="routesdefinition.md">RoutesDefinition</a></i>
    <a href="#trustedclients" title="TrustedClients">TrustedClients</a>: <i>
      - <a href="trustedclientsdefinition.md">TrustedClientsDefinition</a></i>
    <a href="#useridentification" title="UserIdentification">UserIdentification</a>: <i>
      - <a href="useridentificationdefinition.md">UserIdentificationDefinition</a></i>
    <a href="#waf" title="Waf">Waf</a>: <i>
      - <a href="wafdefinition.md">WafDefinition</a></i>
    <a href="#wafexclusionrules" title="WafExclusionRules">WafExclusionRules</a>: <i>
      - <a href="wafexclusionrulesdefinition.md">WafExclusionRulesDefinition</a></i>
    <a href="#wafrule" title="WafRule">WafRule</a>: <i>
      - <a href="wafruledefinition.md">WafRuleDefinition</a></i>
</pre>

## Properties

#### AddLocation

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvertiseOnPublicDefaultVip

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Annotations

_Required_: No

_Type_: List of <a href="annotationsdefinition.md">AnnotationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableRateLimit

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableWaf

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DoNotAdvertise

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domains

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LeastActive

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoChallenge

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoServicePolicies

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Random

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoundRobin

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServicePoliciesFromNamespace

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIpStickiness

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActiveServicePolicies

_Required_: No

_Type_: List of <a href="activeservicepoliciesdefinition.md">ActiveServicePoliciesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvertiseCustom

_Required_: No

_Type_: List of <a href="advertisecustomdefinition.md">AdvertiseCustomDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvertiseOnPublic

_Required_: No

_Type_: List of <a href="advertiseonpublicdefinition.md">AdvertiseOnPublicDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockedClients

_Required_: No

_Type_: List of <a href="blockedclientsdefinition.md">BlockedClientsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaptchaChallenge

_Required_: No

_Type_: List of <a href="captchachallengedefinition.md">CaptchaChallengeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CookieStickiness

_Required_: No

_Type_: List of <a href="cookiestickinessdefinition.md">CookieStickinessDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CorsPolicy

_Required_: No

_Type_: List of <a href="corspolicydefinition.md">CorsPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultRoutePools

_Required_: No

_Type_: List of <a href="defaultroutepoolsdefinition.md">DefaultRoutePoolsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Http

_Required_: No

_Type_: List of <a href="httpdefinition.md">HttpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Https

_Required_: No

_Type_: List of <a href="httpsdefinition.md">HttpsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpsAutoCert

_Required_: No

_Type_: List of <a href="httpsautocertdefinition.md">HttpsAutoCertDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JsChallenge

_Required_: No

_Type_: List of <a href="jschallengedefinition.md">JsChallengeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaliciousUserMitigation

_Required_: No

_Type_: List of <a href="malicioususermitigationdefinition.md">MaliciousUserMitigationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MoreOption

_Required_: No

_Type_: List of <a href="moreoptiondefinition.md">MoreOptionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyBasedChallenge

_Required_: No

_Type_: List of <a href="policybasedchallengedefinition.md">PolicyBasedChallengeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateLimit

_Required_: No

_Type_: List of <a href="ratelimitdefinition.md">RateLimitDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RingHash

_Required_: No

_Type_: List of <a href="ringhashdefinition.md">RingHashDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Routes

_Required_: No

_Type_: List of <a href="routesdefinition.md">RoutesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrustedClients

_Required_: No

_Type_: List of <a href="trustedclientsdefinition.md">TrustedClientsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserIdentification

_Required_: No

_Type_: List of <a href="useridentificationdefinition.md">UserIdentificationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Waf

_Required_: No

_Type_: List of <a href="wafdefinition.md">WafDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WafExclusionRules

_Required_: No

_Type_: List of <a href="wafexclusionrulesdefinition.md">WafExclusionRulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WafRule

_Required_: No

_Type_: List of <a href="wafruledefinition.md">WafRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

