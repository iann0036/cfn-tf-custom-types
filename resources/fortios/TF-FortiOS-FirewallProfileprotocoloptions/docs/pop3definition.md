# TF::FortiOS::FirewallProfileprotocoloptions Pop3Definition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#inspectall" title="InspectAll">InspectAll</a>" : <i>String</i>,
    "<a href="#options" title="Options">Options</a>" : <i>String</i>,
    "<a href="#oversizelimit" title="OversizeLimit">OversizeLimit</a>" : <i>Double</i>,
    "<a href="#ports" title="Ports">Ports</a>" : <i>Double</i>,
    "<a href="#proxyaftertcphandshake" title="ProxyAfterTcpHandshake">ProxyAfterTcpHandshake</a>" : <i>String</i>,
    "<a href="#scanbzip2" title="ScanBzip2">ScanBzip2</a>" : <i>String</i>,
    "<a href="#ssloffloaded" title="SslOffloaded">SslOffloaded</a>" : <i>String</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#uncompressednestlimit" title="UncompressedNestLimit">UncompressedNestLimit</a>" : <i>Double</i>,
    "<a href="#uncompressedoversizelimit" title="UncompressedOversizeLimit">UncompressedOversizeLimit</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#inspectall" title="InspectAll">InspectAll</a>: <i>String</i>
<a href="#options" title="Options">Options</a>: <i>String</i>
<a href="#oversizelimit" title="OversizeLimit">OversizeLimit</a>: <i>Double</i>
<a href="#ports" title="Ports">Ports</a>: <i>Double</i>
<a href="#proxyaftertcphandshake" title="ProxyAfterTcpHandshake">ProxyAfterTcpHandshake</a>: <i>String</i>
<a href="#scanbzip2" title="ScanBzip2">ScanBzip2</a>: <i>String</i>
<a href="#ssloffloaded" title="SslOffloaded">SslOffloaded</a>: <i>String</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#uncompressednestlimit" title="UncompressedNestLimit">UncompressedNestLimit</a>: <i>Double</i>
<a href="#uncompressedoversizelimit" title="UncompressedOversizeLimit">UncompressedOversizeLimit</a>: <i>Double</i>
</pre>

## Properties

#### InspectAll

Enable/disable the inspection of all ports for the protocol. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Options

One or more options that can be applied to the session. Valid values: `fragmail`, `oversize`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OversizeLimit

Maximum in-memory file size that can be scanned (1 - 383 MB, default = 10).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ports

Ports to scan for content (1 - 65535, default = 110).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyAfterTcpHandshake

Proxy traffic after the TCP 3-way handshake has been established (not before). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScanBzip2

Enable/disable scanning of BZip2 compressed files. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslOffloaded

SSL decryption and encryption performed by an external device. Valid values: `no`, `yes`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable the active status of scanning for this protocol. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UncompressedNestLimit

Maximum nested levels of compression that can be uncompressed and scanned (2 - 100, default = 12).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UncompressedOversizeLimit

Maximum in-memory uncompressed file size that can be scanned (0 - 383 MB, 0 = unlimited, default = 10).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

