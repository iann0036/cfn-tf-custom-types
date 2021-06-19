# TF::Alicloud::AutoProvisioningGroup LaunchTemplateConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
    "<a href="#maxprice" title="MaxPrice">MaxPrice</a>" : <i>String</i>,
    "<a href="#priority" title="Priority">Priority</a>" : <i>String</i>,
    "<a href="#vswitchid" title="VswitchId">VswitchId</a>" : <i>String</i>,
    "<a href="#weightedcapacity" title="WeightedCapacity">WeightedCapacity</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
<a href="#maxprice" title="MaxPrice">MaxPrice</a>: <i>String</i>
<a href="#priority" title="Priority">Priority</a>: <i>String</i>
<a href="#vswitchid" title="VswitchId">VswitchId</a>: <i>String</i>
<a href="#weightedcapacity" title="WeightedCapacity">WeightedCapacity</a>: <i>String</i>
</pre>

## Properties

#### InstanceType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPrice

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VswitchId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeightedCapacity

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

