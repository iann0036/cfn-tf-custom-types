# TF::Volterra::AwsTgwSite WorkloadSubnetDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#existingsubnetid" title="ExistingSubnetId">ExistingSubnetId</a>" : <i>String</i>,
    "<a href="#subnetparam" title="SubnetParam">SubnetParam</a>" : <i>[ <a href="subnetparamdefinition.md">SubnetParamDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#existingsubnetid" title="ExistingSubnetId">ExistingSubnetId</a>: <i>String</i>
<a href="#subnetparam" title="SubnetParam">SubnetParam</a>: <i>
      - <a href="subnetparamdefinition.md">SubnetParamDefinition</a></i>
</pre>

## Properties

#### ExistingSubnetId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetParam

_Required_: No

_Type_: List of <a href="subnetparamdefinition.md">SubnetParamDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

