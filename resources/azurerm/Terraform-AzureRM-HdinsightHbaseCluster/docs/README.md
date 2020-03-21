# Terraform::AzureRM::HdinsightHbaseCluster

CloudFormation equivalent of azurerm_hdinsight_hbase_cluster

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::HdinsightHbaseCluster",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#clusterversion" title="ClusterVersion">ClusterVersion</a>" : <i>String</i>,
        "<a href="#httpsendpoint" title="HttpsEndpoint">HttpsEndpoint</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#sshendpoint" title="SshEndpoint">SshEndpoint</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#tier" title="Tier">Tier</a>" : <i>String</i>,
        "<a href="#componentversion" title="ComponentVersion">ComponentVersion</a>" : <i>[ &lt;a href=&#34;componentversion.md&#34;&gt;ComponentVersion&lt;/a&gt;, ... ]</i>,
        "<a href="#gateway" title="Gateway">Gateway</a>" : <i>[ &lt;a href=&#34;gateway.md&#34;&gt;Gateway&lt;/a&gt;, ... ]</i>,
        "<a href="#roles" title="Roles">Roles</a>" : <i>[ &lt;a href=&#34;roles.md&#34;&gt;Roles&lt;/a&gt;, ... ]</i>,
        "<a href="#storageaccount" title="StorageAccount">StorageAccount</a>" : <i>[ &lt;a href=&#34;storageaccount.md&#34;&gt;StorageAccount&lt;/a&gt;, ... ]</i>,
        "<a href="#storageaccountgen2" title="StorageAccountGen2">StorageAccountGen2</a>" : <i>[ &lt;a href=&#34;storageaccountgen2.md&#34;&gt;StorageAccountGen2&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#headnode" title="HeadNode">HeadNode</a>" : <i>[ &lt;a href=&#34;headnode.md&#34;&gt;HeadNode&lt;/a&gt;, ... ]</i>,
        "<a href="#workernode" title="WorkerNode">WorkerNode</a>" : <i>[ &lt;a href=&#34;workernode.md&#34;&gt;WorkerNode&lt;/a&gt;, ... ]</i>,
        "<a href="#zookeepernode" title="ZookeeperNode">ZookeeperNode</a>" : <i>[ &lt;a href=&#34;zookeepernode.md&#34;&gt;ZookeeperNode&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::HdinsightHbaseCluster
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#clusterversion" title="ClusterVersion">ClusterVersion</a>: <i>String</i>
    <a href="#httpsendpoint" title="HttpsEndpoint">HttpsEndpoint</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#sshendpoint" title="SshEndpoint">SshEndpoint</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#tier" title="Tier">Tier</a>: <i>String</i>
    <a href="#componentversion" title="ComponentVersion">ComponentVersion</a>: <i>
      - &lt;a href=&#34;componentversion.md&#34;&gt;ComponentVersion&lt;/a&gt;</i>
    <a href="#gateway" title="Gateway">Gateway</a>: <i>
      - &lt;a href=&#34;gateway.md&#34;&gt;Gateway&lt;/a&gt;</i>
    <a href="#roles" title="Roles">Roles</a>: <i>
      - &lt;a href=&#34;roles.md&#34;&gt;Roles&lt;/a&gt;</i>
    <a href="#storageaccount" title="StorageAccount">StorageAccount</a>: <i>
      - &lt;a href=&#34;storageaccount.md&#34;&gt;StorageAccount&lt;/a&gt;</i>
    <a href="#storageaccountgen2" title="StorageAccountGen2">StorageAccountGen2</a>: <i>
      - &lt;a href=&#34;storageaccountgen2.md&#34;&gt;StorageAccountGen2&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#headnode" title="HeadNode">HeadNode</a>: <i>
      - &lt;a href=&#34;headnode.md&#34;&gt;HeadNode&lt;/a&gt;</i>
    <a href="#workernode" title="WorkerNode">WorkerNode</a>: <i>
      - &lt;a href=&#34;workernode.md&#34;&gt;WorkerNode&lt;/a&gt;</i>
    <a href="#zookeepernode" title="ZookeeperNode">ZookeeperNode</a>: <i>
      - &lt;a href=&#34;zookeepernode.md&#34;&gt;ZookeeperNode&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterVersion

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpsEndpoint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshEndpoint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tier

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComponentVersion

_Required_: No

_Type_: List of &lt;a href=&#34;componentversion.md&#34;&gt;ComponentVersion&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gateway

_Required_: No

_Type_: List of &lt;a href=&#34;gateway.md&#34;&gt;Gateway&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Roles

_Required_: No

_Type_: List of &lt;a href=&#34;roles.md&#34;&gt;Roles&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccount

_Required_: No

_Type_: List of &lt;a href=&#34;storageaccount.md&#34;&gt;StorageAccount&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountGen2

_Required_: No

_Type_: List of &lt;a href=&#34;storageaccountgen2.md&#34;&gt;StorageAccountGen2&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeadNode

_Required_: No

_Type_: List of &lt;a href=&#34;headnode.md&#34;&gt;HeadNode&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerNode

_Required_: No

_Type_: List of &lt;a href=&#34;workernode.md&#34;&gt;WorkerNode&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZookeeperNode

_Required_: No

_Type_: List of &lt;a href=&#34;zookeepernode.md&#34;&gt;ZookeeperNode&lt;/a&gt;

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

Returns the &lt;code&gt;HttpsEndpoint&lt;/code&gt; value.

#### SshEndpoint

Returns the &lt;code&gt;SshEndpoint&lt;/code&gt; value.

