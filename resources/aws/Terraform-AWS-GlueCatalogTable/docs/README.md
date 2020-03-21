# Terraform::AWS::GlueCatalogTable

CloudFormation equivalent of aws_glue_catalog_table

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::GlueCatalogTable",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#catalogid" title="CatalogId">CatalogId</a>" : <i>String</i>,
        "<a href="#databasename" title="DatabaseName">DatabaseName</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#owner" title="Owner">Owner</a>" : <i>String</i>,
        "<a href="#parameters" title="Parameters">Parameters</a>" : <i>[ &lt;a href=&#34;parameters.md&#34;&gt;Parameters&lt;/a&gt;, ... ]</i>,
        "<a href="#retention" title="Retention">Retention</a>" : <i>Double</i>,
        "<a href="#tabletype" title="TableType">TableType</a>" : <i>String</i>,
        "<a href="#viewexpandedtext" title="ViewExpandedText">ViewExpandedText</a>" : <i>String</i>,
        "<a href="#vieworiginaltext" title="ViewOriginalText">ViewOriginalText</a>" : <i>String</i>,
        "<a href="#partitionkeys" title="PartitionKeys">PartitionKeys</a>" : <i>[ &lt;a href=&#34;partitionkeys.md&#34;&gt;PartitionKeys&lt;/a&gt;, ... ]</i>,
        "<a href="#storagedescriptor" title="StorageDescriptor">StorageDescriptor</a>" : <i>[ &lt;a href=&#34;storagedescriptor.md&#34;&gt;StorageDescriptor&lt;/a&gt;, ... ]</i>,
        "<a href="#columns" title="Columns">Columns</a>" : <i>[ &lt;a href=&#34;columns.md&#34;&gt;Columns&lt;/a&gt;, ... ]</i>,
        "<a href="#serdeinfo" title="SerDeInfo">SerDeInfo</a>" : <i>[ &lt;a href=&#34;serdeinfo.md&#34;&gt;SerDeInfo&lt;/a&gt;, ... ]</i>,
        "<a href="#skewedinfo" title="SkewedInfo">SkewedInfo</a>" : <i>[ &lt;a href=&#34;skewedinfo.md&#34;&gt;SkewedInfo&lt;/a&gt;, ... ]</i>,
        "<a href="#sortcolumns" title="SortColumns">SortColumns</a>" : <i>[ &lt;a href=&#34;sortcolumns.md&#34;&gt;SortColumns&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::GlueCatalogTable
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#catalogid" title="CatalogId">CatalogId</a>: <i>String</i>
    <a href="#databasename" title="DatabaseName">DatabaseName</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#owner" title="Owner">Owner</a>: <i>String</i>
    <a href="#parameters" title="Parameters">Parameters</a>: <i>
      - &lt;a href=&#34;parameters.md&#34;&gt;Parameters&lt;/a&gt;</i>
    <a href="#retention" title="Retention">Retention</a>: <i>Double</i>
    <a href="#tabletype" title="TableType">TableType</a>: <i>String</i>
    <a href="#viewexpandedtext" title="ViewExpandedText">ViewExpandedText</a>: <i>String</i>
    <a href="#vieworiginaltext" title="ViewOriginalText">ViewOriginalText</a>: <i>String</i>
    <a href="#partitionkeys" title="PartitionKeys">PartitionKeys</a>: <i>
      - &lt;a href=&#34;partitionkeys.md&#34;&gt;PartitionKeys&lt;/a&gt;</i>
    <a href="#storagedescriptor" title="StorageDescriptor">StorageDescriptor</a>: <i>
      - &lt;a href=&#34;storagedescriptor.md&#34;&gt;StorageDescriptor&lt;/a&gt;</i>
    <a href="#columns" title="Columns">Columns</a>: <i>
      - &lt;a href=&#34;columns.md&#34;&gt;Columns&lt;/a&gt;</i>
    <a href="#serdeinfo" title="SerDeInfo">SerDeInfo</a>: <i>
      - &lt;a href=&#34;serdeinfo.md&#34;&gt;SerDeInfo&lt;/a&gt;</i>
    <a href="#skewedinfo" title="SkewedInfo">SkewedInfo</a>: <i>
      - &lt;a href=&#34;skewedinfo.md&#34;&gt;SkewedInfo&lt;/a&gt;</i>
    <a href="#sortcolumns" title="SortColumns">SortColumns</a>: <i>
      - &lt;a href=&#34;sortcolumns.md&#34;&gt;SortColumns&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CatalogId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Owner

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameters

_Required_: No

_Type_: List of &lt;a href=&#34;parameters.md&#34;&gt;Parameters&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Retention

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TableType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ViewExpandedText

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ViewOriginalText

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PartitionKeys

_Required_: No

_Type_: List of &lt;a href=&#34;partitionkeys.md&#34;&gt;PartitionKeys&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageDescriptor

_Required_: No

_Type_: List of &lt;a href=&#34;storagedescriptor.md&#34;&gt;StorageDescriptor&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Columns

_Required_: No

_Type_: List of &lt;a href=&#34;columns.md&#34;&gt;Columns&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SerDeInfo

_Required_: No

_Type_: List of &lt;a href=&#34;serdeinfo.md&#34;&gt;SerDeInfo&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkewedInfo

_Required_: No

_Type_: List of &lt;a href=&#34;skewedinfo.md&#34;&gt;SkewedInfo&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SortColumns

_Required_: No

_Type_: List of &lt;a href=&#34;sortcolumns.md&#34;&gt;SortColumns&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

