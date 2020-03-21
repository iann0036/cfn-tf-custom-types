# Terraform::BIGIP::SysIapp Tables

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#columnnames" title="ColumnNames">ColumnNames</a>" : <i>[ String, ... ]</i>,
    "<a href="#encryptedcolumns" title="EncryptedColumns">EncryptedColumns</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#rows" title="Rows">Rows</a>" : <i>[ <a href="tables-rows.md">Rows</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#columnnames" title="ColumnNames">ColumnNames</a>: <i>
      - String</i>
<a href="#encryptedcolumns" title="EncryptedColumns">EncryptedColumns</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#rows" title="Rows">Rows</a>: <i>
      - <a href="tables-rows.md">Rows</a></i>
</pre>

## Properties

#### ColumnNames

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptedColumns

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rows

_Required_: No
_Type_: List of <a href="tables-rows.md">Rows</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

