# TF::AzureRM::DataFactoryDatasetJson AzureBlobStorageLocationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#container" title="Container">Container</a>" : <i>String</i>,
    "<a href="#filename" title="Filename">Filename</a>" : <i>String</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#container" title="Container">Container</a>: <i>String</i>
<a href="#filename" title="Filename">Filename</a>: <i>String</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
</pre>

## Properties

#### Container

The container on the Azure Blob Storage Account hosting the file.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filename

The filename of the file on the web server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

The folder path to the file on the web server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

