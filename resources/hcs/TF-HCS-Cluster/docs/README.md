# TF::HCS::Cluster

CloudFormation equivalent of hcs_cluster

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::HCS::Cluster",
    "Properties" : {
        "<a href="#auditlogstoragecontainerurl" title="AuditLogStorageContainerUrl">AuditLogStorageContainerUrl</a>" : <i>String</i>,
        "<a href="#auditloggingenabled" title="AuditLoggingEnabled">AuditLoggingEnabled</a>" : <i>Boolean</i>,
        "<a href="#clustermode" title="ClusterMode">ClusterMode</a>" : <i>String</i>,
        "<a href="#clustername" title="ClusterName">ClusterName</a>" : <i>String</i>,
        "<a href="#consuldatacenter" title="ConsulDatacenter">ConsulDatacenter</a>" : <i>String</i>,
        "<a href="#consulexternalendpoint" title="ConsulExternalEndpoint">ConsulExternalEndpoint</a>" : <i>Boolean</i>,
        "<a href="#consulfederationtoken" title="ConsulFederationToken">ConsulFederationToken</a>" : <i>String</i>,
        "<a href="#email" title="Email">Email</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#managedapplicationname" title="ManagedApplicationName">ManagedApplicationName</a>" : <i>String</i>,
        "<a href="#managedresourcegroupname" title="ManagedResourceGroupName">ManagedResourceGroupName</a>" : <i>String</i>,
        "<a href="#minconsulversion" title="MinConsulVersion">MinConsulVersion</a>" : <i>String</i>,
        "<a href="#planname" title="PlanName">PlanName</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#vnetcidr" title="VnetCidr">VnetCidr</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::HCS::Cluster
Properties:
    <a href="#auditlogstoragecontainerurl" title="AuditLogStorageContainerUrl">AuditLogStorageContainerUrl</a>: <i>String</i>
    <a href="#auditloggingenabled" title="AuditLoggingEnabled">AuditLoggingEnabled</a>: <i>Boolean</i>
    <a href="#clustermode" title="ClusterMode">ClusterMode</a>: <i>String</i>
    <a href="#clustername" title="ClusterName">ClusterName</a>: <i>String</i>
    <a href="#consuldatacenter" title="ConsulDatacenter">ConsulDatacenter</a>: <i>String</i>
    <a href="#consulexternalendpoint" title="ConsulExternalEndpoint">ConsulExternalEndpoint</a>: <i>Boolean</i>
    <a href="#consulfederationtoken" title="ConsulFederationToken">ConsulFederationToken</a>: <i>String</i>
    <a href="#email" title="Email">Email</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#managedapplicationname" title="ManagedApplicationName">ManagedApplicationName</a>: <i>String</i>
    <a href="#managedresourcegroupname" title="ManagedResourceGroupName">ManagedResourceGroupName</a>: <i>String</i>
    <a href="#minconsulversion" title="MinConsulVersion">MinConsulVersion</a>: <i>String</i>
    <a href="#planname" title="PlanName">PlanName</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#vnetcidr" title="VnetCidr">VnetCidr</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AuditLogStorageContainerUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuditLoggingEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterMode

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConsulDatacenter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConsulExternalEndpoint

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConsulFederationToken

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedApplicationName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedResourceGroupName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinConsulVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlanName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VnetCidr

_Required_: No

_Type_: String

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

#### BlobContainerName

Returns the <code>BlobContainerName</code> value.

#### ConsulAutomaticUpgrades

Returns the <code>ConsulAutomaticUpgrades</code> value.

#### ConsulCaFile

Returns the <code>ConsulCaFile</code> value.

#### ConsulClusterId

Returns the <code>ConsulClusterId</code> value.

#### ConsulConfigFile

Returns the <code>ConsulConfigFile</code> value.

#### ConsulConnect

Returns the <code>ConsulConnect</code> value.

#### ConsulExternalEndpointUrl

Returns the <code>ConsulExternalEndpointUrl</code> value.

#### ConsulPrivateEndpointUrl

Returns the <code>ConsulPrivateEndpointUrl</code> value.

#### ConsulRootTokenAccessorId

Returns the <code>ConsulRootTokenAccessorId</code> value.

#### ConsulRootTokenSecretId

Returns the <code>ConsulRootTokenSecretId</code> value.

#### ConsulSnapshotInterval

Returns the <code>ConsulSnapshotInterval</code> value.

#### ConsulSnapshotRetention

Returns the <code>ConsulSnapshotRetention</code> value.

#### ConsulVersion

Returns the <code>ConsulVersion</code> value.

#### Id

Returns the <code>Id</code> value.

#### ManagedApplicationId

Returns the <code>ManagedApplicationId</code> value.

#### ManagedIdentityName

Returns the <code>ManagedIdentityName</code> value.

#### State

Returns the <code>State</code> value.

#### StorageAccountName

Returns the <code>StorageAccountName</code> value.

#### StorageAccountResourceGroup

Returns the <code>StorageAccountResourceGroup</code> value.

#### VnetId

Returns the <code>VnetId</code> value.

#### VnetName

Returns the <code>VnetName</code> value.

#### VnetResourceGroupName

Returns the <code>VnetResourceGroupName</code> value.

