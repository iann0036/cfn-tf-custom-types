# Terraform::Google::ComputeResourcePolicy

CloudFormation equivalent of google_compute_resource_policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::ComputeResourcePolicy",
    "Properties" : {
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#snapshotschedulepolicy" title="SnapshotSchedulePolicy">SnapshotSchedulePolicy</a>" : <i>[ <a href="snapshotschedulepolicy.md">SnapshotSchedulePolicy</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#retentionpolicy" title="RetentionPolicy">RetentionPolicy</a>" : <i>[ <a href="retentionpolicy.md">RetentionPolicy</a>, ... ]</i>,
        "<a href="#schedule" title="Schedule">Schedule</a>" : <i>[ <a href="schedule.md">Schedule</a>, ... ]</i>,
        "<a href="#snapshotproperties" title="SnapshotProperties">SnapshotProperties</a>" : <i>[ <a href="snapshotproperties.md">SnapshotProperties</a>, ... ]</i>,
        "<a href="#dailyschedule" title="DailySchedule">DailySchedule</a>" : <i>[ <a href="dailyschedule.md">DailySchedule</a>, ... ]</i>,
        "<a href="#hourlyschedule" title="HourlySchedule">HourlySchedule</a>" : <i>[ <a href="hourlyschedule.md">HourlySchedule</a>, ... ]</i>,
        "<a href="#weeklyschedule" title="WeeklySchedule">WeeklySchedule</a>" : <i>[ <a href="weeklyschedule.md">WeeklySchedule</a>, ... ]</i>,
        "<a href="#dayofweeks" title="DayOfWeeks">DayOfWeeks</a>" : <i>[ <a href="dayofweeks.md">DayOfWeeks</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::ComputeResourcePolicy
Properties:
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#snapshotschedulepolicy" title="SnapshotSchedulePolicy">SnapshotSchedulePolicy</a>: <i>
      - <a href="snapshotschedulepolicy.md">SnapshotSchedulePolicy</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#retentionpolicy" title="RetentionPolicy">RetentionPolicy</a>: <i>
      - <a href="retentionpolicy.md">RetentionPolicy</a></i>
    <a href="#schedule" title="Schedule">Schedule</a>: <i>
      - <a href="schedule.md">Schedule</a></i>
    <a href="#snapshotproperties" title="SnapshotProperties">SnapshotProperties</a>: <i>
      - <a href="snapshotproperties.md">SnapshotProperties</a></i>
    <a href="#dailyschedule" title="DailySchedule">DailySchedule</a>: <i>
      - <a href="dailyschedule.md">DailySchedule</a></i>
    <a href="#hourlyschedule" title="HourlySchedule">HourlySchedule</a>: <i>
      - <a href="hourlyschedule.md">HourlySchedule</a></i>
    <a href="#weeklyschedule" title="WeeklySchedule">WeeklySchedule</a>: <i>
      - <a href="weeklyschedule.md">WeeklySchedule</a></i>
    <a href="#dayofweeks" title="DayOfWeeks">DayOfWeeks</a>: <i>
      - <a href="dayofweeks.md">DayOfWeeks</a></i>
</pre>

## Properties

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotSchedulePolicy

_Required_: No

_Type_: List of <a href="snapshotschedulepolicy.md">SnapshotSchedulePolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionPolicy

_Required_: No

_Type_: List of <a href="retentionpolicy.md">RetentionPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

_Required_: No

_Type_: List of <a href="schedule.md">Schedule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotProperties

_Required_: No

_Type_: List of <a href="snapshotproperties.md">SnapshotProperties</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DailySchedule

_Required_: No

_Type_: List of <a href="dailyschedule.md">DailySchedule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HourlySchedule

_Required_: No

_Type_: List of <a href="hourlyschedule.md">HourlySchedule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeeklySchedule

_Required_: No

_Type_: List of <a href="weeklyschedule.md">WeeklySchedule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DayOfWeeks

_Required_: No

_Type_: List of <a href="dayofweeks.md">DayOfWeeks</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### SelfLink

Returns the <code>SelfLink</code> value.
