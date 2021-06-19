# TF::AVI::Serviceengine MgmtVnicDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#adapter" title="Adapter">Adapter</a>" : <i>String</i>,
    "<a href="#aggregatorchgd" title="AggregatorChgd">AggregatorChgd</a>" : <i>Boolean</i>,
    "<a href="#cansedptakeover" title="CanSeDpTakeover">CanSeDpTakeover</a>" : <i>Boolean</i>,
    "<a href="#connected" title="Connected">Connected</a>" : <i>Boolean</i>,
    "<a href="#delpending" title="DelPending">DelPending</a>" : <i>Boolean</i>,
    "<a href="#deletevnic" title="DeleteVnic">DeleteVnic</a>" : <i>Boolean</i>,
    "<a href="#dhcpenabled" title="DhcpEnabled">DhcpEnabled</a>" : <i>Boolean</i>,
    "<a href="#dpdeletiondone" title="DpDeletionDone">DpDeletionDone</a>" : <i>Boolean</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#ifname" title="IfName">IfName</a>" : <i>String</i>,
    "<a href="#ip6autocfgenabled" title="Ip6AutocfgEnabled">Ip6AutocfgEnabled</a>" : <i>Boolean</i>,
    "<a href="#isasm" title="IsAsm">IsAsm</a>" : <i>Boolean</i>,
    "<a href="#isaviinternalnetwork" title="IsAviInternalNetwork">IsAviInternalNetwork</a>" : <i>Boolean</i>,
    "<a href="#ishsm" title="IsHsm">IsHsm</a>" : <i>Boolean</i>,
    "<a href="#ismgmt" title="IsMgmt">IsMgmt</a>" : <i>Boolean</i>,
    "<a href="#isportchannel" title="IsPortchannel">IsPortchannel</a>" : <i>Boolean</i>,
    "<a href="#linkup" title="LinkUp">LinkUp</a>" : <i>Boolean</i>,
    "<a href="#linuxname" title="LinuxName">LinuxName</a>" : <i>String</i>,
    "<a href="#macaddress" title="MacAddress">MacAddress</a>" : <i>String</i>,
    "<a href="#mtu" title="Mtu">Mtu</a>" : <i>Double</i>,
    "<a href="#networkname" title="NetworkName">NetworkName</a>" : <i>String</i>,
    "<a href="#networkref" title="NetworkRef">NetworkRef</a>" : <i>String</i>,
    "<a href="#pciid" title="PciId">PciId</a>" : <i>String</i>,
    "<a href="#portuuid" title="PortUuid">PortUuid</a>" : <i>String</i>,
    "<a href="#vlanid" title="VlanId">VlanId</a>" : <i>Double</i>,
    "<a href="#vrfid" title="VrfId">VrfId</a>" : <i>Double</i>,
    "<a href="#vrfref" title="VrfRef">VrfRef</a>" : <i>String</i>,
    "<a href="#members" title="Members">Members</a>" : <i>[ <a href="membersdefinition.md">MembersDefinition</a>, ... ]</i>,
    "<a href="#vlaninterfaces" title="VlanInterfaces">VlanInterfaces</a>" : <i>[ <a href="vlaninterfacesdefinition.md">VlanInterfacesDefinition</a>, ... ]</i>,
    "<a href="#vnicnetworks" title="VnicNetworks">VnicNetworks</a>" : <i>[ <a href="vnicnetworksdefinition.md">VnicNetworksDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#adapter" title="Adapter">Adapter</a>: <i>String</i>
<a href="#aggregatorchgd" title="AggregatorChgd">AggregatorChgd</a>: <i>Boolean</i>
<a href="#cansedptakeover" title="CanSeDpTakeover">CanSeDpTakeover</a>: <i>Boolean</i>
<a href="#connected" title="Connected">Connected</a>: <i>Boolean</i>
<a href="#delpending" title="DelPending">DelPending</a>: <i>Boolean</i>
<a href="#deletevnic" title="DeleteVnic">DeleteVnic</a>: <i>Boolean</i>
<a href="#dhcpenabled" title="DhcpEnabled">DhcpEnabled</a>: <i>Boolean</i>
<a href="#dpdeletiondone" title="DpDeletionDone">DpDeletionDone</a>: <i>Boolean</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#ifname" title="IfName">IfName</a>: <i>String</i>
<a href="#ip6autocfgenabled" title="Ip6AutocfgEnabled">Ip6AutocfgEnabled</a>: <i>Boolean</i>
<a href="#isasm" title="IsAsm">IsAsm</a>: <i>Boolean</i>
<a href="#isaviinternalnetwork" title="IsAviInternalNetwork">IsAviInternalNetwork</a>: <i>Boolean</i>
<a href="#ishsm" title="IsHsm">IsHsm</a>: <i>Boolean</i>
<a href="#ismgmt" title="IsMgmt">IsMgmt</a>: <i>Boolean</i>
<a href="#isportchannel" title="IsPortchannel">IsPortchannel</a>: <i>Boolean</i>
<a href="#linkup" title="LinkUp">LinkUp</a>: <i>Boolean</i>
<a href="#linuxname" title="LinuxName">LinuxName</a>: <i>String</i>
<a href="#macaddress" title="MacAddress">MacAddress</a>: <i>String</i>
<a href="#mtu" title="Mtu">Mtu</a>: <i>Double</i>
<a href="#networkname" title="NetworkName">NetworkName</a>: <i>String</i>
<a href="#networkref" title="NetworkRef">NetworkRef</a>: <i>String</i>
<a href="#pciid" title="PciId">PciId</a>: <i>String</i>
<a href="#portuuid" title="PortUuid">PortUuid</a>: <i>String</i>
<a href="#vlanid" title="VlanId">VlanId</a>: <i>Double</i>
<a href="#vrfid" title="VrfId">VrfId</a>: <i>Double</i>
<a href="#vrfref" title="VrfRef">VrfRef</a>: <i>String</i>
<a href="#members" title="Members">Members</a>: <i>
      - <a href="membersdefinition.md">MembersDefinition</a></i>
<a href="#vlaninterfaces" title="VlanInterfaces">VlanInterfaces</a>: <i>
      - <a href="vlaninterfacesdefinition.md">VlanInterfacesDefinition</a></i>
<a href="#vnicnetworks" title="VnicNetworks">VnicNetworks</a>: <i>
      - <a href="vnicnetworksdefinition.md">VnicNetworksDefinition</a></i>
</pre>

## Properties

#### Adapter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AggregatorChgd

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CanSeDpTakeover

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Connected

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DelPending

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteVnic

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DpDeletionDone

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IfName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6AutocfgEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsAsm

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsAviInternalNetwork

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsHsm

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsMgmt

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsPortchannel

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinkUp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinuxName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacAddress

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mtu

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PciId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortUuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VrfId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VrfRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Members

_Required_: No

_Type_: List of <a href="membersdefinition.md">MembersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanInterfaces

_Required_: No

_Type_: List of <a href="vlaninterfacesdefinition.md">VlanInterfacesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VnicNetworks

_Required_: No

_Type_: List of <a href="vnicnetworksdefinition.md">VnicNetworksDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

