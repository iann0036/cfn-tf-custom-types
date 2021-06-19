# TF::Volterra::AwsVpcSite VpcDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
    "<a href="#newvpc" title="NewVpc">NewVpc</a>" : <i>[ <a href="newvpcdefinition.md">NewVpcDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
<a href="#newvpc" title="NewVpc">NewVpc</a>: <i>
      - <a href="newvpcdefinition.md">NewVpcDefinition</a></i>
</pre>

## Properties

#### VpcId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NewVpc

_Required_: No

_Type_: List of <a href="newvpcdefinition.md">NewVpcDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

