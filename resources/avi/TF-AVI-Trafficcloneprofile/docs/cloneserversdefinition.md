# TF::AVI::Trafficcloneprofile CloneServersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#mac" title="Mac">Mac</a>" : <i>String</i>,
    "<a href="#networkref" title="NetworkRef">NetworkRef</a>" : <i>String</i>,
    "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>[ <a href="ipaddressdefinition.md">IpAddressDefinition</a>, ... ]</i>,
    "<a href="#subnet" title="Subnet">Subnet</a>" : <i>[ <a href="subnetdefinition.md">SubnetDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#mac" title="Mac">Mac</a>: <i>String</i>
<a href="#networkref" title="NetworkRef">NetworkRef</a>: <i>String</i>
<a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>
      - <a href="ipaddressdefinition.md">IpAddressDefinition</a></i>
<a href="#subnet" title="Subnet">Subnet</a>: <i>
      - <a href="subnetdefinition.md">SubnetDefinition</a></i>
</pre>

## Properties

#### Mac

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddress

_Required_: No

_Type_: List of <a href="ipaddressdefinition.md">IpAddressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet

_Required_: No

_Type_: List of <a href="subnetdefinition.md">SubnetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

