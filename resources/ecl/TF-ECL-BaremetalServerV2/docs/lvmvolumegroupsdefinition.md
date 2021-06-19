# TF::ECL::BaremetalServerV2 LvmVolumeGroupsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#physicalvolumepartitionlabels" title="PhysicalVolumePartitionLabels">PhysicalVolumePartitionLabels</a>" : <i>[ String, ... ]</i>,
    "<a href="#vglabel" title="VgLabel">VgLabel</a>" : <i>String</i>,
    "<a href="#logicalvolumes" title="LogicalVolumes">LogicalVolumes</a>" : <i>[ <a href="logicalvolumesdefinition.md">LogicalVolumesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#physicalvolumepartitionlabels" title="PhysicalVolumePartitionLabels">PhysicalVolumePartitionLabels</a>: <i>
      - String</i>
<a href="#vglabel" title="VgLabel">VgLabel</a>: <i>String</i>
<a href="#logicalvolumes" title="LogicalVolumes">LogicalVolumes</a>: <i>
      - <a href="logicalvolumesdefinition.md">LogicalVolumesDefinition</a></i>
</pre>

## Properties

#### PhysicalVolumePartitionLabels

List of physical volume partition
label. Changing this creates a new server.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VgLabel

Volume group label. Changing this creates a new server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogicalVolumes

_Required_: No

_Type_: List of <a href="logicalvolumesdefinition.md">LogicalVolumesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

