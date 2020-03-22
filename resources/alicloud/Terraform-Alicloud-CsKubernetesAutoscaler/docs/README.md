# Terraform::Alicloud::CsKubernetesAutoscaler

This resource will help you to manager cluster-autoscaler in Kubernetes Cluster. 

-> **NOTE:** The scaling group must use CentOS7 or AliyunLinux2 as base image.

-> **NOTE:** The cluster-autoscaler can only use the same size of instanceTypes in one scaling group. 

-> **NOTE:** Add Policy to RAM role of the node to deploy cluster-autoscaler if you need.

-> **NOTE:** Available in 1.65.0+.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::CsKubernetesAutoscaler",
    "Properties" : {
        "<a href="#clusterid" title="ClusterId">ClusterId</a>" : <i>String</i>,
        "<a href="#cooldownduration" title="CoolDownDuration">CoolDownDuration</a>" : <i>String</i>,
        "<a href="#deferscaleinduration" title="DeferScaleInDuration">DeferScaleInDuration</a>" : <i>String</i>,
        "<a href="#utilization" title="Utilization">Utilization</a>" : <i>String</i>,
        "<a href="#nodepools" title="Nodepools">Nodepools</a>" : <i>[ <a href="nodepools.md">Nodepools</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::CsKubernetesAutoscaler
Properties:
    <a href="#clusterid" title="ClusterId">ClusterId</a>: <i>String</i>
    <a href="#cooldownduration" title="CoolDownDuration">CoolDownDuration</a>: <i>String</i>
    <a href="#deferscaleinduration" title="DeferScaleInDuration">DeferScaleInDuration</a>: <i>String</i>
    <a href="#utilization" title="Utilization">Utilization</a>: <i>String</i>
    <a href="#nodepools" title="Nodepools">Nodepools</a>: <i>
      - <a href="nodepools.md">Nodepools</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### ClusterId

The id of kubernetes cluster.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoolDownDuration

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeferScaleInDuration

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Utilization

The utilization option of cluster-autoscaler.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nodepools

_Required_: No

_Type_: List of <a href="nodepools.md">Nodepools</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

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

