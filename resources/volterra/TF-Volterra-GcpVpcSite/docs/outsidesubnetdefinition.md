# TF::Volterra::GcpVpcSite OutsideSubnetDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#existingsubnet" title="ExistingSubnet">ExistingSubnet</a>" : <i>[ <a href="existingsubnetdefinition.md">ExistingSubnetDefinition</a>, ... ]</i>,
    "<a href="#newsubnet" title="NewSubnet">NewSubnet</a>" : <i>[ <a href="newsubnetdefinition.md">NewSubnetDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#existingsubnet" title="ExistingSubnet">ExistingSubnet</a>: <i>
      - <a href="existingsubnetdefinition.md">ExistingSubnetDefinition</a></i>
<a href="#newsubnet" title="NewSubnet">NewSubnet</a>: <i>
      - <a href="newsubnetdefinition.md">NewSubnetDefinition</a></i>
</pre>

## Properties

#### ExistingSubnet

_Required_: No

_Type_: List of <a href="existingsubnetdefinition.md">ExistingSubnetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NewSubnet

_Required_: No

_Type_: List of <a href="newsubnetdefinition.md">NewSubnetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

