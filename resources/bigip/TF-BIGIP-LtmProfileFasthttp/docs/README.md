# TF::BIGIP::LtmProfileFasthttp

`bigip_ltm_profile_fasthttp` Configures a custom profile_fasthttp for use by health checks.

For resources should be named with their "full path". The full path is the combination of the partition + name of the resource. For example /Common/my-pool.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::BIGIP::LtmProfileFasthttp",
    "Properties" : {
        "<a href="#connpoolmaxreuse" title="ConnpoolMaxreuse">ConnpoolMaxreuse</a>" : <i>Double</i>,
        "<a href="#connpoolmaxsize" title="ConnpoolMaxsize">ConnpoolMaxsize</a>" : <i>Double</i>,
        "<a href="#connpoolminsize" title="ConnpoolMinsize">ConnpoolMinsize</a>" : <i>Double</i>,
        "<a href="#connpoolreplenish" title="ConnpoolReplenish">ConnpoolReplenish</a>" : <i>String</i>,
        "<a href="#connpoolstep" title="ConnpoolStep">ConnpoolStep</a>" : <i>Double</i>,
        "<a href="#connpoolidletimeoutoverride" title="ConnpoolidleTimeoutoverride">ConnpoolidleTimeoutoverride</a>" : <i>Double</i>,
        "<a href="#defaultsfrom" title="DefaultsFrom">DefaultsFrom</a>" : <i>String</i>,
        "<a href="#forcehttp10response" title="Forcehttp10response">Forcehttp10response</a>" : <i>String</i>,
        "<a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>" : <i>Double</i>,
        "<a href="#maxheadersize" title="MaxheaderSize">MaxheaderSize</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::BIGIP::LtmProfileFasthttp
Properties:
    <a href="#connpoolmaxreuse" title="ConnpoolMaxreuse">ConnpoolMaxreuse</a>: <i>Double</i>
    <a href="#connpoolmaxsize" title="ConnpoolMaxsize">ConnpoolMaxsize</a>: <i>Double</i>
    <a href="#connpoolminsize" title="ConnpoolMinsize">ConnpoolMinsize</a>: <i>Double</i>
    <a href="#connpoolreplenish" title="ConnpoolReplenish">ConnpoolReplenish</a>: <i>String</i>
    <a href="#connpoolstep" title="ConnpoolStep">ConnpoolStep</a>: <i>Double</i>
    <a href="#connpoolidletimeoutoverride" title="ConnpoolidleTimeoutoverride">ConnpoolidleTimeoutoverride</a>: <i>Double</i>
    <a href="#defaultsfrom" title="DefaultsFrom">DefaultsFrom</a>: <i>String</i>
    <a href="#forcehttp10response" title="Forcehttp10response">Forcehttp10response</a>: <i>String</i>
    <a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>: <i>Double</i>
    <a href="#maxheadersize" title="MaxheaderSize">MaxheaderSize</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### ConnpoolMaxreuse

Specifies the maximum number of times that the system can re-use a current connection. The default value is 0 (zero).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnpoolMaxsize

Specifies the maximum number of connections to a load balancing pool. A setting of 0 specifies that a pool can accept an unlimited number of connections. The default value is 2048.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnpoolMinsize

Specifies the minimum number of connections to a load balancing pool. A setting of 0 specifies that there is no minimum. The default value is 10.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnpoolReplenish

The default value is enabled. When this option is enabled, the system replenishes the number of connections to a load balancing pool to the number of connections that existed when the server closed the connection to the pool. When disabled, the system replenishes the connection that was closed by the server, only when there are fewer connections to the pool than the number of connections set in the connpool-min-size connections option. Also see the connpool-min-size option..

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnpoolStep

Specifies the increment in which the system makes additional connections available, when all available connections are in use. The default value is 4.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnpoolidleTimeoutoverride

Specifies the number of seconds after which a server-side connection in a OneConnect pool is eligible for deletion, when the connection has no traffic.The value of this option overrides the idle-timeout value that you specify. The default value is 0 (zero) seconds, which disables the override setting.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultsFrom

Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Forcehttp10response

Specifies whether to rewrite the HTTP version in the status line of the server to HTTP 1.0 to discourage the client from pipelining or chunking data. The default value is disabled.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdleTimeout

Specifies an idle timeout in seconds. This setting specifies the number of seconds that a connection is idle before the connection is eligible for deletion.When you specify an idle timeout for the Fast L4 profile, the value must be greater than the bigdb database variable Pva.Scrub time in msec for it to work properly.The default value is 300 seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxheaderSize

Specifies the maximum amount of HTTP header data that the system buffers before making a load balancing decision. The default setting is 32768.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

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

