# Terraform::AzureRM::HdinsightSparkCluster StorageAccountGen2

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#filesystemid" title="FilesystemId">FilesystemId</a>" : <i>String</i>,
    "<a href="#isdefault" title="IsDefault">IsDefault</a>" : <i>Boolean</i>,
    "<a href="#managedidentityresourceid" title="ManagedIdentityResourceId">ManagedIdentityResourceId</a>" : <i>String</i>,
    "<a href="#storageresourceid" title="StorageResourceId">StorageResourceId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#filesystemid" title="FilesystemId">FilesystemId</a>: <i>String</i>
<a href="#isdefault" title="IsDefault">IsDefault</a>: <i>Boolean</i>
<a href="#managedidentityresourceid" title="ManagedIdentityResourceId">ManagedIdentityResourceId</a>: <i>String</i>
<a href="#storageresourceid" title="StorageResourceId">StorageResourceId</a>: <i>String</i>
</pre>

## Properties

#### FilesystemId

The ID of the Gen2 Filesystem. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsDefault

Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedIdentityResourceId

The ID of Managed Identity to use for accessing the Gen2 filesystem. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageResourceId

The ID of the Storage Account. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

