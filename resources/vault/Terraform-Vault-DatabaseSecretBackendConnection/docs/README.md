# Terraform::Vault::DatabaseSecretBackendConnection

CloudFormation equivalent of vault_database_secret_backend_connection

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Vault::DatabaseSecretBackendConnection",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#allowedroles" title="AllowedRoles">AllowedRoles</a>" : <i>[ String, ... ]</i>,
        "<a href="#backend" title="Backend">Backend</a>" : <i>String</i>,
        "<a href="#data" title="Data">Data</a>" : <i>[ &lt;a href=&#34;data.md&#34;&gt;Data&lt;/a&gt;, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#rootrotationstatements" title="RootRotationStatements">RootRotationStatements</a>" : <i>[ String, ... ]</i>,
        "<a href="#verifyconnection" title="VerifyConnection">VerifyConnection</a>" : <i>Boolean</i>,
        "<a href="#cassandra" title="Cassandra">Cassandra</a>" : <i>[ &lt;a href=&#34;cassandra.md&#34;&gt;Cassandra&lt;/a&gt;, ... ]</i>,
        "<a href="#hana" title="Hana">Hana</a>" : <i>[ &lt;a href=&#34;hana.md&#34;&gt;Hana&lt;/a&gt;, ... ]</i>,
        "<a href="#mongodb" title="Mongodb">Mongodb</a>" : <i>[ &lt;a href=&#34;mongodb.md&#34;&gt;Mongodb&lt;/a&gt;, ... ]</i>,
        "<a href="#mssql" title="Mssql">Mssql</a>" : <i>[ &lt;a href=&#34;mssql.md&#34;&gt;Mssql&lt;/a&gt;, ... ]</i>,
        "<a href="#mysql" title="Mysql">Mysql</a>" : <i>[ &lt;a href=&#34;mysql.md&#34;&gt;Mysql&lt;/a&gt;, ... ]</i>,
        "<a href="#mysqlaurora" title="MysqlAurora">MysqlAurora</a>" : <i>[ &lt;a href=&#34;mysqlaurora.md&#34;&gt;MysqlAurora&lt;/a&gt;, ... ]</i>,
        "<a href="#mysqllegacy" title="MysqlLegacy">MysqlLegacy</a>" : <i>[ &lt;a href=&#34;mysqllegacy.md&#34;&gt;MysqlLegacy&lt;/a&gt;, ... ]</i>,
        "<a href="#mysqlrds" title="MysqlRds">MysqlRds</a>" : <i>[ &lt;a href=&#34;mysqlrds.md&#34;&gt;MysqlRds&lt;/a&gt;, ... ]</i>,
        "<a href="#oracle" title="Oracle">Oracle</a>" : <i>[ &lt;a href=&#34;oracle.md&#34;&gt;Oracle&lt;/a&gt;, ... ]</i>,
        "<a href="#postgresql" title="Postgresql">Postgresql</a>" : <i>[ &lt;a href=&#34;postgresql.md&#34;&gt;Postgresql&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Vault::DatabaseSecretBackendConnection
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#allowedroles" title="AllowedRoles">AllowedRoles</a>: <i>
      - String</i>
    <a href="#backend" title="Backend">Backend</a>: <i>String</i>
    <a href="#data" title="Data">Data</a>: <i>
      - &lt;a href=&#34;data.md&#34;&gt;Data&lt;/a&gt;</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#rootrotationstatements" title="RootRotationStatements">RootRotationStatements</a>: <i>
      - String</i>
    <a href="#verifyconnection" title="VerifyConnection">VerifyConnection</a>: <i>Boolean</i>
    <a href="#cassandra" title="Cassandra">Cassandra</a>: <i>
      - &lt;a href=&#34;cassandra.md&#34;&gt;Cassandra&lt;/a&gt;</i>
    <a href="#hana" title="Hana">Hana</a>: <i>
      - &lt;a href=&#34;hana.md&#34;&gt;Hana&lt;/a&gt;</i>
    <a href="#mongodb" title="Mongodb">Mongodb</a>: <i>
      - &lt;a href=&#34;mongodb.md&#34;&gt;Mongodb&lt;/a&gt;</i>
    <a href="#mssql" title="Mssql">Mssql</a>: <i>
      - &lt;a href=&#34;mssql.md&#34;&gt;Mssql&lt;/a&gt;</i>
    <a href="#mysql" title="Mysql">Mysql</a>: <i>
      - &lt;a href=&#34;mysql.md&#34;&gt;Mysql&lt;/a&gt;</i>
    <a href="#mysqlaurora" title="MysqlAurora">MysqlAurora</a>: <i>
      - &lt;a href=&#34;mysqlaurora.md&#34;&gt;MysqlAurora&lt;/a&gt;</i>
    <a href="#mysqllegacy" title="MysqlLegacy">MysqlLegacy</a>: <i>
      - &lt;a href=&#34;mysqllegacy.md&#34;&gt;MysqlLegacy&lt;/a&gt;</i>
    <a href="#mysqlrds" title="MysqlRds">MysqlRds</a>: <i>
      - &lt;a href=&#34;mysqlrds.md&#34;&gt;MysqlRds&lt;/a&gt;</i>
    <a href="#oracle" title="Oracle">Oracle</a>: <i>
      - &lt;a href=&#34;oracle.md&#34;&gt;Oracle&lt;/a&gt;</i>
    <a href="#postgresql" title="Postgresql">Postgresql</a>: <i>
      - &lt;a href=&#34;postgresql.md&#34;&gt;Postgresql&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedRoles

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backend

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Data

_Required_: No

_Type_: List of &lt;a href=&#34;data.md&#34;&gt;Data&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootRotationStatements

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VerifyConnection

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cassandra

_Required_: No

_Type_: List of &lt;a href=&#34;cassandra.md&#34;&gt;Cassandra&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hana

_Required_: No

_Type_: List of &lt;a href=&#34;hana.md&#34;&gt;Hana&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mongodb

_Required_: No

_Type_: List of &lt;a href=&#34;mongodb.md&#34;&gt;Mongodb&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mssql

_Required_: No

_Type_: List of &lt;a href=&#34;mssql.md&#34;&gt;Mssql&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mysql

_Required_: No

_Type_: List of &lt;a href=&#34;mysql.md&#34;&gt;Mysql&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MysqlAurora

_Required_: No

_Type_: List of &lt;a href=&#34;mysqlaurora.md&#34;&gt;MysqlAurora&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MysqlLegacy

_Required_: No

_Type_: List of &lt;a href=&#34;mysqllegacy.md&#34;&gt;MysqlLegacy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MysqlRds

_Required_: No

_Type_: List of &lt;a href=&#34;mysqlrds.md&#34;&gt;MysqlRds&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Oracle

_Required_: No

_Type_: List of &lt;a href=&#34;oracle.md&#34;&gt;Oracle&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Postgresql

_Required_: No

_Type_: List of &lt;a href=&#34;postgresql.md&#34;&gt;Postgresql&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

