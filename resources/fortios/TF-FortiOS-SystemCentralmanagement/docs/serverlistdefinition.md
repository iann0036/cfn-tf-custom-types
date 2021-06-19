# TF::FortiOS::SystemCentralmanagement ServerListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#addrtype" title="AddrType">AddrType</a>" : <i>String</i>,
    "<a href="#fqdn" title="Fqdn">Fqdn</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#serveraddress" title="ServerAddress">ServerAddress</a>" : <i>String</i>,
    "<a href="#serveraddress6" title="ServerAddress6">ServerAddress6</a>" : <i>String</i>,
    "<a href="#servertype" title="ServerType">ServerType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#addrtype" title="AddrType">AddrType</a>: <i>String</i>
<a href="#fqdn" title="Fqdn">Fqdn</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#serveraddress" title="ServerAddress">ServerAddress</a>: <i>String</i>
<a href="#serveraddress6" title="ServerAddress6">ServerAddress6</a>: <i>String</i>
<a href="#servertype" title="ServerType">ServerType</a>: <i>String</i>
</pre>

## Properties

#### AddrType

Indicate whether the FortiGate communicates with the override server using an IPv4 address, an IPv6 address or a FQDN. Valid values: `ipv4`, `ipv6`, `fqdn`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fqdn

FQDN address of override server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerAddress

IPv4 address of override server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerAddress6

IPv6 address of override server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerType

FortiGuard service type. Valid values: `update`, `rating`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

