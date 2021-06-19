# TF::Gridscale::Mariadb

Provides a MariaDB resource. This can be used to create, modify, and delete MariaDB instances.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Gridscale::Mariadb",
    "Properties" : {
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ String, ... ]</i>,
        "<a href="#mariadbbinlogformat" title="MariadbBinlogFormat">MariadbBinlogFormat</a>" : <i>String</i>,
        "<a href="#mariadbdefaulttimezone" title="MariadbDefaultTimeZone">MariadbDefaultTimeZone</a>" : <i>String</i>,
        "<a href="#mariadblogbin" title="MariadbLogBin">MariadbLogBin</a>" : <i>Boolean</i>,
        "<a href="#mariadbmaxallowedpacket" title="MariadbMaxAllowedPacket">MariadbMaxAllowedPacket</a>" : <i>String</i>,
        "<a href="#mariadbmaxconnections" title="MariadbMaxConnections">MariadbMaxConnections</a>" : <i>Double</i>,
        "<a href="#mariadbquerycache" title="MariadbQueryCache">MariadbQueryCache</a>" : <i>Boolean</i>,
        "<a href="#mariadbquerycachelimit" title="MariadbQueryCacheLimit">MariadbQueryCacheLimit</a>" : <i>String</i>,
        "<a href="#mariadbquerycachesize" title="MariadbQueryCacheSize">MariadbQueryCacheSize</a>" : <i>String</i>,
        "<a href="#mariadbserverid" title="MariadbServerId">MariadbServerId</a>" : <i>Double</i>,
        "<a href="#mariadbsqlmode" title="MariadbSqlMode">MariadbSqlMode</a>" : <i>String</i>,
        "<a href="#maxcorecount" title="MaxCoreCount">MaxCoreCount</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#performanceclass" title="PerformanceClass">PerformanceClass</a>" : <i>String</i>,
        "<a href="#release" title="Release">Release</a>" : <i>String</i>,
        "<a href="#securityzoneuuid" title="SecurityZoneUuid">SecurityZoneUuid</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Gridscale::Mariadb
Properties:
    <a href="#labels" title="Labels">Labels</a>: <i>
      - String</i>
    <a href="#mariadbbinlogformat" title="MariadbBinlogFormat">MariadbBinlogFormat</a>: <i>String</i>
    <a href="#mariadbdefaulttimezone" title="MariadbDefaultTimeZone">MariadbDefaultTimeZone</a>: <i>String</i>
    <a href="#mariadblogbin" title="MariadbLogBin">MariadbLogBin</a>: <i>Boolean</i>
    <a href="#mariadbmaxallowedpacket" title="MariadbMaxAllowedPacket">MariadbMaxAllowedPacket</a>: <i>String</i>
    <a href="#mariadbmaxconnections" title="MariadbMaxConnections">MariadbMaxConnections</a>: <i>Double</i>
    <a href="#mariadbquerycache" title="MariadbQueryCache">MariadbQueryCache</a>: <i>Boolean</i>
    <a href="#mariadbquerycachelimit" title="MariadbQueryCacheLimit">MariadbQueryCacheLimit</a>: <i>String</i>
    <a href="#mariadbquerycachesize" title="MariadbQueryCacheSize">MariadbQueryCacheSize</a>: <i>String</i>
    <a href="#mariadbserverid" title="MariadbServerId">MariadbServerId</a>: <i>Double</i>
    <a href="#mariadbsqlmode" title="MariadbSqlMode">MariadbSqlMode</a>: <i>String</i>
    <a href="#maxcorecount" title="MaxCoreCount">MaxCoreCount</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#performanceclass" title="PerformanceClass">PerformanceClass</a>: <i>String</i>
    <a href="#release" title="Release">Release</a>: <i>String</i>
    <a href="#securityzoneuuid" title="SecurityZoneUuid">SecurityZoneUuid</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Labels

List of labels in the format [ "label1", "label2" ].

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MariadbBinlogFormat

MariaDB parameter: Binary Logging Format. Default: "MIXED".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MariadbDefaultTimeZone

MariaDB parameter: Server Timezone. Default: UTC.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MariadbLogBin

MariaDB parameter: Binary Logging. Default: false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MariadbMaxAllowedPacket

MariaDB parameter: Max Allowed Packet Size. Format: xM (where x is an integer, M stands for unit: k(kB), M(MB), G(GB)). Default: 64M.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MariadbMaxConnections

MariaDB parameter: Max Connections. Default: 4000.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MariadbQueryCache

MariaDB parameter: Enable query cache. Default: true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MariadbQueryCacheLimit

MariaDB parameter: Query Cache Limit. Format: xM (where x is an integer, M stands for unit: k(kB), M(MB), G(GB)). Default: 1M.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MariadbQueryCacheSize

MariaDB parameter: Query Cache Size. Format: xM (where x is an integer, M stands for unit: k(kB), M(MB), G(GB)). Default: 128M.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MariadbServerId

MariaDB parameter: Server Id. Default: 1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MariadbSqlMode

MariaDB parameter: SQL Mode. Default: "NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxCoreCount

Maximum CPU core count. The MariaDB instance's CPU core count will be autoscaled based on the workload. The number of cores stays between 1 and `max_core_count`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The human-readable name of the object. It supports the full UTF-8 character set, with a maximum of 64 characters.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PerformanceClass

Performance class of MariaDB service. Available performance classes at the time of writing: `standard`, `high`, `insane`, `ultra`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Release

The MariaDB release of this instance. For convenience, please use [gscloud](https://github.com/gridscale/gscloud) to get the list of available MariaDB service releases.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityZoneUuid

The UUID of the security zone that the service is running in.

_Required_: No

_Type_: String

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

#### ChangeTime

Returns the <code>ChangeTime</code> value.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### ListenPort

Returns the <code>ListenPort</code> value.

#### NetworkUuid

Returns the <code>NetworkUuid</code> value.

#### Password

Returns the <code>Password</code> value.

#### ServiceTemplateUuid

Returns the <code>ServiceTemplateUuid</code> value.

#### Status

Returns the <code>Status</code> value.

#### UsageInMinutes

Returns the <code>UsageInMinutes</code> value.

#### Username

Returns the <code>Username</code> value.

