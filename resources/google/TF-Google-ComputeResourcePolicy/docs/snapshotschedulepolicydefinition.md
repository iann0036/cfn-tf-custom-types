# TF::Google::ComputeResourcePolicy SnapshotSchedulePolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#retentionpolicy" title="RetentionPolicy">RetentionPolicy</a>" : <i>[ <a href="retentionpolicydefinition.md">RetentionPolicyDefinition</a>, ... ]</i>,
    "<a href="#schedule" title="Schedule">Schedule</a>" : <i>[ <a href="scheduledefinition.md">ScheduleDefinition</a>, ... ]</i>,
    "<a href="#snapshotproperties" title="SnapshotProperties">SnapshotProperties</a>" : <i>[ <a href="snapshotpropertiesdefinition.md">SnapshotPropertiesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#retentionpolicy" title="RetentionPolicy">RetentionPolicy</a>: <i>
      - <a href="retentionpolicydefinition.md">RetentionPolicyDefinition</a></i>
<a href="#schedule" title="Schedule">Schedule</a>: <i>
      - <a href="scheduledefinition.md">ScheduleDefinition</a></i>
<a href="#snapshotproperties" title="SnapshotProperties">SnapshotProperties</a>: <i>
      - <a href="snapshotpropertiesdefinition.md">SnapshotPropertiesDefinition</a></i>
</pre>

## Properties

#### RetentionPolicy

_Required_: No

_Type_: List of <a href="retentionpolicydefinition.md">RetentionPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

_Required_: No

_Type_: List of <a href="scheduledefinition.md">ScheduleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotProperties

_Required_: No

_Type_: List of <a href="snapshotpropertiesdefinition.md">SnapshotPropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

