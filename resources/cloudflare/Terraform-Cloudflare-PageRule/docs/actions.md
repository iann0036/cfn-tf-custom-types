# Terraform::Cloudflare::PageRule Actions

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#alwaysonline" title="AlwaysOnline">AlwaysOnline</a>" : <i>String</i>,
    "<a href="#alwaysusehttps" title="AlwaysUseHttps">AlwaysUseHttps</a>" : <i>Boolean</i>,
    "<a href="#automatichttpsrewrites" title="AutomaticHttpsRewrites">AutomaticHttpsRewrites</a>" : <i>String</i>,
    "<a href="#browsercachettl" title="BrowserCacheTtl">BrowserCacheTtl</a>" : <i>String</i>,
    "<a href="#browsercheck" title="BrowserCheck">BrowserCheck</a>" : <i>String</i>,
    "<a href="#bypasscacheoncookie" title="BypassCacheOnCookie">BypassCacheOnCookie</a>" : <i>String</i>,
    "<a href="#cachebydevicetype" title="CacheByDeviceType">CacheByDeviceType</a>" : <i>String</i>,
    "<a href="#cachedeceptionarmor" title="CacheDeceptionArmor">CacheDeceptionArmor</a>" : <i>String</i>,
    "<a href="#cachelevel" title="CacheLevel">CacheLevel</a>" : <i>String</i>,
    "<a href="#cacheoncookie" title="CacheOnCookie">CacheOnCookie</a>" : <i>String</i>,
    "<a href="#disableapps" title="DisableApps">DisableApps</a>" : <i>Boolean</i>,
    "<a href="#disableperformance" title="DisablePerformance">DisablePerformance</a>" : <i>Boolean</i>,
    "<a href="#disablerailgun" title="DisableRailgun">DisableRailgun</a>" : <i>Boolean</i>,
    "<a href="#disablesecurity" title="DisableSecurity">DisableSecurity</a>" : <i>Boolean</i>,
    "<a href="#edgecachettl" title="EdgeCacheTtl">EdgeCacheTtl</a>" : <i>Double</i>,
    "<a href="#emailobfuscation" title="EmailObfuscation">EmailObfuscation</a>" : <i>String</i>,
    "<a href="#explicitcachecontrol" title="ExplicitCacheControl">ExplicitCacheControl</a>" : <i>String</i>,
    "<a href="#hostheaderoverride" title="HostHeaderOverride">HostHeaderOverride</a>" : <i>String</i>,
    "<a href="#ipgeolocation" title="IpGeolocation">IpGeolocation</a>" : <i>String</i>,
    "<a href="#mirage" title="Mirage">Mirage</a>" : <i>String</i>,
    "<a href="#opportunisticencryption" title="OpportunisticEncryption">OpportunisticEncryption</a>" : <i>String</i>,
    "<a href="#originerrorpagepassthru" title="OriginErrorPagePassThru">OriginErrorPagePassThru</a>" : <i>String</i>,
    "<a href="#polish" title="Polish">Polish</a>" : <i>String</i>,
    "<a href="#resolveoverride" title="ResolveOverride">ResolveOverride</a>" : <i>String</i>,
    "<a href="#respectstrongetag" title="RespectStrongEtag">RespectStrongEtag</a>" : <i>String</i>,
    "<a href="#responsebuffering" title="ResponseBuffering">ResponseBuffering</a>" : <i>String</i>,
    "<a href="#rocketloader" title="RocketLoader">RocketLoader</a>" : <i>String</i>,
    "<a href="#securitylevel" title="SecurityLevel">SecurityLevel</a>" : <i>String</i>,
    "<a href="#serversideexclude" title="ServerSideExclude">ServerSideExclude</a>" : <i>String</i>,
    "<a href="#sortquerystringforcache" title="SortQueryStringForCache">SortQueryStringForCache</a>" : <i>String</i>,
    "<a href="#ssl" title="Ssl">Ssl</a>" : <i>String</i>,
    "<a href="#trueclientipheader" title="TrueClientIpHeader">TrueClientIpHeader</a>" : <i>String</i>,
    "<a href="#waf" title="Waf">Waf</a>" : <i>String</i>,
    "<a href="#forwardingurl" title="ForwardingUrl">ForwardingUrl</a>" : <i>[ <a href="actions-forwardingurl.md">ForwardingUrl</a>, ... ]</i>,
    "<a href="#minify" title="Minify">Minify</a>" : <i>[ <a href="actions-minify.md">Minify</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#alwaysonline" title="AlwaysOnline">AlwaysOnline</a>: <i>String</i>
