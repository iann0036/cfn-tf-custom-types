# Terraform::Kubernetes::ReplicationController Volume

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#awselasticblockstore" title="AwsElasticBlockStore">AwsElasticBlockStore</a>" : <i>[ <a href="volume-awselasticblockstore.md">AwsElasticBlockStore</a>, ... ]</i>,
    "<a href="#azuredisk" title="AzureDisk">AzureDisk</a>" : <i>[ <a href="volume-azuredisk.md">AzureDisk</a>, ... ]</i>,
    "<a href="#azurefile" title="AzureFile">AzureFile</a>" : <i>[ <a href="volume-azurefile.md">AzureFile</a>, ... ]</i>,
    "<a href="#cephfs" title="CephFs">CephFs</a>" : <i>[ <a href="volume-cephfs.md">CephFs</a>, ... ]</i>,
    "<a href="#cinder" title="Cinder">Cinder</a>" : <i>[ <a href="volume-cinder.md">Cinder</a>, ... ]</i>,
    "<a href="#configmap" title="ConfigMap">ConfigMap</a>" : <i>[ <a href="volume-configmap.md">ConfigMap</a>, ... ]</i>,
    "<a href="#downwardapi" title="DownwardApi">DownwardApi</a>" : <i>[ <a href="volume-downwardapi.md">DownwardApi</a>, ... ]</i>,
    "<a href="#emptydir" title="EmptyDir">EmptyDir</a>" : <i>[ <a href="volume-emptydir.md">EmptyDir</a>, ... ]</i>,
    "<a href="#fc" title="Fc">Fc</a>" : <i>[ <a href="volume-fc.md">Fc</a>, ... ]</i>,
    "<a href="#flexvolume" title="FlexVolume">FlexVolume</a>" : <i>[ <a href="volume-flexvolume.md">FlexVolume</a>, ... ]</i>,
    "<a href="#flocker" title="Flocker">Flocker</a>" : <i>[ <a href="volume-flocker.md">Flocker</a>, ... ]</i>,
    "<a href="#gcepersistentdisk" title="GcePersistentDisk">GcePersistentDisk</a>" : <i>[ <a href="volume-gcepersistentdisk.md">GcePersistentDisk</a>, ... ]</i>,
    "<a href="#gitrepo" title="GitRepo">GitRepo</a>" : <i>[ <a href="volume-gitrepo.md">GitRepo</a>, ... ]</i>,
    "<a href="#glusterfs" title="Glusterfs">Glusterfs</a>" : <i>[ <a href="volume-glusterfs.md">Glusterfs</a>, ... ]</i>,
    "<a href="#hostpath" title="HostPath">HostPath</a>" : <i>[ <a href="volume-hostpath.md">HostPath</a>, ... ]</i>,
    "<a href="#iscsi" title="Iscsi">Iscsi</a>" : <i>[ <a href="volume-iscsi.md">Iscsi</a>, ... ]</i>,
    "<a href="#local" title="Local">Local</a>" : <i>[ <a href="volume-local.md">Local</a>, ... ]</i>,
    "<a href="#nfs" title="Nfs">Nfs</a>" : <i>[ <a href="volume-nfs.md">Nfs</a>, ... ]</i>,
    "<a href="#persistentvolumeclaim" title="PersistentVolumeClaim">PersistentVolumeClaim</a>" : <i>[ <a href="volume-persistentvolumeclaim.md">PersistentVolumeClaim</a>, ... ]</i>,
    "<a href="#photonpersistentdisk" title="PhotonPersistentDisk">PhotonPersistentDisk</a>" : <i>[ <a href="volume-photonpersistentdisk.md">PhotonPersistentDisk</a>, ... ]</i>,
    "<a href="#quobyte" title="Quobyte">Quobyte</a>" : <i>[ <a href="volume-quobyte.md">Quobyte</a>, ... ]</i>,
    "<a href="#rbd" title="Rbd">Rbd</a>" : <i>[ <a href="volume-rbd.md">Rbd</a>, ... ]</i>,
    "<a href="#secret" title="Secret">Secret</a>" : <i>[ <a href="volume-secret.md">Secret</a>, ... ]</i>,
    "<a href="#vspherevolume" title="VsphereVolume">VsphereVolume</a>" : <i>[ <a href="volume-vspherevolume.md">VsphereVolume</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#awselasticblockstore" title="AwsElasticBlockStore">AwsElasticBlockStore</a>: <i>
      - <a href="volume-awselasticblockstore.md">AwsElasticBlockStore</a></i>
<a href="#azuredisk" title="AzureDisk">AzureDisk</a>: <i>
      - <a href="volume-azuredisk.md">AzureDisk</a></i>
<a href="#azurefile" title="AzureFile">AzureFile</a>: <i>
      - <a href="volume-azurefile.md">AzureFile</a></i>
<a href="#cephfs" title="CephFs">CephFs</a>: <i>
      - <a href="volume-cephfs.md">CephFs</a></i>
<a href="#cinder" title="Cinder">Cinder</a>: <i>
      - <a href="volume-cinder.md">Cinder</a></i>
<a href="#configmap" title="ConfigMap">ConfigMap</a>: <i>
      - <a href="volume-configmap.md">ConfigMap</a></i>
