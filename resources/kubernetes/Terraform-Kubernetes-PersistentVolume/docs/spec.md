# Terraform::Kubernetes::PersistentVolume Spec

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accessmodes" title="AccessModes">AccessModes</a>" : <i>[ String, ... ]</i>,
    "<a href="#capacity" title="Capacity">Capacity</a>" : <i>[ &lt;a href=&#34;spec-capacity.md&#34;&gt;Capacity&lt;/a&gt;, ... ]</i>,
    "<a href="#mountoptions" title="MountOptions">MountOptions</a>" : <i>[ String, ... ]</i>,
    "<a href="#persistentvolumereclaimpolicy" title="PersistentVolumeReclaimPolicy">PersistentVolumeReclaimPolicy</a>" : <i>String</i>,
    "<a href="#storageclassname" title="StorageClassName">StorageClassName</a>" : <i>String</i>,
    "<a href="#nodeaffinity" title="NodeAffinity">NodeAffinity</a>" : <i>[ &lt;a href=&#34;spec-nodeaffinity.md&#34;&gt;NodeAffinity&lt;/a&gt;, ... ]</i>,
    "<a href="#persistentvolumesource" title="PersistentVolumeSource">PersistentVolumeSource</a>" : <i>[ &lt;a href=&#34;spec-persistentvolumesource.md&#34;&gt;PersistentVolumeSource&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#accessmodes" title="AccessModes">AccessModes</a>: <i>
      - String</i>
<a href="#capacity" title="Capacity">Capacity</a>: <i>
      - &lt;a href=&#34;spec-capacity.md&#34;&gt;Capacity&lt;/a&gt;</i>
<a href="#mountoptions" title="MountOptions">MountOptions</a>: <i>
      - String</i>
<a href="#persistentvolumereclaimpolicy" title="PersistentVolumeReclaimPolicy">PersistentVolumeReclaimPolicy</a>: <i>String</i>
<a href="#storageclassname" title="StorageClassName">StorageClassName</a>: <i>String</i>
<a href="#nodeaffinity" title="NodeAffinity">NodeAffinity</a>: <i>
      - &lt;a href=&#34;spec-nodeaffinity.md&#34;&gt;NodeAffinity&lt;/a&gt;</i>
<a href="#persistentvolumesource" title="PersistentVolumeSource">PersistentVolumeSource</a>: <i>
      - &lt;a href=&#34;spec-persistentvolumesource.md&#34;&gt;PersistentVolumeSource&lt;/a&gt;</i>
</pre>

## Properties

#### AccessModes

_Required_: Yes
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Capacity

_Required_: Yes
_Type_: List of &lt;a href=&#34;spec-capacity.md&#34;&gt;Capacity&lt;/a&gt;

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

#### NodeAffinity

_Required_: No
_Type_: List of &lt;a href=&#34;spec-nodeaffinity.md&#34;&gt;NodeAffinity&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PersistentVolumeSource

_Required_: No
_Type_: List of &lt;a href=&#34;spec-persistentvolumesource.md&#34;&gt;PersistentVolumeSource&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

