# Terraform::AzureRM::DataFactoryDatasetMysql

Manages a MySQL Dataset inside a Azure Data Factory.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::DataFactoryDatasetMysql",
    "Properties" : {
        "<a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>" : <i>[ <a href="additionalproperties.md">AdditionalProperties</a>, ... ]</i>,
        "<a href="#annotations" title="Annotations">Annotations</a>" : <i>[ String, ... ]</i>,
        "<a href="#datafactoryname" title="DataFactoryName">DataFactoryName</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#folder" title="Folder">Folder</a>" : <i>String</i>,
        "<a href="#linkedservicename" title="LinkedServiceName">LinkedServiceName</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#parameters" title="Parameters">Parameters</a>" : <i>[ <a href="parameters.md">Parameters</a>, ... ]</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tablename" title="TableName">TableName</a>" : <i>String</i>,
        "<a href="#schemacolumn" title="SchemaColumn">SchemaColumn</a>" : <i>[ <a href="schemacolumn.md">SchemaColumn</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::DataFactoryDatasetMysql
Properties:
    <a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>: <i>
      - <a href="additionalproperties.md">AdditionalProperties</a></i>
    <a href="#annotations" title="Annotations">Annotations</a>: <i>
      - String</i>
    <a href="#datafactoryname" title="DataFactoryName">DataFactoryName</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#folder" title="Folder">Folder</a>: <i>String</i>
    <a href="#linkedservicename" title="LinkedServiceName">LinkedServiceName</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#parameters" title="Parameters">Parameters</a>: <i>
      - <a href="parameters.md">Parameters</a></i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tablename" title="TableName">TableName</a>: <i>String</i>
    <a href="#schemacolumn" title="SchemaColumn">SchemaColumn</a>: <i>
      - <a href="schemacolumn.md">SchemaColumn</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AdditionalProperties

A map of additional properties to associate with the Data Factory Dataset MySQL.

_Required_: No

_Type_: List of <a href="additionalproperties.md">AdditionalProperties</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Annotations

List of tags that can be used for describing the Data Factory Dataset MySQL.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataFactoryName

The Data Factory name in which to associate the Dataset with. Changing this forces a new resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description for the Data Factory Dataset MySQL.

_Required_: No

_Type_: String

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

Specifies the name of the Data Factory Dataset MySQL. Changing this forces a new resource to be created. Must be globally unique. See the [Microsoft documentation](https://docs.microsoft.com/en-us/azure/data-factory/naming-rules) for all restrictions.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameters

A map of parameters to associate with the Data Factory Dataset MySQL.

_Required_: No

_Type_: List of <a href="parameters.md">Parameters</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to create the Data Factory Dataset MySQL. Changing this forces a new resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TableName

The table name of the Data Factory Dataset MySQL.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SchemaColumn

_Required_: No

_Type_: List of <a href="schemacolumn.md">SchemaColumn</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

