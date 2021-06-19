# TF::Nutanix::ProtectionRule AvailabilityZoneConnectivityListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#destinationavailabilityzoneindex" title="DestinationAvailabilityZoneIndex">DestinationAvailabilityZoneIndex</a>" : <i>Double</i>,
    "<a href="#sourceavailabilityzoneindex" title="SourceAvailabilityZoneIndex">SourceAvailabilityZoneIndex</a>" : <i>Double</i>,
    "<a href="#snapshotschedulelist" title="SnapshotScheduleList">SnapshotScheduleList</a>" : <i>[ <a href="snapshotschedulelistdefinition.md">SnapshotScheduleListDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#destinationavailabilityzoneindex" title="DestinationAvailabilityZoneIndex">DestinationAvailabilityZoneIndex</a>: <i>Double</i>
<a href="#sourceavailabilityzoneindex" title="SourceAvailabilityZoneIndex">SourceAvailabilityZoneIndex</a>: <i>Double</i>
<a href="#snapshotschedulelist" title="SnapshotScheduleList">SnapshotScheduleList</a>: <i>
      - <a href="snapshotschedulelistdefinition.md">SnapshotScheduleListDefinition</a></i>
</pre>

## Properties

#### DestinationAvailabilityZoneIndex

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceAvailabilityZoneIndex

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotScheduleList

_Required_: No

_Type_: List of <a href="snapshotschedulelistdefinition.md">SnapshotScheduleListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

