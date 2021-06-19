# TF::TencentCloud::KubernetesAsScalingGroup

Provide a resource to create an auto scaling group for kubernetes cluster.

~> **NOTE:**  It has been deprecated and replaced by `tencentcloud_cluster_node_pool`.
~> **NOTE:** To use the custom Kubernetes component startup parameter function (parameter `extra_args`), you need to submit a ticket for application.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::KubernetesAsScalingGroup",
    "Properties" : {
        "<a href="#clusterid" title="ClusterId">ClusterId</a>" : <i>String</i>,
        "<a href="#extraargs" title="ExtraArgs">ExtraArgs</a>" : <i>[ String, ... ]</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#unschedulable" title="Unschedulable">Unschedulable</a>" : <i>Double</i>,
        "<a href="#autoscalingconfig" title="AutoScalingConfig">AutoScalingConfig</a>" : <i>[ <a href="autoscalingconfigdefinition.md">AutoScalingConfigDefinition</a>, ... ]</i>,
        "<a href="#autoscalinggroup" title="AutoScalingGroup">AutoScalingGroup</a>" : <i>[ <a href="autoscalinggroupdefinition.md">AutoScalingGroupDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::KubernetesAsScalingGroup
Properties:
    <a href="#clusterid" title="ClusterId">ClusterId</a>: <i>String</i>
    <a href="#extraargs" title="ExtraArgs">ExtraArgs</a>: <i>
      - String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#unschedulable" title="Unschedulable">Unschedulable</a>: <i>Double</i>
    <a href="#autoscalingconfig" title="AutoScalingConfig">AutoScalingConfig</a>: <i>
      - <a href="autoscalingconfigdefinition.md">AutoScalingConfigDefinition</a></i>
    <a href="#autoscalinggroup" title="AutoScalingGroup">AutoScalingGroup</a>: <i>
      - <a href="autoscalinggroupdefinition.md">AutoScalingGroupDefinition</a></i>
</pre>

## Properties

#### ClusterId

ID of the cluster.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtraArgs

Custom parameter information related to the node.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

Labels of kubernetes AS Group created nodes.

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unschedulable

Sets whether the joining node participates in the schedule. Default is '0'. Participate in scheduling.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoScalingConfig

_Required_: No

_Type_: List of <a href="autoscalingconfigdefinition.md">AutoScalingConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoScalingGroup

_Required_: No

_Type_: List of <a href="autoscalinggroupdefinition.md">AutoScalingGroupDefinition</a>

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

