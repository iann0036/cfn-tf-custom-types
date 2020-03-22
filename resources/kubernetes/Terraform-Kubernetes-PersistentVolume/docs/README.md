# Terraform::Kubernetes::PersistentVolume

The resource provides a piece of networked storage in the cluster provisioned by an administrator. It is a resource in the cluster just like a node is a cluster resource. Persistent Volumes have a lifecycle independent of any individual pod that uses the PV.

For more info see [Kubernetes reference](https://kubernetes.io/docs/concepts/storage/persistent-volumes)/

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Kubernetes::PersistentVolume",
    "Properties" : {
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadata.md">Metadata</a>, ... ]</i>,
        "<a href="#spec" title="Spec">Spec</a>" : <i>[ <a href="spec.md">Spec</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#nodeaffinity" title="NodeAffinity">NodeAffinity</a>" : <i>[ <a href="nodeaffinity.md">NodeAffinity</a>, ... ]</i>,
        "<a href="#persistentvolumesource" title="PersistentVolumeSource">PersistentVolumeSource</a>" : <i>[ <a href="persistentvolumesource.md">PersistentVolumeSource</a>, ... ]</i>,
        "<a href="#required" title="Required">Required</a>" : <i>[ <a href="required.md">Required</a>, ... ]</i>,
        "<a href="#awselasticblockstore" title="AwsElasticBlockStore">AwsElasticBlockStore</a>" : <i>[ <a href="awselasticblockstore.md">AwsElasticBlockStore</a>, ... ]</i>,
        "<a href="#azuredisk" title="AzureDisk">AzureDisk</a>" : <i>[ <a href="azuredisk.md">AzureDisk</a>, ... ]</i>,
        "<a href="#azurefile" title="AzureFile">AzureFile</a>" : <i>[ <a href="azurefile.md">AzureFile</a>, ... ]</i>,
        "<a href="#cephfs" title="CephFs">CephFs</a>" : <i>[ <a href="cephfs.md">CephFs</a>, ... ]</i>,
        "<a href="#cinder" title="Cinder">Cinder</a>" : <i>[ <a href="cinder.md">Cinder</a>, ... ]</i>,
        "<a href="#fc" title="Fc">Fc</a>" : <i>[ <a href="fc.md">Fc</a>, ... ]</i>,
        "<a href="#flexvolume" title="FlexVolume">FlexVolume</a>" : <i>[ <a href="flexvolume.md">FlexVolume</a>, ... ]</i>,
        "<a href="#flocker" title="Flocker">Flocker</a>" : <i>[ <a href="flocker.md">Flocker</a>, ... ]</i>,
        "<a href="#gcepersistentdisk" title="GcePersistentDisk">GcePersistentDisk</a>" : <i>[ <a href="gcepersistentdisk.md">GcePersistentDisk</a>, ... ]</i>,
        "<a href="#glusterfs" title="Glusterfs">Glusterfs</a>" : <i>[ <a href="glusterfs.md">Glusterfs</a>, ... ]</i>,
        "<a href="#hostpath" title="HostPath">HostPath</a>" : <i>[ <a href="hostpath.md">HostPath</a>, ... ]</i>,
        "<a href="#iscsi" title="Iscsi">Iscsi</a>" : <i>[ <a href="iscsi.md">Iscsi</a>, ... ]</i>,
        "<a href="#local" title="Local">Local</a>" : <i>[ <a href="local.md">Local</a>, ... ]</i>,
        "<a href="#nfs" title="Nfs">Nfs</a>" : <i>[ <a href="nfs.md">Nfs</a>, ... ]</i>,
        "<a href="#photonpersistentdisk" title="PhotonPersistentDisk">PhotonPersistentDisk</a>" : <i>[ <a href="photonpersistentdisk.md">PhotonPersistentDisk</a>, ... ]</i>,
        "<a href="#quobyte" title="Quobyte">Quobyte</a>" : <i>[ <a href="quobyte.md">Quobyte</a>, ... ]</i>,
        "<a href="#rbd" title="Rbd">Rbd</a>" : <i>[ <a href="rbd.md">Rbd</a>, ... ]</i>,
        "<a href="#vspherevolume" title="VsphereVolume">VsphereVolume</a>" : <i>[ <a href="vspherevolume.md">VsphereVolume</a>, ... ]</i>,
        "<a href="#nodeselectorterm" title="NodeSelectorTerm">NodeSelectorTerm</a>" : <i>[ <a href="nodeselectorterm.md">NodeSelectorTerm</a>, ... ]</i>,
        "<a href="#secretref" title="SecretRef">SecretRef</a>" : <i>[ <a href="secretref.md">SecretRef</a>, ... ]</i>,
        "<a href="#matchexpressions" title="MatchExpressions">MatchExpressions</a>" : <i>[ <a href="matchexpressions.md">MatchExpressions</a>, ... ]</i>,
        "<a href="#matchfields" title="MatchFields">MatchFields</a>" : <i>[ <a href="matchfields.md">MatchFields</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Kubernetes::PersistentVolume
Properties:
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadata.md">Metadata</a></i>
    <a href="#spec" title="Spec">Spec</a>: <i>
      - <a href="spec.md">Spec</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#nodeaffinity" title="NodeAffinity">NodeAffinity</a>: <i>
      - <a href="nodeaffinity.md">NodeAffinity</a></i>
    <a href="#persistentvolumesource" title="PersistentVolumeSource">PersistentVolumeSource</a>: <i>
      - <a href="persistentvolumesource.md">PersistentVolumeSource</a></i>
    <a href="#required" title="Required">Required</a>: <i>
      - <a href="required.md">Required</a></i>
    <a href="#awselasticblockstore" title="AwsElasticBlockStore">AwsElasticBlockStore</a>: <i>
      - <a href="awselasticblockstore.md">AwsElasticBlockStore</a></i>
    <a href="#azuredisk" title="AzureDisk">AzureDisk</a>: <i>
      - <a href="azuredisk.md">AzureDisk</a></i>
    <a href="#azurefile" title="AzureFile">AzureFile</a>: <i>
      - <a href="azurefile.md">AzureFile</a></i>
    <a href="#cephfs" title="CephFs">CephFs</a>: <i>
      - <a href="cephfs.md">CephFs</a></i>
    <a href="#cinder" title="Cinder">Cinder</a>: <i>
      - <a href="cinder.md">Cinder</a></i>
    <a href="#fc" title="Fc">Fc</a>: <i>
      - <a href="fc.md">Fc</a></i>
    <a href="#flexvolume" title="FlexVolume">FlexVolume</a>: <i>
      - <a href="flexvolume.md">FlexVolume</a></i>
    <a href="#flocker" title="Flocker">Flocker</a>: <i>
      - <a href="flocker.md">Flocker</a></i>
    <a href="#gcepersistentdisk" title="GcePersistentDisk">GcePersistentDisk</a>: <i>
      - <a href="gcepersistentdisk.md">GcePersistentDisk</a></i>
    <a href="#glusterfs" title="Glusterfs">Glusterfs</a>: <i>
      - <a href="glusterfs.md">Glusterfs</a></i>
    <a href="#hostpath" title="HostPath">HostPath</a>: <i>
      - <a href="hostpath.md">HostPath</a></i>
    <a href="#iscsi" title="Iscsi">Iscsi</a>: <i>
      - <a href="iscsi.md">Iscsi</a></i>
    <a href="#local" title="Local">Local</a>: <i>
      - <a href="local.md">Local</a></i>
    <a href="#nfs" title="Nfs">Nfs</a>: <i>
      - <a href="nfs.md">Nfs</a></i>
    <a href="#photonpersistentdisk" title="PhotonPersistentDisk">PhotonPersistentDisk</a>: <i>
      - <a href="photonpersistentdisk.md">PhotonPersistentDisk</a></i>
    <a href="#quobyte" title="Quobyte">Quobyte</a>: <i>
      - <a href="quobyte.md">Quobyte</a></i>
    <a href="#rbd" title="Rbd">Rbd</a>: <i>
      - <a href="rbd.md">Rbd</a></i>
    <a href="#vspherevolume" title="VsphereVolume">VsphereVolume</a>: <i>
      - <a href="vspherevolume.md">VsphereVolume</a></i>
    <a href="#nodeselectorterm" title="NodeSelectorTerm">NodeSelectorTerm</a>: <i>
      - <a href="nodeselectorterm.md">NodeSelectorTerm</a></i>
    <a href="#secretref" title="SecretRef">SecretRef</a>: <i>
      - <a href="secretref.md">SecretRef</a></i>
    <a href="#matchexpressions" title="MatchExpressions">MatchExpressions</a>: <i>
      - <a href="matchexpressions.md">MatchExpressions</a></i>
    <a href="#matchfields" title="MatchFields">MatchFields</a>: <i>
      - <a href="matchfields.md">MatchFields</a></i>
</pre>

## Properties

#### Metadata

_Required_: No

_Type_: List of <a href="metadata.md">Metadata</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Spec

_Required_: No

_Type_: List of <a href="spec.md">Spec</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeAffinity

_Required_: No

_Type_: List of <a href="nodeaffinity.md">NodeAffinity</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PersistentVolumeSource

_Required_: No

_Type_: List of <a href="persistentvolumesource.md">PersistentVolumeSource</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Required

_Required_: No

_Type_: List of <a href="required.md">Required</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsElasticBlockStore

_Required_: No

_Type_: List of <a href="awselasticblockstore.md">AwsElasticBlockStore</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureDisk

_Required_: No

_Type_: List of <a href="azuredisk.md">AzureDisk</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureFile

_Required_: No

_Type_: List of <a href="azurefile.md">AzureFile</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CephFs

_Required_: No

_Type_: List of <a href="cephfs.md">CephFs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cinder

_Required_: No

_Type_: List of <a href="cinder.md">Cinder</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fc

_Required_: No

_Type_: List of <a href="fc.md">Fc</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlexVolume

_Required_: No

_Type_: List of <a href="flexvolume.md">FlexVolume</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Flocker

_Required_: No

_Type_: List of <a href="flocker.md">Flocker</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcePersistentDisk

_Required_: No

_Type_: List of <a href="gcepersistentdisk.md">GcePersistentDisk</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Glusterfs

_Required_: No

_Type_: List of <a href="glusterfs.md">Glusterfs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostPath

_Required_: No

_Type_: List of <a href="hostpath.md">HostPath</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Iscsi

_Required_: No

_Type_: List of <a href="iscsi.md">Iscsi</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Local

_Required_: No

_Type_: List of <a href="local.md">Local</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nfs

_Required_: No

_Type_: List of <a href="nfs.md">Nfs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PhotonPersistentDisk

_Required_: No

_Type_: List of <a href="photonpersistentdisk.md">PhotonPersistentDisk</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Quobyte

_Required_: No

_Type_: List of <a href="quobyte.md">Quobyte</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rbd

_Required_: No

_Type_: List of <a href="rbd.md">Rbd</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsphereVolume

_Required_: No

_Type_: List of <a href="vspherevolume.md">VsphereVolume</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeSelectorTerm

_Required_: No

_Type_: List of <a href="nodeselectorterm.md">NodeSelectorTerm</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretRef

_Required_: No

_Type_: List of <a href="secretref.md">SecretRef</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchExpressions

_Required_: No

_Type_: List of <a href="matchexpressions.md">MatchExpressions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchFields

_Required_: No

_Type_: List of <a href="matchfields.md">MatchFields</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

