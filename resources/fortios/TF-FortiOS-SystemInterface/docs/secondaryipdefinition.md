# TF::FortiOS::SystemInterface SecondaryipDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowaccess" title="Allowaccess">Allowaccess</a>" : <i>String</i>,
    "<a href="#detectprotocol" title="Detectprotocol">Detectprotocol</a>" : <i>String</i>,
    "<a href="#detectserver" title="Detectserver">Detectserver</a>" : <i>String</i>,
    "<a href="#gwdetect" title="Gwdetect">Gwdetect</a>" : <i>String</i>,
    "<a href="#hapriority" title="HaPriority">HaPriority</a>" : <i>Double</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>,
    "<a href="#pingservstatus" title="PingServStatus">PingServStatus</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#allowaccess" title="Allowaccess">Allowaccess</a>: <i>String</i>
<a href="#detectprotocol" title="Detectprotocol">Detectprotocol</a>: <i>String</i>
<a href="#detectserver" title="Detectserver">Detectserver</a>: <i>String</i>
<a href="#gwdetect" title="Gwdetect">Gwdetect</a>: <i>String</i>
<a href="#hapriority" title="HaPriority">HaPriority</a>: <i>Double</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#ip" title="Ip">Ip</a>: <i>String</i>
<a href="#pingservstatus" title="PingServStatus">PingServStatus</a>: <i>Double</i>
</pre>

## Properties

#### Allowaccess

Management access settings for the secondary IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Detectprotocol

Protocols used to detect the server. Valid values: `ping`, `tcp-echo`, `udp-echo`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Detectserver

Gateway's ping server for this IP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gwdetect

Enable/disable detect gateway alive for first. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaPriority

HA election priority for the PING server.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

Secondary IP address of the interface.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PingServStatus

PING server status.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

