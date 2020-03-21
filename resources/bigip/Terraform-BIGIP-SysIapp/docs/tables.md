# Terraform::BIGIP::SysIapp Tables

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#columnnames" title="ColumnNames">ColumnNames</a>" : <i>[ String, ... ]</i>,
    "<a href="#encryptedcolumns" title="EncryptedColumns">EncryptedColumns</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#rows" title="Rows">Rows</a>" : <i>[ &lt;a href=&#34;tables-rows.md&#34;&gt;Rows&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#columnnames" title="ColumnNames">ColumnNames</a>: <i>
      - String</i>
<a href="#encryptedcolumns" title="EncryptedColumns">EncryptedColumns</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#rows" title="Rows">Rows</a>: <i>
      - &lt;a href=&#34;tables-rows.md&#34;&gt;Rows&lt;/a&gt;</i>
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
_Type_: List of &lt;a href=&#34;tables-rows.md&#34;&gt;Rows&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

