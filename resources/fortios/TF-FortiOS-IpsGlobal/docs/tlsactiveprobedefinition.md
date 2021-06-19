# TF::FortiOS::IpsGlobal TlsActiveProbeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#interface" title="Interface">Interface</a>" : <i>String</i>,
    "<a href="#interfaceselectmethod" title="InterfaceSelectMethod">InterfaceSelectMethod</a>" : <i>String</i>,
    "<a href="#sourceip" title="SourceIp">SourceIp</a>" : <i>String</i>,
    "<a href="#sourceip6" title="SourceIp6">SourceIp6</a>" : <i>String</i>,
    "<a href="#vdom" title="Vdom">Vdom</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#interface" title="Interface">Interface</a>: <i>String</i>
<a href="#interfaceselectmethod" title="InterfaceSelectMethod">InterfaceSelectMethod</a>: <i>String</i>
<a href="#sourceip" title="SourceIp">SourceIp</a>: <i>String</i>
<a href="#sourceip6" title="SourceIp6">SourceIp6</a>: <i>String</i>
<a href="#vdom" title="Vdom">Vdom</a>: <i>String</i>
</pre>

## Properties

#### Interface

Specify outgoing interface to reach server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterfaceSelectMethod

Specify how to select outgoing interface to reach server. Valid values: `auto`, `sdwan`, `specify`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIp

Source IP address used for TLS active probe.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIp6

Source IPv6 address used for TLS active probe.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdom

Virtual domain name for TLS active probe.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

