# TF::Kubernetes::PersistentVolume SpecDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accessmodes" title="AccessModes">AccessModes</a>" : <i>[ String, ... ]</i>,
    "<a href="#capacity" title="Capacity">Capacity</a>" : <i>[ <a href="capacitydefinition.md">CapacityDefinition</a>, ... ]</i>,
    "<a href="#mountoptions" title="MountOptions">MountOptions</a>" : <i>[ String, ... ]</i>,
    "<a href="#persistentvolumereclaimpolicy" title="PersistentVolumeReclaimPolicy">PersistentVolumeReclaimPolicy</a>" : <i>String</i>,
    "<a href="#storageclassname" title="StorageClassName">StorageClassName</a>" : <i>String</i>,
    "<a href="#volumemode" title="VolumeMode">VolumeMode</a>" : <i>String</i>,
    "<a href="#claimref" title="ClaimRef">ClaimRef</a>" : <i>[ <a href="claimrefdefinition.md">ClaimRefDefinition</a>, ... ]</i>,
    "<a href="#nodeaffinity" title="NodeAffinity">NodeAffinity</a>" : <i>[ <a href="nodeaffinitydefinition.md">NodeAffinityDefinition</a>, ... ]</i>,
    "<a href="#persistentvolumesource" title="PersistentVolumeSource">PersistentVolumeSource</a>" : <i>[ <a href="persistentvolumesourcedefinition.md">PersistentVolumeSourceDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#accessmodes" title="AccessModes">AccessModes</a>: <i>
      - String</i>
<a href="#capacity" title="Capacity">Capacity</a>: <i>
      - <a href="capacitydefinition.md">CapacityDefinition</a></i>
<a href="#mountoptions" title="MountOptions">MountOptions</a>: <i>
      - String</i>
<a href="#persistentvolumereclaimpolicy" title="PersistentVolumeReclaimPolicy">PersistentVolumeReclaimPolicy</a>: <i>String</i>
<a href="#storageclassname" title="StorageClassName">StorageClassName</a>: <i>String</i>
<a href="#volumemode" title="VolumeMode">VolumeMode</a>: <i>String</i>
<a href="#claimref" title="ClaimRef">ClaimRef</a>: <i>
      - <a href="claimrefdefinition.md">ClaimRefDefinition</a></i>
<a href="#nodeaffinity" title="NodeAffinity">NodeAffinity</a>: <i>
      - <a href="nodeaffinitydefinition.md">NodeAffinityDefinition</a></i>
<a href="#persistentvolumesource" title="PersistentVolumeSource">PersistentVolumeSource</a>: <i>
      - <a href="persistentvolumesourcedefinition.md">PersistentVolumeSourceDefinition</a></i>
</pre>

## Properties

#### AccessModes

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Capacity

_Required_: Yes

_Type_: List of <a href="capacitydefinition.md">CapacityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MountOptions

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PersistentVolumeReclaimPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageClassName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClaimRef

_Required_: No

_Type_: List of <a href="claimrefdefinition.md">ClaimRefDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeAffinity

_Required_: No

_Type_: List of <a href="nodeaffinitydefinition.md">NodeAffinityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PersistentVolumeSource

_Required_: No

_Type_: List of <a href="persistentvolumesourcedefinition.md">PersistentVolumeSourceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

