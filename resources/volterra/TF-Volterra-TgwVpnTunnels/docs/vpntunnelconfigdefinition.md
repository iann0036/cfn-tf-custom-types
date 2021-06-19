# TF::Volterra::TgwVpnTunnels VpnTunnelConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#nodeid" title="NodeId">NodeId</a>" : <i>String</i>,
    "<a href="#nodename" title="NodeName">NodeName</a>" : <i>String</i>,
    "<a href="#tunnelremoteips" title="TunnelRemoteIps">TunnelRemoteIps</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#nodeid" title="NodeId">NodeId</a>: <i>String</i>
<a href="#nodename" title="NodeName">NodeName</a>: <i>String</i>
<a href="#tunnelremoteips" title="TunnelRemoteIps">TunnelRemoteIps</a>: <i>
      - String</i>
</pre>

## Properties

#### NodeId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelRemoteIps

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

