# TF::Thunder::SnmpServerSnmpv1V2cUserOid RemoteDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#hostlist" title="HostList">HostList</a>" : <i>[ <a href="hostlistdefinition.md">HostListDefinition</a>, ... ]</i>,
    "<a href="#ipv4list" title="Ipv4List">Ipv4List</a>" : <i>[ <a href="ipv4listdefinition.md">Ipv4ListDefinition</a>, ... ]</i>,
    "<a href="#ipv6list" title="Ipv6List">Ipv6List</a>" : <i>[ <a href="ipv6listdefinition.md">Ipv6ListDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#hostlist" title="HostList">HostList</a>: <i>
      - <a href="hostlistdefinition.md">HostListDefinition</a></i>
<a href="#ipv4list" title="Ipv4List">Ipv4List</a>: <i>
      - <a href="ipv4listdefinition.md">Ipv4ListDefinition</a></i>
<a href="#ipv6list" title="Ipv6List">Ipv6List</a>: <i>
      - <a href="ipv6listdefinition.md">Ipv6ListDefinition</a></i>
</pre>

## Properties

#### HostList

_Required_: No

_Type_: List of <a href="hostlistdefinition.md">HostListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4List

_Required_: No

_Type_: List of <a href="ipv4listdefinition.md">Ipv4ListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6List

_Required_: No

_Type_: List of <a href="ipv6listdefinition.md">Ipv6ListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

