# Terraform::Kubernetes::PersistentVolume

CloudFormation equivalent of kubernetes_persistent_volume

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Kubernetes::PersistentVolume",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ &lt;a href=&#34;metadata.md&#34;&gt;Metadata&lt;/a&gt;, ... ]</i>,
        "<a href="#spec" title="Spec">Spec</a>" : <i>[ &lt;a href=&#34;spec.md&#34;&gt;Spec&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#nodeaffinity" title="NodeAffinity">NodeAffinity</a>" : <i>[ &lt;a href=&#34;nodeaffinity.md&#34;&gt;NodeAffinity&lt;/a&gt;, ... ]</i>,
        "<a href="#persistentvolumesource" title="PersistentVolumeSource">PersistentVolumeSource</a>" : <i>[ &lt;a href=&#34;persistentvolumesource.md&#34;&gt;PersistentVolumeSource&lt;/a&gt;, ... ]</i>,
        "<a href="#required" title="Required">Required</a>" : <i>[ &lt;a href=&#34;required.md&#34;&gt;Required&lt;/a&gt;, ... ]</i>,
        "<a href="#awselasticblockstore" title="AwsElasticBlockStore">AwsElasticBlockStore</a>" : <i>[ &lt;a href=&#34;awselasticblockstore.md&#34;&gt;AwsElasticBlockStore&lt;/a&gt;, ... ]</i>,
        "<a href="#azuredisk" title="AzureDisk">AzureDisk</a>" : <i>[ &lt;a href=&#34;azuredisk.md&#34;&gt;AzureDisk&lt;/a&gt;, ... ]</i>,
        "<a href="#azurefile" title="AzureFile">AzureFile</a>" : <i>[ &lt;a href=&#34;azurefile.md&#34;&gt;AzureFile&lt;/a&gt;, ... ]</i>,
        "<a href="#cephfs" title="CephFs">CephFs</a>" : <i>[ &lt;a href=&#34;cephfs.md&#34;&gt;CephFs&lt;/a&gt;, ... ]</i>,
        "<a href="#cinder" title="Cinder">Cinder</a>" : <i>[ &lt;a href=&#34;cinder.md&#34;&gt;Cinder&lt;/a&gt;, ... ]</i>,
        "<a href="#fc" title="Fc">Fc</a>" : <i>[ &lt;a href=&#34;fc.md&#34;&gt;Fc&lt;/a&gt;, ... ]</i>,
        "<a href="#flexvolume" title="FlexVolume">FlexVolume</a>" : <i>[ &lt;a href=&#34;flexvolume.md&#34;&gt;FlexVolume&lt;/a&gt;, ... ]</i>,
        "<a href="#flocker" title="Flocker">Flocker</a>" : <i>[ &lt;a href=&#34;flocker.md&#34;&gt;Flocker&lt;/a&gt;, ... ]</i>,
        "<a href="#gcepersistentdisk" title="GcePersistentDisk">GcePersistentDisk</a>" : <i>[ &lt;a href=&#34;gcepersistentdisk.md&#34;&gt;GcePersistentDisk&lt;/a&gt;, ... ]</i>,
        "<a href="#glusterfs" title="Glusterfs">Glusterfs</a>" : <i>[ &lt;a href=&#34;glusterfs.md&#34;&gt;Glusterfs&lt;/a&gt;, ... ]</i>,
        "<a href="#hostpath" title="HostPath">HostPath</a>" : <i>[ &lt;a href=&#34;hostpath.md&#34;&gt;HostPath&lt;/a&gt;, ... ]</i>,
        "<a href="#iscsi" title="Iscsi">Iscsi</a>" : <i>[ &lt;a href=&#34;iscsi.md&#34;&gt;Iscsi&lt;/a&gt;, ... ]</i>,
        "<a href="#local" title="Local">Local</a>" : <i>[ &lt;a href=&#34;local.md&#34;&gt;Local&lt;/a&gt;, ... ]</i>,
        "<a href="#nfs" title="Nfs">Nfs</a>" : <i>[ &lt;a href=&#34;nfs.md&#34;&gt;Nfs&lt;/a&gt;, ... ]</i>,
        "<a href="#photonpersistentdisk" title="PhotonPersistentDisk">PhotonPersistentDisk</a>" : <i>[ &lt;a href=&#34;photonpersistentdisk.md&#34;&gt;PhotonPersistentDisk&lt;/a&gt;, ... ]</i>,
        "<a href="#quobyte" title="Quobyte">Quobyte</a>" : <i>[ &lt;a href=&#34;quobyte.md&#34;&gt;Quobyte&lt;/a&gt;, ... ]</i>,
        "<a href="#rbd" title="Rbd">Rbd</a>" : <i>[ &lt;a href=&#34;rbd.md&#34;&gt;Rbd&lt;/a&gt;, ... ]</i>,
        "<a href="#vspherevolume" title="VsphereVolume">VsphereVolume</a>" : <i>[ &lt;a href=&#34;vspherevolume.md&#34;&gt;VsphereVolume&lt;/a&gt;, ... ]</i>,
        "<a href="#nodeselectorterm" title="NodeSelectorTerm">NodeSelectorTerm</a>" : <i>[ &lt;a href=&#34;nodeselectorterm.md&#34;&gt;NodeSelectorTerm&lt;/a&gt;, ... ]</i>,
        "<a href="#secretref" title="SecretRef">SecretRef</a>" : <i>[ &lt;a href=&#34;secretref.md&#34;&gt;SecretRef&lt;/a&gt;, ... ]</i>,
        "<a href="#matchexpressions" title="MatchExpressions">MatchExpressions</a>" : <i>[ &lt;a href=&#34;matchexpressions.md&#34;&gt;MatchExpressions&lt;/a&gt;, ... ]</i>,
        "<a href="#matchfields" title="MatchFields">MatchFields</a>" : <i>[ &lt;a href=&#34;matchfields.md&#34;&gt;MatchFields&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Kubernetes::PersistentVolume
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - &lt;a href=&#34;metadata.md&#34;&gt;Metadata&lt;/a&gt;</i>
    <a href="#spec" title="Spec">Spec</a>: <i>
      - &lt;a href=&#34;spec.md&#34;&gt;Spec&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#nodeaffinity" title="NodeAffinity">NodeAffinity</a>: <i>
      - &lt;a href=&#34;nodeaffinity.md&#34;&gt;NodeAffinity&lt;/a&gt;</i>
    <a href="#persistentvolumesource" title="PersistentVolumeSource">PersistentVolumeSource</a>: <i>
      - &lt;a href=&#34;persistentvolumesource.md&#34;&gt;PersistentVolumeSource&lt;/a&gt;</i>
    <a href="#required" title="Required">Required</a>: <i>
      - &lt;a href=&#34;required.md&#34;&gt;Required&lt;/a&gt;</i>
    <a href="#awselasticblockstore" title="AwsElasticBlockStore">AwsElasticBlockStore</a>: <i>
      - &lt;a href=&#34;awselasticblockstore.md&#34;&gt;AwsElasticBlockStore&lt;/a&gt;</i>
    <a href="#azuredisk" title="AzureDisk">AzureDisk</a>: <i>
      - &lt;a href=&#34;azuredisk.md&#34;&gt;AzureDisk&lt;/a&gt;</i>
    <a href="#azurefile" title="AzureFile">AzureFile</a>: <i>
      - &lt;a href=&#34;azurefile.md&#34;&gt;AzureFile&lt;/a&gt;</i>
    <a href="#cephfs" title="CephFs">CephFs</a>: <i>
      - &lt;a href=&#34;cephfs.md&#34;&gt;CephFs&lt;/a&gt;</i>
    <a href="#cinder" title="Cinder">Cinder</a>: <i>
      - &lt;a href=&#34;cinder.md&#34;&gt;Cinder&lt;/a&gt;</i>
    <a href="#fc" title="Fc">Fc</a>: <i>
      - &lt;a href=&#34;fc.md&#34;&gt;Fc&lt;/a&gt;</i>
    <a href="#flexvolume" title="FlexVolume">FlexVolume</a>: <i>
      - &lt;a href=&#34;flexvolume.md&#34;&gt;FlexVolume&lt;/a&gt;</i>
    <a href="#flocker" title="Flocker">Flocker</a>: <i>
      - &lt;a href=&#34;flocker.md&#34;&gt;Flocker&lt;/a&gt;</i>
    <a href="#gcepersistentdisk" title="GcePersistentDisk">GcePersistentDisk</a>: <i>
      - &lt;a href=&#34;gcepersistentdisk.md&#34;&gt;GcePersistentDisk&lt;/a&gt;</i>
    <a href="#glusterfs" title="Glusterfs">Glusterfs</a>: <i>
      - &lt;a href=&#34;glusterfs.md&#34;&gt;Glusterfs&lt;/a&gt;</i>
    <a href="#hostpath" title="HostPath">HostPath</a>: <i>
      - &lt;a href=&#34;hostpath.md&#34;&gt;HostPath&lt;/a&gt;</i>
    <a href="#iscsi" title="Iscsi">Iscsi</a>: <i>
      - &lt;a href=&#34;iscsi.md&#34;&gt;Iscsi&lt;/a&gt;</i>
    <a href="#local" title="Local">Local</a>: <i>
      - &lt;a href=&#34;local.md&#34;&gt;Local&lt;/a&gt;</i>
    <a href="#nfs" title="Nfs">Nfs</a>: <i>
      - &lt;a href=&#34;nfs.md&#34;&gt;Nfs&lt;/a&gt;</i>
    <a href="#photonpersistentdisk" title="PhotonPersistentDisk">PhotonPersistentDisk</a>: <i>
      - &lt;a href=&#34;photonpersistentdisk.md&#34;&gt;PhotonPersistentDisk&lt;/a&gt;</i>
    <a href="#quobyte" title="Quobyte">Quobyte</a>: <i>
      - &lt;a href=&#34;quobyte.md&#34;&gt;Quobyte&lt;/a&gt;</i>
    <a href="#rbd" title="Rbd">Rbd</a>: <i>
      - &lt;a href=&#34;rbd.md&#34;&gt;Rbd&lt;/a&gt;</i>
    <a href="#vspherevolume" title="VsphereVolume">VsphereVolume</a>: <i>
      - &lt;a href=&#34;vspherevolume.md&#34;&gt;VsphereVolume&lt;/a&gt;</i>
    <a href="#nodeselectorterm" title="NodeSelectorTerm">NodeSelectorTerm</a>: <i>
      - &lt;a href=&#34;nodeselectorterm.md&#34;&gt;NodeSelectorTerm&lt;/a&gt;</i>
    <a href="#secretref" title="SecretRef">SecretRef</a>: <i>
      - &lt;a href=&#34;secretref.md&#34;&gt;SecretRef&lt;/a&gt;</i>
    <a href="#matchexpressions" title="MatchExpressions">MatchExpressions</a>: <i>
      - &lt;a href=&#34;matchexpressions.md&#34;&gt;MatchExpressions&lt;/a&gt;</i>
    <a href="#matchfields" title="MatchFields">MatchFields</a>: <i>
      - &lt;a href=&#34;matchfields.md&#34;&gt;MatchFields&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of &lt;a href=&#34;metadata.md&#34;&gt;Metadata&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Spec

