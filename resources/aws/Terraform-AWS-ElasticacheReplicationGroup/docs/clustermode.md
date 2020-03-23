# Terraform::AWS::ElasticacheReplicationGroup ClusterMode

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#numnodegroups" title="NumNodeGroups">NumNodeGroups</a>" : <i>Double</i>,
    "<a href="#replicaspernodegroup" title="ReplicasPerNodeGroup">ReplicasPerNodeGroup</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#numnodegroups" title="NumNodeGroups">NumNodeGroups</a>: <i>Double</i>
<a href="#replicaspernodegroup" title="ReplicasPerNodeGroup">ReplicasPerNodeGroup</a>: <i>Double</i>
</pre>

## Properties

#### NumNodeGroups

Specify the number of node groups (shards) for this Redis replication group. Changing this number will trigger an online resizing operation before other settings modifications.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplicasPerNodeGroup

Specify the number of replica nodes in each node group. Valid values are 0 to 5. Changing this number will force a new resource.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

