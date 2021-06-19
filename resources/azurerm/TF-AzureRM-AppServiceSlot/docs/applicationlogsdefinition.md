# TF::AzureRM::AppServiceSlot ApplicationLogsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#filesystemlevel" title="FileSystemLevel">FileSystemLevel</a>" : <i>String</i>,
    "<a href="#azureblobstorage" title="AzureBlobStorage">AzureBlobStorage</a>" : <i>[ <a href="azureblobstoragedefinition.md">AzureBlobStorageDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#filesystemlevel" title="FileSystemLevel">FileSystemLevel</a>: <i>String</i>
<a href="#azureblobstorage" title="AzureBlobStorage">AzureBlobStorage</a>: <i>
      - <a href="azureblobstoragedefinition.md">AzureBlobStorageDefinition</a></i>
</pre>

## Properties

#### FileSystemLevel

The file system log level. Possible values are `Off`, `Error`, `Warning`, `Information`, and `Verbose`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureBlobStorage

_Required_: No

_Type_: List of <a href="azureblobstoragedefinition.md">AzureBlobStorageDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

