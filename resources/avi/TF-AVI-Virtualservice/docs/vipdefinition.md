# TF::AVI::Virtualservice VipDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autoallocatefloatingip" title="AutoAllocateFloatingIp">AutoAllocateFloatingIp</a>" : <i>Boolean</i>,
    "<a href="#autoallocateip" title="AutoAllocateIp">AutoAllocateIp</a>" : <i>Boolean</i>,
    "<a href="#autoallocateiptype" title="AutoAllocateIpType">AutoAllocateIpType</a>" : <i>String</i>,
    "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
    "<a href="#aviallocatedfip" title="AviAllocatedFip">AviAllocatedFip</a>" : <i>Boolean</i>,
    "<a href="#aviallocatedvip" title="AviAllocatedVip">AviAllocatedVip</a>" : <i>Boolean</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#floatingsubnet6uuid" title="FloatingSubnet6Uuid">FloatingSubnet6Uuid</a>" : <i>String</i>,
    "<a href="#floatingsubnetuuid" title="FloatingSubnetUuid">FloatingSubnetUuid</a>" : <i>String</i>,
    "<a href="#networkref" title="NetworkRef">NetworkRef</a>" : <i>String</i>,
    "<a href="#portuuid" title="PortUuid">PortUuid</a>" : <i>String</i>,
    "<a href="#prefixlength" title="PrefixLength">PrefixLength</a>" : <i>Double</i>,
    "<a href="#subnet6uuid" title="Subnet6Uuid">Subnet6Uuid</a>" : <i>String</i>,
    "<a href="#subnetuuid" title="SubnetUuid">SubnetUuid</a>" : <i>String</i>,
    "<a href="#vipid" title="VipId">VipId</a>" : <i>String</i>,
    "<a href="#discoverednetworks" title="DiscoveredNetworks">DiscoveredNetworks</a>" : <i>[ <a href="discoverednetworksdefinition.md">DiscoveredNetworksDefinition</a>, ... ]</i>,
    "<a href="#floatingip" title="FloatingIp">FloatingIp</a>" : <i>[ <a href="floatingipdefinition.md">FloatingIpDefinition</a>, ... ]</i>,
    "<a href="#floatingip6" title="FloatingIp6">FloatingIp6</a>" : <i>[ <a href="floatingip6definition.md">FloatingIp6Definition</a>, ... ]</i>,
    "<a href="#ip6address" title="Ip6Address">Ip6Address</a>" : <i>[ <a href="ip6addressdefinition.md">Ip6AddressDefinition</a>, ... ]</i>,
    "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>[ <a href="ipaddressdefinition.md">IpAddressDefinition</a>, ... ]</i>,
    "<a href="#ipamnetworksubnet" title="IpamNetworkSubnet">IpamNetworkSubnet</a>" : <i>[ <a href="ipamnetworksubnetdefinition.md">IpamNetworkSubnetDefinition</a>, ... ]</i>,
    "<a href="#placementnetworks" title="PlacementNetworks">PlacementNetworks</a>" : <i>[ <a href="placementnetworksdefinition.md">PlacementNetworksDefinition</a>, ... ]</i>,
    "<a href="#subnet" title="Subnet">Subnet</a>" : <i>[ <a href="subnetdefinition.md">SubnetDefinition</a>, ... ]</i>,
    "<a href="#subnet6" title="Subnet6">Subnet6</a>" : <i>[ <a href="subnet6definition.md">Subnet6Definition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#autoallocatefloatingip" title="AutoAllocateFloatingIp">AutoAllocateFloatingIp</a>: <i>Boolean</i>
