# TF::FortiOS::FirewallProfileprotocoloptions FtpDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#comfortamount" title="ComfortAmount">ComfortAmount</a>" : <i>Double</i>,
    "<a href="#comfortinterval" title="ComfortInterval">ComfortInterval</a>" : <i>Double</i>,
    "<a href="#inspectall" title="InspectAll">InspectAll</a>" : <i>String</i>,
    "<a href="#options" title="Options">Options</a>" : <i>String</i>,
    "<a href="#oversizelimit" title="OversizeLimit">OversizeLimit</a>" : <i>Double</i>,
    "<a href="#ports" title="Ports">Ports</a>" : <i>Double</i>,
    "<a href="#scanbzip2" title="ScanBzip2">ScanBzip2</a>" : <i>String</i>,
    "<a href="#ssloffloaded" title="SslOffloaded">SslOffloaded</a>" : <i>String</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#streambaseduncompressedlimit" title="StreamBasedUncompressedLimit">StreamBasedUncompressedLimit</a>" : <i>Double</i>,
    "<a href="#tcpwindowmaximum" title="TcpWindowMaximum">TcpWindowMaximum</a>" : <i>Double</i>,
    "<a href="#tcpwindowminimum" title="TcpWindowMinimum">TcpWindowMinimum</a>" : <i>Double</i>,
    "<a href="#tcpwindowsize" title="TcpWindowSize">TcpWindowSize</a>" : <i>Double</i>,
    "<a href="#tcpwindowtype" title="TcpWindowType">TcpWindowType</a>" : <i>String</i>,
    "<a href="#uncompressednestlimit" title="UncompressedNestLimit">UncompressedNestLimit</a>" : <i>Double</i>,
    "<a href="#uncompressedoversizelimit" title="UncompressedOversizeLimit">UncompressedOversizeLimit</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#comfortamount" title="ComfortAmount">ComfortAmount</a>: <i>Double</i>
<a href="#comfortinterval" title="ComfortInterval">ComfortInterval</a>: <i>Double</i>
<a href="#inspectall" title="InspectAll">InspectAll</a>: <i>String</i>
<a href="#options" title="Options">Options</a>: <i>String</i>
<a href="#oversizelimit" title="OversizeLimit">OversizeLimit</a>: <i>Double</i>
<a href="#ports" title="Ports">Ports</a>: <i>Double</i>
<a href="#scanbzip2" title="ScanBzip2">ScanBzip2</a>: <i>String</i>
<a href="#ssloffloaded" title="SslOffloaded">SslOffloaded</a>: <i>String</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#streambaseduncompressedlimit" title="StreamBasedUncompressedLimit">StreamBasedUncompressedLimit</a>: <i>Double</i>
<a href="#tcpwindowmaximum" title="TcpWindowMaximum">TcpWindowMaximum</a>: <i>Double</i>
<a href="#tcpwindowminimum" title="TcpWindowMinimum">TcpWindowMinimum</a>: <i>Double</i>
<a href="#tcpwindowsize" title="TcpWindowSize">TcpWindowSize</a>: <i>Double</i>
<a href="#tcpwindowtype" title="TcpWindowType">TcpWindowType</a>: <i>String</i>
<a href="#uncompressednestlimit" title="UncompressedNestLimit">UncompressedNestLimit</a>: <i>Double</i>
<a href="#uncompressedoversizelimit" title="UncompressedOversizeLimit">UncompressedOversizeLimit</a>: <i>Double</i>
</pre>

## Properties

#### ComfortAmount

Amount of data to send in a transmission for client comforting (1 - 10240 bytes, default = 1).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComfortInterval

Period of time between start, or last transmission, and the next client comfort transmission of data (1 - 900 sec, default = 10).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InspectAll

Enable/disable the inspection of all ports for the protocol. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Options

One or more options that can be applied to the session. Valid values: `clientcomfort`, `oversize`, `splice`, `bypass-rest-command`, `bypass-mode-command`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OversizeLimit

Maximum in-memory file size that can be scanned (1 - 383 MB, default = 10).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ports

Ports to scan for content (1 - 65535, default = 21).

_Required_: No

_Type_: Double

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

#### StreamBasedUncompressedLimit

Maximum stream-based uncompressed data size that will be scanned (MB, 0 = unlimited (default).  Stream-based uncompression used only under certain conditions.).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpWindowMaximum

Maximum dynamic TCP window size.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpWindowMinimum

Minimum dynamic TCP window size.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpWindowSize

Set TCP static window size.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpWindowType

TCP window type to use for this protocol. Valid values: `system`, `static`, `dynamic`.

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

