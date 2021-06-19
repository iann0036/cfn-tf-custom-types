# TF::Spotinst::ElastigroupAzureV3 NetworkInterfacesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#assignpublicip" title="AssignPublicIp">AssignPublicIp</a>" : <i>Boolean</i>,
    "<a href="#isprimary" title="IsPrimary">IsPrimary</a>" : <i>Boolean</i>,
    "<a href="#subnetname" title="SubnetName">SubnetName</a>" : <i>String</i>,
    "<a href="#additionalipconfigs" title="AdditionalIpConfigs">AdditionalIpConfigs</a>" : <i>[ <a href="additionalipconfigsdefinition.md">AdditionalIpConfigsDefinition</a>, ... ]</i>,
    "<a href="#applicationsecuritygroup" title="ApplicationSecurityGroup">ApplicationSecurityGroup</a>" : <i>[ <a href="applicationsecuritygroupdefinition.md">ApplicationSecurityGroupDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#assignpublicip" title="AssignPublicIp">AssignPublicIp</a>: <i>Boolean</i>
<a href="#isprimary" title="IsPrimary">IsPrimary</a>: <i>Boolean</i>
<a href="#subnetname" title="SubnetName">SubnetName</a>: <i>String</i>
<a href="#additionalipconfigs" title="AdditionalIpConfigs">AdditionalIpConfigs</a>: <i>
      - <a href="additionalipconfigsdefinition.md">AdditionalIpConfigsDefinition</a></i>
<a href="#applicationsecuritygroup" title="ApplicationSecurityGroup">ApplicationSecurityGroup</a>: <i>
      - <a href="applicationsecuritygroupdefinition.md">ApplicationSecurityGroupDefinition</a></i>
</pre>

## Properties

#### AssignPublicIp

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsPrimary

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalIpConfigs

_Required_: No

_Type_: List of <a href="additionalipconfigsdefinition.md">AdditionalIpConfigsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationSecurityGroup

_Required_: No

_Type_: List of <a href="applicationsecuritygroupdefinition.md">ApplicationSecurityGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