<a href="#autoallocateip" title="AutoAllocateIp">AutoAllocateIp</a>: <i>Boolean</i>
<a href="#autoallocateiptype" title="AutoAllocateIpType">AutoAllocateIpType</a>: <i>String</i>
<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
<a href="#aviallocatedfip" title="AviAllocatedFip">AviAllocatedFip</a>: <i>Boolean</i>
<a href="#aviallocatedvip" title="AviAllocatedVip">AviAllocatedVip</a>: <i>Boolean</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#floatingsubnet6uuid" title="FloatingSubnet6Uuid">FloatingSubnet6Uuid</a>: <i>String</i>
<a href="#floatingsubnetuuid" title="FloatingSubnetUuid">FloatingSubnetUuid</a>: <i>String</i>
<a href="#networkref" title="NetworkRef">NetworkRef</a>: <i>String</i>
<a href="#portuuid" title="PortUuid">PortUuid</a>: <i>String</i>
<a href="#prefixlength" title="PrefixLength">PrefixLength</a>: <i>Double</i>
<a href="#subnet6uuid" title="Subnet6Uuid">Subnet6Uuid</a>: <i>String</i>
<a href="#subnetuuid" title="SubnetUuid">SubnetUuid</a>: <i>String</i>
<a href="#vipid" title="VipId">VipId</a>: <i>String</i>
<a href="#discoverednetworks" title="DiscoveredNetworks">DiscoveredNetworks</a>: <i>
      - <a href="discoverednetworksdefinition.md">DiscoveredNetworksDefinition</a></i>
<a href="#floatingip" title="FloatingIp">FloatingIp</a>: <i>
      - <a href="floatingipdefinition.md">FloatingIpDefinition</a></i>
<a href="#floatingip6" title="FloatingIp6">FloatingIp6</a>: <i>
      - <a href="floatingip6definition.md">FloatingIp6Definition</a></i>
<a href="#ip6address" title="Ip6Address">Ip6Address</a>: <i>
      - <a href="ip6addressdefinition.md">Ip6AddressDefinition</a></i>
<a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>
      - <a href="ipaddressdefinition.md">IpAddressDefinition</a></i>
<a href="#ipamnetworksubnet" title="IpamNetworkSubnet">IpamNetworkSubnet</a>: <i>
      - <a href="ipamnetworksubnetdefinition.md">IpamNetworkSubnetDefinition</a></i>
<a href="#placementnetworks" title="PlacementNetworks">PlacementNetworks</a>: <i>
      - <a href="placementnetworksdefinition.md">PlacementNetworksDefinition</a></i>
<a href="#subnet" title="Subnet">Subnet</a>: <i>
      - <a href="subnetdefinition.md">SubnetDefinition</a></i>
<a href="#subnet6" title="Subnet6">Subnet6</a>: <i>
      - <a href="subnet6definition.md">Subnet6Definition</a></i>
</pre>

## Properties

#### AutoAllocateFloatingIp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoAllocateIp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoAllocateIpType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityZone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AviAllocatedFip

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AviAllocatedVip

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FloatingSubnet6Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FloatingSubnetUuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortUuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefixLength

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet6Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetUuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VipId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiscoveredNetworks

_Required_: No

_Type_: List of <a href="discoverednetworksdefinition.md">DiscoveredNetworksDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FloatingIp

_Required_: No

_Type_: List of <a href="floatingipdefinition.md">FloatingIpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FloatingIp6

_Required_: No

_Type_: List of <a href="floatingip6definition.md">FloatingIp6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6Address

_Required_: No

_Type_: List of <a href="ip6addressdefinition.md">Ip6AddressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddress

_Required_: No

_Type_: List of <a href="ipaddressdefinition.md">IpAddressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpamNetworkSubnet

_Required_: No

_Type_: List of <a href="ipamnetworksubnetdefinition.md">IpamNetworkSubnetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlacementNetworks

_Required_: No

_Type_: List of <a href="placementnetworksdefinition.md">PlacementNetworksDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet

_Required_: No

_Type_: List of <a href="subnetdefinition.md">SubnetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet6

_Required_: No

_Type_: List of <a href="subnet6definition.md">Subnet6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

