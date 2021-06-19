# TF::Thunder::SlbTemplateServer

`thunder_slb_template_server` Provides details about thunder slb template server

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SlbTemplateServer",
    "Properties" : {
        "<a href="#add" title="Add">Add</a>" : <i>Double</i>,
        "<a href="#bwratelimit" title="BwRateLimit">BwRateLimit</a>" : <i>Double</i>,
        "<a href="#bwratelimitacct" title="BwRateLimitAcct">BwRateLimitAcct</a>" : <i>String</i>,
        "<a href="#bwratelimitduration" title="BwRateLimitDuration">BwRateLimitDuration</a>" : <i>Double</i>,
        "<a href="#bwratelimitnologging" title="BwRateLimitNoLogging">BwRateLimitNoLogging</a>" : <i>Double</i>,
        "<a href="#bwratelimitresume" title="BwRateLimitResume">BwRateLimitResume</a>" : <i>Double</i>,
        "<a href="#connlimit" title="ConnLimit">ConnLimit</a>" : <i>Double</i>,
        "<a href="#connlimitnologging" title="ConnLimitNoLogging">ConnLimitNoLogging</a>" : <i>Double</i>,
        "<a href="#connratelimit" title="ConnRateLimit">ConnRateLimit</a>" : <i>Double</i>,
        "<a href="#connratelimitnologging" title="ConnRateLimitNoLogging">ConnRateLimitNoLogging</a>" : <i>Double</i>,
        "<a href="#dnsqueryinterval" title="DnsQueryInterval">DnsQueryInterval</a>" : <i>Double</i>,
        "<a href="#dynamicserverprefix" title="DynamicServerPrefix">DynamicServerPrefix</a>" : <i>String</i>,
        "<a href="#every" title="Every">Every</a>" : <i>Double</i>,
        "<a href="#extendedstats" title="ExtendedStats">ExtendedStats</a>" : <i>Double</i>,
        "<a href="#healthcheck" title="HealthCheck">HealthCheck</a>" : <i>String</i>,
        "<a href="#healthcheckdisable" title="HealthCheckDisable">HealthCheckDisable</a>" : <i>Double</i>,
        "<a href="#initialslowstart" title="InitialSlowStart">InitialSlowStart</a>" : <i>Double</i>,
        "<a href="#logselectionfailure" title="LogSelectionFailure">LogSelectionFailure</a>" : <i>Double</i>,
        "<a href="#maxdynamicserver" title="MaxDynamicServer">MaxDynamicServer</a>" : <i>Double</i>,
        "<a href="#minttlratio" title="MinTtlRatio">MinTtlRatio</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#rateinterval" title="RateInterval">RateInterval</a>" : <i>String</i>,
        "<a href="#resume" title="Resume">Resume</a>" : <i>Double</i>,
        "<a href="#slowstart" title="SlowStart">SlowStart</a>" : <i>Double</i>,
        "<a href="#spoofingcache" title="SpoofingCache">SpoofingCache</a>" : <i>Double</i>,
        "<a href="#statsdataaction" title="StatsDataAction">StatsDataAction</a>" : <i>String</i>,
        "<a href="#till" title="Till">Till</a>" : <i>Double</i>,
        "<a href="#times" title="Times">Times</a>" : <i>Double</i>,
        "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#weight" title="Weight">Weight</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SlbTemplateServer
Properties:
    <a href="#add" title="Add">Add</a>: <i>Double</i>
    <a href="#bwratelimit" title="BwRateLimit">BwRateLimit</a>: <i>Double</i>
    <a href="#bwratelimitacct" title="BwRateLimitAcct">BwRateLimitAcct</a>: <i>String</i>
    <a href="#bwratelimitduration" title="BwRateLimitDuration">BwRateLimitDuration</a>: <i>Double</i>
    <a href="#bwratelimitnologging" title="BwRateLimitNoLogging">BwRateLimitNoLogging</a>: <i>Double</i>
    <a href="#bwratelimitresume" title="BwRateLimitResume">BwRateLimitResume</a>: <i>Double</i>
    <a href="#connlimit" title="ConnLimit">ConnLimit</a>: <i>Double</i>
    <a href="#connlimitnologging" title="ConnLimitNoLogging">ConnLimitNoLogging</a>: <i>Double</i>
    <a href="#connratelimit" title="ConnRateLimit">ConnRateLimit</a>: <i>Double</i>
    <a href="#connratelimitnologging" title="ConnRateLimitNoLogging">ConnRateLimitNoLogging</a>: <i>Double</i>
    <a href="#dnsqueryinterval" title="DnsQueryInterval">DnsQueryInterval</a>: <i>Double</i>
    <a href="#dynamicserverprefix" title="DynamicServerPrefix">DynamicServerPrefix</a>: <i>String</i>
    <a href="#every" title="Every">Every</a>: <i>Double</i>
    <a href="#extendedstats" title="ExtendedStats">ExtendedStats</a>: <i>Double</i>
    <a href="#healthcheck" title="HealthCheck">HealthCheck</a>: <i>String</i>
    <a href="#healthcheckdisable" title="HealthCheckDisable">HealthCheckDisable</a>: <i>Double</i>
    <a href="#initialslowstart" title="InitialSlowStart">InitialSlowStart</a>: <i>Double</i>
    <a href="#logselectionfailure" title="LogSelectionFailure">LogSelectionFailure</a>: <i>Double</i>
    <a href="#maxdynamicserver" title="MaxDynamicServer">MaxDynamicServer</a>: <i>Double</i>
    <a href="#minttlratio" title="MinTtlRatio">MinTtlRatio</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#rateinterval" title="RateInterval">RateInterval</a>: <i>String</i>
    <a href="#resume" title="Resume">Resume</a>: <i>Double</i>
    <a href="#slowstart" title="SlowStart">SlowStart</a>: <i>Double</i>
    <a href="#spoofingcache" title="SpoofingCache">SpoofingCache</a>: <i>Double</i>
    <a href="#statsdataaction" title="StatsDataAction">StatsDataAction</a>: <i>String</i>
    <a href="#till" title="Till">Till</a>: <i>Double</i>
    <a href="#times" title="Times">Times</a>: <i>Double</i>
    <a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#weight" title="Weight">Weight</a>: <i>Double</i>
</pre>

## Properties

#### Add

Slow start connection limit add by a number every interval (Add by this number every interval).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BwRateLimit

Configure bandwidth rate limit on real server (Bandwidth rate limit in Kbps).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BwRateLimitAcct

‘to-server-only’: Only account for traffic sent to server; ‘from-server-only’: Only account for traffic received from server; ‘all’: Account for all traffic sent to and received from server;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BwRateLimitDuration

Duration in seconds the observed rate needs to honor.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BwRateLimitNoLogging

Do not log bandwidth rate limit related state transitions.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BwRateLimitResume

Resume server selection after bandwidth drops below this threshold (in Kbps) (Bandwidth rate limit resume threshold (in Kbps)).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnLimit

Connection limit.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnLimitNoLogging

Do not log connection over limit event.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnRateLimit

Connection rate limit.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnRateLimitNoLogging

Do not log connection over limit event.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsQueryInterval

The interval to query DNS server for the hostname (DNS query interval (in minute, default is 10)).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicServerPrefix

Prefix of dynamic server (Prefix of dynamic server (default is “DRS”)).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Every

Slow start connection limit increment interval (default 10).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtendedStats

Enable extended statistics on real server.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheck

Health Check Monitor (Health monitor name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckDisable

Disable configured health check configuration.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitialSlowStart

Initial slow start connection limit (default 128).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogSelectionFailure

Enable real-time logging for server selection failure event.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxDynamicServer

Maximum dynamic server number (Maximum dynamic server number (default is 255)).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinTtlRatio

Minimum TTL to DNS query interval ratio (Minimum TTL ratio (default is 2)).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Server template name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateInterval

‘100ms’: Use 100 ms as sampling interval; ‘second’: Use 1 second as sampling interval;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resume

Resume accepting new connection after connection number drops below threshold (Connection resume threshold).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlowStart

Slowly ramp up the connection number after server is up.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpoofingCache

Servers under the template are spoofing cache.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatsDataAction

‘stats-data-enable’: Enable statistical data collection for real server; ‘stats-data-disable’: Disable statistical data collection for real server;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Till

Slow start ends when slow start connection limit reaches a number (default 4096) (Slow start ends when connection limit reaches this number).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Times

Slow start connection limit multiply by a number every interval (default 2) (Multiply by this number every interval).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserTag

Customized tag.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Weight

Weight for the Real Servers (Connection Weight).

_Required_: No

_Type_: Double

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

