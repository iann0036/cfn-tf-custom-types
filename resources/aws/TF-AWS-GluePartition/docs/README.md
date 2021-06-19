# TF::AWS::GluePartition

Provides a Glue Partition Resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::GluePartition",
    "Properties" : {
        "<a href="#catalogid" title="CatalogId">CatalogId</a>" : <i>String</i>,
        "<a href="#databasename" title="DatabaseName">DatabaseName</a>" : <i>String</i>,
        "<a href="#parameters" title="Parameters">Parameters</a>" : <i>[ <a href="parametersdefinition.md">ParametersDefinition</a>, ... ]</i>,
        "<a href="#partitionvalues" title="PartitionValues">PartitionValues</a>" : <i>[ String, ... ]</i>,
        "<a href="#tablename" title="TableName">TableName</a>" : <i>String</i>,
        "<a href="#storagedescriptor" title="StorageDescriptor">StorageDescriptor</a>" : <i>[ <a href="storagedescriptordefinition.md">StorageDescriptorDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::GluePartition
Properties:
    <a href="#catalogid" title="CatalogId">CatalogId</a>: <i>String</i>
    <a href="#databasename" title="DatabaseName">DatabaseName</a>: <i>String</i>
    <a href="#parameters" title="Parameters">Parameters</a>: <i>
      - <a href="parametersdefinition.md">ParametersDefinition</a></i>
    <a href="#partitionvalues" title="PartitionValues">PartitionValues</a>: <i>
      - String</i>
    <a href="#tablename" title="TableName">TableName</a>: <i>String</i>
    <a href="#storagedescriptor" title="StorageDescriptor">StorageDescriptor</a>: <i>
      - <a href="storagedescriptordefinition.md">StorageDescriptorDefinition</a></i>
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

#### Parameters

Properties associated with this table, as a list of key-value pairs.

_Required_: No

_Type_: List of <a href="parametersdefinition.md">ParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PartitionValues

The values that define the partition.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TableName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageDescriptor

_Required_: No

_Type_: List of <a href="storagedescriptordefinition.md">StorageDescriptorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreationTime

Returns the <code>CreationTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### LastAccessedTime

Returns the <code>LastAccessedTime</code> value.

#### LastAnalyzedTime

Returns the <code>LastAnalyzedTime</code> value.

