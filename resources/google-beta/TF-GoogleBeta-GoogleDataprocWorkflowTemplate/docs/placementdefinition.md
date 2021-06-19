# TF::GoogleBeta::GoogleDataprocWorkflowTemplate PlacementDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#clusterselector" title="ClusterSelector">ClusterSelector</a>" : <i>[ <a href="clusterselectordefinition.md">ClusterSelectorDefinition</a>, ... ]</i>,
    "<a href="#managedcluster" title="ManagedCluster">ManagedCluster</a>" : <i>[ <a href="managedclusterdefinition.md">ManagedClusterDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#clusterselector" title="ClusterSelector">ClusterSelector</a>: <i>
      - <a href="clusterselectordefinition.md">ClusterSelectorDefinition</a></i>
<a href="#managedcluster" title="ManagedCluster">ManagedCluster</a>: <i>
      - <a href="managedclusterdefinition.md">ManagedClusterDefinition</a></i>
</pre>

## Properties

#### ClusterSelector

_Required_: No

_Type_: List of <a href="clusterselectordefinition.md">ClusterSelectorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedCluster

_Required_: No

_Type_: List of <a href="managedclusterdefinition.md">ManagedClusterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

