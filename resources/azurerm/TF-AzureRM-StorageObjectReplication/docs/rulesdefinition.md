# TF::AzureRM::StorageObjectReplication RulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#copyblobscreatedafter" title="CopyBlobsCreatedAfter">CopyBlobsCreatedAfter</a>" : <i>String</i>,
    "<a href="#destinationcontainername" title="DestinationContainerName">DestinationContainerName</a>" : <i>String</i>,
    "<a href="#filteroutblobswithprefix" title="FilterOutBlobsWithPrefix">FilterOutBlobsWithPrefix</a>" : <i>[ String, ... ]</i>,
    "<a href="#sourcecontainername" title="SourceContainerName">SourceContainerName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#copyblobscreatedafter" title="CopyBlobsCreatedAfter">CopyBlobsCreatedAfter</a>: <i>String</i>
<a href="#destinationcontainername" title="DestinationContainerName">DestinationContainerName</a>: <i>String</i>
<a href="#filteroutblobswithprefix" title="FilterOutBlobsWithPrefix">FilterOutBlobsWithPrefix</a>: <i>
      - String</i>
<a href="#sourcecontainername" title="SourceContainerName">SourceContainerName</a>: <i>String</i>
</pre>

## Properties

#### CopyBlobsCreatedAfter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationContainerName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterOutBlobsWithPrefix

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceContainerName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

