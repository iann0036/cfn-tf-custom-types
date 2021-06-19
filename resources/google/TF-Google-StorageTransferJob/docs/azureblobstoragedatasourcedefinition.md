# TF::Google::StorageTransferJob AzureBlobStorageDataSourceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#container" title="Container">Container</a>" : <i>String</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>,
    "<a href="#storageaccount" title="StorageAccount">StorageAccount</a>" : <i>String</i>,
    "<a href="#azurecredentials" title="AzureCredentials">AzureCredentials</a>" : <i>[ <a href="azurecredentialsdefinition.md">AzureCredentialsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#container" title="Container">Container</a>: <i>String</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
<a href="#storageaccount" title="StorageAccount">StorageAccount</a>: <i>String</i>
<a href="#azurecredentials" title="AzureCredentials">AzureCredentials</a>: <i>
      - <a href="azurecredentialsdefinition.md">AzureCredentialsDefinition</a></i>
</pre>

## Properties

#### Container

The container to transfer from the Azure Storage account.`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

Root path to transfer objects. Must be an empty string or full path name that ends with a '/'. This field is treated as an object prefix. As such, it should generally not begin with a '/'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccount

The name of the Azure Storage account.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureCredentials

_Required_: No

_Type_: List of <a href="azurecredentialsdefinition.md">AzureCredentialsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

