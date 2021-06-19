# TF::Google::ComputeInstance NetworkInterfaceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#network" title="Network">Network</a>" : <i>String</i>,
    "<a href="#networkip" title="NetworkIp">NetworkIp</a>" : <i>String</i>,
    "<a href="#nictype" title="NicType">NicType</a>" : <i>String</i>,
    "<a href="#subnetwork" title="Subnetwork">Subnetwork</a>" : <i>String</i>,
    "<a href="#subnetworkproject" title="SubnetworkProject">SubnetworkProject</a>" : <i>String</i>,
    "<a href="#accessconfig" title="AccessConfig">AccessConfig</a>" : <i>[ <a href="accessconfigdefinition.md">AccessConfigDefinition</a>, ... ]</i>,
    "<a href="#aliasiprange" title="AliasIpRange">AliasIpRange</a>" : <i>[ <a href="aliasiprangedefinition.md">AliasIpRangeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#network" title="Network">Network</a>: <i>String</i>
<a href="#networkip" title="NetworkIp">NetworkIp</a>: <i>String</i>
<a href="#nictype" title="NicType">NicType</a>: <i>String</i>
<a href="#subnetwork" title="Subnetwork">Subnetwork</a>: <i>String</i>
<a href="#subnetworkproject" title="SubnetworkProject">SubnetworkProject</a>: <i>String</i>
<a href="#accessconfig" title="AccessConfig">AccessConfig</a>: <i>
      - <a href="accessconfigdefinition.md">AccessConfigDefinition</a></i>
<a href="#aliasiprange" title="AliasIpRange">AliasIpRange</a>: <i>
      - <a href="aliasiprangedefinition.md">AliasIpRangeDefinition</a></i>
</pre>

## Properties

#### Network

The name or self_link of the network to attach this interface to.
Either `network` or `subnetwork` must be provided.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkIp

The private IP address to assign to the instance. If
empty, the address will be automatically assigned.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NicType

The type of vNIC to be used on this interface. Possible values: GVNIC, VIRTIO_NET.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnetwork

The name or self_link of the subnetwork to attach this
interface to. The subnetwork must exist in the same region this instance will be
created in. If network isn't provided it will be inferred from the subnetwork.
Either `network` or `subnetwork` must be provided.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetworkProject

The project in which the subnetwork belongs.
If the `subnetwork` is a self_link, this field is ignored in favor of the project
defined in the subnetwork self_link. If the `subnetwork` is a name and this
field is not provided, the provider project is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessConfig

_Required_: No

_Type_: List of <a href="accessconfigdefinition.md">AccessConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AliasIpRange

_Required_: No

_Type_: List of <a href="aliasiprangedefinition.md">AliasIpRangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

