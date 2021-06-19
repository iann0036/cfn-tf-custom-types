# TF::Alicloud::DbInstance

Provides an RDS instance resource. A DB instance is an isolated database
environment in the cloud. A DB instance can contain multiple user-created
databases.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::DbInstance",
    "Properties" : {
        "<a href="#acl" title="Acl">Acl</a>" : <i>String</i>,
        "<a href="#autorenew" title="AutoRenew">AutoRenew</a>" : <i>Boolean</i>,
        "<a href="#autorenewperiod" title="AutoRenewPeriod">AutoRenewPeriod</a>" : <i>Double</i>,
        "<a href="#autoupgrademinorversion" title="AutoUpgradeMinorVersion">AutoUpgradeMinorVersion</a>" : <i>String</i>,
        "<a href="#catype" title="CaType">CaType</a>" : <i>String</i>,
        "<a href="#clientcacert" title="ClientCaCert">ClientCaCert</a>" : <i>String</i>,
        "<a href="#clientcaenabled" title="ClientCaEnabled">ClientCaEnabled</a>" : <i>Double</i>,
        "<a href="#clientcertrevocationlist" title="ClientCertRevocationList">ClientCertRevocationList</a>" : <i>String</i>,
        "<a href="#clientcrlenabled" title="ClientCrlEnabled">ClientCrlEnabled</a>" : <i>Double</i>,
        "<a href="#dbinstancestoragetype" title="DbInstanceStorageType">DbInstanceStorageType</a>" : <i>String</i>,
        "<a href="#encryptionkey" title="EncryptionKey">EncryptionKey</a>" : <i>String</i>,
        "<a href="#engine" title="Engine">Engine</a>" : <i>String</i>,
        "<a href="#engineversion" title="EngineVersion">EngineVersion</a>" : <i>String</i>,
        "<a href="#forcerestart" title="ForceRestart">ForceRestart</a>" : <i>Boolean</i>,
        "<a href="#instancechargetype" title="InstanceChargeType">InstanceChargeType</a>" : <i>String</i>,
        "<a href="#instancename" title="InstanceName">InstanceName</a>" : <i>String</i>,
        "<a href="#instancestorage" title="InstanceStorage">InstanceStorage</a>" : <i>Double</i>,
        "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
        "<a href="#maintaintime" title="MaintainTime">MaintainTime</a>" : <i>String</i>,
        "<a href="#monitoringperiod" title="MonitoringPeriod">MonitoringPeriod</a>" : <i>Double</i>,
        "<a href="#period" title="Period">Period</a>" : <i>Double</i>,
        "<a href="#replicationacl" title="ReplicationAcl">ReplicationAcl</a>" : <i>String</i>,
        "<a href="#resourcegroupid" title="ResourceGroupId">ResourceGroupId</a>" : <i>String</i>,
        "<a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>" : <i>String</i>,
        "<a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#securityipmode" title="SecurityIpMode">SecurityIpMode</a>" : <i>String</i>,
        "<a href="#securityips" title="SecurityIps">SecurityIps</a>" : <i>[ String, ... ]</i>,
        "<a href="#servercert" title="ServerCert">ServerCert</a>" : <i>String</i>,
        "<a href="#serverkey" title="ServerKey">ServerKey</a>" : <i>String</i>,
        "<a href="#sqlcollectorconfigvalue" title="SqlCollectorConfigValue">SqlCollectorConfigValue</a>" : <i>Double</i>,
        "<a href="#sqlcollectorstatus" title="SqlCollectorStatus">SqlCollectorStatus</a>" : <i>String</i>,
        "<a href="#sslaction" title="SslAction">SslAction</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tdestatus" title="TdeStatus">TdeStatus</a>" : <i>String</i>,
        "<a href="#vswitchid" title="VswitchId">VswitchId</a>" : <i>String</i>,
        "<a href="#zoneid" title="ZoneId">ZoneId</a>" : <i>String</i>,
        "<a href="#zoneidslavea" title="ZoneIdSlaveA">ZoneIdSlaveA</a>" : <i>String</i>,
        "<a href="#zoneidslaveb" title="ZoneIdSlaveB">ZoneIdSlaveB</a>" : <i>String</i>,
        "<a href="#parameters" title="Parameters">Parameters</a>" : <i>[ <a href="parametersdefinition.md">ParametersDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::DbInstance
Properties:
    <a href="#acl" title="Acl">Acl</a>: <i>String</i>
    <a href="#autorenew" title="AutoRenew">AutoRenew</a>: <i>Boolean</i>
    <a href="#autorenewperiod" title="AutoRenewPeriod">AutoRenewPeriod</a>: <i>Double</i>
    <a href="#autoupgrademinorversion" title="AutoUpgradeMinorVersion">AutoUpgradeMinorVersion</a>: <i>String</i>
    <a href="#catype" title="CaType">CaType</a>: <i>String</i>
    <a href="#clientcacert" title="ClientCaCert">ClientCaCert</a>: <i>String</i>
    <a href="#clientcaenabled" title="ClientCaEnabled">ClientCaEnabled</a>: <i>Double</i>
    <a href="#clientcertrevocationlist" title="ClientCertRevocationList">ClientCertRevocationList</a>: <i>String</i>
    <a href="#clientcrlenabled" title="ClientCrlEnabled">ClientCrlEnabled</a>: <i>Double</i>
    <a href="#dbinstancestoragetype" title="DbInstanceStorageType">DbInstanceStorageType</a>: <i>String</i>
    <a href="#encryptionkey" title="EncryptionKey">EncryptionKey</a>: <i>String</i>
    <a href="#engine" title="Engine">Engine</a>: <i>String</i>
    <a href="#engineversion" title="EngineVersion">EngineVersion</a>: <i>String</i>
    <a href="#forcerestart" title="ForceRestart">ForceRestart</a>: <i>Boolean</i>
    <a href="#instancechargetype" title="InstanceChargeType">InstanceChargeType</a>: <i>String</i>
    <a href="#instancename" title="InstanceName">InstanceName</a>: <i>String</i>
    <a href="#instancestorage" title="InstanceStorage">InstanceStorage</a>: <i>Double</i>
    <a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
    <a href="#maintaintime" title="MaintainTime">MaintainTime</a>: <i>String</i>
    <a href="#monitoringperiod" title="MonitoringPeriod">MonitoringPeriod</a>: <i>Double</i>
    <a href="#period" title="Period">Period</a>: <i>Double</i>
    <a href="#replicationacl" title="ReplicationAcl">ReplicationAcl</a>: <i>String</i>
    <a href="#resourcegroupid" title="ResourceGroupId">ResourceGroupId</a>: <i>String</i>
    <a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>: <i>String</i>
    <a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>: <i>
      - String</i>
    <a href="#securityipmode" title="SecurityIpMode">SecurityIpMode</a>: <i>String</i>
    <a href="#securityips" title="SecurityIps">SecurityIps</a>: <i>
      - String</i>
    <a href="#servercert" title="ServerCert">ServerCert</a>: <i>String</i>
    <a href="#serverkey" title="ServerKey">ServerKey</a>: <i>String</i>
    <a href="#sqlcollectorconfigvalue" title="SqlCollectorConfigValue">SqlCollectorConfigValue</a>: <i>Double</i>
    <a href="#sqlcollectorstatus" title="SqlCollectorStatus">SqlCollectorStatus</a>: <i>String</i>
    <a href="#sslaction" title="SslAction">SslAction</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tdestatus" title="TdeStatus">TdeStatus</a>: <i>String</i>
    <a href="#vswitchid" title="VswitchId">VswitchId</a>: <i>String</i>
    <a href="#zoneid" title="ZoneId">ZoneId</a>: <i>String</i>
    <a href="#zoneidslavea" title="ZoneIdSlaveA">ZoneIdSlaveA</a>: <i>String</i>
    <a href="#zoneidslaveb" title="ZoneIdSlaveB">ZoneIdSlaveB</a>: <i>String</i>
    <a href="#parameters" title="Parameters">Parameters</a>: <i>
      - <a href="parametersdefinition.md">ParametersDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Acl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoRenew

Whether to renewal a DB instance automatically or not. It is valid when instance_charge_type is `PrePaid`. Default to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoRenewPeriod

Auto-renewal period of an instance, in the unit of the month. It is valid when instance_charge_type is `PrePaid`. Valid value:[1~12], Default to 1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoUpgradeMinorVersion

The upgrade method to use. Valid values:
- Auto: Instances are automatically upgraded to a higher minor version.
- Manual: Instances are forcibly upgraded to a higher minor version when the current version is unpublished.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientCaCert

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientCaEnabled

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientCertRevocationList

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientCrlEnabled

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbInstanceStorageType

The storage type of the instance. Valid values:
- local_ssd: specifies to use local SSDs. This value is recommended.
- cloud_ssd: specifies to use standard SSDs.
- cloud_essd: specifies to use enhanced SSDs (ESSDs).
- cloud_essd2: specifies to use enhanced SSDs (ESSDs).
- cloud_essd3: specifies to use enhanced SSDs (ESSDs).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Engine

Database type. Value options: MySQL, SQLServer, PostgreSQL, and PPAS.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EngineVersion

Database version. Value options can refer to the latest docs [CreateDBInstance](https://www.alibabacloud.com/help/doc-detail/26228.htm) `EngineVersion`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceRestart

Set it to true to make some parameter efficient when modifying them. Default to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceChargeType

Valid values are `Prepaid`, `Postpaid`, Default to `Postpaid`. Currently, the resource only supports PostPaid to PrePaid.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceName

The name of DB instance. It a string of 2 to 256 characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceStorage

User-defined DB instance storage space. Value range:
- [5, 2000] for MySQL/PostgreSQL/PPAS HA dual node edition;
- [20,1000] for MySQL 5.7 basic single node edition;
- [10, 2000] for SQL Server 2008R2;
- [20,2000] for SQL Server 2012 basic single node edition
Increase progressively at a rate of 5 GB. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).
Note: There is extra 5 GB storage for SQL Server Instance and it is not in specified `instance_storage`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceType

DB Instance type. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintainTime

Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitoringPeriod

The monitoring frequency in seconds. Valid values are 5, 60, 300. Defaults to 300.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Period

The duration that you will buy DB instance (in month). It is valid when instance_charge_type is `PrePaid`. Valid values: [1~9], 12, 24, 36. Default to 1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplicationAcl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupId

It has been deprecated from 1.69.0 and use `security_group_ids` instead.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupIds

, Available in 1.69.0+) The list IDs to join ECS Security Group. At most supports three security groups.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityIpMode

