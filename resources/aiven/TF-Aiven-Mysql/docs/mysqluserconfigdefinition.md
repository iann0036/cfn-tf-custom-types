# TF::Aiven::Mysql MysqlUserConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#adminpassword" title="AdminPassword">AdminPassword</a>" : <i>String</i>,
    "<a href="#adminusername" title="AdminUsername">AdminUsername</a>" : <i>String</i>,
    "<a href="#backuphour" title="BackupHour">BackupHour</a>" : <i>String</i>,
    "<a href="#backupminute" title="BackupMinute">BackupMinute</a>" : <i>String</i>,
    "<a href="#binlogretentionperiod" title="BinlogRetentionPeriod">BinlogRetentionPeriod</a>" : <i>String</i>,
    "<a href="#ipfilter" title="IpFilter">IpFilter</a>" : <i>[ String, ... ]</i>,
    "<a href="#mysqlversion" title="MysqlVersion">MysqlVersion</a>" : <i>String</i>,
    "<a href="#projecttoforkfrom" title="ProjectToForkFrom">ProjectToForkFrom</a>" : <i>String</i>,
    "<a href="#recoverytargettime" title="RecoveryTargetTime">RecoveryTargetTime</a>" : <i>String</i>,
    "<a href="#servicetoforkfrom" title="ServiceToForkFrom">ServiceToForkFrom</a>" : <i>String</i>,
    "<a href="#migration" title="Migration">Migration</a>" : <i>[ <a href="migrationdefinition.md">MigrationDefinition</a>, ... ]</i>,
    "<a href="#mysql" title="Mysql">Mysql</a>" : <i>[ <a href="mysqldefinition.md">MysqlDefinition</a>, ... ]</i>,
    "<a href="#privateaccess" title="PrivateAccess">PrivateAccess</a>" : <i>[ <a href="privateaccessdefinition.md">PrivateAccessDefinition</a>, ... ]</i>,
    "<a href="#privatelinkaccess" title="PrivatelinkAccess">PrivatelinkAccess</a>" : <i>[ <a href="privatelinkaccessdefinition.md">PrivatelinkAccessDefinition</a>, ... ]</i>,
    "<a href="#publicaccess" title="PublicAccess">PublicAccess</a>" : <i>[ <a href="publicaccessdefinition.md">PublicAccessDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#adminpassword" title="AdminPassword">AdminPassword</a>: <i>String</i>
<a href="#adminusername" title="AdminUsername">AdminUsername</a>: <i>String</i>
<a href="#backuphour" title="BackupHour">BackupHour</a>: <i>String</i>
<a href="#backupminute" title="BackupMinute">BackupMinute</a>: <i>String</i>
<a href="#binlogretentionperiod" title="BinlogRetentionPeriod">BinlogRetentionPeriod</a>: <i>String</i>
<a href="#ipfilter" title="IpFilter">IpFilter</a>: <i>
      - String</i>
<a href="#mysqlversion" title="MysqlVersion">MysqlVersion</a>: <i>String</i>
<a href="#projecttoforkfrom" title="ProjectToForkFrom">ProjectToForkFrom</a>: <i>String</i>
<a href="#recoverytargettime" title="RecoveryTargetTime">RecoveryTargetTime</a>: <i>String</i>
<a href="#servicetoforkfrom" title="ServiceToForkFrom">ServiceToForkFrom</a>: <i>String</i>
<a href="#migration" title="Migration">Migration</a>: <i>
      - <a href="migrationdefinition.md">MigrationDefinition</a></i>
<a href="#mysql" title="Mysql">Mysql</a>: <i>
      - <a href="mysqldefinition.md">MysqlDefinition</a></i>
<a href="#privateaccess" title="PrivateAccess">PrivateAccess</a>: <i>
      - <a href="privateaccessdefinition.md">PrivateAccessDefinition</a></i>
<a href="#privatelinkaccess" title="PrivatelinkAccess">PrivatelinkAccess</a>: <i>
      - <a href="privatelinkaccessdefinition.md">PrivatelinkAccessDefinition</a></i>
<a href="#publicaccess" title="PublicAccess">PublicAccess</a>: <i>
      - <a href="publicaccessdefinition.md">PublicAccessDefinition</a></i>
</pre>

## Properties

#### AdminPassword

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminUsername

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupHour

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupMinute

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BinlogRetentionPeriod

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpFilter

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MysqlVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectToForkFrom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecoveryTargetTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceToForkFrom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Migration

_Required_: No

_Type_: List of <a href="migrationdefinition.md">MigrationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mysql

_Required_: No

_Type_: List of <a href="mysqldefinition.md">MysqlDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateAccess

_Required_: No

_Type_: List of <a href="privateaccessdefinition.md">PrivateAccessDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivatelinkAccess

_Required_: No

_Type_: List of <a href="privatelinkaccessdefinition.md">PrivatelinkAccessDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicAccess

_Required_: No

_Type_: List of <a href="publicaccessdefinition.md">PublicAccessDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

