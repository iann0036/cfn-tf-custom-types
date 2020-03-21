# Terraform::TencentCloud::MysqlPrivilege Database

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#databasename" title="DatabaseName">DatabaseName</a>" : <i>String</i>,
    "<a href="#privileges" title="Privileges">Privileges</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#databasename" title="DatabaseName">DatabaseName</a>: <i>String</i>
<a href="#privileges" title="Privileges">Privileges</a>: <i>
      - String</i>
</pre>

## Properties

#### DatabaseName

Database name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Privileges

Database privilege.available values for Privileges:SELECT,INSERT,UPDATE,DELETE,CREATE,DROP,REFERENCES,INDEX,ALTER,CREATE TEMPORARY TABLES,LOCK TABLES,EXECUTE,CREATE VIEW,SHOW VIEW,CREATE ROUTINE,ALTER ROUTINE,EVENT,TRIGGER.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

