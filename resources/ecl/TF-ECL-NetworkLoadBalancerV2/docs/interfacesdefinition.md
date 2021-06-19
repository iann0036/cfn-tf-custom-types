# TF::ECL::NetworkLoadBalancerV2 InterfacesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#networkid" title="NetworkId">NetworkId</a>" : <i>String</i>,
    "<a href="#slotnumber" title="SlotNumber">SlotNumber</a>" : <i>Double</i>,
    "<a href="#virtualipaddress" title="VirtualIpAddress">VirtualIpAddress</a>" : <i>String</i>,
    "<a href="#virtualipproperties" title="VirtualIpProperties">VirtualIpProperties</a>" : <i>[ <a href="virtualippropertiesdefinition.md">VirtualIpPropertiesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#networkid" title="NetworkId">NetworkId</a>: <i>String</i>
<a href="#slotnumber" title="SlotNumber">SlotNumber</a>: <i>Double</i>
<a href="#virtualipaddress" title="VirtualIpAddress">VirtualIpAddress</a>: <i>String</i>
<a href="#virtualipproperties" title="VirtualIpProperties">VirtualIpProperties</a>: <i>
      - <a href="virtualippropertiesdefinition.md">VirtualIpPropertiesDefinition</a></i>
</pre>

## Properties

#### Description

Load Balancer Interface description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddress

The physical IP address associated with the interface.
The IP address must be in the network specified as the argument `network_id`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Load Balancer Interface.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkId

The UUID of the network associated with the interface.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotNumber

The slot number of interface.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualIpAddress

The virtual IP address associated with the interface. The IP address must be in
the network specified as the argument `network_id`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualIpProperties

_Required_: No

_Type_: List of <a href="virtualippropertiesdefinition.md">VirtualIpPropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

