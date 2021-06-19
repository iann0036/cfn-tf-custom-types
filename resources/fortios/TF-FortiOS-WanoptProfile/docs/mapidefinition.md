# TF::FortiOS::WanoptProfile MapiDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bytecaching" title="ByteCaching">ByteCaching</a>" : <i>String</i>,
    "<a href="#logtraffic" title="LogTraffic">LogTraffic</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#securetunnel" title="SecureTunnel">SecureTunnel</a>" : <i>String</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#tunnelsharing" title="TunnelSharing">TunnelSharing</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#bytecaching" title="ByteCaching">ByteCaching</a>: <i>String</i>
<a href="#logtraffic" title="LogTraffic">LogTraffic</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#securetunnel" title="SecureTunnel">SecureTunnel</a>: <i>String</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#tunnelsharing" title="TunnelSharing">TunnelSharing</a>: <i>String</i>
</pre>

## Properties

#### ByteCaching

Enable/disable byte-caching for HTTP. Byte caching reduces the amount of traffic by caching file data sent across the WAN and in future serving if from the cache. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogTraffic

Enable/disable logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

Single port number or port number range for MAPI. Only packets with a destination port number that matches this port number or range are accepted by this profile.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecureTunnel

Enable/disable securing the WAN Opt tunnel using SSL. Secure and non-secure tunnels use the same TCP port (7810). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable HTTP WAN Optimization. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelSharing

Tunnel sharing mode for aggressive/non-aggressive and/or interactive/non-interactive protocols. Valid values: `private`, `shared`, `express-shared`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

