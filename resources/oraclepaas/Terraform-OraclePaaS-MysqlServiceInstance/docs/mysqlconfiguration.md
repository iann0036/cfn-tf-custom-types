# Terraform::OraclePaaS::MysqlServiceInstance MysqlConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dbname" title="DbName">DbName</a>" : <i>String</i>,
    "<a href="#dbstorage" title="DbStorage">DbStorage</a>" : <i>Double</i>,
    "<a href="#mysqlcharset" title="MysqlCharset">MysqlCharset</a>" : <i>String</i>,
    "<a href="#mysqlcollation" title="MysqlCollation">MysqlCollation</a>" : <i>String</i>,
    "<a href="#mysqlpassword" title="MysqlPassword">MysqlPassword</a>" : <i>String</i>,
    "<a href="#mysqlport" title="MysqlPort">MysqlPort</a>" : <i>Double</i>,
    "<a href="#mysqlusername" title="MysqlUsername">MysqlUsername</a>" : <i>String</i>,
    "<a href="#snapshotname" title="SnapshotName">SnapshotName</a>" : <i>String</i>,
    "<a href="#sourceservicename" title="SourceServiceName">SourceServiceName</a>" : <i>String</i>,
    "<a href="#enterprisemonitorconfiguration" title="EnterpriseMonitorConfiguration">EnterpriseMonitorConfiguration</a>" : <i>[ <a href="mysqlconfiguration-enterprisemonitorconfiguration.md">EnterpriseMonitorConfiguration</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dbname" title="DbName">DbName</a>: <i>String</i>
<a href="#dbstorage" title="DbStorage">DbStorage</a>: <i>Double</i>
<a href="#mysqlcharset" title="MysqlCharset">MysqlCharset</a>: <i>String</i>
<a href="#mysqlcollation" title="MysqlCollation">MysqlCollation</a>: <i>String</i>
<a href="#mysqlpassword" title="MysqlPassword">MysqlPassword</a>: <i>String</i>
<a href="#mysqlport" title="MysqlPort">MysqlPort</a>: <i>Double</i>
<a href="#mysqlusername" title="MysqlUsername">MysqlUsername</a>: <i>String</i>
<a href="#snapshotname" title="SnapshotName">SnapshotName</a>: <i>String</i>
<a href="#sourceservicename" title="SourceServiceName">SourceServiceName</a>: <i>String</i>
<a href="#enterprisemonitorconfiguration" title="EnterpriseMonitorConfiguration">EnterpriseMonitorConfiguration</a>: <i>
      - <a href="mysqlconfiguration-enterprisemonitorconfiguration.md">EnterpriseMonitorConfiguration</a></i>
</pre>

## Properties

#### DbName

. The name of the database instance. Default value is `mydatabase`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbStorage

. The storage volume sice for MySQL data. The value must be between 25 to 1024. Defaults to 25 (GB).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MysqlCharset

MySQL server character set. See [Supported Character Sets and Collation](http://dev.mysql.com/doc/en/charset-charsets.html). Default value is `utf8mb4`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MysqlCollation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MysqlPassword

The password for the MySQL Administration user.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MysqlPort

The port number for the MySQL Server. The value must be between 3200-3399. Default value is `3306`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MysqlUsername

The Administration user for connecting to the service via th MySQL protocol. Default value is `root`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotName

The name of the snapshot of the service instance specified by `source_service_name` that is to be used to create a "snapshot clone". This parameter is valid only if `source_service_name` is specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceServiceName

When present, indicates that the service instance should be created as a "snapshot clone" of another service instance. Provide the name of the existing service instance whose snapshot is to be used. `db_name`, `mysql_charset`, `mysql_collation`, `enterpriseMonitor`, and associated MySQL server component parameters do not apply when cloning a service from a snapshot. For those parameters, the clone operation uses the values defined in the snapshot of the source service instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnterpriseMonitorConfiguration

_Required_: No

_Type_: List of <a href="mysqlconfiguration-enterprisemonitorconfiguration.md">EnterpriseMonitorConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

