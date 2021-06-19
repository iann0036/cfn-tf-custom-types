# TF::AzureRM::CostManagementExportResourceGroup DeliveryInfoDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#containername" title="ContainerName">ContainerName</a>" : <i>String</i>,
    "<a href="#rootfolderpath" title="RootFolderPath">RootFolderPath</a>" : <i>String</i>,
    "<a href="#storageaccountid" title="StorageAccountId">StorageAccountId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#containername" title="ContainerName">ContainerName</a>: <i>String</i>
<a href="#rootfolderpath" title="RootFolderPath">RootFolderPath</a>: <i>String</i>
<a href="#storageaccountid" title="StorageAccountId">StorageAccountId</a>: <i>String</i>
</pre>

## Properties

#### ContainerName

The name of the container where exports will be uploaded.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootFolderPath

The path of the directory where exports will be uploaded.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountId

The storage account id where exports will be delivered.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