Valid values are `normal`, `safety`, Default to `normal`. support `safety` switch to high security access mode.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityIps

List of IP addresses allowed to access all databases of an instance. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerCert

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SqlCollectorConfigValue

The sql collector keep time of the instance. Valid values are `30`, `180`, `365`, `1095`, `1825`, Default to `30`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SqlCollectorStatus

The sql collector status of the instance. Valid values are `Enabled`, `Disabled`, Default to `Disabled`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslAction

Actions performed on SSL functions, Valid values: `Open`: turn on SSL encryption; `Close`: turn off SSL encryption; `Update`: update SSL certificate. See more [engine and engineVersion limitation](https://www.alibabacloud.com/help/zh/doc-detail/26254.htm).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.
- Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
- Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TdeStatus

The TDE(Transparent Data Encryption) status. See more [engine and engineVersion limitation](https://www.alibabacloud.com/help/zh/doc-detail/26256.htm).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VswitchId

The virtual switch ID to launch DB instances in one VPC. If there are multiple vswitches, separate them with commas.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneId

The Zone to launch the DB instance. From version 1.8.1, it supports multiple zone.
If it is a multi-zone and `vswitch_id` is specified, the vswitch must in the one of them.
The multiple zone ID can be retrieved by setting `multi` to "true" in the data source `alicloud_zones`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneIdSlaveA

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneIdSlaveB

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameters

_Required_: No

_Type_: List of <a href="parametersdefinition.md">ParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ConnectionString

Returns the <code>ConnectionString</code> value.

#### Id

Returns the <code>Id</code> value.

#### Port

Returns the <code>Port</code> value.

#### SslStatus

Returns the <code>SslStatus</code> value.

