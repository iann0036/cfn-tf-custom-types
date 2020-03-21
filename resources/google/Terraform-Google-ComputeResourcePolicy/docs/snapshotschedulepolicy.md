# Terraform::Google::ComputeResourcePolicy SnapshotSchedulePolicy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#retentionpolicy" title="RetentionPolicy">RetentionPolicy</a>" : <i>[ <a href="snapshotschedulepolicy-retentionpolicy.md">RetentionPolicy</a>, ... ]</i>,
    "<a href="#schedule" title="Schedule">Schedule</a>" : <i>[ <a href="snapshotschedulepolicy-schedule.md">Schedule</a>, ... ]</i>,
    "<a href="#snapshotproperties" title="SnapshotProperties">SnapshotProperties</a>" : <i>[ <a href="snapshotschedulepolicy-snapshotproperties.md">SnapshotProperties</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#retentionpolicy" title="RetentionPolicy">RetentionPolicy</a>: <i>
      - <a href="snapshotschedulepolicy-retentionpolicy.md">RetentionPolicy</a></i>
<a href="#schedule" title="Schedule">Schedule</a>: <i>
      - <a href="snapshotschedulepolicy-schedule.md">Schedule</a></i>
<a href="#snapshotproperties" title="SnapshotProperties">SnapshotProperties</a>: <i>
      - <a href="snapshotschedulepolicy-snapshotproperties.md">SnapshotProperties</a></i>
</pre>

## Properties

#### RetentionPolicy

_Required_: No

_Type_: List of <a href="snapshotschedulepolicy-retentionpolicy.md">RetentionPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

_Required_: No

_Type_: List of <a href="snapshotschedulepolicy-schedule.md">Schedule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotProperties

_Required_: No

_Type_: List of <a href="snapshotschedulepolicy-snapshotproperties.md">SnapshotProperties</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

