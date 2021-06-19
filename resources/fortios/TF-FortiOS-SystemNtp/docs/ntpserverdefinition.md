# TF::FortiOS::SystemNtp NtpserverDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authentication" title="Authentication">Authentication</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#interface" title="Interface">Interface</a>" : <i>[ <a href="interfacedefinition.md">InterfaceDefinition</a>, ... ]</i>,
    "<a href="#interfaceselectmethod" title="InterfaceSelectMethod">InterfaceSelectMethod</a>" : <i>String</i>,
    "<a href="#key" title="Key">Key</a>" : <i>String</i>,
    "<a href="#keyid" title="KeyId">KeyId</a>" : <i>Double</i>,
    "<a href="#ntpv3" title="Ntpv3">Ntpv3</a>" : <i>String</i>,
    "<a href="#server" title="Server">Server</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#authentication" title="Authentication">Authentication</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#interface" title="Interface">Interface</a>: <i>
      - <a href="interfacedefinition.md">InterfaceDefinition</a></i>
<a href="#interfaceselectmethod" title="InterfaceSelectMethod">InterfaceSelectMethod</a>: <i>String</i>
<a href="#key" title="Key">Key</a>: <i>String</i>
<a href="#keyid" title="KeyId">KeyId</a>: <i>Double</i>
<a href="#ntpv3" title="Ntpv3">Ntpv3</a>: <i>String</i>
<a href="#server" title="Server">Server</a>: <i>String</i>
</pre>

## Properties

#### Authentication

Enable/disable MD5/SHA1 authentication. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

NTP server ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface

_Required_: No

_Type_: List of <a href="interfacedefinition.md">InterfaceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterfaceSelectMethod

Specify how to select outgoing interface to reach server. Valid values: `auto`, `sdwan`, `specify`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

Key for MD5/SHA1 authentication.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyId

Key ID for authentication.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ntpv3

Enable to use NTPv3 instead of NTPv4. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Server

IP address or hostname of the NTP Server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

