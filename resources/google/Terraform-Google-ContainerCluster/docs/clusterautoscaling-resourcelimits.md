# Terraform::Google::ContainerCluster ClusterAutoscaling ResourceLimits

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#maximum" title="Maximum">Maximum</a>" : <i>Double</i>,
    "<a href="#minimum" title="Minimum">Minimum</a>" : <i>Double</i>,
    "<a href="#resourcetype" title="ResourceType">ResourceType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#maximum" title="Maximum">Maximum</a>: <i>Double</i>
<a href="#minimum" title="Minimum">Minimum</a>: <i>Double</i>
<a href="#resourcetype" title="ResourceType">ResourceType</a>: <i>String</i>
</pre>

## Properties

#### Maximum

Maximum amount of the resource in the cluster.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Minimum

Minimum amount of the resource in the cluster.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceType

The type of the resource. For example, `cpu` and
`memory`.  See the [guide to using Node Auto-Provisioning](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning)
for a list of types.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

