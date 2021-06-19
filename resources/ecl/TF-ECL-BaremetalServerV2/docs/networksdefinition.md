# TF::ECL::BaremetalServerV2 NetworksDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#fixedip" title="FixedIp">FixedIp</a>" : <i>String</i>,
    "<a href="#plane" title="Plane">Plane</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>String</i>,
    "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#fixedip" title="FixedIp">FixedIp</a>: <i>String</i>
<a href="#plane" title="Plane">Plane</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>String</i>
<a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
</pre>

## Properties

#### FixedIp

Specifies a fixed IPv4 address to be used on this
network. Changing this creates a new server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Plane

The port UUID of a
network to attach to the server. Changing this creates a new server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

The port UUID of a
network to attach to the server. Changing this creates a new server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

The network UUID to
attach to the server. Changing this creates a new server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

