# TF::FortiOS::FirewallVip6 RealserversDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#clientip" title="ClientIp">ClientIp</a>" : <i>String</i>,
    "<a href="#healthcheck" title="Healthcheck">Healthcheck</a>" : <i>String</i>,
    "<a href="#holddowninterval" title="HolddownInterval">HolddownInterval</a>" : <i>Double</i>,
    "<a href="#httphost" title="HttpHost">HttpHost</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>,
    "<a href="#maxconnections" title="MaxConnections">MaxConnections</a>" : <i>Double</i>,
    "<a href="#monitor" title="Monitor">Monitor</a>" : <i>[ <a href="monitordefinition.md">MonitorDefinition</a>, ... ]</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#weight" title="Weight">Weight</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#clientip" title="ClientIp">ClientIp</a>: <i>String</i>
<a href="#healthcheck" title="Healthcheck">Healthcheck</a>: <i>String</i>
<a href="#holddowninterval" title="HolddownInterval">HolddownInterval</a>: <i>Double</i>
<a href="#httphost" title="HttpHost">HttpHost</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#ip" title="Ip">Ip</a>: <i>String</i>
<a href="#maxconnections" title="MaxConnections">MaxConnections</a>: <i>Double</i>
<a href="#monitor" title="Monitor">Monitor</a>: <i>
      - <a href="monitordefinition.md">MonitorDefinition</a></i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#weight" title="Weight">Weight</a>: <i>Double</i>
</pre>

## Properties

#### ClientIp

Only clients in this IP range can connect to this real server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Healthcheck

Enable to check the responsiveness of the real server before forwarding traffic. Valid values: `disable`, `enable`, `vip`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HolddownInterval

Time in seconds that the health check monitor continues to monitor an unresponsive server that should be active.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpHost

HTTP server domain name in HTTP header.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

Real server ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

IPv6 address of the real server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxConnections

Max number of active connections that can directed to the real server. When reached, sessions are sent to other real servers.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Monitor

_Required_: No

_Type_: List of <a href="monitordefinition.md">MonitorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

Port for communicating with the real server. Required if port forwarding is enabled.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Set the status of the real server to active so that it can accept traffic, or on standby or disabled so no traffic is sent. Valid values: `active`, `standby`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Weight

Weight of the real server. If weighted load balancing is enabled, the server with the highest weight gets more connections.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

