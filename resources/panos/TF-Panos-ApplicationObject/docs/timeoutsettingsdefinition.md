# TF::Panos::ApplicationObject TimeoutSettingsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#tcphalfclosed" title="TcpHalfClosed">TcpHalfClosed</a>" : <i>Double</i>,
    "<a href="#tcptimewait" title="TcpTimeWait">TcpTimeWait</a>" : <i>Double</i>,
    "<a href="#tcptimeout" title="TcpTimeout">TcpTimeout</a>" : <i>Double</i>,
    "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
    "<a href="#udptimeout" title="UdpTimeout">UdpTimeout</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#tcphalfclosed" title="TcpHalfClosed">TcpHalfClosed</a>: <i>Double</i>
<a href="#tcptimewait" title="TcpTimeWait">TcpTimeWait</a>: <i>Double</i>
<a href="#tcptimeout" title="TcpTimeout">TcpTimeout</a>: <i>Double</i>
<a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
<a href="#udptimeout" title="UdpTimeout">UdpTimeout</a>: <i>Double</i>
</pre>

## Properties

#### TcpHalfClosed

TCP half closed timeout.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpTimeWait

TCP time wait timeout.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpTimeout

TCP timeout.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

The timeout.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UdpTimeout

UDP timeout.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