<a href="#downwardapi" title="DownwardApi">DownwardApi</a>: <i>
      - <a href="volume-downwardapi.md">DownwardApi</a></i>
<a href="#emptydir" title="EmptyDir">EmptyDir</a>: <i>
      - <a href="volume-emptydir.md">EmptyDir</a></i>
<a href="#fc" title="Fc">Fc</a>: <i>
      - <a href="volume-fc.md">Fc</a></i>
<a href="#flexvolume" title="FlexVolume">FlexVolume</a>: <i>
      - <a href="volume-flexvolume.md">FlexVolume</a></i>
<a href="#flocker" title="Flocker">Flocker</a>: <i>
      - <a href="volume-flocker.md">Flocker</a></i>
<a href="#gcepersistentdisk" title="GcePersistentDisk">GcePersistentDisk</a>: <i>
      - <a href="volume-gcepersistentdisk.md">GcePersistentDisk</a></i>
<a href="#gitrepo" title="GitRepo">GitRepo</a>: <i>
      - <a href="volume-gitrepo.md">GitRepo</a></i>
<a href="#glusterfs" title="Glusterfs">Glusterfs</a>: <i>
      - <a href="volume-glusterfs.md">Glusterfs</a></i>
<a href="#hostpath" title="HostPath">HostPath</a>: <i>
      - <a href="volume-hostpath.md">HostPath</a></i>
<a href="#iscsi" title="Iscsi">Iscsi</a>: <i>
      - <a href="volume-iscsi.md">Iscsi</a></i>
<a href="#local" title="Local">Local</a>: <i>
      - <a href="volume-local.md">Local</a></i>
<a href="#nfs" title="Nfs">Nfs</a>: <i>
      - <a href="volume-nfs.md">Nfs</a></i>
<a href="#persistentvolumeclaim" title="PersistentVolumeClaim">PersistentVolumeClaim</a>: <i>
      - <a href="volume-persistentvolumeclaim.md">PersistentVolumeClaim</a></i>
<a href="#photonpersistentdisk" title="PhotonPersistentDisk">PhotonPersistentDisk</a>: <i>
      - <a href="volume-photonpersistentdisk.md">PhotonPersistentDisk</a></i>
<a href="#quobyte" title="Quobyte">Quobyte</a>: <i>
      - <a href="volume-quobyte.md">Quobyte</a></i>
<a href="#rbd" title="Rbd">Rbd</a>: <i>
      - <a href="volume-rbd.md">Rbd</a></i>
<a href="#secret" title="Secret">Secret</a>: <i>
      - <a href="volume-secret.md">Secret</a></i>
<a href="#vspherevolume" title="VsphereVolume">VsphereVolume</a>: <i>
      - <a href="volume-vspherevolume.md">VsphereVolume</a></i>
</pre>

## Properties

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsElasticBlockStore

_Required_: No

_Type_: List of <a href="volume-awselasticblockstore.md">AwsElasticBlockStore</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureDisk

_Required_: No

_Type_: List of <a href="volume-azuredisk.md">AzureDisk</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureFile

_Required_: No

_Type_: List of <a href="volume-azurefile.md">AzureFile</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CephFs

_Required_: No

_Type_: List of <a href="volume-cephfs.md">CephFs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cinder

_Required_: No

_Type_: List of <a href="volume-cinder.md">Cinder</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigMap

_Required_: No

_Type_: List of <a href="volume-configmap.md">ConfigMap</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DownwardApi

_Required_: No

_Type_: List of <a href="volume-downwardapi.md">DownwardApi</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmptyDir

_Required_: No

_Type_: List of <a href="volume-emptydir.md">EmptyDir</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fc

_Required_: No

_Type_: List of <a href="volume-fc.md">Fc</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlexVolume

_Required_: No

_Type_: List of <a href="volume-flexvolume.md">FlexVolume</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Flocker

_Required_: No

_Type_: List of <a href="volume-flocker.md">Flocker</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcePersistentDisk

_Required_: No

_Type_: List of <a href="volume-gcepersistentdisk.md">GcePersistentDisk</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GitRepo

_Required_: No

_Type_: List of <a href="volume-gitrepo.md">GitRepo</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Glusterfs

_Required_: No

_Type_: List of <a href="volume-glusterfs.md">Glusterfs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostPath

_Required_: No

_Type_: List of <a href="volume-hostpath.md">HostPath</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Iscsi

_Required_: No

_Type_: List of <a href="volume-iscsi.md">Iscsi</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Local

_Required_: No

_Type_: List of <a href="volume-local.md">Local</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nfs

_Required_: No

_Type_: List of <a href="volume-nfs.md">Nfs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PersistentVolumeClaim

_Required_: No

_Type_: List of <a href="volume-persistentvolumeclaim.md">PersistentVolumeClaim</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PhotonPersistentDisk

_Required_: No

_Type_: List of <a href="volume-photonpersistentdisk.md">PhotonPersistentDisk</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Quobyte

_Required_: No

_Type_: List of <a href="volume-quobyte.md">Quobyte</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rbd

_Required_: No

_Type_: List of <a href="volume-rbd.md">Rbd</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Secret

_Required_: No

_Type_: List of <a href="volume-secret.md">Secret</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsphereVolume

_Required_: No

_Type_: List of <a href="volume-vspherevolume.md">VsphereVolume</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

