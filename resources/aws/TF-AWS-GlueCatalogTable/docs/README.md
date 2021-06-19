# TF::AWS::GlueCatalogTable

Provides a Glue Catalog Table Resource. You can refer to the [Glue Developer Guide](http://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html) for a full explanation of the Glue Data Catalog functionality.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::GlueCatalogTable",
    "Properties" : {
        "<a href="#catalogid" title="CatalogId">CatalogId</a>" : <i>String</i>,
        "<a href="#databasename" title="DatabaseName">DatabaseName</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#owner" title="Owner">Owner</a>" : <i>String</i>,
        "<a href="#parameters" title="Parameters">Parameters</a>" : <i>[ <a href="parametersdefinition.md">ParametersDefinition</a>, ... ]</i>,
        "<a href="#retention" title="Retention">Retention</a>" : <i>Double</i>,
        "<a href="#tabletype" title="TableType">TableType</a>" : <i>String</i>,
        "<a href="#viewexpandedtext" title="ViewExpandedText">ViewExpandedText</a>" : <i>String</i>,
        "<a href="#vieworiginaltext" title="ViewOriginalText">ViewOriginalText</a>" : <i>String</i>,
        "<a href="#partitionindex" title="PartitionIndex">PartitionIndex</a>" : <i>[ <a href="partitionindexdefinition.md">PartitionIndexDefinition</a>, ... ]</i>,
        "<a href="#partitionkeys" title="PartitionKeys">PartitionKeys</a>" : <i>[ <a href="partitionkeysdefinition.md">PartitionKeysDefinition</a>, ... ]</i>,
        "<a href="#storagedescriptor" title="StorageDescriptor">StorageDescriptor</a>" : <i>[ <a href="storagedescriptordefinition.md">StorageDescriptorDefinition</a>, ... ]</i>,
        "<a href="#targettable" title="TargetTable">TargetTable</a>" : <i>[ <a href="targettabledefinition.md">TargetTableDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::GlueCatalogTable
Properties:
    <a href="#catalogid" title="CatalogId">CatalogId</a>: <i>String</i>
    <a href="#databasename" title="DatabaseName">DatabaseName</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#owner" title="Owner">Owner</a>: <i>String</i>
    <a href="#parameters" title="Parameters">Parameters</a>: <i>
      - <a href="parametersdefinition.md">ParametersDefinition</a></i>
    <a href="#retention" title="Retention">Retention</a>: <i>Double</i>
    <a href="#tabletype" title="TableType">TableType</a>: <i>String</i>
    <a href="#viewexpandedtext" title="ViewExpandedText">ViewExpandedText</a>: <i>String</i>
    <a href="#vieworiginaltext" title="ViewOriginalText">ViewOriginalText</a>: <i>String</i>
    <a href="#partitionindex" title="PartitionIndex">PartitionIndex</a>: <i>
      - <a href="partitionindexdefinition.md">PartitionIndexDefinition</a></i>
    <a href="#partitionkeys" title="PartitionKeys">PartitionKeys</a>: <i>
      - <a href="partitionkeysdefinition.md">PartitionKeysDefinition</a></i>
    <a href="#storagedescriptor" title="StorageDescriptor">StorageDescriptor</a>: <i>
      - <a href="storagedescriptordefinition.md">StorageDescriptorDefinition</a></i>
    <a href="#targettable" title="TargetTable">TargetTable</a>: <i>
      - <a href="targettabledefinition.md">TargetTableDefinition</a></i>
</pre>

## Properties

#### CatalogId

ID of the Glue Catalog and database to create the table in. If omitted, this defaults to the AWS Account ID plus the database name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseName

Name of the metadata database where the table metadata resides. For Hive compatibility, this must be all lowercase.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of the table.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the table. For Hive compatibility, this must be entirely lowercase.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Owner

Owner of the table.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameters

Properties associated with this table, as a list of key-value pairs.

_Required_: No

_Type_: List of <a href="parametersdefinition.md">ParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Retention

Retention time for this table.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TableType

Type of this table (EXTERNAL_TABLE, VIRTUAL_VIEW, etc.). While optional, some Athena DDL queries such as `ALTER TABLE` and `SHOW CREATE TABLE` will fail if this argument is empty.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ViewExpandedText

If the table is a view, the expanded text of the view; otherwise null.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ViewOriginalText

If the table is a view, the original text of the view; otherwise null.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PartitionIndex

_Required_: No

_Type_: List of <a href="partitionindexdefinition.md">PartitionIndexDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PartitionKeys

_Required_: No

_Type_: List of <a href="partitionkeysdefinition.md">PartitionKeysDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageDescriptor

_Required_: No

_Type_: List of <a href="storagedescriptordefinition.md">StorageDescriptorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetTable

_Required_: No

_Type_: List of <a href="targettabledefinition.md">TargetTableDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

