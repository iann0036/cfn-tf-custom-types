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

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbStorage

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MysqlCharset

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MysqlCollation

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MysqlPassword

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MysqlPort

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MysqlUsername

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotName

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceServiceName

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnterpriseMonitorConfiguration

_Required_: No
_Type_: List of <a href="mysqlconfiguration-enterprisemonitorconfiguration.md">EnterpriseMonitorConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

