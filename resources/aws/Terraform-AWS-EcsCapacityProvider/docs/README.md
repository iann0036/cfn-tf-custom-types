# Terraform::AWS::EcsCapacityProvider

CloudFormation equivalent of aws_ecs_capacity_provider

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::EcsCapacityProvider",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#autoscalinggroupprovider" title="AutoScalingGroupProvider">AutoScalingGroupProvider</a>" : <i>[ <a href="autoscalinggroupprovider.md">AutoScalingGroupProvider</a>, ... ]</i>,
        "<a href="#managedscaling" title="ManagedScaling">ManagedScaling</a>" : <i>[ <a href="managedscaling.md">ManagedScaling</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::EcsCapacityProvider
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#autoscalinggroupprovider" title="AutoScalingGroupProvider">AutoScalingGroupProvider</a>: <i>
      - <a href="autoscalinggroupprovider.md">AutoScalingGroupProvider</a></i>
    <a href="#managedscaling" title="ManagedScaling">ManagedScaling</a>: <i>
      - <a href="managedscaling.md">ManagedScaling</a></i>
</pre>

## Properties

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoScalingGroupProvider

_Required_: No

_Type_: List of <a href="autoscalinggroupprovider.md">AutoScalingGroupProvider</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedScaling

_Required_: No

_Type_: List of <a href="managedscaling.md">ManagedScaling</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

