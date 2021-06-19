# TF::MongoDBAtlas::Cluster SnapshotBackupPolicyDefinition3

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#clusterid" title="ClusterId">ClusterId</a>" : <i>String</i>,
    "<a href="#clustername" title="ClusterName">ClusterName</a>" : <i>String</i>,
    "<a href="#nextsnapshot" title="NextSnapshot">NextSnapshot</a>" : <i>String</i>,
    "<a href="#policies" title="Policies">Policies</a>" : <i>[ <a href="snapshotbackuppolicydefinition2.md">SnapshotBackupPolicyDefinition2</a>, ... ]</i>,
    "<a href="#referencehourofday" title="ReferenceHourOfDay">ReferenceHourOfDay</a>" : <i>Double</i>,
    "<a href="#referenceminuteofhour" title="ReferenceMinuteOfHour">ReferenceMinuteOfHour</a>" : <i>Double</i>,
    "<a href="#restorewindowdays" title="RestoreWindowDays">RestoreWindowDays</a>" : <i>Double</i>,
    "<a href="#updatesnapshots" title="UpdateSnapshots">UpdateSnapshots</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#clusterid" title="ClusterId">ClusterId</a>: <i>String</i>
<a href="#clustername" title="ClusterName">ClusterName</a>: <i>String</i>
<a href="#nextsnapshot" title="NextSnapshot">NextSnapshot</a>: <i>String</i>
<a href="#policies" title="Policies">Policies</a>: <i>
      - <a href="snapshotbackuppolicydefinition2.md">SnapshotBackupPolicyDefinition2</a></i>
<a href="#referencehourofday" title="ReferenceHourOfDay">ReferenceHourOfDay</a>: <i>Double</i>
<a href="#referenceminuteofhour" title="ReferenceMinuteOfHour">ReferenceMinuteOfHour</a>: <i>Double</i>
<a href="#restorewindowdays" title="RestoreWindowDays">RestoreWindowDays</a>: <i>Double</i>
<a href="#updatesnapshots" title="UpdateSnapshots">UpdateSnapshots</a>: <i>Boolean</i>
</pre>

## Properties

#### ClusterId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NextSnapshot

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policies

_Required_: No

_Type_: List of <a href="snapshotbackuppolicydefinition2.md">SnapshotBackupPolicyDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReferenceHourOfDay

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReferenceMinuteOfHour

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestoreWindowDays

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateSnapshots

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

