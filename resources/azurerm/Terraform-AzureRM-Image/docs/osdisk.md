# Terraform::AzureRM::Image OsDisk

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bloburi" title="BlobUri">BlobUri</a>" : <i>String</i>,
    "<a href="#caching" title="Caching">Caching</a>" : <i>String</i>,
    "<a href="#manageddiskid" title="ManagedDiskId">ManagedDiskId</a>" : <i>String</i>,
    "<a href="#osstate" title="OsState">OsState</a>" : <i>String</i>,
    "<a href="#ostype" title="OsType">OsType</a>" : <i>String</i>,
    "<a href="#sizegb" title="SizeGb">SizeGb</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#bloburi" title="BlobUri">BlobUri</a>: <i>String</i>
<a href="#caching" title="Caching">Caching</a>: <i>String</i>
<a href="#manageddiskid" title="ManagedDiskId">ManagedDiskId</a>: <i>String</i>
<a href="#osstate" title="OsState">OsState</a>: <i>String</i>
<a href="#ostype" title="OsType">OsType</a>: <i>String</i>
<a href="#sizegb" title="SizeGb">SizeGb</a>: <i>Double</i>
</pre>

## Properties

#### BlobUri

Specifies the URI in Azure storage of the blob that you want to use to create the image.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Caching

Specifies the caching mode as `ReadWrite`, `ReadOnly`, or `None`. The default is `None`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedDiskId

Specifies the ID of the managed disk resource that you want to use to create the image.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsState

Specifies the state of the operating system contained in the blob. Currently, the only value is Generalized.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsType

Specifies the type of operating system contained in the virtual machine image. Possible values are: Windows or Linux.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SizeGb

Specifies the size of the image to be created. The target size can't be smaller than the source size.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

