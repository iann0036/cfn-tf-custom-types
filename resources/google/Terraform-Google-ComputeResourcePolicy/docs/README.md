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
        "<a href="#snapshotschedulepolicy" title="SnapshotSchedulePolicy">SnapshotSchedulePolicy</a>" : <i>[ &lt;a href=&#34;snapshotschedulepolicy.md&#34;&gt;SnapshotSchedulePolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#retentionpolicy" title="RetentionPolicy">RetentionPolicy</a>" : <i>[ &lt;a href=&#34;retentionpolicy.md&#34;&gt;RetentionPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#schedule" title="Schedule">Schedule</a>" : <i>[ &lt;a href=&#34;schedule.md&#34;&gt;Schedule&lt;/a&gt;, ... ]</i>,
        "<a href="#snapshotproperties" title="SnapshotProperties">SnapshotProperties</a>" : <i>[ &lt;a href=&#34;snapshotproperties.md&#34;&gt;SnapshotProperties&lt;/a&gt;, ... ]</i>,
        "<a href="#dailyschedule" title="DailySchedule">DailySchedule</a>" : <i>[ &lt;a href=&#34;dailyschedule.md&#34;&gt;DailySchedule&lt;/a&gt;, ... ]</i>,
        "<a href="#hourlyschedule" title="HourlySchedule">HourlySchedule</a>" : <i>[ &lt;a href=&#34;hourlyschedule.md&#34;&gt;HourlySchedule&lt;/a&gt;, ... ]</i>,
        "<a href="#weeklyschedule" title="WeeklySchedule">WeeklySchedule</a>" : <i>[ &lt;a href=&#34;weeklyschedule.md&#34;&gt;WeeklySchedule&lt;/a&gt;, ... ]</i>,
        "<a href="#dayofweeks" title="DayOfWeeks">DayOfWeeks</a>" : <i>[ &lt;a href=&#34;dayofweeks.md&#34;&gt;DayOfWeeks&lt;/a&gt;, ... ]</i>
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
      - &lt;a href=&#34;snapshotschedulepolicy.md&#34;&gt;SnapshotSchedulePolicy&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#retentionpolicy" title="RetentionPolicy">RetentionPolicy</a>: <i>
      - &lt;a href=&#34;retentionpolicy.md&#34;&gt;RetentionPolicy&lt;/a&gt;</i>
    <a href="#schedule" title="Schedule">Schedule</a>: <i>
      - &lt;a href=&#34;schedule.md&#34;&gt;Schedule&lt;/a&gt;</i>
    <a href="#snapshotproperties" title="SnapshotProperties">SnapshotProperties</a>: <i>
      - &lt;a href=&#34;snapshotproperties.md&#34;&gt;SnapshotProperties&lt;/a&gt;</i>
    <a href="#dailyschedule" title="DailySchedule">DailySchedule</a>: <i>
      - &lt;a href=&#34;dailyschedule.md&#34;&gt;DailySchedule&lt;/a&gt;</i>
    <a href="#hourlyschedule" title="HourlySchedule">HourlySchedule</a>: <i>
      - &lt;a href=&#34;hourlyschedule.md&#34;&gt;HourlySchedule&lt;/a&gt;</i>
    <a href="#weeklyschedule" title="WeeklySchedule">WeeklySchedule</a>: <i>
      - &lt;a href=&#34;weeklyschedule.md&#34;&gt;WeeklySchedule&lt;/a&gt;</i>
    <a href="#dayofweeks" title="DayOfWeeks">DayOfWeeks</a>: <i>
      - &lt;a href=&#34;dayofweeks.md&#34;&gt;DayOfWeeks&lt;/a&gt;</i>
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

_Type_: List of &lt;a href=&#34;snapshotschedulepolicy.md&#34;&gt;SnapshotSchedulePolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;retentionpolicy.md&#34;&gt;RetentionPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

_Required_: No

_Type_: List of &lt;a href=&#34;schedule.md&#34;&gt;Schedule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotProperties

_Required_: No

_Type_: List of &lt;a href=&#34;snapshotproperties.md&#34;&gt;SnapshotProperties&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DailySchedule

_Required_: No

_Type_: List of &lt;a href=&#34;dailyschedule.md&#34;&gt;DailySchedule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HourlySchedule

_Required_: No

_Type_: List of &lt;a href=&#34;hourlyschedule.md&#34;&gt;HourlySchedule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeeklySchedule

_Required_: No

_Type_: List of &lt;a href=&#34;weeklyschedule.md&#34;&gt;WeeklySchedule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DayOfWeeks

_Required_: No

_Type_: List of &lt;a href=&#34;dayofweeks.md&#34;&gt;DayOfWeeks&lt;/a&gt;

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

Returns the &lt;code&gt;SelfLink&lt;/code&gt; value.

