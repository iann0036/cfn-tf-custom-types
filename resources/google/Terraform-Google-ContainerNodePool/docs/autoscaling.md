# Terraform::Google::ContainerNodePool Autoscaling

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#maxnodecount" title="MaxNodeCount">MaxNodeCount</a>" : <i>Double</i>,
    "<a href="#minnodecount" title="MinNodeCount">MinNodeCount</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#maxnodecount" title="MaxNodeCount">MaxNodeCount</a>: <i>Double</i>
<a href="#minnodecount" title="MinNodeCount">MinNodeCount</a>: <i>Double</i>
</pre>

## Properties

#### MaxNodeCount

Maximum number of nodes in the NodePool. Must be >= min_node_count.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinNodeCount

Minimum number of nodes in the NodePool. Must be >=0 and
<= `max_node_count`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

