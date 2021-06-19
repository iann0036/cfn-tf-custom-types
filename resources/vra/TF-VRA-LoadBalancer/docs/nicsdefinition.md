# TF::VRA::LoadBalancer NicsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#addresses" title="Addresses">Addresses</a>" : <i>[ String, ... ]</i>,
    "<a href="#customproperties" title="CustomProperties">CustomProperties</a>" : <i>[ <a href="custompropertiesdefinition.md">CustomPropertiesDefinition</a>, ... ]</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#deviceindex" title="DeviceIndex">DeviceIndex</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#networkid" title="NetworkId">NetworkId</a>" : <i>String</i>,
    "<a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#addresses" title="Addresses">Addresses</a>: <i>
      - String</i>
<a href="#customproperties" title="CustomProperties">CustomProperties</a>: <i>
      - <a href="custompropertiesdefinition.md">CustomPropertiesDefinition</a></i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#deviceindex" title="DeviceIndex">DeviceIndex</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#networkid" title="NetworkId">NetworkId</a>: <i>String</i>
<a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>: <i>
      - String</i>
</pre>

## Properties

#### Addresses

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomProperties

_Required_: No

_Type_: List of <a href="custompropertiesdefinition.md">CustomPropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceIndex

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

