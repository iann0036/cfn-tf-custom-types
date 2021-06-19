# TF::Volterra::GcpVpcSite IngressGwDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#gcpcertifiedhw" title="GcpCertifiedHw">GcpCertifiedHw</a>" : <i>String</i>,
    "<a href="#gcpzonenames" title="GcpZoneNames">GcpZoneNames</a>" : <i>[ String, ... ]</i>,
    "<a href="#nodenumber" title="NodeNumber">NodeNumber</a>" : <i>Double</i>,
    "<a href="#localnetwork" title="LocalNetwork">LocalNetwork</a>" : <i>[ <a href="localnetworkdefinition.md">LocalNetworkDefinition</a>, ... ]</i>,
    "<a href="#localsubnet" title="LocalSubnet">LocalSubnet</a>" : <i>[ <a href="localsubnetdefinition.md">LocalSubnetDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#gcpcertifiedhw" title="GcpCertifiedHw">GcpCertifiedHw</a>: <i>String</i>
<a href="#gcpzonenames" title="GcpZoneNames">GcpZoneNames</a>: <i>
      - String</i>
<a href="#nodenumber" title="NodeNumber">NodeNumber</a>: <i>Double</i>
<a href="#localnetwork" title="LocalNetwork">LocalNetwork</a>: <i>
      - <a href="localnetworkdefinition.md">LocalNetworkDefinition</a></i>
<a href="#localsubnet" title="LocalSubnet">LocalSubnet</a>: <i>
      - <a href="localsubnetdefinition.md">LocalSubnetDefinition</a></i>
</pre>

## Properties

#### GcpCertifiedHw

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcpZoneNames

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeNumber

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalNetwork

_Required_: No

_Type_: List of <a href="localnetworkdefinition.md">LocalNetworkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalSubnet

_Required_: No

_Type_: List of <a href="localsubnetdefinition.md">LocalSubnetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

