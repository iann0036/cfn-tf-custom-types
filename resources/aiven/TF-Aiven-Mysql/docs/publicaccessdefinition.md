# TF::Aiven::Mysql PublicAccessDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#mysql" title="Mysql">Mysql</a>" : <i>[ <a href="mysqldefinition.md">MysqlDefinition</a>, ... ]</i>,
    "<a href="#mysqlx" title="Mysqlx">Mysqlx</a>" : <i>String</i>,
    "<a href="#prometheus" title="Prometheus">Prometheus</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#mysql" title="Mysql">Mysql</a>: <i>
      - <a href="mysqldefinition.md">MysqlDefinition</a></i>
<a href="#mysqlx" title="Mysqlx">Mysqlx</a>: <i>String</i>
<a href="#prometheus" title="Prometheus">Prometheus</a>: <i>String</i>
</pre>

## Properties

#### Mysql

_Required_: No

_Type_: List of <a href="mysqldefinition.md">MysqlDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mysqlx

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prometheus

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

