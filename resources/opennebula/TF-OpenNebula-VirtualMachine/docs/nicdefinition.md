# TF::OpenNebula::VirtualMachine NicDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>,
    "<a href="#mac" title="Mac">Mac</a>" : <i>String</i>,
    "<a href="#model" title="Model">Model</a>" : <i>String</i>,
    "<a href="#networkid" title="NetworkId">NetworkId</a>" : <i>Double</i>,
    "<a href="#physicaldevice" title="PhysicalDevice">PhysicalDevice</a>" : <i>String</i>,
    "<a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>" : <i>[ Double, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ip" title="Ip">Ip</a>: <i>String</i>
<a href="#mac" title="Mac">Mac</a>: <i>String</i>
<a href="#model" title="Model">Model</a>: <i>String</i>
<a href="#networkid" title="NetworkId">NetworkId</a>: <i>Double</i>
<a href="#physicaldevice" title="PhysicalDevice">PhysicalDevice</a>: <i>String</i>
<a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>: <i>
      - Double</i>
</pre>

## Properties

#### Ip

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mac

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Model

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkId

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PhysicalDevice

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroups

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

