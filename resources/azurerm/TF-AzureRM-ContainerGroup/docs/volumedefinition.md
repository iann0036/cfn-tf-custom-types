# TF::AzureRM::ContainerGroup VolumeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#emptydir" title="EmptyDir">EmptyDir</a>" : <i>Boolean</i>,
    "<a href="#mountpath" title="MountPath">MountPath</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#readonly" title="ReadOnly">ReadOnly</a>" : <i>Boolean</i>,
    "<a href="#secret" title="Secret">Secret</a>" : <i>[ <a href="secretdefinition.md">SecretDefinition</a>, ... ]</i>,
    "<a href="#sharename" title="ShareName">ShareName</a>" : <i>String</i>,
    "<a href="#storageaccountkey" title="StorageAccountKey">StorageAccountKey</a>" : <i>String</i>,
    "<a href="#storageaccountname" title="StorageAccountName">StorageAccountName</a>" : <i>String</i>,
    "<a href="#gitrepo" title="GitRepo">GitRepo</a>" : <i>[ <a href="gitrepodefinition.md">GitRepoDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#emptydir" title="EmptyDir">EmptyDir</a>: <i>Boolean</i>
<a href="#mountpath" title="MountPath">MountPath</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#readonly" title="ReadOnly">ReadOnly</a>: <i>Boolean</i>
<a href="#secret" title="Secret">Secret</a>: <i>
      - <a href="secretdefinition.md">SecretDefinition</a></i>
<a href="#sharename" title="ShareName">ShareName</a>: <i>String</i>
<a href="#storageaccountkey" title="StorageAccountKey">StorageAccountKey</a>: <i>String</i>
<a href="#storageaccountname" title="StorageAccountName">StorageAccountName</a>: <i>String</i>
<a href="#gitrepo" title="GitRepo">GitRepo</a>: <i>
      - <a href="gitrepodefinition.md">GitRepoDefinition</a></i>
</pre>

## Properties

#### EmptyDir

Boolean as to whether the mounted volume should be an empty directory. Defaults to `false`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

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

#### Secret

A map of secrets that will be mounted as files in the volume. Changing this forces a new resource to be created.

_Required_: No

_Type_: List of <a href="secretdefinition.md">SecretDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShareName

The Azure storage share that is to be mounted as a volume. This must be created on the storage account specified as above. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountKey

The access key for the Azure Storage account specified as above. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountName

The Azure storage account from which the volume is to be mounted. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GitRepo

_Required_: No

_Type_: List of <a href="gitrepodefinition.md">GitRepoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

