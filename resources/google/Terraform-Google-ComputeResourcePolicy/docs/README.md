# Terraform::Google::ComputeResourcePolicy

A policy that can be attached to a resource to specify or schedule actions on that resource.



<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=resource_policy_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div>

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::ComputeResourcePolicy",
    "Properties" : {
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

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

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

