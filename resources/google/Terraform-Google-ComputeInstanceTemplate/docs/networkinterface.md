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
    "<a href="#accessconfig" title="AccessConfig">AccessConfig</a>" : <i>[ &lt;a href=&#34;networkinterface-accessconfig.md&#34;&gt;AccessConfig&lt;/a&gt;, ... ]</i>,
    "<a href="#aliasiprange" title="AliasIpRange">AliasIpRange</a>" : <i>[ &lt;a href=&#34;networkinterface-aliasiprange.md&#34;&gt;AliasIpRange&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#network" title="Network">Network</a>: <i>String</i>
<a href="#networkip" title="NetworkIp">NetworkIp</a>: <i>String</i>
<a href="#subnetwork" title="Subnetwork">Subnetwork</a>: <i>String</i>
<a href="#subnetworkproject" title="SubnetworkProject">SubnetworkProject</a>: <i>String</i>
<a href="#accessconfig" title="AccessConfig">AccessConfig</a>: <i>
      - &lt;a href=&#34;networkinterface-accessconfig.md&#34;&gt;AccessConfig&lt;/a&gt;</i>
<a href="#aliasiprange" title="AliasIpRange">AliasIpRange</a>: <i>
      - &lt;a href=&#34;networkinterface-aliasiprange.md&#34;&gt;AliasIpRange&lt;/a&gt;</i>
</pre>

## Properties

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

#### AccessConfig

_Required_: No
_Type_: List of &lt;a href=&#34;networkinterface-accessconfig.md&#34;&gt;AccessConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AliasIpRange

_Required_: No
_Type_: List of &lt;a href=&#34;networkinterface-aliasiprange.md&#34;&gt;AliasIpRange&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

