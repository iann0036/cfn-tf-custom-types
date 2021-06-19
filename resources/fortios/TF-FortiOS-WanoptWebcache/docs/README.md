# TF::FortiOS::WanoptWebcache

Configure global Web cache settings.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::WanoptWebcache",
    "Properties" : {
        "<a href="#alwaysrevalidate" title="AlwaysRevalidate">AlwaysRevalidate</a>" : <i>String</i>,
        "<a href="#cachebydefault" title="CacheByDefault">CacheByDefault</a>" : <i>String</i>,
        "<a href="#cachecookie" title="CacheCookie">CacheCookie</a>" : <i>String</i>,
        "<a href="#cacheexpired" title="CacheExpired">CacheExpired</a>" : <i>String</i>,
        "<a href="#defaultttl" title="DefaultTtl">DefaultTtl</a>" : <i>Double</i>,
        "<a href="#external" title="External">External</a>" : <i>String</i>,
        "<a href="#freshfactor" title="FreshFactor">FreshFactor</a>" : <i>Double</i>,
        "<a href="#hostvalidate" title="HostValidate">HostValidate</a>" : <i>String</i>,
        "<a href="#ignoreconditional" title="IgnoreConditional">IgnoreConditional</a>" : <i>String</i>,
        "<a href="#ignoreiereload" title="IgnoreIeReload">IgnoreIeReload</a>" : <i>String</i>,
        "<a href="#ignoreims" title="IgnoreIms">IgnoreIms</a>" : <i>String</i>,
        "<a href="#ignorepnc" title="IgnorePnc">IgnorePnc</a>" : <i>String</i>,
        "<a href="#maxobjectsize" title="MaxObjectSize">MaxObjectSize</a>" : <i>Double</i>,
        "<a href="#maxttl" title="MaxTtl">MaxTtl</a>" : <i>Double</i>,
        "<a href="#minttl" title="MinTtl">MinTtl</a>" : <i>Double</i>,
        "<a href="#negresptime" title="NegRespTime">NegRespTime</a>" : <i>Double</i>,
        "<a href="#revalpnc" title="RevalPnc">RevalPnc</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::WanoptWebcache
Properties:
    <a href="#alwaysrevalidate" title="AlwaysRevalidate">AlwaysRevalidate</a>: <i>String</i>
    <a href="#cachebydefault" title="CacheByDefault">CacheByDefault</a>: <i>String</i>
    <a href="#cachecookie" title="CacheCookie">CacheCookie</a>: <i>String</i>
    <a href="#cacheexpired" title="CacheExpired">CacheExpired</a>: <i>String</i>
    <a href="#defaultttl" title="DefaultTtl">DefaultTtl</a>: <i>Double</i>
    <a href="#external" title="External">External</a>: <i>String</i>
    <a href="#freshfactor" title="FreshFactor">FreshFactor</a>: <i>Double</i>
    <a href="#hostvalidate" title="HostValidate">HostValidate</a>: <i>String</i>
    <a href="#ignoreconditional" title="IgnoreConditional">IgnoreConditional</a>: <i>String</i>
    <a href="#ignoreiereload" title="IgnoreIeReload">IgnoreIeReload</a>: <i>String</i>
    <a href="#ignoreims" title="IgnoreIms">IgnoreIms</a>: <i>String</i>
    <a href="#ignorepnc" title="IgnorePnc">IgnorePnc</a>: <i>String</i>
    <a href="#maxobjectsize" title="MaxObjectSize">MaxObjectSize</a>: <i>Double</i>
    <a href="#maxttl" title="MaxTtl">MaxTtl</a>: <i>Double</i>
    <a href="#minttl" title="MinTtl">MinTtl</a>: <i>Double</i>
    <a href="#negresptime" title="NegRespTime">NegRespTime</a>: <i>Double</i>
    <a href="#revalpnc" title="RevalPnc">RevalPnc</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### AlwaysRevalidate

Enable/disable revalidation of requested cached objects, which have content on the server, before serving it to the client. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheByDefault

Enable/disable caching content that lacks explicit caching policies from the server. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheCookie

Enable/disable caching cookies. Since cookies contain information for or about individual users, they not usually cached. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheExpired

Enable/disable caching type-1 objects that are already expired on arrival. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultTtl

Default object expiry time (default = 1440 min (1 day); maximum = 5256000 min (10 years)). This only applies to those objects that do not have an expiry time set by the web server.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### External

Enable/disable external Web caching. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreshFactor

Frequency that the server is checked to see if any objects have expired (1 - 100, default = 100). The higher the fresh factor, the less often the checks occur.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostValidate

Enable/disable validating "Host:" with original server IP. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreConditional

Enable/disable controlling the behavior of cache-control HTTP 1.1 header values. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreIeReload

Enable/disable ignoring the PNC-interpretation of Internet Explorer's Accept: / header. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreIms

Enable/disable ignoring the if-modified-since (IMS) header. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnorePnc

Enable/disable ignoring the pragma no-cache (PNC) header. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxObjectSize

Maximum cacheable object size in kB (1 - 2147483 kb (2GB). All objects that exceed this are delivered to the client but not stored in the web cache.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxTtl

Maximum time an object can stay in the web cache without checking to see if it has expired on the server (default = 7200 min (5 days); maximum = 5256000 min (10 years)).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinTtl

Minimum time an object can stay in the web cache without checking to see if it has expired on the server (default = 5 min; maximum = 5256000 (10 years)).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NegRespTime

Time in minutes to cache negative responses or errors (0 - 4294967295, default = 0  which means negative responses are not cached).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RevalPnc

Enable/disable revalidation of pragma-no-cache (PNC) to address bandwidth concerns. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

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

