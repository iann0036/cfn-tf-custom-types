# TF::Volterra::AwsVpcSite AzNodesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#awsazname" title="AwsAzName">AwsAzName</a>" : <i>String</i>,
    "<a href="#disksize" title="DiskSize">DiskSize</a>" : <i>Double</i>,
    "<a href="#localsubnet" title="LocalSubnet">LocalSubnet</a>" : <i>[ <a href="localsubnetdefinition.md">LocalSubnetDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#awsazname" title="AwsAzName">AwsAzName</a>: <i>String</i>
<a href="#disksize" title="DiskSize">DiskSize</a>: <i>Double</i>
<a href="#localsubnet" title="LocalSubnet">LocalSubnet</a>: <i>
      - <a href="localsubnetdefinition.md">LocalSubnetDefinition</a></i>
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

#### LocalSubnet

_Required_: No

_Type_: List of <a href="localsubnetdefinition.md">LocalSubnetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

