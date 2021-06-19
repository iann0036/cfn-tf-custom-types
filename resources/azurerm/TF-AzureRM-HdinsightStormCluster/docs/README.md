# TF::AzureRM::HdinsightStormCluster

Manages a HDInsight Storm Cluster.

!> **Note:** [HDInsight 3.6 is deprecated and will be retired on 2020-12-31 - HDInsight 4.0 no longer supports Storm Clusters](https://docs.microsoft.com/en-us/azure/hdinsight/hdinsight-component-versioning#available-versions) - as such this Terraform resource is deprecated and will be removed in the next major version of the AzureRM Terraform Provider.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::HdinsightStormCluster",
    "Properties" : {
        "<a href="#clusterversion" title="ClusterVersion">ClusterVersion</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tier" title="Tier">Tier</a>" : <i>String</i>,
        "<a href="#tlsminversion" title="TlsMinVersion">TlsMinVersion</a>" : <i>String</i>,
        "<a href="#componentversion" title="ComponentVersion">ComponentVersion</a>" : <i>[ <a href="componentversiondefinition.md">ComponentVersionDefinition</a>, ... ]</i>,
        "<a href="#gateway" title="Gateway">Gateway</a>" : <i>[ <a href="gatewaydefinition.md">GatewayDefinition</a>, ... ]</i>,
        "<a href="#metastores" title="Metastores">Metastores</a>" : <i>[ <a href="metastoresdefinition.md">MetastoresDefinition</a>, ... ]</i>,
        "<a href="#monitor" title="Monitor">Monitor</a>" : <i>[ <a href="monitordefinition.md">MonitorDefinition</a>, ... ]</i>,
        "<a href="#roles" title="Roles">Roles</a>" : <i>[ <a href="rolesdefinition.md">RolesDefinition</a>, ... ]</i>,
        "<a href="#storageaccount" title="StorageAccount">StorageAccount</a>" : <i>[ <a href="storageaccountdefinition.md">StorageAccountDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::HdinsightStormCluster
Properties:
    <a href="#clusterversion" title="ClusterVersion">ClusterVersion</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tier" title="Tier">Tier</a>: <i>String</i>
    <a href="#tlsminversion" title="TlsMinVersion">TlsMinVersion</a>: <i>String</i>
    <a href="#componentversion" title="ComponentVersion">ComponentVersion</a>: <i>
      - <a href="componentversiondefinition.md">ComponentVersionDefinition</a></i>
    <a href="#gateway" title="Gateway">Gateway</a>: <i>
      - <a href="gatewaydefinition.md">GatewayDefinition</a></i>
    <a href="#metastores" title="Metastores">Metastores</a>: <i>
      - <a href="metastoresdefinition.md">MetastoresDefinition</a></i>
    <a href="#monitor" title="Monitor">Monitor</a>: <i>
      - <a href="monitordefinition.md">MonitorDefinition</a></i>
    <a href="#roles" title="Roles">Roles</a>: <i>
      - <a href="rolesdefinition.md">RolesDefinition</a></i>
    <a href="#storageaccount" title="StorageAccount">StorageAccount</a>: <i>
      - <a href="storageaccountdefinition.md">StorageAccountDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### ClusterVersion

Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

Specifies the Azure Region which this HDInsight Storm Cluster should exist. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name for this HDInsight Storm Cluster. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

Specifies the name of the Resource Group in which this HDInsight Storm Cluster should exist. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A map of Tags which should be assigned to this HDInsight Storm Cluster.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tier

Specifies the Tier which should be used for this HDInsight Storm Cluster. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsMinVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComponentVersion

_Required_: No

_Type_: List of <a href="componentversiondefinition.md">ComponentVersionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gateway

_Required_: No

_Type_: List of <a href="gatewaydefinition.md">GatewayDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metastores

_Required_: No

_Type_: List of <a href="metastoresdefinition.md">MetastoresDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Monitor

_Required_: No

_Type_: List of <a href="monitordefinition.md">MonitorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Roles

_Required_: No

_Type_: List of <a href="rolesdefinition.md">RolesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccount

_Required_: No

_Type_: List of <a href="storageaccountdefinition.md">StorageAccountDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

