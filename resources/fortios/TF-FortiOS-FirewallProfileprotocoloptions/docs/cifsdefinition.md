# TF::FortiOS::FirewallProfileprotocoloptions CifsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#domaincontroller" title="DomainController">DomainController</a>" : <i>String</i>,
    "<a href="#options" title="Options">Options</a>" : <i>String</i>,
    "<a href="#oversizelimit" title="OversizeLimit">OversizeLimit</a>" : <i>Double</i>,
    "<a href="#ports" title="Ports">Ports</a>" : <i>Double</i>,
    "<a href="#scanbzip2" title="ScanBzip2">ScanBzip2</a>" : <i>String</i>,
    "<a href="#servercredentialtype" title="ServerCredentialType">ServerCredentialType</a>" : <i>String</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#tcpwindowmaximum" title="TcpWindowMaximum">TcpWindowMaximum</a>" : <i>Double</i>,
    "<a href="#tcpwindowminimum" title="TcpWindowMinimum">TcpWindowMinimum</a>" : <i>Double</i>,
    "<a href="#tcpwindowsize" title="TcpWindowSize">TcpWindowSize</a>" : <i>Double</i>,
    "<a href="#tcpwindowtype" title="TcpWindowType">TcpWindowType</a>" : <i>String</i>,
    "<a href="#uncompressednestlimit" title="UncompressedNestLimit">UncompressedNestLimit</a>" : <i>Double</i>,
    "<a href="#uncompressedoversizelimit" title="UncompressedOversizeLimit">UncompressedOversizeLimit</a>" : <i>Double</i>,
    "<a href="#serverkeytab" title="ServerKeytab">ServerKeytab</a>" : <i>[ <a href="serverkeytabdefinition.md">ServerKeytabDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#domaincontroller" title="DomainController">DomainController</a>: <i>String</i>
<a href="#options" title="Options">Options</a>: <i>String</i>
<a href="#oversizelimit" title="OversizeLimit">OversizeLimit</a>: <i>Double</i>
<a href="#ports" title="Ports">Ports</a>: <i>Double</i>
<a href="#scanbzip2" title="ScanBzip2">ScanBzip2</a>: <i>String</i>
<a href="#servercredentialtype" title="ServerCredentialType">ServerCredentialType</a>: <i>String</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#tcpwindowmaximum" title="TcpWindowMaximum">TcpWindowMaximum</a>: <i>Double</i>
<a href="#tcpwindowminimum" title="TcpWindowMinimum">TcpWindowMinimum</a>: <i>Double</i>
<a href="#tcpwindowsize" title="TcpWindowSize">TcpWindowSize</a>: <i>Double</i>
<a href="#tcpwindowtype" title="TcpWindowType">TcpWindowType</a>: <i>String</i>
<a href="#uncompressednestlimit" title="UncompressedNestLimit">UncompressedNestLimit</a>: <i>Double</i>
<a href="#uncompressedoversizelimit" title="UncompressedOversizeLimit">UncompressedOversizeLimit</a>: <i>Double</i>
<a href="#serverkeytab" title="ServerKeytab">ServerKeytab</a>: <i>
      - <a href="serverkeytabdefinition.md">ServerKeytabDefinition</a></i>
</pre>

## Properties

#### DomainController

Domain for which to decrypt CIFS traffic.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Options

One or more options that can be applied to the session. Valid values: `oversize`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OversizeLimit

Maximum in-memory file size that can be scanned (1 - 383 MB, default = 10).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ports

Ports to scan for content (1 - 65535, default = 445).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScanBzip2

Enable/disable scanning of BZip2 compressed files. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerCredentialType

CIFS server credential type. Valid values: `none`, `credential-replication`, `credential-keytab`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable the active status of scanning for this protocol. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpWindowMaximum

Maximum dynamic TCP window size (default = 8MB).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpWindowMinimum

Minimum dynamic TCP window size (default = 128KB).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpWindowSize

Set TCP static window size (default = 256KB).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpWindowType

Specify type of TCP window to use for this protocol. Valid values: `system`, `static`, `dynamic`.

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

#### ServerKeytab

_Required_: No

_Type_: List of <a href="serverkeytabdefinition.md">ServerKeytabDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

