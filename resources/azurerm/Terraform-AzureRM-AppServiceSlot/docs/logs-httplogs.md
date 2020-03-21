# Terraform::AzureRM::AppServiceSlot Logs HttpLogs

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#azureblobstorage" title="AzureBlobStorage">AzureBlobStorage</a>" : <i>[ <a href="logs-httplogs-azureblobstorage.md">AzureBlobStorage</a>, ... ]</i>,
    "<a href="#filesystem" title="FileSystem">FileSystem</a>" : <i>[ <a href="logs-httplogs-filesystem.md">FileSystem</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#azureblobstorage" title="AzureBlobStorage">AzureBlobStorage</a>: <i>
      - <a href="logs-httplogs-azureblobstorage.md">AzureBlobStorage</a></i>
<a href="#filesystem" title="FileSystem">FileSystem</a>: <i>
      - <a href="logs-httplogs-filesystem.md">FileSystem</a></i>
</pre>

## Properties

#### AzureBlobStorage

_Required_: No

_Type_: List of <a href="logs-httplogs-azureblobstorage.md">AzureBlobStorage</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileSystem

_Required_: No

_Type_: List of <a href="logs-httplogs-filesystem.md">FileSystem</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

