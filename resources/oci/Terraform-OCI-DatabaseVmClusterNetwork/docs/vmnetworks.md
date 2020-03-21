# Terraform::OCI::DatabaseVmClusterNetwork VmNetworks

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#domainname" title="DomainName">DomainName</a>" : <i>String</i>,
    "<a href="#gateway" title="Gateway">Gateway</a>" : <i>String</i>,
    "<a href="#netmask" title="Netmask">Netmask</a>" : <i>String</i>,
    "<a href="#networktype" title="NetworkType">NetworkType</a>" : <i>String</i>,
    "<a href="#vlanid" title="VlanId">VlanId</a>" : <i>String</i>,
    "<a href="#nodes" title="Nodes">Nodes</a>" : <i>[ <a href="vmnetworks-nodes.md">Nodes</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#domainname" title="DomainName">DomainName</a>: <i>String</i>
<a href="#gateway" title="Gateway">Gateway</a>: <i>String</i>
<a href="#netmask" title="Netmask">Netmask</a>: <i>String</i>
<a href="#networktype" title="NetworkType">NetworkType</a>: <i>String</i>
<a href="#vlanid" title="VlanId">VlanId</a>: <i>String</i>
<a href="#nodes" title="Nodes">Nodes</a>: <i>
      - <a href="vmnetworks-nodes.md">Nodes</a></i>
</pre>

## Properties

#### DomainName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gateway

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Netmask

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nodes

_Required_: No

_Type_: List of <a href="vmnetworks-nodes.md">Nodes</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

