# TF::Thunder::SlbTemplateVirtualServer

`thunder_slb_template_virtual_server` Provides details about thunder slb template virtual server

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SlbTemplateVirtualServer",
    "Properties" : {
        "<a href="#connlimit" title="ConnLimit">ConnLimit</a>" : <i>Double</i>,
        "<a href="#connlimitnologging" title="ConnLimitNoLogging">ConnLimitNoLogging</a>" : <i>Double</i>,
        "<a href="#connlimitreset" title="ConnLimitReset">ConnLimitReset</a>" : <i>Double</i>,
        "<a href="#connratelimit" title="ConnRateLimit">ConnRateLimit</a>" : <i>Double</i>,
        "<a href="#connratelimitnologging" title="ConnRateLimitNoLogging">ConnRateLimitNoLogging</a>" : <i>Double</i>,
        "<a href="#connratelimitreset" title="ConnRateLimitReset">ConnRateLimitReset</a>" : <i>Double</i>,
        "<a href="#icmplockup" title="IcmpLockup">IcmpLockup</a>" : <i>Double</i>,
        "<a href="#icmplockupperiod" title="IcmpLockupPeriod">IcmpLockupPeriod</a>" : <i>Double</i>,
        "<a href="#icmpratelimit" title="IcmpRateLimit">IcmpRateLimit</a>" : <i>Double</i>,
        "<a href="#icmpv6lockup" title="Icmpv6Lockup">Icmpv6Lockup</a>" : <i>Double</i>,
        "<a href="#icmpv6lockupperiod" title="Icmpv6LockupPeriod">Icmpv6LockupPeriod</a>" : <i>Double</i>,
        "<a href="#icmpv6ratelimit" title="Icmpv6RateLimit">Icmpv6RateLimit</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#rateinterval" title="RateInterval">RateInterval</a>" : <i>String</i>,
        "<a href="#subnetgratuitousarp" title="SubnetGratuitousArp">SubnetGratuitousArp</a>" : <i>Double</i>,
        "<a href="#tcpstacktfoactiveconnlimit" title="TcpStackTfoActiveConnLimit">TcpStackTfoActiveConnLimit</a>" : <i>Double</i>,
        "<a href="#tcpstacktfobackofftime" title="TcpStackTfoBackoffTime">TcpStackTfoBackoffTime</a>" : <i>Double</i>,
        "<a href="#tcpstacktfocookietimelimit" title="TcpStackTfoCookieTimeLimit">TcpStackTfoCookieTimeLimit</a>" : <i>Double</i>,
        "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SlbTemplateVirtualServer
Properties:
    <a href="#connlimit" title="ConnLimit">ConnLimit</a>: <i>Double</i>
    <a href="#connlimitnologging" title="ConnLimitNoLogging">ConnLimitNoLogging</a>: <i>Double</i>
    <a href="#connlimitreset" title="ConnLimitReset">ConnLimitReset</a>: <i>Double</i>
    <a href="#connratelimit" title="ConnRateLimit">ConnRateLimit</a>: <i>Double</i>
    <a href="#connratelimitnologging" title="ConnRateLimitNoLogging">ConnRateLimitNoLogging</a>: <i>Double</i>
    <a href="#connratelimitreset" title="ConnRateLimitReset">ConnRateLimitReset</a>: <i>Double</i>
    <a href="#icmplockup" title="IcmpLockup">IcmpLockup</a>: <i>Double</i>
    <a href="#icmplockupperiod" title="IcmpLockupPeriod">IcmpLockupPeriod</a>: <i>Double</i>
    <a href="#icmpratelimit" title="IcmpRateLimit">IcmpRateLimit</a>: <i>Double</i>
    <a href="#icmpv6lockup" title="Icmpv6Lockup">Icmpv6Lockup</a>: <i>Double</i>
    <a href="#icmpv6lockupperiod" title="Icmpv6LockupPeriod">Icmpv6LockupPeriod</a>: <i>Double</i>
    <a href="#icmpv6ratelimit" title="Icmpv6RateLimit">Icmpv6RateLimit</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#rateinterval" title="RateInterval">RateInterval</a>: <i>String</i>
    <a href="#subnetgratuitousarp" title="SubnetGratuitousArp">SubnetGratuitousArp</a>: <i>Double</i>
    <a href="#tcpstacktfoactiveconnlimit" title="TcpStackTfoActiveConnLimit">TcpStackTfoActiveConnLimit</a>: <i>Double</i>
    <a href="#tcpstacktfobackofftime" title="TcpStackTfoBackoffTime">TcpStackTfoBackoffTime</a>: <i>Double</i>
    <a href="#tcpstacktfocookietimelimit" title="TcpStackTfoCookieTimeLimit">TcpStackTfoCookieTimeLimit</a>: <i>Double</i>
    <a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
</pre>

## Properties

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

#### ConnLimitReset

Send client reset when connection over limit.

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

#### ConnRateLimitReset

Send client reset when connection rate over limit.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcmpLockup

Enter lockup state when ICMP rate exceeds lockup rate limit (Maximum rate limit. If exceeds this limit, drop all ICMP packet for a time period).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcmpLockupPeriod

Lockup period (second).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcmpRateLimit

ICMP rate limit (Normal rate limit. If exceeds this limit, drop the ICMP packet that goes over the limit).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Icmpv6Lockup

Enter lockup state when ICMP rate exceeds lockup rate limit (Maximum rate limit. If exceeds this limit, drop all ICMP packet for a time period).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Icmpv6LockupPeriod

Lockup period (second).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Icmpv6RateLimit

ICMPv6 rate limit (Normal rate limit. If exceeds this limit, drop the ICMP packet that goes over the limit).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Virtual server template name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateInterval

‘100ms’: Use 100 ms as sampling interval; ‘second’: Use 1 second as sampling interval;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetGratuitousArp

Send gratuitous ARP for every IP in the subnet virtual server.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpStackTfoActiveConnLimit

The allowed active layer 7 tcp fast-open connection limit, default is zero (number).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpStackTfoBackoffTime

The time tcp stack will wait before allowing new fast-open requests after security condition, default 600 seconds (number).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpStackTfoCookieTimeLimit

The time limit (in seconds) that a layer 7 tcp fast-open cookie is valid, default is 60 seconds (number).

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

