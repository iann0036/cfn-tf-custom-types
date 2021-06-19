# TF::FortiOS::FirewallSslsshprofile SshDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#inspectall" title="InspectAll">InspectAll</a>" : <i>String</i>,
    "<a href="#ports" title="Ports">Ports</a>" : <i>String</i>,
    "<a href="#proxyaftertcphandshake" title="ProxyAfterTcpHandshake">ProxyAfterTcpHandshake</a>" : <i>String</i>,
    "<a href="#sshalgorithm" title="SshAlgorithm">SshAlgorithm</a>" : <i>String</i>,
    "<a href="#sshpolicycheck" title="SshPolicyCheck">SshPolicyCheck</a>" : <i>String</i>,
    "<a href="#sshtunpolicycheck" title="SshTunPolicyCheck">SshTunPolicyCheck</a>" : <i>String</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#unsupportedversion" title="UnsupportedVersion">UnsupportedVersion</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#inspectall" title="InspectAll">InspectAll</a>: <i>String</i>
<a href="#ports" title="Ports">Ports</a>: <i>String</i>
<a href="#proxyaftertcphandshake" title="ProxyAfterTcpHandshake">ProxyAfterTcpHandshake</a>: <i>String</i>
<a href="#sshalgorithm" title="SshAlgorithm">SshAlgorithm</a>: <i>String</i>
<a href="#sshpolicycheck" title="SshPolicyCheck">SshPolicyCheck</a>: <i>String</i>
<a href="#sshtunpolicycheck" title="SshTunPolicyCheck">SshTunPolicyCheck</a>: <i>String</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#unsupportedversion" title="UnsupportedVersion">UnsupportedVersion</a>: <i>String</i>
</pre>

## Properties

#### InspectAll

Level of SSL inspection. Valid values: `disable`, `deep-inspection`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ports

Ports to use for scanning (1 - 65535, default = 443).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyAfterTcpHandshake

Proxy traffic after the TCP 3-way handshake has been established (not before). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshAlgorithm

Relative strength of encryption algorithms accepted during negotiation. Valid values: `compatible`, `high-encryption`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshPolicyCheck

Enable/disable SSH policy check. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshTunPolicyCheck

Enable/disable SSH tunnel policy check. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Configure protocol inspection status. Valid values: `disable`, `deep-inspection`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnsupportedVersion

Action based on SSH version being unsupported. Valid values: `bypass`, `block`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

