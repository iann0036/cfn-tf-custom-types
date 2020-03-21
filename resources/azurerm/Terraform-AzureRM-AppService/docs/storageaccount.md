# Terraform::AzureRM::AppService StorageAccount

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accesskey" title="AccessKey">AccessKey</a>" : <i>String</i>,
    "<a href="#accountname" title="AccountName">AccountName</a>" : <i>String</i>,
    "<a href="#mountpath" title="MountPath">MountPath</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#sharename" title="ShareName">ShareName</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#accesskey" title="AccessKey">AccessKey</a>: <i>String</i>
<a href="#accountname" title="AccountName">AccountName</a>: <i>String</i>
<a href="#mountpath" title="MountPath">MountPath</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#sharename" title="ShareName">ShareName</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### AccessKey

The access key for the storage account.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountName

The name of the storage account.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MountPath

The path to mount the storage within the site's runtime environment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the storage account identifier.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShareName

The name of the file share (container name, for Blob storage).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of storage. Possible values are `AzureBlob` and `AzureFiles`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