_Required_: No

_Type_: List of &lt;a href=&#34;spec.md&#34;&gt;Spec&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeAffinity

_Required_: No

_Type_: List of &lt;a href=&#34;nodeaffinity.md&#34;&gt;NodeAffinity&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PersistentVolumeSource

_Required_: No

_Type_: List of &lt;a href=&#34;persistentvolumesource.md&#34;&gt;PersistentVolumeSource&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Required

_Required_: No

_Type_: List of &lt;a href=&#34;required.md&#34;&gt;Required&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsElasticBlockStore

_Required_: No

_Type_: List of &lt;a href=&#34;awselasticblockstore.md&#34;&gt;AwsElasticBlockStore&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureDisk

_Required_: No

_Type_: List of &lt;a href=&#34;azuredisk.md&#34;&gt;AzureDisk&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureFile

_Required_: No

_Type_: List of &lt;a href=&#34;azurefile.md&#34;&gt;AzureFile&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CephFs

_Required_: No

_Type_: List of &lt;a href=&#34;cephfs.md&#34;&gt;CephFs&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cinder

_Required_: No

_Type_: List of &lt;a href=&#34;cinder.md&#34;&gt;Cinder&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fc

_Required_: No

_Type_: List of &lt;a href=&#34;fc.md&#34;&gt;Fc&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlexVolume

