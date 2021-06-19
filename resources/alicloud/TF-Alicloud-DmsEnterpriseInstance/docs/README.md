# TF::Alicloud::DmsEnterpriseInstance

Provides a DMS Enterprise Instance resource.

-> **NOTE:** API users must first register in DMS.
-> **NOTE:** Available in 1.81.0+.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::DmsEnterpriseInstance",
    "Properties" : {
        "<a href="#datalinkname" title="DataLinkName">DataLinkName</a>" : <i>String</i>,
        "<a href="#databasepassword" title="DatabasePassword">DatabasePassword</a>" : <i>String</i>,
        "<a href="#databaseuser" title="DatabaseUser">DatabaseUser</a>" : <i>String</i>,
        "<a href="#dbaid" title="DbaId">DbaId</a>" : <i>String</i>,
        "<a href="#dbauid" title="DbaUid">DbaUid</a>" : <i>Double</i>,
        "<a href="#ddlonline" title="DdlOnline">DdlOnline</a>" : <i>Double</i>,
        "<a href="#ecsinstanceid" title="EcsInstanceId">EcsInstanceId</a>" : <i>String</i>,
        "<a href="#ecsregion" title="EcsRegion">EcsRegion</a>" : <i>String</i>,
        "<a href="#envtype" title="EnvType">EnvType</a>" : <i>String</i>,
        "<a href="#exporttimeout" title="ExportTimeout">ExportTimeout</a>" : <i>Double</i>,
        "<a href="#host" title="Host">Host</a>" : <i>String</i>,
        "<a href="#instancealias" title="InstanceAlias">InstanceAlias</a>" : <i>String</i>,
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
        "<a href="#instancename" title="InstanceName">InstanceName</a>" : <i>String</i>,
        "<a href="#instancesource" title="InstanceSource">InstanceSource</a>" : <i>String</i>,
        "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
        "<a href="#networktype" title="NetworkType">NetworkType</a>" : <i>String</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#querytimeout" title="QueryTimeout">QueryTimeout</a>" : <i>Double</i>,
        "<a href="#saferule" title="SafeRule">SafeRule</a>" : <i>String</i>,
        "<a href="#saferuleid" title="SafeRuleId">SafeRuleId</a>" : <i>String</i>,
        "<a href="#sid" title="Sid">Sid</a>" : <i>String</i>,
        "<a href="#skiptest" title="SkipTest">SkipTest</a>" : <i>Boolean</i>,
        "<a href="#tid" title="Tid">Tid</a>" : <i>Double</i>,
        "<a href="#usedsql" title="UseDsql">UseDsql</a>" : <i>Double</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::DmsEnterpriseInstance
Properties:
    <a href="#datalinkname" title="DataLinkName">DataLinkName</a>: <i>String</i>
    <a href="#databasepassword" title="DatabasePassword">DatabasePassword</a>: <i>String</i>
    <a href="#databaseuser" title="DatabaseUser">DatabaseUser</a>: <i>String</i>
    <a href="#dbaid" title="DbaId">DbaId</a>: <i>String</i>
    <a href="#dbauid" title="DbaUid">DbaUid</a>: <i>Double</i>
    <a href="#ddlonline" title="DdlOnline">DdlOnline</a>: <i>Double</i>
    <a href="#ecsinstanceid" title="EcsInstanceId">EcsInstanceId</a>: <i>String</i>
    <a href="#ecsregion" title="EcsRegion">EcsRegion</a>: <i>String</i>
    <a href="#envtype" title="EnvType">EnvType</a>: <i>String</i>
    <a href="#exporttimeout" title="ExportTimeout">ExportTimeout</a>: <i>Double</i>
    <a href="#host" title="Host">Host</a>: <i>String</i>
    <a href="#instancealias" title="InstanceAlias">InstanceAlias</a>: <i>String</i>
    <a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
    <a href="#instancename" title="InstanceName">InstanceName</a>: <i>String</i>
    <a href="#instancesource" title="InstanceSource">InstanceSource</a>: <i>String</i>
    <a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
    <a href="#networktype" title="NetworkType">NetworkType</a>: <i>String</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#querytimeout" title="QueryTimeout">QueryTimeout</a>: <i>Double</i>
    <a href="#saferule" title="SafeRule">SafeRule</a>: <i>String</i>
    <a href="#saferuleid" title="SafeRuleId">SafeRuleId</a>: <i>String</i>
    <a href="#sid" title="Sid">Sid</a>: <i>String</i>
    <a href="#skiptest" title="SkipTest">SkipTest</a>: <i>Boolean</i>
    <a href="#tid" title="Tid">Tid</a>: <i>Double</i>
    <a href="#usedsql" title="UseDsql">UseDsql</a>: <i>Double</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### DataLinkName

Cross-database query datalink name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabasePassword

Database access password.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseUser

Database access account.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbaId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbaUid

The DBA of the instance is passed into the Alibaba Cloud uid of the DBA.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DdlOnline

Whether to use online services, currently only supports MySQL and PolarDB. Valid values: `0` Not used, `1` Native online DDL priority, `2` DMS lock-free table structure change priority.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EcsInstanceId

ECS instance ID. The value of InstanceSource is the ECS self-built library. This value must be passed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EcsRegion

The region where the instance is located. This value must be passed when the value of InstanceSource is RDS, ECS self-built library, and VPC dedicated line IDC.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvType

Environment type. Valid values: `product` production environment, `dev` development environment, `pre` pre-release environment, `test` test environment, `sit` SIT environment, `uat` UAT environment, `pet` pressure test environment, `stag` STAG environment.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExportTimeout

Export timeout, unit: s (seconds).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Host

Host address of the target database.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceAlias

Instance alias, to help users quickly distinguish positioning.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceSource

The source of the database instance. Valid values: `PUBLIC_OWN`, `RDS`, `ECS_OWN`, `VPC_IDC`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceType

Database type. Valid values: `MySQL`, `SQLServer`, `PostgreSQL`, `Oracle,` `DRDS`, `OceanBase`, `Mongo`, `Redis`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkType

Network type. Valid values: `CLASSIC`, `VPC`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

Access port of the target database.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryTimeout

Query timeout time, unit: s (seconds).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SafeRule

The security rule of the instance is passed into the name of the security rule in the enterprise.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SafeRuleId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sid

The SID. This value must be passed when InstanceType is PostgreSQL or Oracle.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipTest

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tid

The tenant ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseDsql

Whether to enable cross-instance query. Valid values: `0` not open, `1` open.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

VPC ID. This value must be passed when the value of InstanceSource is VPC dedicated line IDC.

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

#### DbaNickName

Returns the <code>DbaNickName</code> value.

#### Id

Returns the <code>Id</code> value.

#### State

Returns the <code>State</code> value.

#### Status

Returns the <code>Status</code> value.

