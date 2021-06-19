# TF::AzureRM::CosmosdbCassandraTable SchemaDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#clusterkey" title="ClusterKey">ClusterKey</a>" : <i>[ <a href="clusterkeydefinition.md">ClusterKeyDefinition</a>, ... ]</i>,
    "<a href="#column" title="Column">Column</a>" : <i>[ <a href="columndefinition.md">ColumnDefinition</a>, ... ]</i>,
    "<a href="#partitionkey" title="PartitionKey">PartitionKey</a>" : <i>[ <a href="partitionkeydefinition.md">PartitionKeyDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#clusterkey" title="ClusterKey">ClusterKey</a>: <i>
      - <a href="clusterkeydefinition.md">ClusterKeyDefinition</a></i>
<a href="#column" title="Column">Column</a>: <i>
      - <a href="columndefinition.md">ColumnDefinition</a></i>
<a href="#partitionkey" title="PartitionKey">PartitionKey</a>: <i>
      - <a href="partitionkeydefinition.md">PartitionKeyDefinition</a></i>
</pre>

## Properties

#### ClusterKey

_Required_: No

_Type_: List of <a href="clusterkeydefinition.md">ClusterKeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Column

_Required_: No

_Type_: List of <a href="columndefinition.md">ColumnDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PartitionKey

_Required_: No

_Type_: List of <a href="partitionkeydefinition.md">PartitionKeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

