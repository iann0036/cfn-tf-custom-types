# TF::Cloudflare::ZoneSettingsOverride SettingsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#alwaysonline" title="AlwaysOnline">AlwaysOnline</a>" : <i>String</i>,
    "<a href="#alwaysusehttps" title="AlwaysUseHttps">AlwaysUseHttps</a>" : <i>String</i>,
    "<a href="#automatichttpsrewrites" title="AutomaticHttpsRewrites">AutomaticHttpsRewrites</a>" : <i>String</i>,
    "<a href="#brotli" title="Brotli">Brotli</a>" : <i>String</i>,
    "<a href="#browsercachettl" title="BrowserCacheTtl">BrowserCacheTtl</a>" : <i>Double</i>,
    "<a href="#browsercheck" title="BrowserCheck">BrowserCheck</a>" : <i>String</i>,
    "<a href="#cachelevel" title="CacheLevel">CacheLevel</a>" : <i>String</i>,
    "<a href="#challengettl" title="ChallengeTtl">ChallengeTtl</a>" : <i>Double</i>,
    "<a href="#cnameflattening" title="CnameFlattening">CnameFlattening</a>" : <i>String</i>,
    "<a href="#developmentmode" title="DevelopmentMode">DevelopmentMode</a>" : <i>String</i>,
    "<a href="#emailobfuscation" title="EmailObfuscation">EmailObfuscation</a>" : <i>String</i>,
    "<a href="#h2prioritization" title="H2Prioritization">H2Prioritization</a>" : <i>String</i>,
    "<a href="#hotlinkprotection" title="HotlinkProtection">HotlinkProtection</a>" : <i>String</i>,
    "<a href="#http2" title="Http2">Http2</a>" : <i>String</i>,
    "<a href="#http3" title="Http3">Http3</a>" : <i>String</i>,
    "<a href="#imageresizing" title="ImageResizing">ImageResizing</a>" : <i>String</i>,
    "<a href="#ipgeolocation" title="IpGeolocation">IpGeolocation</a>" : <i>String</i>,
    "<a href="#ipv6" title="Ipv6">Ipv6</a>" : <i>String</i>,
    "<a href="#maxupload" title="MaxUpload">MaxUpload</a>" : <i>Double</i>,
    "<a href="#mintlsversion" title="MinTlsVersion">MinTlsVersion</a>" : <i>String</i>,
    "<a href="#mirage" title="Mirage">Mirage</a>" : <i>String</i>,
    "<a href="#opportunisticencryption" title="OpportunisticEncryption">OpportunisticEncryption</a>" : <i>String</i>,
    "<a href="#opportunisticonion" title="OpportunisticOnion">OpportunisticOnion</a>" : <i>String</i>,
    "<a href="#originerrorpagepassthru" title="OriginErrorPagePassThru">OriginErrorPagePassThru</a>" : <i>String</i>,
    "<a href="#polish" title="Polish">Polish</a>" : <i>String</i>,
    "<a href="#prefetchpreload" title="PrefetchPreload">PrefetchPreload</a>" : <i>String</i>,
    "<a href="#privacypass" title="PrivacyPass">PrivacyPass</a>" : <i>String</i>,
    "<a href="#pseudoipv4" title="PseudoIpv4">PseudoIpv4</a>" : <i>String</i>,
    "<a href="#responsebuffering" title="ResponseBuffering">ResponseBuffering</a>" : <i>String</i>,
    "<a href="#rocketloader" title="RocketLoader">RocketLoader</a>" : <i>String</i>,
    "<a href="#securitylevel" title="SecurityLevel">SecurityLevel</a>" : <i>String</i>,
    "<a href="#serversideexclude" title="ServerSideExclude">ServerSideExclude</a>" : <i>String</i>,
    "<a href="#sortquerystringforcache" title="SortQueryStringForCache">SortQueryStringForCache</a>" : <i>String</i>,
    "<a href="#ssl" title="Ssl">Ssl</a>" : <i>String</i>,
    "<a href="#tls12only" title="Tls12Only">Tls12Only</a>" : <i>String</i>,
    "<a href="#tls13" title="Tls13">Tls13</a>" : <i>String</i>,
    "<a href="#tlsclientauth" title="TlsClientAuth">TlsClientAuth</a>" : <i>String</i>,
    "<a href="#trueclientipheader" title="TrueClientIpHeader">TrueClientIpHeader</a>" : <i>String</i>,
    "<a href="#universalssl" title="UniversalSsl">UniversalSsl</a>" : <i>String</i>,
    "<a href="#waf" title="Waf">Waf</a>" : <i>String</i>,
    "<a href="#webp" title="Webp">Webp</a>" : <i>String</i>,
    "<a href="#websockets" title="Websockets">Websockets</a>" : <i>String</i>,
    "<a href="#zerortt" title="ZeroRtt">ZeroRtt</a>" : <i>String</i>,
    "<a href="#minify" title="Minify">Minify</a>" : <i>[ <a href="initialsettingsdefinition.md">InitialSettingsDefinition</a>, ... ]</i>,
    "<a href="#mobileredirect" title="MobileRedirect">MobileRedirect</a>" : <i>[ <a href="initialsettingsdefinition2.md">InitialSettingsDefinition2</a>, ... ]</i>,
    "<a href="#securityheader" title="SecurityHeader">SecurityHeader</a>" : <i>[ <a href="initialsettingsdefinition3.md">InitialSettingsDefinition3</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#alwaysonline" title="AlwaysOnline">AlwaysOnline</a>: <i>String</i>
