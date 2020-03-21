# Terraform::AzureRM::ContainerGroup Volume

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#mountpath" title="MountPath">MountPath</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#readonly" title="ReadOnly">ReadOnly</a>" : <i>Boolean</i>,
    "<a href="#sharename" title="ShareName">ShareName</a>" : <i>String</i>,
    "<a href="#storageaccountkey" title="StorageAccountKey">StorageAccountKey</a>" : <i>String</i>,
    "<a href="#storageaccountname" title="StorageAccountName">StorageAccountName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#mountpath" title="MountPath">MountPath</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#readonly" title="ReadOnly">ReadOnly</a>: <i>Boolean</i>
<a href="#sharename" title="ShareName">ShareName</a>: <i>String</i>
<a href="#storageaccountkey" title="StorageAccountKey">StorageAccountKey</a>: <i>String</i>
<a href="#storageaccountname" title="StorageAccountName">StorageAccountName</a>: <i>String</i>
</pre>

## Properties

#### MountPath

The path on which this volume is to be mounted. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the volume mount. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadOnly

Specify if the volume is to be mounted as read only or not. The default value is `false`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShareName

The Azure storage share that is to be mounted as a volume. This must be created on the storage account specified as above. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountKey

The access key for the Azure Storage account specified as above. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountName

The Azure storage account from which the volume is to be mounted. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

