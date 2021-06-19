# TF::AzureRM::DataFactoryDatasetDelimitedText

Manages an Azure Delimited Text Dataset inside an Azure Data Factory.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::DataFactoryDatasetDelimitedText",
    "Properties" : {
        "<a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>" : <i>[ <a href="additionalpropertiesdefinition.md">AdditionalPropertiesDefinition</a>, ... ]</i>,
        "<a href="#annotations" title="Annotations">Annotations</a>" : <i>[ String, ... ]</i>,
        "<a href="#columndelimiter" title="ColumnDelimiter">ColumnDelimiter</a>" : <i>String</i>,
        "<a href="#compressioncodec" title="CompressionCodec">CompressionCodec</a>" : <i>String</i>,
        "<a href="#compressionlevel" title="CompressionLevel">CompressionLevel</a>" : <i>String</i>,
        "<a href="#datafactoryname" title="DataFactoryName">DataFactoryName</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#encoding" title="Encoding">Encoding</a>" : <i>String</i>,
        "<a href="#escapecharacter" title="EscapeCharacter">EscapeCharacter</a>" : <i>String</i>,
        "<a href="#firstrowasheader" title="FirstRowAsHeader">FirstRowAsHeader</a>" : <i>Boolean</i>,
        "<a href="#folder" title="Folder">Folder</a>" : <i>String</i>,
        "<a href="#linkedservicename" title="LinkedServiceName">LinkedServiceName</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nullvalue" title="NullValue">NullValue</a>" : <i>String</i>,
        "<a href="#parameters" title="Parameters">Parameters</a>" : <i>[ <a href="parametersdefinition.md">ParametersDefinition</a>, ... ]</i>,
        "<a href="#quotecharacter" title="QuoteCharacter">QuoteCharacter</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#rowdelimiter" title="RowDelimiter">RowDelimiter</a>" : <i>String</i>,
        "<a href="#azureblobfslocation" title="AzureBlobFsLocation">AzureBlobFsLocation</a>" : <i>[ <a href="azureblobfslocationdefinition.md">AzureBlobFsLocationDefinition</a>, ... ]</i>,
        "<a href="#azureblobstoragelocation" title="AzureBlobStorageLocation">AzureBlobStorageLocation</a>" : <i>[ <a href="azureblobstoragelocationdefinition.md">AzureBlobStorageLocationDefinition</a>, ... ]</i>,
        "<a href="#httpserverlocation" title="HttpServerLocation">HttpServerLocation</a>" : <i>[ <a href="httpserverlocationdefinition.md">HttpServerLocationDefinition</a>, ... ]</i>,
        "<a href="#schemacolumn" title="SchemaColumn">SchemaColumn</a>" : <i>[ <a href="schemacolumndefinition.md">SchemaColumnDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::DataFactoryDatasetDelimitedText
Properties:
    <a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>: <i>
      - <a href="additionalpropertiesdefinition.md">AdditionalPropertiesDefinition</a></i>
    <a href="#annotations" title="Annotations">Annotations</a>: <i>
      - String</i>
    <a href="#columndelimiter" title="ColumnDelimiter">ColumnDelimiter</a>: <i>String</i>
    <a href="#compressioncodec" title="CompressionCodec">CompressionCodec</a>: <i>String</i>
    <a href="#compressionlevel" title="CompressionLevel">CompressionLevel</a>: <i>String</i>
    <a href="#datafactoryname" title="DataFactoryName">DataFactoryName</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#encoding" title="Encoding">Encoding</a>: <i>String</i>
    <a href="#escapecharacter" title="EscapeCharacter">EscapeCharacter</a>: <i>String</i>
    <a href="#firstrowasheader" title="FirstRowAsHeader">FirstRowAsHeader</a>: <i>Boolean</i>
    <a href="#folder" title="Folder">Folder</a>: <i>String</i>
    <a href="#linkedservicename" title="LinkedServiceName">LinkedServiceName</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nullvalue" title="NullValue">NullValue</a>: <i>String</i>
    <a href="#parameters" title="Parameters">Parameters</a>: <i>
      - <a href="parametersdefinition.md">ParametersDefinition</a></i>
    <a href="#quotecharacter" title="QuoteCharacter">QuoteCharacter</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#rowdelimiter" title="RowDelimiter">RowDelimiter</a>: <i>String</i>
    <a href="#azureblobfslocation" title="AzureBlobFsLocation">AzureBlobFsLocation</a>: <i>
      - <a href="azureblobfslocationdefinition.md">AzureBlobFsLocationDefinition</a></i>
    <a href="#azureblobstoragelocation" title="AzureBlobStorageLocation">AzureBlobStorageLocation</a>: <i>
      - <a href="azureblobstoragelocationdefinition.md">AzureBlobStorageLocationDefinition</a></i>
    <a href="#httpserverlocation" title="HttpServerLocation">HttpServerLocation</a>: <i>
      - <a href="httpserverlocationdefinition.md">HttpServerLocationDefinition</a></i>
    <a href="#schemacolumn" title="SchemaColumn">SchemaColumn</a>: <i>
      - <a href="schemacolumndefinition.md">SchemaColumnDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AdditionalProperties

A map of additional properties to associate with the Data Factory Dataset.

_Required_: No

_Type_: List of <a href="additionalpropertiesdefinition.md">AdditionalPropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Annotations

List of tags that can be used for describing the Data Factory Dataset.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ColumnDelimiter

The column delimiter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompressionCodec

The compression codec used to read/write text files. Valid values are `bzip2`, `gzip`, `deflate`, `ZipDeflate`, `TarGzip`, `Tar`, `snappy`, or `lz4`. Please note these values are case sensitive.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompressionLevel

The compression ratio for the Data Factory Dataset. Valid values are `Fastest` or `Optimal`. Please note these values are case sensitive.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataFactoryName

The Data Factory name in which to associate the Dataset with. Changing this forces a new resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description for the Data Factory Dataset.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encoding

The encoding format for the file.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EscapeCharacter

The escape character.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirstRowAsHeader

When used as input, treat the first row of data as headers. When used as output, write the headers into the output as the first row of data.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Folder

The folder that this Dataset is in. If not specified, the Dataset will appear at the root level.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinkedServiceName

The Data Factory Linked Service name in which to associate the Dataset with.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the Data Factory Dataset. Changing this forces a new resource to be created. Must be globally unique. See the [Microsoft documentation](https://docs.microsoft.com/en-us/azure/data-factory/naming-rules) for all restrictions.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NullValue

The null value string.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameters

A map of parameters to associate with the Data Factory Dataset.

_Required_: No

_Type_: List of <a href="parametersdefinition.md">ParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuoteCharacter

The quote character.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to create the Data Factory Dataset. Changing this forces a new resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RowDelimiter

The row delimiter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureBlobFsLocation

_Required_: No

_Type_: List of <a href="azureblobfslocationdefinition.md">AzureBlobFsLocationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureBlobStorageLocation

_Required_: No

_Type_: List of <a href="azureblobstoragelocationdefinition.md">AzureBlobStorageLocationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpServerLocation

_Required_: No

_Type_: List of <a href="httpserverlocationdefinition.md">HttpServerLocationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SchemaColumn

_Required_: No

_Type_: List of <a href="schemacolumndefinition.md">SchemaColumnDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