<a href="#alwaysusehttps" title="AlwaysUseHttps">AlwaysUseHttps</a>: <i>Boolean</i>
<a href="#automatichttpsrewrites" title="AutomaticHttpsRewrites">AutomaticHttpsRewrites</a>: <i>String</i>
<a href="#browsercachettl" title="BrowserCacheTtl">BrowserCacheTtl</a>: <i>String</i>
<a href="#browsercheck" title="BrowserCheck">BrowserCheck</a>: <i>String</i>
<a href="#bypasscacheoncookie" title="BypassCacheOnCookie">BypassCacheOnCookie</a>: <i>String</i>
<a href="#cachebydevicetype" title="CacheByDeviceType">CacheByDeviceType</a>: <i>String</i>
<a href="#cachedeceptionarmor" title="CacheDeceptionArmor">CacheDeceptionArmor</a>: <i>String</i>
<a href="#cachelevel" title="CacheLevel">CacheLevel</a>: <i>String</i>
<a href="#cacheoncookie" title="CacheOnCookie">CacheOnCookie</a>: <i>String</i>
<a href="#disableapps" title="DisableApps">DisableApps</a>: <i>Boolean</i>
<a href="#disableperformance" title="DisablePerformance">DisablePerformance</a>: <i>Boolean</i>
<a href="#disablerailgun" title="DisableRailgun">DisableRailgun</a>: <i>Boolean</i>
<a href="#disablesecurity" title="DisableSecurity">DisableSecurity</a>: <i>Boolean</i>
<a href="#edgecachettl" title="EdgeCacheTtl">EdgeCacheTtl</a>: <i>Double</i>
<a href="#emailobfuscation" title="EmailObfuscation">EmailObfuscation</a>: <i>String</i>
<a href="#explicitcachecontrol" title="ExplicitCacheControl">ExplicitCacheControl</a>: <i>String</i>
<a href="#hostheaderoverride" title="HostHeaderOverride">HostHeaderOverride</a>: <i>String</i>
<a href="#ipgeolocation" title="IpGeolocation">IpGeolocation</a>: <i>String</i>
<a href="#mirage" title="Mirage">Mirage</a>: <i>String</i>
<a href="#opportunisticencryption" title="OpportunisticEncryption">OpportunisticEncryption</a>: <i>String</i>
<a href="#originerrorpagepassthru" title="OriginErrorPagePassThru">OriginErrorPagePassThru</a>: <i>String</i>
<a href="#polish" title="Polish">Polish</a>: <i>String</i>
<a href="#resolveoverride" title="ResolveOverride">ResolveOverride</a>: <i>String</i>
<a href="#respectstrongetag" title="RespectStrongEtag">RespectStrongEtag</a>: <i>String</i>
<a href="#responsebuffering" title="ResponseBuffering">ResponseBuffering</a>: <i>String</i>
<a href="#rocketloader" title="RocketLoader">RocketLoader</a>: <i>String</i>
<a href="#securitylevel" title="SecurityLevel">SecurityLevel</a>: <i>String</i>
<a href="#serversideexclude" title="ServerSideExclude">ServerSideExclude</a>: <i>String</i>
<a href="#sortquerystringforcache" title="SortQueryStringForCache">SortQueryStringForCache</a>: <i>String</i>
<a href="#ssl" title="Ssl">Ssl</a>: <i>String</i>
<a href="#trueclientipheader" title="TrueClientIpHeader">TrueClientIpHeader</a>: <i>String</i>
<a href="#waf" title="Waf">Waf</a>: <i>String</i>
<a href="#forwardingurl" title="ForwardingUrl">ForwardingUrl</a>: <i>
      - <a href="actions-forwardingurl.md">ForwardingUrl</a></i>
<a href="#minify" title="Minify">Minify</a>: <i>
      - <a href="actions-minify.md">Minify</a></i>
</pre>

## Properties

#### AlwaysOnline

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlwaysUseHttps

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutomaticHttpsRewrites

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BrowserCacheTtl

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BrowserCheck

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BypassCacheOnCookie

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheByDeviceType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheDeceptionArmor

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheLevel

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheOnCookie

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableApps

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisablePerformance

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableRailgun

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableSecurity

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EdgeCacheTtl

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailObfuscation

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExplicitCacheControl

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostHeaderOverride

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpGeolocation

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

#### OriginErrorPagePassThru

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Polish

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResolveOverride

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RespectStrongEtag

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

#### TrueClientIpHeader

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Waf

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardingUrl

_Required_: No
_Type_: List of <a href="actions-forwardingurl.md">ForwardingUrl</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Minify

_Required_: No
_Type_: List of <a href="actions-minify.md">Minify</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

