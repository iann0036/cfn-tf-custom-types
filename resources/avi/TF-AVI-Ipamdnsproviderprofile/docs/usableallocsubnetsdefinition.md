# TF::AVI::Ipamdnsproviderprofile UsableAllocSubnetsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#subnet" title="Subnet">Subnet</a>" : <i>[ <a href="subnetdefinition.md">SubnetDefinition</a>, ... ]</i>,
    "<a href="#subnet6" title="Subnet6">Subnet6</a>" : <i>[ <a href="subnet6definition.md">Subnet6Definition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#subnet" title="Subnet">Subnet</a>: <i>
      - <a href="subnetdefinition.md">SubnetDefinition</a></i>
<a href="#subnet6" title="Subnet6">Subnet6</a>: <i>
      - <a href="subnet6definition.md">Subnet6Definition</a></i>
</pre>

## Properties

#### Subnet

_Required_: No

_Type_: List of <a href="subnetdefinition.md">SubnetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet6

_Required_: No

_Type_: List of <a href="subnet6definition.md">Subnet6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

