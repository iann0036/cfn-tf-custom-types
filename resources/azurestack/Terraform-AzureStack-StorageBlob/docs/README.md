# Terraform::AzureStack::StorageBlob

Manages an Azure Storage Blob.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureStack::StorageBlob",
    "Properties" : {
        "<a href="#attempts" title="Attempts">Attempts</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#parallelism" title="Parallelism">Parallelism</a>" : <i>Double</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#size" title="Size">Size</a>" : <i>Double</i>,
        "<a href="#source" title="Source">Source</a>" : <i>String</i>,
        "<a href="#sourceuri" title="SourceUri">SourceUri</a>" : <i>String</i>,
        "<a href="#storageaccountname" title="StorageAccountName">StorageAccountName</a>" : <i>String</i>,
        "<a href="#storagecontainername" title="StorageContainerName">StorageContainerName</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureStack::StorageBlob
Properties:
    <a href="#attempts" title="Attempts">Attempts</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#parallelism" title="Parallelism">Parallelism</a>: <i>Double</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#size" title="Size">Size</a>: <i>Double</i>
    <a href="#source" title="Source">Source</a>: <i>String</i>
    <a href="#sourceuri" title="SourceUri">SourceUri</a>: <i>String</i>
    <a href="#storageaccountname" title="StorageAccountName">StorageAccountName</a>: <i>String</i>
    <a href="#storagecontainername" title="StorageContainerName">StorageContainerName</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### Attempts

The number of attempts to make per page or block when uploading. Defaults to `1`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the storage blob. Must be unique within the storage container the blob is located.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parallelism

The number of workers per CPU core to run for concurrent uploads. Defaults to `8`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to
create the storage container. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

Used only for `page` blobs to specify the size in bytes of the blob to be created. Must be a multiple of 512. Defaults to 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

An absolute path to a file on the local system. Cannot be defined if `source_uri` is defined.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceUri

The URI of an existing blob, or a file in the Azure File service, to use as the source contents
for the blob to be created. Changing this forces a new resource to be created. Cannot be defined if `source` is defined.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountName

Specifies the storage account in which to create the storage container.
Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageContainerName

The name of the storage container in which this blob should be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of the storage blob to be created. One of either `block` or `page`. When not copying from an existing blob,
this becomes required.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### Url

Returns the <code>Url</code> value.