_Required_: No

_Type_: List of &lt;a href=&#34;flexvolume.md&#34;&gt;FlexVolume&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Flocker

_Required_: No

_Type_: List of &lt;a href=&#34;flocker.md&#34;&gt;Flocker&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcePersistentDisk

_Required_: No

_Type_: List of &lt;a href=&#34;gcepersistentdisk.md&#34;&gt;GcePersistentDisk&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Glusterfs

_Required_: No

_Type_: List of &lt;a href=&#34;glusterfs.md&#34;&gt;Glusterfs&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostPath

_Required_: No

_Type_: List of &lt;a href=&#34;hostpath.md&#34;&gt;HostPath&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Iscsi

_Required_: No

_Type_: List of &lt;a href=&#34;iscsi.md&#34;&gt;Iscsi&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Local

_Required_: No

_Type_: List of &lt;a href=&#34;local.md&#34;&gt;Local&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nfs

_Required_: No

_Type_: List of &lt;a href=&#34;nfs.md&#34;&gt;Nfs&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PhotonPersistentDisk

_Required_: No

_Type_: List of &lt;a href=&#34;photonpersistentdisk.md&#34;&gt;PhotonPersistentDisk&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Quobyte

_Required_: No

_Type_: List of &lt;a href=&#34;quobyte.md&#34;&gt;Quobyte&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rbd

_Required_: No

_Type_: List of &lt;a href=&#34;rbd.md&#34;&gt;Rbd&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsphereVolume

_Required_: No

_Type_: List of &lt;a href=&#34;vspherevolume.md&#34;&gt;VsphereVolume&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeSelectorTerm

_Required_: No

_Type_: List of &lt;a href=&#34;nodeselectorterm.md&#34;&gt;NodeSelectorTerm&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretRef

_Required_: No

_Type_: List of &lt;a href=&#34;secretref.md&#34;&gt;SecretRef&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchExpressions

_Required_: No

_Type_: List of &lt;a href=&#34;matchexpressions.md&#34;&gt;MatchExpressions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchFields

_Required_: No

_Type_: List of &lt;a href=&#34;matchfields.md&#34;&gt;MatchFields&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

