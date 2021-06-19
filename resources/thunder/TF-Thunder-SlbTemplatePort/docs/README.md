# TF::Thunder::SlbTemplatePort

`thunder_slb_template_port` Provides details about thunder slb template port

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SlbTemplatePort",
    "Properties" : {
        "<a href="#add" title="Add">Add</a>" : <i>Double</i>,
        "<a href="#bwratelimit" title="BwRateLimit">BwRateLimit</a>" : <i>Double</i>,
        "<a href="#bwratelimitduration" title="BwRateLimitDuration">BwRateLimitDuration</a>" : <i>Double</i>,
        "<a href="#bwratelimitnologging" title="BwRateLimitNoLogging">BwRateLimitNoLogging</a>" : <i>Double</i>,
        "<a href="#bwratelimitresume" title="BwRateLimitResume">BwRateLimitResume</a>" : <i>Double</i>,
        "<a href="#connlimit" title="ConnLimit">ConnLimit</a>" : <i>Double</i>,
        "<a href="#connlimitnologging" title="ConnLimitNoLogging">ConnLimitNoLogging</a>" : <i>Double</i>,
        "<a href="#connratelimit" title="ConnRateLimit">ConnRateLimit</a>" : <i>Double</i>,
        "<a href="#connratelimitnologging" title="ConnRateLimitNoLogging">ConnRateLimitNoLogging</a>" : <i>Double</i>,
        "<a href="#dampeningflaps" title="DampeningFlaps">DampeningFlaps</a>" : <i>Double</i>,
        "<a href="#decrement" title="Decrement">Decrement</a>" : <i>Double</i>,
        "<a href="#delsessiononserverdown" title="DelSessionOnServerDown">DelSessionOnServerDown</a>" : <i>Double</i>,
        "<a href="#destnat" title="DestNat">DestNat</a>" : <i>Double</i>,
        "<a href="#downgraceperiod" title="DownGracePeriod">DownGracePeriod</a>" : <i>Double</i>,
        "<a href="#downtimer" title="DownTimer">DownTimer</a>" : <i>Double</i>,
        "<a href="#dscp" title="Dscp">Dscp</a>" : <i>Double</i>,
        "<a href="#dynamicmemberpriority" title="DynamicMemberPriority">DynamicMemberPriority</a>" : <i>Double</i>,
        "<a href="#every" title="Every">Every</a>" : <i>Double</i>,
        "<a href="#extendedstats" title="ExtendedStats">ExtendedStats</a>" : <i>Double</i>,
        "<a href="#flapperiod" title="FlapPeriod">FlapPeriod</a>" : <i>Double</i>,
        "<a href="#healthcheck" title="HealthCheck">HealthCheck</a>" : <i>String</i>,
        "<a href="#healthcheckdisable" title="HealthCheckDisable">HealthCheckDisable</a>" : <i>Double</i>,
        "<a href="#inbandhealthcheck" title="InbandHealthCheck">InbandHealthCheck</a>" : <i>Double</i>,
        "<a href="#initialslowstart" title="InitialSlowStart">InitialSlowStart</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nossl" title="NoSsl">NoSsl</a>" : <i>Double</i>,
        "<a href="#rateinterval" title="RateInterval">RateInterval</a>" : <i>String</i>,
        "<a href="#reassign" title="Reassign">Reassign</a>" : <i>Double</i>,
        "<a href="#requestrateinterval" title="RequestRateInterval">RequestRateInterval</a>" : <i>String</i>,
        "<a href="#requestratelimit" title="RequestRateLimit">RequestRateLimit</a>" : <i>Double</i>,
        "<a href="#requestratenologging" title="RequestRateNoLogging">RequestRateNoLogging</a>" : <i>Double</i>,
        "<a href="#reselonreset" title="ReselOnReset">ReselOnReset</a>" : <i>Double</i>,
        "<a href="#reset" title="Reset">Reset</a>" : <i>Double</i>,
        "<a href="#restoresvctime" title="RestoreSvcTime">RestoreSvcTime</a>" : <i>Double</i>,
        "<a href="#resume" title="Resume">Resume</a>" : <i>Double</i>,
        "<a href="#retry" title="Retry">Retry</a>" : <i>Double</i>,
        "<a href="#sharedpartitionpool" title="SharedPartitionPool">SharedPartitionPool</a>" : <i>Double</i>,
        "<a href="#slowstart" title="SlowStart">SlowStart</a>" : <i>Double</i>,
        "<a href="#sourcenat" title="SourceNat">SourceNat</a>" : <i>String</i>,
        "<a href="#statsdataaction" title="StatsDataAction">StatsDataAction</a>" : <i>String</i>,
        "<a href="#subgroup" title="SubGroup">SubGroup</a>" : <i>Double</i>,
        "<a href="#templateportpoolshared" title="TemplatePortPoolShared">TemplatePortPoolShared</a>" : <i>String</i>,
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
Type: TF::Thunder::SlbTemplatePort
Properties:
    <a href="#add" title="Add">Add</a>: <i>Double</i>
    <a href="#bwratelimit" title="BwRateLimit">BwRateLimit</a>: <i>Double</i>
    <a href="#bwratelimitduration" title="BwRateLimitDuration">BwRateLimitDuration</a>: <i>Double</i>
    <a href="#bwratelimitnologging" title="BwRateLimitNoLogging">BwRateLimitNoLogging</a>: <i>Double</i>
    <a href="#bwratelimitresume" title="BwRateLimitResume">BwRateLimitResume</a>: <i>Double</i>
    <a href="#connlimit" title="ConnLimit">ConnLimit</a>: <i>Double</i>
    <a href="#connlimitnologging" title="ConnLimitNoLogging">ConnLimitNoLogging</a>: <i>Double</i>
    <a href="#connratelimit" title="ConnRateLimit">ConnRateLimit</a>: <i>Double</i>
    <a href="#connratelimitnologging" title="ConnRateLimitNoLogging">ConnRateLimitNoLogging</a>: <i>Double</i>
    <a href="#dampeningflaps" title="DampeningFlaps">DampeningFlaps</a>: <i>Double</i>
    <a href="#decrement" title="Decrement">Decrement</a>: <i>Double</i>
    <a href="#delsessiononserverdown" title="DelSessionOnServerDown">DelSessionOnServerDown</a>: <i>Double</i>
    <a href="#destnat" title="DestNat">DestNat</a>: <i>Double</i>
    <a href="#downgraceperiod" title="DownGracePeriod">DownGracePeriod</a>: <i>Double</i>
    <a href="#downtimer" title="DownTimer">DownTimer</a>: <i>Double</i>
    <a href="#dscp" title="Dscp">Dscp</a>: <i>Double</i>
    <a href="#dynamicmemberpriority" title="DynamicMemberPriority">DynamicMemberPriority</a>: <i>Double</i>
    <a href="#every" title="Every">Every</a>: <i>Double</i>
    <a href="#extendedstats" title="ExtendedStats">ExtendedStats</a>: <i>Double</i>
    <a href="#flapperiod" title="FlapPeriod">FlapPeriod</a>: <i>Double</i>
    <a href="#healthcheck" title="HealthCheck">HealthCheck</a>: <i>String</i>
    <a href="#healthcheckdisable" title="HealthCheckDisable">HealthCheckDisable</a>: <i>Double</i>
    <a href="#inbandhealthcheck" title="InbandHealthCheck">InbandHealthCheck</a>: <i>Double</i>
    <a href="#initialslowstart" title="InitialSlowStart">InitialSlowStart</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nossl" title="NoSsl">NoSsl</a>: <i>Double</i>
    <a href="#rateinterval" title="RateInterval">RateInterval</a>: <i>String</i>
    <a href="#reassign" title="Reassign">Reassign</a>: <i>Double</i>
    <a href="#requestrateinterval" title="RequestRateInterval">RequestRateInterval</a>: <i>String</i>
    <a href="#requestratelimit" title="RequestRateLimit">RequestRateLimit</a>: <i>Double</i>
    <a href="#requestratenologging" title="RequestRateNoLogging">RequestRateNoLogging</a>: <i>Double</i>
    <a href="#reselonreset" title="ReselOnReset">ReselOnReset</a>: <i>Double</i>
    <a href="#reset" title="Reset">Reset</a>: <i>Double</i>
    <a href="#restoresvctime" title="RestoreSvcTime">RestoreSvcTime</a>: <i>Double</i>
    <a href="#resume" title="Resume">Resume</a>: <i>Double</i>
    <a href="#retry" title="Retry">Retry</a>: <i>Double</i>
    <a href="#sharedpartitionpool" title="SharedPartitionPool">SharedPartitionPool</a>: <i>Double</i>
    <a href="#slowstart" title="SlowStart">SlowStart</a>: <i>Double</i>
    <a href="#sourcenat" title="SourceNat">SourceNat</a>: <i>String</i>
    <a href="#statsdataaction" title="StatsDataAction">StatsDataAction</a>: <i>String</i>
    <a href="#subgroup" title="SubGroup">SubGroup</a>: <i>Double</i>
    <a href="#templateportpoolshared" title="TemplatePortPoolShared">TemplatePortPoolShared</a>: <i>String</i>
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

Configure bandwidth rate limit on real server port (Bandwidth rate limit in Kbps).

_Required_: No

_Type_: Double

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

#### DampeningFlaps

service dampening flaps count (max-flaps allowed in flap period).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Decrement

Decrease after every round of DNS query (default is 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DelSessionOnServerDown

Delete session if the server/port goes down (either disabled/hm down).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestNat

Destination NAT.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DownGracePeriod

Port down grace period.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DownTimer

The timer to bring the marked down server/port to up (default is 0, never bring up) (The timer to bring up server (in second, default is 0)).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dscp

Differentiated Services Code Point (DSCP to Real Server IP Mapping Value).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicMemberPriority

Set dynamic member’s priority (Initial priority (default is 16)).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Every

Slow start connection limit increment interval (default 10).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtendedStats

Enable extended statistics on real server port.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlapPeriod

take service out of rotation if max-flaps exceeded within time in seconds.

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

#### InbandHealthCheck

Use inband traffic to detect port’s health status.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitialSlowStart

Initial slow start connection limit (default 128).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Port template name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoSsl

No SSL.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateInterval

‘100ms’: Use 100 ms as sampling interval; ‘second’: Use 1 second as sampling interval;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Reassign

Maximum reassign times before declear the server/port down (default is 25) (The maximum reassign number).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestRateInterval

‘100ms’: Use 100 ms as sampling interval; ‘second’: Use 1 second as sampling interval;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestRateLimit

Request rate limit.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestRateNoLogging

Do not log connection over limit event.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReselOnReset

When receiving reset from server, do the server/port reselection (default is 0, don’t do reselection).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Reset

Send client reset when connection rate over limit.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestoreSvcTime

put the service back to the rotation after time in seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resume

Resume accepting new connection after connection number drops below threshold (Connection resume threshold).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Retry

Maximum retry times before reassign this connection to another server/port (default is 2) (The maximum retry number).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionPool

Reference a NAT pool or pool-group from shared partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlowStart

Slowly ramp up the connection number after port is up.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceNat

Source NAT (IP NAT Pool or pool group name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatsDataAction

‘stats-data-enable’: Enable statistical data collection for real server port; ‘stats-data-disable’: Disable statistical data collection for real server port;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubGroup

Divide service group members into different sub groups (Sub group ID (default is 0)).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplatePortPoolShared

Source NAT (IP NAT Pool or pool group name).

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

Weight (port weight).

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

