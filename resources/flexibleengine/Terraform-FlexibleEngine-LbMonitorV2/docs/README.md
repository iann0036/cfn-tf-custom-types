# Terraform::FlexibleEngine::LbMonitorV2

Manages a V2 monitor resource within FlexibleEngine.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::FlexibleEngine::LbMonitorV2",
    "Properties" : {
        "<a href="#adminstateup" title="AdminStateUp">AdminStateUp</a>" : <i>Boolean</i>,
        "<a href="#delay" title="Delay">Delay</a>" : <i>Double</i>,
        "<a href="#expectedcodes" title="ExpectedCodes">ExpectedCodes</a>" : <i>String</i>,
        "<a href="#httpmethod" title="HttpMethod">HttpMethod</a>" : <i>String</i>,
        "<a href="#maxretries" title="MaxRetries">MaxRetries</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#poolid" title="PoolId">PoolId</a>" : <i>String</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>,
        "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#urlpath" title="UrlPath">UrlPath</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::FlexibleEngine::LbMonitorV2
Properties:
    <a href="#adminstateup" title="AdminStateUp">AdminStateUp</a>: <i>Boolean</i>
    <a href="#delay" title="Delay">Delay</a>: <i>Double</i>
    <a href="#expectedcodes" title="ExpectedCodes">ExpectedCodes</a>: <i>String</i>
    <a href="#httpmethod" title="HttpMethod">HttpMethod</a>: <i>String</i>
    <a href="#maxretries" title="MaxRetries">MaxRetries</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#poolid" title="PoolId">PoolId</a>: <i>String</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#tenantid" title="TenantId">TenantId</a>: <i>String</i>
    <a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#urlpath" title="UrlPath">UrlPath</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AdminStateUp

The administrative state of the monitor.
A valid value is true (UP) or false (DOWN).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Delay

The time, in seconds, between sending probes to members.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpectedCodes

Required for HTTP(S) types. Expected HTTP codes
for a passing HTTP(S) monitor. You can either specify a single status like
"200", or a range like "200-202".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpMethod

Required for HTTP(S) types. The HTTP method used
for requests by the monitor. If this attribute is not specified, it
defaults to "GET".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxRetries

Number of permissible ping failures before
changing the member's status to INACTIVE. Must be a number between 1
and 10..

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The Name of the Monitor.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PoolId

The id of the pool that this monitor will be assigned to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

Specifies the health check port. The value ranges from 1 to 65536.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
`region` argument of the provider is used. Changing this creates a new
monitor.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

Required for admins. The UUID of the tenant who owns
the monitor.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new monitor.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

Maximum number of seconds for a monitor to wait for a
ping reply before it times out. The value must be less than the delay
value.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of probe, which is PING, TCP, HTTP, or HTTPS,
that is sent by the load balancer to verify the member state. Changing this
creates a new monitor.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlPath

Required for HTTP(S) types. URI path that will be
accessed if monitor type is HTTP or HTTPS.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

