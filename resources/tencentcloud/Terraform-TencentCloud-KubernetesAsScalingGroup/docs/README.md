# Terraform::TencentCloud::KubernetesAsScalingGroup

Provide a resource to create an auto scaling group for kubernetes cluster.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::KubernetesAsScalingGroup",
    "Properties" : {
        "<a href="#clusterid" title="ClusterId">ClusterId</a>" : <i>String</i>,
        "<a href="#autoscalingconfig" title="AutoScalingConfig">AutoScalingConfig</a>" : <i>[ <a href="autoscalingconfig.md">AutoScalingConfig</a>, ... ]</i>,
        "<a href="#autoscalinggroup" title="AutoScalingGroup">AutoScalingGroup</a>" : <i>[ <a href="autoscalinggroup.md">AutoScalingGroup</a>, ... ]</i>,
        "<a href="#datadisk" title="DataDisk">DataDisk</a>" : <i>[ <a href="datadisk.md">DataDisk</a>, ... ]</i>,
        "<a href="#forwardbalancerids" title="ForwardBalancerIds">ForwardBalancerIds</a>" : <i>[ <a href="forwardbalancerids.md">ForwardBalancerIds</a>, ... ]</i>,
        "<a href="#targetattribute" title="TargetAttribute">TargetAttribute</a>" : <i>[ <a href="targetattribute.md">TargetAttribute</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::KubernetesAsScalingGroup
Properties:
    <a href="#clusterid" title="ClusterId">ClusterId</a>: <i>String</i>
    <a href="#autoscalingconfig" title="AutoScalingConfig">AutoScalingConfig</a>: <i>
      - <a href="autoscalingconfig.md">AutoScalingConfig</a></i>
    <a href="#autoscalinggroup" title="AutoScalingGroup">AutoScalingGroup</a>: <i>
      - <a href="autoscalinggroup.md">AutoScalingGroup</a></i>
    <a href="#datadisk" title="DataDisk">DataDisk</a>: <i>
      - <a href="datadisk.md">DataDisk</a></i>
    <a href="#forwardbalancerids" title="ForwardBalancerIds">ForwardBalancerIds</a>: <i>
      - <a href="forwardbalancerids.md">ForwardBalancerIds</a></i>
    <a href="#targetattribute" title="TargetAttribute">TargetAttribute</a>: <i>
      - <a href="targetattribute.md">TargetAttribute</a></i>
</pre>

## Properties

#### ClusterId

ID of the cluster.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoScalingConfig

_Required_: No

_Type_: List of <a href="autoscalingconfig.md">AutoScalingConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoScalingGroup

_Required_: No

_Type_: List of <a href="autoscalinggroup.md">AutoScalingGroup</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataDisk

_Required_: No

_Type_: List of <a href="datadisk.md">DataDisk</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardBalancerIds

_Required_: No

_Type_: List of <a href="forwardbalancerids.md">ForwardBalancerIds</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetAttribute

_Required_: No

_Type_: List of <a href="targetattribute.md">TargetAttribute</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

