# TF::Volterra::AwsTgwSite AzNodesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#awsazname" title="AwsAzName">AwsAzName</a>" : <i>String</i>,
    "<a href="#disksize" title="DiskSize">DiskSize</a>" : <i>Double</i>,
    "<a href="#reservedinsidesubnet" title="ReservedInsideSubnet">ReservedInsideSubnet</a>" : <i>Boolean</i>,
    "<a href="#insidesubnet" title="InsideSubnet">InsideSubnet</a>" : <i>[ <a href="insidesubnetdefinition.md">InsideSubnetDefinition</a>, ... ]</i>,
    "<a href="#outsidesubnet" title="OutsideSubnet">OutsideSubnet</a>" : <i>[ <a href="outsidesubnetdefinition.md">OutsideSubnetDefinition</a>, ... ]</i>,
    "<a href="#workloadsubnet" title="WorkloadSubnet">WorkloadSubnet</a>" : <i>[ <a href="workloadsubnetdefinition.md">WorkloadSubnetDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#awsazname" title="AwsAzName">AwsAzName</a>: <i>String</i>
<a href="#disksize" title="DiskSize">DiskSize</a>: <i>Double</i>
<a href="#reservedinsidesubnet" title="ReservedInsideSubnet">ReservedInsideSubnet</a>: <i>Boolean</i>
<a href="#insidesubnet" title="InsideSubnet">InsideSubnet</a>: <i>
      - <a href="insidesubnetdefinition.md">InsideSubnetDefinition</a></i>
<a href="#outsidesubnet" title="OutsideSubnet">OutsideSubnet</a>: <i>
      - <a href="outsidesubnetdefinition.md">OutsideSubnetDefinition</a></i>
<a href="#workloadsubnet" title="WorkloadSubnet">WorkloadSubnet</a>: <i>
      - <a href="workloadsubnetdefinition.md">WorkloadSubnetDefinition</a></i>
</pre>

## Properties

#### AwsAzName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReservedInsideSubnet

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsideSubnet

_Required_: No

_Type_: List of <a href="insidesubnetdefinition.md">InsideSubnetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutsideSubnet

_Required_: No

_Type_: List of <a href="outsidesubnetdefinition.md">OutsideSubnetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkloadSubnet

_Required_: No

_Type_: List of <a href="workloadsubnetdefinition.md">WorkloadSubnetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

