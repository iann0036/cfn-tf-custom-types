# TF::Volterra::AzureVnetSite LocalSubnetDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#subnet" title="Subnet">Subnet</a>" : <i>[ <a href="subnetdefinition.md">SubnetDefinition</a>, ... ]</i>,
    "<a href="#subnetparam" title="SubnetParam">SubnetParam</a>" : <i>[ <a href="subnetparamdefinition.md">SubnetParamDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#subnet" title="Subnet">Subnet</a>: <i>
      - <a href="subnetdefinition.md">SubnetDefinition</a></i>
<a href="#subnetparam" title="SubnetParam">SubnetParam</a>: <i>
      - <a href="subnetparamdefinition.md">SubnetParamDefinition</a></i>
</pre>

## Properties

#### Subnet

_Required_: No

_Type_: List of <a href="subnetdefinition.md">SubnetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetParam

_Required_: No

_Type_: List of <a href="subnetparamdefinition.md">SubnetParamDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

