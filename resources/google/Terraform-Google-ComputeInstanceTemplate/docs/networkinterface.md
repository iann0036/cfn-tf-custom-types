# Terraform::Google::ComputeInstanceTemplate NetworkInterface

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#network" title="Network">Network</a>" : <i>String</i>,
    "<a href="#networkip" title="NetworkIp">NetworkIp</a>" : <i>String</i>,
    "<a href="#subnetwork" title="Subnetwork">Subnetwork</a>" : <i>String</i>,
    "<a href="#subnetworkproject" title="SubnetworkProject">SubnetworkProject</a>" : <i>String</i>,
    "<a href="#accessconfig" title="AccessConfig">AccessConfig</a>" : <i>[ <a href="networkinterface-accessconfig.md">AccessConfig</a>, ... ]</i>,
    "<a href="#aliasiprange" title="AliasIpRange">AliasIpRange</a>" : <i>[ <a href="networkinterface-aliasiprange.md">AliasIpRange</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#network" title="Network">Network</a>: <i>String</i>
<a href="#networkip" title="NetworkIp">NetworkIp</a>: <i>String</i>
<a href="#subnetwork" title="Subnetwork">Subnetwork</a>: <i>String</i>
<a href="#subnetworkproject" title="SubnetworkProject">SubnetworkProject</a>: <i>String</i>
<a href="#accessconfig" title="AccessConfig">AccessConfig</a>: <i>
      - <a href="networkinterface-accessconfig.md">AccessConfig</a></i>
<a href="#aliasiprange" title="AliasIpRange">AliasIpRange</a>: <i>
      - <a href="networkinterface-aliasiprange.md">AliasIpRange</a></i>
</pre>

## Properties

#### Network

The name or self_link of the network to attach this interface to.
Use `network` attribute for Legacy or Auto subnetted networks and
`subnetwork` for custom subnetted networks.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkIp

The private IP address to assign to the instance. If
empty, the address will be automatically assigned.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnetwork

the name of the subnetwork to attach this interface
to. The subnetwork must exist in the same `region` this instance will be
created in. Either `network` or `subnetwork` must be provided.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetworkProject

The ID of the project in which the subnetwork belongs.
If it is not provided, the provider project is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessConfig

_Required_: No

_Type_: List of <a href="networkinterface-accessconfig.md">AccessConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AliasIpRange

_Required_: No

_Type_: List of <a href="networkinterface-aliasiprange.md">AliasIpRange</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

