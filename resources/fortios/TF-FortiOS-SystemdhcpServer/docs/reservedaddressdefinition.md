# TF::FortiOS::SystemdhcpServer ReservedAddressDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#circuitid" title="CircuitId">CircuitId</a>" : <i>String</i>,
    "<a href="#circuitidtype" title="CircuitIdType">CircuitIdType</a>" : <i>String</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>,
    "<a href="#mac" title="Mac">Mac</a>" : <i>String</i>,
    "<a href="#remoteid" title="RemoteId">RemoteId</a>" : <i>String</i>,
    "<a href="#remoteidtype" title="RemoteIdType">RemoteIdType</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#circuitid" title="CircuitId">CircuitId</a>: <i>String</i>
<a href="#circuitidtype" title="CircuitIdType">CircuitIdType</a>: <i>String</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#ip" title="Ip">Ip</a>: <i>String</i>
<a href="#mac" title="Mac">Mac</a>: <i>String</i>
<a href="#remoteid" title="RemoteId">RemoteId</a>: <i>String</i>
<a href="#remoteidtype" title="RemoteIdType">RemoteIdType</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### Action

Options for the DHCP server to configure the client with the reserved MAC address. Valid values: `assign`, `block`, `reserved`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CircuitId

Option 82 circuit-ID of the client that will get the reserved IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CircuitIdType

DHCP option type. Valid values: `hex`, `string`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

IP address to be reserved for the MAC address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mac

MAC address of the client that will get the reserved IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteId

Option 82 remote-ID of the client that will get the reserved IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteIdType

DHCP option type. Valid values: `hex`, `string`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

DHCP reserved-address type. Valid values: `mac`, `option82`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

