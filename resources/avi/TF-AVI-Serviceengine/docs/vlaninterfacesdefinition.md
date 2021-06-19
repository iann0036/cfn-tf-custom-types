# TF::AVI::Serviceengine VlanInterfacesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dhcpenabled" title="DhcpEnabled">DhcpEnabled</a>" : <i>Boolean</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#ifname" title="IfName">IfName</a>" : <i>String</i>,
    "<a href="#ip6autocfgenabled" title="Ip6AutocfgEnabled">Ip6AutocfgEnabled</a>" : <i>Boolean</i>,
    "<a href="#ismgmt" title="IsMgmt">IsMgmt</a>" : <i>Boolean</i>,
    "<a href="#vlanid" title="VlanId">VlanId</a>" : <i>Double</i>,
    "<a href="#vrfref" title="VrfRef">VrfRef</a>" : <i>String</i>,
    "<a href="#vnicnetworks" title="VnicNetworks">VnicNetworks</a>" : <i>[ <a href="vnicnetworksdefinition.md">VnicNetworksDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dhcpenabled" title="DhcpEnabled">DhcpEnabled</a>: <i>Boolean</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#ifname" title="IfName">IfName</a>: <i>String</i>
<a href="#ip6autocfgenabled" title="Ip6AutocfgEnabled">Ip6AutocfgEnabled</a>: <i>Boolean</i>
<a href="#ismgmt" title="IsMgmt">IsMgmt</a>: <i>Boolean</i>
<a href="#vlanid" title="VlanId">VlanId</a>: <i>Double</i>
<a href="#vrfref" title="VrfRef">VrfRef</a>: <i>String</i>
<a href="#vnicnetworks" title="VnicNetworks">VnicNetworks</a>: <i>
      - <a href="vnicnetworksdefinition.md">VnicNetworksDefinition</a></i>
</pre>

## Properties

#### DhcpEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IfName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6AutocfgEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsMgmt

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VrfRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VnicNetworks

_Required_: No

_Type_: List of <a href="vnicnetworksdefinition.md">VnicNetworksDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

