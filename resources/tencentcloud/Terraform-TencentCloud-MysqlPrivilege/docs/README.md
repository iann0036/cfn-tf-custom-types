# Terraform::TencentCloud::MysqlPrivilege

Provides a mysql account privilege resource to grant different access privilege to different database. A database can be granted by multiple account.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::MysqlPrivilege",
    "Properties" : {
        "<a href="#accountname" title="AccountName">AccountName</a>" : <i>String</i>,
        "<a href="#global" title="Global">Global</a>" : <i>[ String, ... ]</i>,
        "<a href="#mysqlid" title="MysqlId">MysqlId</a>" : <i>String</i>,
        "<a href="#column" title="Column">Column</a>" : <i>[ <a href="column.md">Column</a>, ... ]</i>,
        "<a href="#database" title="Database">Database</a>" : <i>[ <a href="database.md">Database</a>, ... ]</i>,
        "<a href="#table" title="Table">Table</a>" : <i>[ <a href="table.md">Table</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::MysqlPrivilege
Properties:
    <a href="#accountname" title="AccountName">AccountName</a>: <i>String</i>
    <a href="#global" title="Global">Global</a>: <i>
      - String</i>
    <a href="#mysqlid" title="MysqlId">MysqlId</a>: <i>String</i>
    <a href="#column" title="Column">Column</a>: <i>
      - <a href="column.md">Column</a></i>
    <a href="#database" title="Database">Database</a>: <i>
      - <a href="database.md">Database</a></i>
    <a href="#table" title="Table">Table</a>: <i>
      - <a href="table.md">Table</a></i>
</pre>

## Properties

#### AccountName

Account name.the forbidden value is:root,mysql.sys,tencentroot.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Global

Global privileges. available values for Privileges:SELECT,INSERT,UPDATE,DELETE,CREATE,PROCESS,DROP,REFERENCES,INDEX,ALTER,SHOW DATABASES,CREATE TEMPORARY TABLES,LOCK TABLES,EXECUTE,CREATE VIEW,SHOW VIEW,CREATE ROUTINE,ALTER ROUTINE,EVENT,TRIGGER.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MysqlId

Instance ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Column

_Required_: No

_Type_: List of <a href="column.md">Column</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Database

_Required_: No

_Type_: List of <a href="database.md">Database</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Table

_Required_: No

_Type_: List of <a href="table.md">Table</a>

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

