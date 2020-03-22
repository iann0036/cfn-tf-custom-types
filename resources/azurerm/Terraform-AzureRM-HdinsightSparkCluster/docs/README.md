# Terraform::AzureRM::HdinsightSparkCluster

Manages a HDInsight Spark Cluster.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::HdinsightSparkCluster",
    "Properties" : {
        "<a href="#clusterversion" title="ClusterVersion">ClusterVersion</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#tier" title="Tier">Tier</a>" : <i>String</i>,
        "<a href="#componentversion" title="ComponentVersion">ComponentVersion</a>" : <i>[ <a href="componentversion.md">ComponentVersion</a>, ... ]</i>,
        "<a href="#gateway" title="Gateway">Gateway</a>" : <i>[ <a href="gateway.md">Gateway</a>, ... ]</i>,
        "<a href="#roles" title="Roles">Roles</a>" : <i>[ <a href="roles.md">Roles</a>, ... ]</i>,
        "<a href="#storageaccount" title="StorageAccount">StorageAccount</a>" : <i>[ <a href="storageaccount.md">StorageAccount</a>, ... ]</i>,
        "<a href="#storageaccountgen2" title="StorageAccountGen2">StorageAccountGen2</a>" : <i>[ <a href="storageaccountgen2.md">StorageAccountGen2</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#headnode" title="HeadNode">HeadNode</a>" : <i>[ <a href="headnode.md">HeadNode</a>, ... ]</i>,
        "<a href="#workernode" title="WorkerNode">WorkerNode</a>" : <i>[ <a href="workernode.md">WorkerNode</a>, ... ]</i>,
        "<a href="#zookeepernode" title="ZookeeperNode">ZookeeperNode</a>" : <i>[ <a href="zookeepernode.md">ZookeeperNode</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::HdinsightSparkCluster
Properties:
    <a href="#clusterversion" title="ClusterVersion">ClusterVersion</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#tier" title="Tier">Tier</a>: <i>String</i>
    <a href="#componentversion" title="ComponentVersion">ComponentVersion</a>: <i>
      - <a href="componentversion.md">ComponentVersion</a></i>
    <a href="#gateway" title="Gateway">Gateway</a>: <i>
      - <a href="gateway.md">Gateway</a></i>
    <a href="#roles" title="Roles">Roles</a>: <i>
      - <a href="roles.md">Roles</a></i>
    <a href="#storageaccount" title="StorageAccount">StorageAccount</a>: <i>
      - <a href="storageaccount.md">StorageAccount</a></i>
    <a href="#storageaccountgen2" title="StorageAccountGen2">StorageAccountGen2</a>: <i>
      - <a href="storageaccountgen2.md">StorageAccountGen2</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#headnode" title="HeadNode">HeadNode</a>: <i>
      - <a href="headnode.md">HeadNode</a></i>
    <a href="#workernode" title="WorkerNode">WorkerNode</a>: <i>
      - <a href="workernode.md">WorkerNode</a></i>
    <a href="#zookeepernode" title="ZookeeperNode">ZookeeperNode</a>: <i>
      - <a href="zookeepernode.md">ZookeeperNode</a></i>
</pre>

## Properties

#### ClusterVersion

Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

Specifies the Azure Region which this HDInsight Spark Cluster should exist. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name for this HDInsight Spark Cluster. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

Specifies the name of the Resource Group in which this HDInsight Spark Cluster should exist. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A map of Tags which should be assigned to this HDInsight Spark Cluster.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tier

Specifies the Tier which should be used for this HDInsight Spark Cluster. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComponentVersion

_Required_: No

_Type_: List of <a href="componentversion.md">ComponentVersion</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gateway

_Required_: No

_Type_: List of <a href="gateway.md">Gateway</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Roles

_Required_: No

_Type_: List of <a href="roles.md">Roles</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccount

_Required_: No

_Type_: List of <a href="storageaccount.md">StorageAccount</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountGen2

_Required_: No

_Type_: List of <a href="storageaccountgen2.md">StorageAccountGen2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeadNode

_Required_: No

_Type_: List of <a href="headnode.md">HeadNode</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerNode

_Required_: No

_Type_: List of <a href="workernode.md">WorkerNode</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZookeeperNode

_Required_: No

_Type_: List of <a href="zookeepernode.md">ZookeeperNode</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### HttpsEndpoint

Returns the <code>HttpsEndpoint</code> value.

#### Id

Returns the <code>Id</code> value.

#### SshEndpoint

Returns the <code>SshEndpoint</code> value.

