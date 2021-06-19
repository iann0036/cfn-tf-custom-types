# TF::AzureRM::HdinsightRserverCluster StorageAccountDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#isdefault" title="IsDefault">IsDefault</a>" : <i>Boolean</i>,
    "<a href="#storageaccountkey" title="StorageAccountKey">StorageAccountKey</a>" : <i>String</i>,
    "<a href="#storagecontainerid" title="StorageContainerId">StorageContainerId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#isdefault" title="IsDefault">IsDefault</a>: <i>Boolean</i>
<a href="#storageaccountkey" title="StorageAccountKey">StorageAccountKey</a>: <i>String</i>
<a href="#storagecontainerid" title="StorageContainerId">StorageContainerId</a>: <i>String</i>
</pre>

## Properties

#### IsDefault

Is this the Default Storage Account for the HDInsight RServer Cluster? Changing this forces a new resource to be created.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountKey

The Access Key which should be used to connect to the Storage Account. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageContainerId

The ID of the Storage Container. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

