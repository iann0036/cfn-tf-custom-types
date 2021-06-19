# TF::AzureRM::SharedImageVersion TargetRegionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#regionalreplicacount" title="RegionalReplicaCount">RegionalReplicaCount</a>" : <i>Double</i>,
    "<a href="#storageaccounttype" title="StorageAccountType">StorageAccountType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#regionalreplicacount" title="RegionalReplicaCount">RegionalReplicaCount</a>: <i>Double</i>
<a href="#storageaccounttype" title="StorageAccountType">StorageAccountType</a>: <i>String</i>
</pre>

## Properties

#### Name

The Azure Region in which this Image Version should exist.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegionalReplicaCount

The number of replicas of the Image Version to be created per region.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountType

The storage account type for the image version. Possible values are `Standard_LRS` and `Standard_ZRS`. Defaults to `Standard_LRS`. You can store all of your image version replicas in Zone Redundant Storage by specifying `Standard_ZRS`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

