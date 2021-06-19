# TF::Thunder::SlbTemplateVirtualPort

`thunder_slb_template_virtual_port` Provides details about thunder slb template virtual port

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SlbTemplateVirtualPort",
    "Properties" : {
        "<a href="#aflow" title="Aflow">Aflow</a>" : <i>Double</i>,
        "<a href="#allowsynotherflags" title="AllowSynOtherflags">AllowSynOtherflags</a>" : <i>Double</i>,
        "<a href="#allowviptorportmapping" title="AllowVipToRportMapping">AllowVipToRportMapping</a>" : <i>Double</i>,
        "<a href="#connlimit" title="ConnLimit">ConnLimit</a>" : <i>Double</i>,
        "<a href="#connlimitnologging" title="ConnLimitNoLogging">ConnLimitNoLogging</a>" : <i>Double</i>,
        "<a href="#connlimitreset" title="ConnLimitReset">ConnLimitReset</a>" : <i>Double</i>,
        "<a href="#connratelimit" title="ConnRateLimit">ConnRateLimit</a>" : <i>Double</i>,
        "<a href="#connratelimitnologging" title="ConnRateLimitNoLogging">ConnRateLimitNoLogging</a>" : <i>Double</i>,
        "<a href="#connratelimitreset" title="ConnRateLimitReset">ConnRateLimitReset</a>" : <i>Double</i>,
        "<a href="#dropunknownconn" title="DropUnknownConn">DropUnknownConn</a>" : <i>Double</i>,
        "<a href="#dscp" title="Dscp">Dscp</a>" : <i>Double</i>,
        "<a href="#ignoretcpmsl" title="IgnoreTcpMsl">IgnoreTcpMsl</a>" : <i>Double</i>,
        "<a href="#logoptions" title="LogOptions">LogOptions</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nonsyninitiation" title="NonSynInitiation">NonSynInitiation</a>" : <i>Double</i>,
        "<a href="#pktrateinterval" title="PktRateInterval">PktRateInterval</a>" : <i>String</i>,
        "<a href="#pktratelimitreset" title="PktRateLimitReset">PktRateLimitReset</a>" : <i>Double</i>,
        "<a href="#pktratetype" title="PktRateType">PktRateType</a>" : <i>String</i>,
        "<a href="#rate" title="Rate">Rate</a>" : <i>Double</i>,
        "<a href="#rateinterval" title="RateInterval">RateInterval</a>" : <i>String</i>,
        "<a href="#resetl7onfailover" title="ResetL7OnFailover">ResetL7OnFailover</a>" : <i>Double</i>,
        "<a href="#resetunknownconn" title="ResetUnknownConn">ResetUnknownConn</a>" : <i>Double</i>,
        "<a href="#snatmsl" title="SnatMsl">SnatMsl</a>" : <i>Double</i>,
        "<a href="#snatportpreserve" title="SnatPortPreserve">SnatPortPreserve</a>" : <i>Double</i>,
        "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#whenrrenable" title="WhenRrEnable">WhenRrEnable</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SlbTemplateVirtualPort
Properties:
    <a href="#aflow" title="Aflow">Aflow</a>: <i>Double</i>
    <a href="#allowsynotherflags" title="AllowSynOtherflags">AllowSynOtherflags</a>: <i>Double</i>
    <a href="#allowviptorportmapping" title="AllowVipToRportMapping">AllowVipToRportMapping</a>: <i>Double</i>
    <a href="#connlimit" title="ConnLimit">ConnLimit</a>: <i>Double</i>
    <a href="#connlimitnologging" title="ConnLimitNoLogging">ConnLimitNoLogging</a>: <i>Double</i>
    <a href="#connlimitreset" title="ConnLimitReset">ConnLimitReset</a>: <i>Double</i>
    <a href="#connratelimit" title="ConnRateLimit">ConnRateLimit</a>: <i>Double</i>
    <a href="#connratelimitnologging" title="ConnRateLimitNoLogging">ConnRateLimitNoLogging</a>: <i>Double</i>
    <a href="#connratelimitreset" title="ConnRateLimitReset">ConnRateLimitReset</a>: <i>Double</i>
    <a href="#dropunknownconn" title="DropUnknownConn">DropUnknownConn</a>: <i>Double</i>
    <a href="#dscp" title="Dscp">Dscp</a>: <i>Double</i>
    <a href="#ignoretcpmsl" title="IgnoreTcpMsl">IgnoreTcpMsl</a>: <i>Double</i>
    <a href="#logoptions" title="LogOptions">LogOptions</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nonsyninitiation" title="NonSynInitiation">NonSynInitiation</a>: <i>Double</i>
    <a href="#pktrateinterval" title="PktRateInterval">PktRateInterval</a>: <i>String</i>
    <a href="#pktratelimitreset" title="PktRateLimitReset">PktRateLimitReset</a>: <i>Double</i>
    <a href="#pktratetype" title="PktRateType">PktRateType</a>: <i>String</i>
    <a href="#rate" title="Rate">Rate</a>: <i>Double</i>
    <a href="#rateinterval" title="RateInterval">RateInterval</a>: <i>String</i>
    <a href="#resetl7onfailover" title="ResetL7OnFailover">ResetL7OnFailover</a>: <i>Double</i>
    <a href="#resetunknownconn" title="ResetUnknownConn">ResetUnknownConn</a>: <i>Double</i>
    <a href="#snatmsl" title="SnatMsl">SnatMsl</a>: <i>Double</i>
    <a href="#snatportpreserve" title="SnatPortPreserve">SnatPortPreserve</a>: <i>Double</i>
    <a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#whenrrenable" title="WhenRrEnable">WhenRrEnable</a>: <i>Double</i>
</pre>

## Properties

#### Aflow

Use aFlow to eliminate the traffic surge.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowSynOtherflags

Allow initial SYN packet with other flags.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowVipToRportMapping

Allow mapping of VIP to real port.

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

#### DropUnknownConn

Drop conection if receives TCP packet without SYN or RST flag and it does not belong to any existing connections.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dscp

Differentiated Services Code Point (DSCP to Real Server IP Mapping Value).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreTcpMsl

reclaim TCP resource immediately without MSL.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogOptions

‘no-logging’: Do not log over limit event; ‘no-repeat-logging’: log once for over limit event. Default is log once per minute;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Virtual port template name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NonSynInitiation

Allow initial TCP packet to be non-SYN.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PktRateInterval

‘100ms’: Source IP and port rate limit per 100ms; ‘second’: Source IP and port rate limit per second (default);.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PktRateLimitReset

send client-side reset (reset after packet limit).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PktRateType

‘src-ip-port’: Source IP and port rate limit; ‘src-port’: Source port rate limit;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rate

Source IP and port rate limit (Packet rate limit).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateInterval

‘100ms’: Use 100 ms as sampling interval; ‘second’: Use 1 second as sampling interval;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResetL7OnFailover

Send reset to L7 client and server connection upon a failover.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResetUnknownConn

Send reset back if receives TCP packet without SYN or RST flag and it does not belong to any existing connections.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnatMsl

Source NAT MSL (Source NAT MSL value).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnatPortPreserve

Source NAT Port Preservation.

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

#### WhenRrEnable

Only do rate limit if CPU RR triggered.

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

