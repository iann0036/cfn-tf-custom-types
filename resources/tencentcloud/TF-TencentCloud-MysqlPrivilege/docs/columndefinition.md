# TF::TencentCloud::MysqlPrivilege ColumnDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#columnname" title="ColumnName">ColumnName</a>" : <i>String</i>,
    "<a href="#databasename" title="DatabaseName">DatabaseName</a>" : <i>String</i>,
    "<a href="#privileges" title="Privileges">Privileges</a>" : <i>[ String, ... ]</i>,
    "<a href="#tablename" title="TableName">TableName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#columnname" title="ColumnName">ColumnName</a>: <i>String</i>
<a href="#databasename" title="DatabaseName">DatabaseName</a>: <i>String</i>
<a href="#privileges" title="Privileges">Privileges</a>: <i>
      - String</i>
<a href="#tablename" title="TableName">TableName</a>: <i>String</i>
</pre>

## Properties

#### ColumnName

Column name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseName

Database name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Privileges

Column privilege.available values for Privileges:SELECT,INSERT,UPDATE,REFERENCES.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TableName

Table name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

