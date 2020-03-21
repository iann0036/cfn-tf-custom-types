# Terraform::TencentCloud::MysqlPrivilege

CloudFormation equivalent of tencentcloud_mysql_privilege

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::MysqlPrivilege",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#accountname" title="AccountName">AccountName</a>" : <i>String</i>,
        "<a href="#global" title="Global">Global</a>" : <i>[ String, ... ]</i>,
        "<a href="#mysqlid" title="MysqlId">MysqlId</a>" : <i>String</i>,
        "<a href="#column" title="Column">Column</a>" : <i>[ &lt;a href=&#34;column.md&#34;&gt;Column&lt;/a&gt;, ... ]</i>,
        "<a href="#database" title="Database">Database</a>" : <i>[ &lt;a href=&#34;database.md&#34;&gt;Database&lt;/a&gt;, ... ]</i>,
        "<a href="#table" title="Table">Table</a>" : <i>[ &lt;a href=&#34;table.md&#34;&gt;Table&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::MysqlPrivilege
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#accountname" title="AccountName">AccountName</a>: <i>String</i>
    <a href="#global" title="Global">Global</a>: <i>
      - String</i>
    <a href="#mysqlid" title="MysqlId">MysqlId</a>: <i>String</i>
    <a href="#column" title="Column">Column</a>: <i>
      - &lt;a href=&#34;column.md&#34;&gt;Column&lt;/a&gt;</i>
    <a href="#database" title="Database">Database</a>: <i>
      - &lt;a href=&#34;database.md&#34;&gt;Database&lt;/a&gt;</i>
    <a href="#table" title="Table">Table</a>: <i>
      - &lt;a href=&#34;table.md&#34;&gt;Table&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Global

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MysqlId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Column

_Required_: No

_Type_: List of &lt;a href=&#34;column.md&#34;&gt;Column&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Database

_Required_: No

_Type_: List of &lt;a href=&#34;database.md&#34;&gt;Database&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Table

_Required_: No

_Type_: List of &lt;a href=&#34;table.md&#34;&gt;Table&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

