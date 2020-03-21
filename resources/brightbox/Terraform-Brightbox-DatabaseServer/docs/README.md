# Terraform::Brightbox::DatabaseServer

Provides a Brightbox Database Server resource. This can be used to create,
modify, and delete Database Servers.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Brightbox::DatabaseServer",
    "Properties" : {
        "<a href="#allowaccess" title="AllowAccess">AllowAccess</a>" : <i>[ String, ... ]</i>,
        "<a href="#databaseengine" title="DatabaseEngine">DatabaseEngine</a>" : <i>String</i>,
        "<a href="#databasetype" title="DatabaseType">DatabaseType</a>" : <i>String</i>,
        "<a href="#databaseversion" title="DatabaseVersion">DatabaseVersion</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#maintenancehour" title="MaintenanceHour">MaintenanceHour</a>" : <i>Double</i>,
        "<a href="#maintenanceweekday" title="MaintenanceWeekday">MaintenanceWeekday</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#snapshot" title="Snapshot">Snapshot</a>" : <i>String</i>,
        "<a href="#snapshotsschedule" title="SnapshotsSchedule">SnapshotsSchedule</a>" : <i>String</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Brightbox::DatabaseServer
Properties:
    <a href="#allowaccess" title="AllowAccess">AllowAccess</a>: <i>
      - String</i>
    <a href="#databaseengine" title="DatabaseEngine">DatabaseEngine</a>: <i>String</i>
    <a href="#databasetype" title="DatabaseType">DatabaseType</a>: <i>String</i>
    <a href="#databaseversion" title="DatabaseVersion">DatabaseVersion</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#maintenancehour" title="MaintenanceHour">MaintenanceHour</a>: <i>Double</i>
    <a href="#maintenanceweekday" title="MaintenanceWeekday">MaintenanceWeekday</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#snapshot" title="Snapshot">Snapshot</a>: <i>String</i>
    <a href="#snapshotsschedule" title="SnapshotsSchedule">SnapshotsSchedule</a>: <i>String</i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AllowAccess

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseEngine

Database engine to request. Default is mysql.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseType

ID of the Database Type required.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseVersion

Database version to request. Default is 8.0.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A further description of the Database Server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintenanceHour

Number representing 24hr time start of maintenance window hour for x:00-x:59 (0-23). Default is 6.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintenanceWeekday

Numerical index of weekday (0 is Sunday, 1 is Monday...) to set when automatic updates may be performed. Default is 0 (Sunday).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A label assigned to the Database Server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Snapshot

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotsSchedule

A crontab pattern to determine approximately when scheduled snapshots will run (must be at least hourly).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

The handle of the zone required (`gb1-a`, `gb1-b`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AdminPassword

Returns the <code>AdminPassword</code> value.

#### AdminUsername

Returns the <code>AdminUsername</code> value.

#### Locked

Returns the <code>Locked</code> value.

#### SnapshotsScheduleNextAt

Returns the <code>SnapshotsScheduleNextAt</code> value.

#### Status

Returns the <code>Status</code> value.

