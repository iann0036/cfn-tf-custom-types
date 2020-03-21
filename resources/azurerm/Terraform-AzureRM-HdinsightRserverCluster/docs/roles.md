# Terraform::AzureRM::HdinsightRserverCluster Roles

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#edgenode" title="EdgeNode">EdgeNode</a>" : <i>[ <a href="roles-edgenode.md">EdgeNode</a>, ... ]</i>,
    "<a href="#headnode" title="HeadNode">HeadNode</a>" : <i>[ <a href="roles-headnode.md">HeadNode</a>, ... ]</i>,
    "<a href="#workernode" title="WorkerNode">WorkerNode</a>" : <i>[ <a href="roles-workernode.md">WorkerNode</a>, ... ]</i>,
    "<a href="#zookeepernode" title="ZookeeperNode">ZookeeperNode</a>" : <i>[ <a href="roles-zookeepernode.md">ZookeeperNode</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#edgenode" title="EdgeNode">EdgeNode</a>: <i>
      - <a href="roles-edgenode.md">EdgeNode</a></i>
<a href="#headnode" title="HeadNode">HeadNode</a>: <i>
      - <a href="roles-headnode.md">HeadNode</a></i>
<a href="#workernode" title="WorkerNode">WorkerNode</a>: <i>
      - <a href="roles-workernode.md">WorkerNode</a></i>
<a href="#zookeepernode" title="ZookeeperNode">ZookeeperNode</a>: <i>
      - <a href="roles-zookeepernode.md">ZookeeperNode</a></i>
</pre>

## Properties

#### EdgeNode

_Required_: No

_Type_: List of <a href="roles-edgenode.md">EdgeNode</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeadNode

_Required_: No

_Type_: List of <a href="roles-headnode.md">HeadNode</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerNode

_Required_: No

_Type_: List of <a href="roles-workernode.md">WorkerNode</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZookeeperNode

_Required_: No

_Type_: List of <a href="roles-zookeepernode.md">ZookeeperNode</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

