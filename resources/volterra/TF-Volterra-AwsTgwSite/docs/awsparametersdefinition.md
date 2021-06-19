# TF::Volterra::AwsTgwSite AwsParametersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#assisted" title="Assisted">Assisted</a>" : <i>Boolean</i>,
    "<a href="#awscertifiedhw" title="AwsCertifiedHw">AwsCertifiedHw</a>" : <i>String</i>,
    "<a href="#awsregion" title="AwsRegion">AwsRegion</a>" : <i>String</i>,
    "<a href="#disksize" title="DiskSize">DiskSize</a>" : <i>Double</i>,
    "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
    "<a href="#nodesperaz" title="NodesPerAz">NodesPerAz</a>" : <i>Double</i>,
    "<a href="#sshkey" title="SshKey">SshKey</a>" : <i>String</i>,
    "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
    "<a href="#awscred" title="AwsCred">AwsCred</a>" : <i>[ <a href="awscreddefinition.md">AwsCredDefinition</a>, ... ]</i>,
    "<a href="#aznodes" title="AzNodes">AzNodes</a>" : <i>[ <a href="aznodesdefinition.md">AzNodesDefinition</a>, ... ]</i>,
    "<a href="#existingtgw" title="ExistingTgw">ExistingTgw</a>" : <i>[ <a href="existingtgwdefinition.md">ExistingTgwDefinition</a>, ... ]</i>,
    "<a href="#newtgw" title="NewTgw">NewTgw</a>" : <i>[ <a href="newtgwdefinition.md">NewTgwDefinition</a>, ... ]</i>,
    "<a href="#newvpc" title="NewVpc">NewVpc</a>" : <i>[ <a href="newvpcdefinition.md">NewVpcDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#assisted" title="Assisted">Assisted</a>: <i>Boolean</i>
<a href="#awscertifiedhw" title="AwsCertifiedHw">AwsCertifiedHw</a>: <i>String</i>
<a href="#awsregion" title="AwsRegion">AwsRegion</a>: <i>String</i>
<a href="#disksize" title="DiskSize">DiskSize</a>: <i>Double</i>
<a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
<a href="#nodesperaz" title="NodesPerAz">NodesPerAz</a>: <i>Double</i>
<a href="#sshkey" title="SshKey">SshKey</a>: <i>String</i>
<a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
<a href="#awscred" title="AwsCred">AwsCred</a>: <i>
      - <a href="awscreddefinition.md">AwsCredDefinition</a></i>
<a href="#aznodes" title="AzNodes">AzNodes</a>: <i>
      - <a href="aznodesdefinition.md">AzNodesDefinition</a></i>
<a href="#existingtgw" title="ExistingTgw">ExistingTgw</a>: <i>
      - <a href="existingtgwdefinition.md">ExistingTgwDefinition</a></i>
<a href="#newtgw" title="NewTgw">NewTgw</a>: <i>
      - <a href="newtgwdefinition.md">NewTgwDefinition</a></i>
<a href="#newvpc" title="NewVpc">NewVpc</a>: <i>
      - <a href="newvpcdefinition.md">NewVpcDefinition</a></i>
</pre>

## Properties

#### Assisted

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsCertifiedHw

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsRegion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodesPerAz

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsCred

_Required_: No

_Type_: List of <a href="awscreddefinition.md">AwsCredDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzNodes

_Required_: No

_Type_: List of <a href="aznodesdefinition.md">AzNodesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExistingTgw

_Required_: No

_Type_: List of <a href="existingtgwdefinition.md">ExistingTgwDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NewTgw

_Required_: No

_Type_: List of <a href="newtgwdefinition.md">NewTgwDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NewVpc

_Required_: No

_Type_: List of <a href="newvpcdefinition.md">NewVpcDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

