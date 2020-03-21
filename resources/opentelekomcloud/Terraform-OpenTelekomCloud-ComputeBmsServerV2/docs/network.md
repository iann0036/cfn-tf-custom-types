# Terraform::OpenTelekomCloud::ComputeBmsServerV2 Network

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accessnetwork" title="AccessNetwork">AccessNetwork</a>" : <i>Boolean</i>,
    "<a href="#fixedipv4" title="FixedIpV4">FixedIpV4</a>" : <i>String</i>,
    "<a href="#fixedipv6" title="FixedIpV6">FixedIpV6</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>String</i>,
    "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#accessnetwork" title="AccessNetwork">AccessNetwork</a>: <i>Boolean</i>
<a href="#fixedipv4" title="FixedIpV4">FixedIpV4</a>: <i>String</i>
<a href="#fixedipv6" title="FixedIpV6">FixedIpV6</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>String</i>
<a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
</pre>

## Properties

#### AccessNetwork

Specifies if this network should be used for
provisioning access. Accepts true or false. Defaults to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FixedIpV4

Specifies a fixed IPv4 address to be used on this
network. Changing this creates a new bms server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FixedIpV6

Specifies a fixed IPv6 address to be used on this
network. Changing this creates a new bms server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The human-readable
name of the network. Changing this creates a new bms server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

The port UUID of a
network to attach to the bms server. Changing this creates a new server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

The network UUID to
attach to the bms server. Changing this creates a new bms server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

