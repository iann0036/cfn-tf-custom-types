# TF::Spotinst::OceanAks NetworkInterfaceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#assignpublicip" title="AssignPublicIp">AssignPublicIp</a>" : <i>Boolean</i>,
    "<a href="#isprimary" title="IsPrimary">IsPrimary</a>" : <i>Boolean</i>,
    "<a href="#subnetname" title="SubnetName">SubnetName</a>" : <i>String</i>,
    "<a href="#additionalipconfig" title="AdditionalIpConfig">AdditionalIpConfig</a>" : <i>[ <a href="additionalipconfigdefinition.md">AdditionalIpConfigDefinition</a>, ... ]</i>,
    "<a href="#securitygroup" title="SecurityGroup">SecurityGroup</a>" : <i>[ <a href="securitygroupdefinition.md">SecurityGroupDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#assignpublicip" title="AssignPublicIp">AssignPublicIp</a>: <i>Boolean</i>
<a href="#isprimary" title="IsPrimary">IsPrimary</a>: <i>Boolean</i>
<a href="#subnetname" title="SubnetName">SubnetName</a>: <i>String</i>
<a href="#additionalipconfig" title="AdditionalIpConfig">AdditionalIpConfig</a>: <i>
      - <a href="additionalipconfigdefinition.md">AdditionalIpConfigDefinition</a></i>
<a href="#securitygroup" title="SecurityGroup">SecurityGroup</a>: <i>
      - <a href="securitygroupdefinition.md">SecurityGroupDefinition</a></i>
</pre>

## Properties

#### AssignPublicIp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsPrimary

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalIpConfig

_Required_: No

_Type_: List of <a href="additionalipconfigdefinition.md">AdditionalIpConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroup

_Required_: No

_Type_: List of <a href="securitygroupdefinition.md">SecurityGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

