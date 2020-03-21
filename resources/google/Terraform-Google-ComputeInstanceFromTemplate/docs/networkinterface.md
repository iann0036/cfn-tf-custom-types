# Terraform::Google::ComputeInstanceFromTemplate NetworkInterface

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accessconfig" title="AccessConfig">AccessConfig</a>" : <i>[ <a href="networkinterface-accessconfig.md">AccessConfig</a>, ... ]</i>,
    "<a href="#aliasiprange" title="AliasIpRange">AliasIpRange</a>" : <i>[ <a href="networkinterface-aliasiprange.md">AliasIpRange</a>, ... ]</i>,
    "<a href="#network" title="Network">Network</a>" : <i>String</i>,
    "<a href="#networkip" title="NetworkIp">NetworkIp</a>" : <i>String</i>,
    "<a href="#subnetwork" title="Subnetwork">Subnetwork</a>" : <i>String</i>,
    "<a href="#subnetworkproject" title="SubnetworkProject">SubnetworkProject</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#accessconfig" title="AccessConfig">AccessConfig</a>: <i>
      - <a href="networkinterface-accessconfig.md">AccessConfig</a></i>
<a href="#aliasiprange" title="AliasIpRange">AliasIpRange</a>: <i>
      - <a href="networkinterface-aliasiprange.md">AliasIpRange</a></i>
<a href="#network" title="Network">Network</a>: <i>String</i>
<a href="#networkip" title="NetworkIp">NetworkIp</a>: <i>String</i>
<a href="#subnetwork" title="Subnetwork">Subnetwork</a>: <i>String</i>
<a href="#subnetworkproject" title="SubnetworkProject">SubnetworkProject</a>: <i>String</i>
</pre>

## Properties

#### AccessConfig

_Required_: No

_Type_: List of <a href="networkinterface-accessconfig.md">AccessConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AliasIpRange

_Required_: No

_Type_: List of <a href="networkinterface-aliasiprange.md">AliasIpRange</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnetwork

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetworkProject

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

