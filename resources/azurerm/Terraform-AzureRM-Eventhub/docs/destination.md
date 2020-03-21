# Terraform::AzureRM::Eventhub Destination

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#archivenameformat" title="ArchiveNameFormat">ArchiveNameFormat</a>" : <i>String</i>,
    "<a href="#blobcontainername" title="BlobContainerName">BlobContainerName</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#storageaccountid" title="StorageAccountId">StorageAccountId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#archivenameformat" title="ArchiveNameFormat">ArchiveNameFormat</a>: <i>String</i>
<a href="#blobcontainername" title="BlobContainerName">BlobContainerName</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#storageaccountid" title="StorageAccountId">StorageAccountId</a>: <i>String</i>
</pre>

## Properties

#### ArchiveNameFormat

The Blob naming convention for archiving. e.g. `{Namespace}/{EventHub}/{PartitionId}/{Year}/{Month}/{Day}/{Hour}/{Minute}/{Second}`. Here all the parameters (Namespace,EventHub .. etc) are mandatory irrespective of order.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlobContainerName

The name of the Container within the Blob Storage Account where messages should be archived.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The Name of the Destination where the capture should take place. At this time the only supported value is `EventHubArchive.AzureBlockBlob`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountId

The ID of the Blob Storage Account where messages should be archived.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

