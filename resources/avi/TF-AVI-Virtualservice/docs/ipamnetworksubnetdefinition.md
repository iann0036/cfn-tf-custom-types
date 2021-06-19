# TF::AVI::Virtualservice IpamNetworkSubnetDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#networkref" title="NetworkRef">NetworkRef</a>" : <i>String</i>,
    "<a href="#subnet6uuid" title="Subnet6Uuid">Subnet6Uuid</a>" : <i>String</i>,
    "<a href="#subnetuuid" title="SubnetUuid">SubnetUuid</a>" : <i>String</i>,
    "<a href="#subnet" title="Subnet">Subnet</a>" : <i>[ <a href="subnetdefinition.md">SubnetDefinition</a>, ... ]</i>,
    "<a href="#subnet6" title="Subnet6">Subnet6</a>" : <i>[ <a href="subnet6definition.md">Subnet6Definition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#networkref" title="NetworkRef">NetworkRef</a>: <i>String</i>
<a href="#subnet6uuid" title="Subnet6Uuid">Subnet6Uuid</a>: <i>String</i>
<a href="#subnetuuid" title="SubnetUuid">SubnetUuid</a>: <i>String</i>
<a href="#subnet" title="Subnet">Subnet</a>: <i>
      - <a href="subnetdefinition.md">SubnetDefinition</a></i>
<a href="#subnet6" title="Subnet6">Subnet6</a>: <i>
      - <a href="subnet6definition.md">Subnet6Definition</a></i>
</pre>

## Properties

#### NetworkRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet6Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetUuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet

_Required_: No

_Type_: List of <a href="subnetdefinition.md">SubnetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet6

_Required_: No

_Type_: List of <a href="subnet6definition.md">Subnet6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