<a href="#alwaysusehttps" title="AlwaysUseHttps">AlwaysUseHttps</a>: <i>String</i>
<a href="#automatichttpsrewrites" title="AutomaticHttpsRewrites">AutomaticHttpsRewrites</a>: <i>String</i>
<a href="#brotli" title="Brotli">Brotli</a>: <i>String</i>
<a href="#browsercachettl" title="BrowserCacheTtl">BrowserCacheTtl</a>: <i>Double</i>
<a href="#browsercheck" title="BrowserCheck">BrowserCheck</a>: <i>String</i>
<a href="#cachelevel" title="CacheLevel">CacheLevel</a>: <i>String</i>
<a href="#challengettl" title="ChallengeTtl">ChallengeTtl</a>: <i>Double</i>
<a href="#cnameflattening" title="CnameFlattening">CnameFlattening</a>: <i>String</i>
<a href="#developmentmode" title="DevelopmentMode">DevelopmentMode</a>: <i>String</i>
<a href="#emailobfuscation" title="EmailObfuscation">EmailObfuscation</a>: <i>String</i>
<a href="#h2prioritization" title="H2Prioritization">H2Prioritization</a>: <i>String</i>
<a href="#hotlinkprotection" title="HotlinkProtection">HotlinkProtection</a>: <i>String</i>
<a href="#http2" title="Http2">Http2</a>: <i>String</i>
<a href="#http3" title="Http3">Http3</a>: <i>String</i>
<a href="#imageresizing" title="ImageResizing">ImageResizing</a>: <i>String</i>
<a href="#ipgeolocation" title="IpGeolocation">IpGeolocation</a>: <i>String</i>
<a href="#ipv6" title="Ipv6">Ipv6</a>: <i>String</i>
<a href="#maxupload" title="MaxUpload">MaxUpload</a>: <i>Double</i>
<a href="#mintlsversion" title="MinTlsVersion">MinTlsVersion</a>: <i>String</i>
<a href="#mirage" title="Mirage">Mirage</a>: <i>String</i>
<a href="#opportunisticencryption" title="OpportunisticEncryption">OpportunisticEncryption</a>: <i>String</i>
<a href="#opportunisticonion" title="OpportunisticOnion">OpportunisticOnion</a>: <i>String</i>
<a href="#originerrorpagepassthru" title="OriginErrorPagePassThru">OriginErrorPagePassThru</a>: <i>String</i>
<a href="#polish" title="Polish">Polish</a>: <i>String</i>
<a href="#prefetchpreload" title="PrefetchPreload">PrefetchPreload</a>: <i>String</i>
<a href="#privacypass" title="PrivacyPass">PrivacyPass</a>: <i>String</i>
<a href="#pseudoipv4" title="PseudoIpv4">PseudoIpv4</a>: <i>String</i>
<a href="#responsebuffering" title="ResponseBuffering">ResponseBuffering</a>: <i>String</i>
<a href="#rocketloader" title="RocketLoader">RocketLoader</a>: <i>String</i>
<a href="#securitylevel" title="SecurityLevel">SecurityLevel</a>: <i>String</i>
<a href="#serversideexclude" title="ServerSideExclude">ServerSideExclude</a>: <i>String</i>
<a href="#sortquerystringforcache" title="SortQueryStringForCache">SortQueryStringForCache</a>: <i>String</i>
<a href="#ssl" title="Ssl">Ssl</a>: <i>String</i>
<a href="#tls12only" title="Tls12Only">Tls12Only</a>: <i>String</i>
<a href="#tls13" title="Tls13">Tls13</a>: <i>String</i>
<a href="#tlsclientauth" title="TlsClientAuth">TlsClientAuth</a>: <i>String</i>
<a href="#trueclientipheader" title="TrueClientIpHeader">TrueClientIpHeader</a>: <i>String</i>
<a href="#universalssl" title="UniversalSsl">UniversalSsl</a>: <i>String</i>
<a href="#waf" title="Waf">Waf</a>: <i>String</i>
<a href="#webp" title="Webp">Webp</a>: <i>String</i>
<a href="#websockets" title="Websockets">Websockets</a>: <i>String</i>
<a href="#zerortt" title="ZeroRtt">ZeroRtt</a>: <i>String</i>
<a href="#minify" title="Minify">Minify</a>: <i>
      - <a href="initialsettingsdefinition.md">InitialSettingsDefinition</a></i>
<a href="#mobileredirect" title="MobileRedirect">MobileRedirect</a>: <i>
      - <a href="initialsettingsdefinition2.md">InitialSettingsDefinition2</a></i>
<a href="#securityheader" title="SecurityHeader">SecurityHeader</a>: <i>
      - <a href="initialsettingsdefinition3.md">InitialSettingsDefinition3</a></i>
</pre>

## Properties

#### AlwaysOnline

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlwaysUseHttps

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutomaticHttpsRewrites

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Brotli

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BrowserCacheTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BrowserCheck

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChallengeTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CnameFlattening

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DevelopmentMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailObfuscation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### H2Prioritization

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HotlinkProtection

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Http2

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Http3

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageResizing

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpGeolocation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxUpload

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinTlsVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mirage

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpportunisticEncryption

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpportunisticOnion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginErrorPagePassThru

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Polish

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefetchPreload

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivacyPass

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PseudoIpv4

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseBuffering

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RocketLoader

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerSideExclude

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SortQueryStringForCache

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ssl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tls12Only

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tls13

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsClientAuth

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrueClientIpHeader

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UniversalSsl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Waf

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Webp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Websockets

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZeroRtt

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Minify

_Required_: No

_Type_: List of <a href="initialsettingsdefinition.md">InitialSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MobileRedirect

_Required_: No

_Type_: List of <a href="initialsettingsdefinition2.md">InitialSettingsDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityHeader

_Required_: No

_Type_: List of <a href="initialsettingsdefinition3.md">InitialSettingsDefinition3</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

