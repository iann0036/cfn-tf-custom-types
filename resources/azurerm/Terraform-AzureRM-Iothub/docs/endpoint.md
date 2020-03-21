# Terraform::AzureRM::Iothub Endpoint

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#batchfrequencyinseconds" title="BatchFrequencyInSeconds">BatchFrequencyInSeconds</a>" : <i>Double</i>,
    "<a href="#connectionstring" title="ConnectionString">ConnectionString</a>" : <i>String</i>,
    "<a href="#containername" title="ContainerName">ContainerName</a>" : <i>String</i>,
    "<a href="#encoding" title="Encoding">Encoding</a>" : <i>String</i>,
    "<a href="#filenameformat" title="FileNameFormat">FileNameFormat</a>" : <i>String</i>,
    "<a href="#maxchunksizeinbytes" title="MaxChunkSizeInBytes">MaxChunkSizeInBytes</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#batchfrequencyinseconds" title="BatchFrequencyInSeconds">BatchFrequencyInSeconds</a>: <i>Double</i>
<a href="#connectionstring" title="ConnectionString">ConnectionString</a>: <i>String</i>
<a href="#containername" title="ContainerName">ContainerName</a>: <i>String</i>
<a href="#encoding" title="Encoding">Encoding</a>: <i>String</i>
<a href="#filenameformat" title="FileNameFormat">FileNameFormat</a>: <i>String</i>
<a href="#maxchunksizeinbytes" title="MaxChunkSizeInBytes">MaxChunkSizeInBytes</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### BatchFrequencyInSeconds

Time interval at which blobs are written to storage. Value should be between 60 and 720 seconds. Default value is 300 seconds. This attribute is mandatory for endpoint type `AzureIotHub.StorageContainer`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionString

The connection string for the endpoint.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContainerName

The name of storage container in the storage account. This attribute is mandatory for endpoint type `AzureIotHub.StorageContainer`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encoding

Encoding that is used to serialize messages to blobs. Supported values are 'avro' and 'avrodeflate'. Default value is 'avro'. This attribute is mandatory for endpoint type `AzureIotHub.StorageContainer`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileNameFormat

File name format for the blob. Default format is ``{iothub}/{partition}/{YYYY}/{MM}/{DD}/{HH}/{mm}``. All parameters are mandatory but can be reordered. This attribute is mandatory for endpoint type `AzureIotHub.StorageContainer`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxChunkSizeInBytes

Maximum number of bytes for each blob written to storage. Value should be between 10485760(10MB) and 524288000(500MB). Default value is 314572800(300MB). This attribute is mandatory for endpoint type `AzureIotHub.StorageContainer`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the endpoint. The name must be unique across endpoint types. The following names are reserved:  `events`, `operationsMonitoringEvents`, `fileNotifications` and `$default`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of the endpoint. Possible values are `AzureIotHub.StorageContainer`, `AzureIotHub.ServiceBusQueue`, `AzureIotHub.ServiceBusTopic` or `AzureIotHub.EventHub`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

