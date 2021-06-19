# TF::Thunder::RouterBgp NeighborDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#tempval" title="TempVal">TempVal</a>" : <i>String</i>,
    "<a href="#distance" title="Distance">Distance</a>" : <i>[ <a href="distancedefinition.md">DistanceDefinition</a>, ... ]</i>,
    "<a href="#ethernetneighboripv6list" title="EthernetNeighborIpv6List">EthernetNeighborIpv6List</a>" : <i>[ <a href="ethernetneighboripv6listdefinition.md">EthernetNeighborIpv6ListDefinition</a>, ... ]</i>,
    "<a href="#ipv4neighborlist" title="Ipv4NeighborList">Ipv4NeighborList</a>" : <i>[ <a href="ipv4neighborlistdefinition.md">Ipv4NeighborListDefinition</a>, ... ]</i>,
    "<a href="#ipv6neighborlist" title="Ipv6NeighborList">Ipv6NeighborList</a>" : <i>[ <a href="ipv6neighborlistdefinition.md">Ipv6NeighborListDefinition</a>, ... ]</i>,
    "<a href="#peergroupneighborlist" title="PeerGroupNeighborList">PeerGroupNeighborList</a>" : <i>[ <a href="peergroupneighborlistdefinition.md">PeerGroupNeighborListDefinition</a>, ... ]</i>,
    "<a href="#trunkneighboripv6list" title="TrunkNeighborIpv6List">TrunkNeighborIpv6List</a>" : <i>[ <a href="trunkneighboripv6listdefinition.md">TrunkNeighborIpv6ListDefinition</a>, ... ]</i>,
    "<a href="#veneighboripv6list" title="VeNeighborIpv6List">VeNeighborIpv6List</a>" : <i>[ <a href="veneighboripv6listdefinition.md">VeNeighborIpv6ListDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#tempval" title="TempVal">TempVal</a>: <i>String</i>
<a href="#distance" title="Distance">Distance</a>: <i>
      - <a href="distancedefinition.md">DistanceDefinition</a></i>
<a href="#ethernetneighboripv6list" title="EthernetNeighborIpv6List">EthernetNeighborIpv6List</a>: <i>
      - <a href="ethernetneighboripv6listdefinition.md">EthernetNeighborIpv6ListDefinition</a></i>
<a href="#ipv4neighborlist" title="Ipv4NeighborList">Ipv4NeighborList</a>: <i>
      - <a href="ipv4neighborlistdefinition.md">Ipv4NeighborListDefinition</a></i>
<a href="#ipv6neighborlist" title="Ipv6NeighborList">Ipv6NeighborList</a>: <i>
      - <a href="ipv6neighborlistdefinition.md">Ipv6NeighborListDefinition</a></i>
<a href="#peergroupneighborlist" title="PeerGroupNeighborList">PeerGroupNeighborList</a>: <i>
      - <a href="peergroupneighborlistdefinition.md">PeerGroupNeighborListDefinition</a></i>
<a href="#trunkneighboripv6list" title="TrunkNeighborIpv6List">TrunkNeighborIpv6List</a>: <i>
      - <a href="trunkneighboripv6listdefinition.md">TrunkNeighborIpv6ListDefinition</a></i>
<a href="#veneighboripv6list" title="VeNeighborIpv6List">VeNeighborIpv6List</a>: <i>
      - <a href="veneighboripv6listdefinition.md">VeNeighborIpv6ListDefinition</a></i>
</pre>

## Properties

#### TempVal

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Distance

_Required_: No

_Type_: List of <a href="distancedefinition.md">DistanceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EthernetNeighborIpv6List

_Required_: No

_Type_: List of <a href="ethernetneighboripv6listdefinition.md">EthernetNeighborIpv6ListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4NeighborList

_Required_: No

_Type_: List of <a href="ipv4neighborlistdefinition.md">Ipv4NeighborListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6NeighborList

_Required_: No

_Type_: List of <a href="ipv6neighborlistdefinition.md">Ipv6NeighborListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerGroupNeighborList

_Required_: No

_Type_: List of <a href="peergroupneighborlistdefinition.md">PeerGroupNeighborListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrunkNeighborIpv6List

_Required_: No

_Type_: List of <a href="trunkneighboripv6listdefinition.md">TrunkNeighborIpv6ListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VeNeighborIpv6List

_Required_: No

_Type_: List of <a href="veneighboripv6listdefinition.md">VeNeighborIpv6ListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

