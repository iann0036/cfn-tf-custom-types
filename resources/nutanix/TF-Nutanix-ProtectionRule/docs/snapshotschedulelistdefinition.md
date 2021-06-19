# TF::Nutanix::ProtectionRule SnapshotScheduleListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autosuspendtimeoutsecs" title="AutoSuspendTimeoutSecs">AutoSuspendTimeoutSecs</a>" : <i>Double</i>,
    "<a href="#recoverypointobjectivesecs" title="RecoveryPointObjectiveSecs">RecoveryPointObjectiveSecs</a>" : <i>Double</i>,
    "<a href="#snapshottype" title="SnapshotType">SnapshotType</a>" : <i>String</i>,
    "<a href="#localsnapshotretentionpolicy" title="LocalSnapshotRetentionPolicy">LocalSnapshotRetentionPolicy</a>" : <i>[ <a href="localsnapshotretentionpolicydefinition.md">LocalSnapshotRetentionPolicyDefinition</a>, ... ]</i>,
    "<a href="#remotesnapshotretentionpolicy" title="RemoteSnapshotRetentionPolicy">RemoteSnapshotRetentionPolicy</a>" : <i>[ <a href="remotesnapshotretentionpolicydefinition.md">RemoteSnapshotRetentionPolicyDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#autosuspendtimeoutsecs" title="AutoSuspendTimeoutSecs">AutoSuspendTimeoutSecs</a>: <i>Double</i>
<a href="#recoverypointobjectivesecs" title="RecoveryPointObjectiveSecs">RecoveryPointObjectiveSecs</a>: <i>Double</i>
<a href="#snapshottype" title="SnapshotType">SnapshotType</a>: <i>String</i>
<a href="#localsnapshotretentionpolicy" title="LocalSnapshotRetentionPolicy">LocalSnapshotRetentionPolicy</a>: <i>
      - <a href="localsnapshotretentionpolicydefinition.md">LocalSnapshotRetentionPolicyDefinition</a></i>
<a href="#remotesnapshotretentionpolicy" title="RemoteSnapshotRetentionPolicy">RemoteSnapshotRetentionPolicy</a>: <i>
      - <a href="remotesnapshotretentionpolicydefinition.md">RemoteSnapshotRetentionPolicyDefinition</a></i>
</pre>

## Properties

#### AutoSuspendTimeoutSecs

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecoveryPointObjectiveSecs

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalSnapshotRetentionPolicy

_Required_: No

_Type_: List of <a href="localsnapshotretentionpolicydefinition.md">LocalSnapshotRetentionPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteSnapshotRetentionPolicy

_Required_: No

_Type_: List of <a href="remotesnapshotretentionpolicydefinition.md">RemoteSnapshotRetentionPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

