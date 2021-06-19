# TF::AzureRM::HdinsightSparkCluster RolesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#headnode" title="HeadNode">HeadNode</a>" : <i>[ <a href="headnodedefinition.md">HeadNodeDefinition</a>, ... ]</i>,
    "<a href="#workernode" title="WorkerNode">WorkerNode</a>" : <i>[ <a href="workernodedefinition.md">WorkerNodeDefinition</a>, ... ]</i>,
    "<a href="#zookeepernode" title="ZookeeperNode">ZookeeperNode</a>" : <i>[ <a href="zookeepernodedefinition.md">ZookeeperNodeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#headnode" title="HeadNode">HeadNode</a>: <i>
      - <a href="headnodedefinition.md">HeadNodeDefinition</a></i>
<a href="#workernode" title="WorkerNode">WorkerNode</a>: <i>
      - <a href="workernodedefinition.md">WorkerNodeDefinition</a></i>
<a href="#zookeepernode" title="ZookeeperNode">ZookeeperNode</a>: <i>
      - <a href="zookeepernodedefinition.md">ZookeeperNodeDefinition</a></i>
</pre>

## Properties

#### HeadNode

_Required_: No

_Type_: List of <a href="headnodedefinition.md">HeadNodeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerNode

_Required_: No

_Type_: List of <a href="workernodedefinition.md">WorkerNodeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZookeeperNode

_Required_: No

_Type_: List of <a href="zookeepernodedefinition.md">ZookeeperNodeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

