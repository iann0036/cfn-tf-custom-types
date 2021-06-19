# TF::TencentCloud::ClbTargetGroup

Provides a resource to create a CLB target group.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::ClbTargetGroup",
    "Properties" : {
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#targetgroupname" title="TargetGroupName">TargetGroupName</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#targetgroupinstances" title="TargetGroupInstances">TargetGroupInstances</a>" : <i>[ <a href="targetgroupinstancesdefinition.md">TargetGroupInstancesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::ClbTargetGroup
Properties:
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#targetgroupname" title="TargetGroupName">TargetGroupName</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#targetgroupinstances" title="TargetGroupInstances">TargetGroupInstances</a>: <i>
      - <a href="targetgroupinstancesdefinition.md">TargetGroupInstancesDefinition</a></i>
</pre>

## Properties

#### Port

The default port of target group, add server after can use it.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetGroupName

Target group name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

VPC ID, default is based on the network.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetGroupInstances

_Required_: No

_Type_: List of <a href="targetgroupinstancesdefinition.md">TargetGroupInstancesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

