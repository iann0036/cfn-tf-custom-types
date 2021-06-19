# TF::Nutanix::RecoveryPlan RecoveryNetworkDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#usevpcreference" title="UseVpcReference">UseVpcReference</a>" : <i>Boolean</i>,
    "<a href="#subnetlist" title="SubnetList">SubnetList</a>" : <i>[ <a href="subnetlistdefinition.md">SubnetListDefinition</a>, ... ]</i>,
    "<a href="#virtualnetworkreference" title="VirtualNetworkReference">VirtualNetworkReference</a>" : <i>[ <a href="virtualnetworkreferencedefinition.md">VirtualNetworkReferenceDefinition</a>, ... ]</i>,
    "<a href="#vpcreference" title="VpcReference">VpcReference</a>" : <i>[ <a href="vpcreferencedefinition.md">VpcReferenceDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#usevpcreference" title="UseVpcReference">UseVpcReference</a>: <i>Boolean</i>
<a href="#subnetlist" title="SubnetList">SubnetList</a>: <i>
      - <a href="subnetlistdefinition.md">SubnetListDefinition</a></i>
<a href="#virtualnetworkreference" title="VirtualNetworkReference">VirtualNetworkReference</a>: <i>
      - <a href="virtualnetworkreferencedefinition.md">VirtualNetworkReferenceDefinition</a></i>
<a href="#vpcreference" title="VpcReference">VpcReference</a>: <i>
      - <a href="vpcreferencedefinition.md">VpcReferenceDefinition</a></i>
</pre>

## Properties

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseVpcReference

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetList

_Required_: No

_Type_: List of <a href="subnetlistdefinition.md">SubnetListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualNetworkReference

_Required_: No

_Type_: List of <a href="virtualnetworkreferencedefinition.md">VirtualNetworkReferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcReference

_Required_: No

_Type_: List of <a href="vpcreferencedefinition.md">VpcReferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

