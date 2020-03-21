# Terraform::Kubernetes::PersistentVolume PersistentVolumeSource

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#awselasticblockstore" title="AwsElasticBlockStore">AwsElasticBlockStore</a>" : <i>[ &lt;a href=&#34;persistentvolumesource-awselasticblockstore.md&#34;&gt;AwsElasticBlockStore&lt;/a&gt;, ... ]</i>,
    "<a href="#azuredisk" title="AzureDisk">AzureDisk</a>" : <i>[ &lt;a href=&#34;persistentvolumesource-azuredisk.md&#34;&gt;AzureDisk&lt;/a&gt;, ... ]</i>,
    "<a href="#azurefile" title="AzureFile">AzureFile</a>" : <i>[ &lt;a href=&#34;persistentvolumesource-azurefile.md&#34;&gt;AzureFile&lt;/a&gt;, ... ]</i>,
    "<a href="#cephfs" title="CephFs">CephFs</a>" : <i>[ &lt;a href=&#34;persistentvolumesource-cephfs.md&#34;&gt;CephFs&lt;/a&gt;, ... ]</i>,
    "<a href="#cinder" title="Cinder">Cinder</a>" : <i>[ &lt;a href=&#34;persistentvolumesource-cinder.md&#34;&gt;Cinder&lt;/a&gt;, ... ]</i>,
    "<a href="#fc" title="Fc">Fc</a>" : <i>[ &lt;a href=&#34;persistentvolumesource-fc.md&#34;&gt;Fc&lt;/a&gt;, ... ]</i>,
    "<a href="#flexvolume" title="FlexVolume">FlexVolume</a>" : <i>[ &lt;a href=&#34;persistentvolumesource-flexvolume.md&#34;&gt;FlexVolume&lt;/a&gt;, ... ]</i>,
    "<a href="#flocker" title="Flocker">Flocker</a>" : <i>[ &lt;a href=&#34;persistentvolumesource-flocker.md&#34;&gt;Flocker&lt;/a&gt;, ... ]</i>,
    "<a href="#gcepersistentdisk" title="GcePersistentDisk">GcePersistentDisk</a>" : <i>[ &lt;a href=&#34;persistentvolumesource-gcepersistentdisk.md&#34;&gt;GcePersistentDisk&lt;/a&gt;, ... ]</i>,
    "<a href="#glusterfs" title="Glusterfs">Glusterfs</a>" : <i>[ &lt;a href=&#34;persistentvolumesource-glusterfs.md&#34;&gt;Glusterfs&lt;/a&gt;, ... ]</i>,
    "<a href="#hostpath" title="HostPath">HostPath</a>" : <i>[ &lt;a href=&#34;persistentvolumesource-hostpath.md&#34;&gt;HostPath&lt;/a&gt;, ... ]</i>,
    "<a href="#iscsi" title="Iscsi">Iscsi</a>" : <i>[ &lt;a href=&#34;persistentvolumesource-iscsi.md&#34;&gt;Iscsi&lt;/a&gt;, ... ]</i>,
    "<a href="#local" title="Local">Local</a>" : <i>[ &lt;a href=&#34;persistentvolumesource-local.md&#34;&gt;Local&lt;/a&gt;, ... ]</i>,
    "<a href="#nfs" title="Nfs">Nfs</a>" : <i>[ &lt;a href=&#34;persistentvolumesource-nfs.md&#34;&gt;Nfs&lt;/a&gt;, ... ]</i>,
    "<a href="#photonpersistentdisk" title="PhotonPersistentDisk">PhotonPersistentDisk</a>" : <i>[ &lt;a href=&#34;persistentvolumesource-photonpersistentdisk.md&#34;&gt;PhotonPersistentDisk&lt;/a&gt;, ... ]</i>,
    "<a href="#quobyte" title="Quobyte">Quobyte</a>" : <i>[ &lt;a href=&#34;persistentvolumesource-quobyte.md&#34;&gt;Quobyte&lt;/a&gt;, ... ]</i>,
    "<a href="#rbd" title="Rbd">Rbd</a>" : <i>[ &lt;a href=&#34;persistentvolumesource-rbd.md&#34;&gt;Rbd&lt;/a&gt;, ... ]</i>,
    "<a href="#vspherevolume" title="VsphereVolume">VsphereVolume</a>" : <i>[ &lt;a href=&#34;persistentvolumesource-vspherevolume.md&#34;&gt;VsphereVolume&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#awselasticblockstore" title="AwsElasticBlockStore">AwsElasticBlockStore</a>: <i>
      - &lt;a href=&#34;persistentvolumesource-awselasticblockstore.md&#34;&gt;AwsElasticBlockStore&lt;/a&gt;</i>
<a href="#azuredisk" title="AzureDisk">AzureDisk</a>: <i>
      - &lt;a href=&#34;persistentvolumesource-azuredisk.md&#34;&gt;AzureDisk&lt;/a&gt;</i>
<a href="#azurefile" title="AzureFile">AzureFile</a>: <i>
      - &lt;a href=&#34;persistentvolumesource-azurefile.md&#34;&gt;AzureFile&lt;/a&gt;</i>
<a href="#cephfs" title="CephFs">CephFs</a>: <i>
      - &lt;a href=&#34;persistentvolumesource-cephfs.md&#34;&gt;CephFs&lt;/a&gt;</i>
<a href="#cinder" title="Cinder">Cinder</a>: <i>
      - &lt;a href=&#34;persistentvolumesource-cinder.md&#34;&gt;Cinder&lt;/a&gt;</i>
<a href="#fc" title="Fc">Fc</a>: <i>
      - &lt;a href=&#34;persistentvolumesource-fc.md&#34;&gt;Fc&lt;/a&gt;</i>
<a href="#flexvolume" title="FlexVolume">FlexVolume</a>: <i>
      - &lt;a href=&#34;persistentvolumesource-flexvolume.md&#34;&gt;FlexVolume&lt;/a&gt;</i>
<a href="#flocker" title="Flocker">Flocker</a>: <i>
      - &lt;a href=&#34;persistentvolumesource-flocker.md&#34;&gt;Flocker&lt;/a&gt;</i>
<a href="#gcepersistentdisk" title="GcePersistentDisk">GcePersistentDisk</a>: <i>
      - &lt;a href=&#34;persistentvolumesource-gcepersistentdisk.md&#34;&gt;GcePersistentDisk&lt;/a&gt;</i>
<a href="#glusterfs" title="Glusterfs">Glusterfs</a>: <i>
      - &lt;a href=&#34;persistentvolumesource-glusterfs.md&#34;&gt;Glusterfs&lt;/a&gt;</i>
<a href="#hostpath" title="HostPath">HostPath</a>: <i>
      - &lt;a href=&#34;persistentvolumesource-hostpath.md&#34;&gt;HostPath&lt;/a&gt;</i>
<a href="#iscsi" title="Iscsi">Iscsi</a>: <i>
      - &lt;a href=&#34;persistentvolumesource-iscsi.md&#34;&gt;Iscsi&lt;/a&gt;</i>
<a href="#local" title="Local">Local</a>: <i>
      - &lt;a href=&#34;persistentvolumesource-local.md&#34;&gt;Local&lt;/a&gt;</i>
<a href="#nfs" title="Nfs">Nfs</a>: <i>
      - &lt;a href=&#34;persistentvolumesource-nfs.md&#34;&gt;Nfs&lt;/a&gt;</i>
<a href="#photonpersistentdisk" title="PhotonPersistentDisk">PhotonPersistentDisk</a>: <i>
      - &lt;a href=&#34;persistentvolumesource-photonpersistentdisk.md&#34;&gt;PhotonPersistentDisk&lt;/a&gt;</i>
<a href="#quobyte" title="Quobyte">Quobyte</a>: <i>
      - &lt;a href=&#34;persistentvolumesource-quobyte.md&#34;&gt;Quobyte&lt;/a&gt;</i>
<a href="#rbd" title="Rbd">Rbd</a>: <i>
      - &lt;a href=&#34;persistentvolumesource-rbd.md&#34;&gt;Rbd&lt;/a&gt;</i>
<a href="#vspherevolume" title="VsphereVolume">VsphereVolume</a>: <i>
      - &lt;a href=&#34;persistentvolumesource-vspherevolume.md&#34;&gt;VsphereVolume&lt;/a&gt;</i>
</pre>

## Properties

#### AwsElasticBlockStore

_Required_: No
_Type_: List of &lt;a href=&#34;persistentvolumesource-awselasticblockstore.md&#34;&gt;AwsElasticBlockStore&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureDisk

_Required_: No
_Type_: List of &lt;a href=&#34;persistentvolumesource-azuredisk.md&#34;&gt;AzureDisk&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureFile

_Required_: No
_Type_: List of &lt;a href=&#34;persistentvolumesource-azurefile.md&#34;&gt;AzureFile&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CephFs

_Required_: No
_Type_: List of &lt;a href=&#34;persistentvolumesource-cephfs.md&#34;&gt;CephFs&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cinder

_Required_: No
_Type_: List of &lt;a href=&#34;persistentvolumesource-cinder.md&#34;&gt;Cinder&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fc

_Required_: No
_Type_: List of &lt;a href=&#34;persistentvolumesource-fc.md&#34;&gt;Fc&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlexVolume

_Required_: No
_Type_: List of &lt;a href=&#34;persistentvolumesource-flexvolume.md&#34;&gt;FlexVolume&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Flocker

_Required_: No
_Type_: List of &lt;a href=&#34;persistentvolumesource-flocker.md&#34;&gt;Flocker&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcePersistentDisk

_Required_: No
_Type_: List of &lt;a href=&#34;persistentvolumesource-gcepersistentdisk.md&#34;&gt;GcePersistentDisk&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Glusterfs

_Required_: No
_Type_: List of &lt;a href=&#34;persistentvolumesource-glusterfs.md&#34;&gt;Glusterfs&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostPath

_Required_: No
_Type_: List of &lt;a href=&#34;persistentvolumesource-hostpath.md&#34;&gt;HostPath&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Iscsi

_Required_: No
_Type_: List of &lt;a href=&#34;persistentvolumesource-iscsi.md&#34;&gt;Iscsi&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Local

_Required_: No
_Type_: List of &lt;a href=&#34;persistentvolumesource-local.md&#34;&gt;Local&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nfs

_Required_: No
_Type_: List of &lt;a href=&#34;persistentvolumesource-nfs.md&#34;&gt;Nfs&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PhotonPersistentDisk

_Required_: No
_Type_: List of &lt;a href=&#34;persistentvolumesource-photonpersistentdisk.md&#34;&gt;PhotonPersistentDisk&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Quobyte

_Required_: No
_Type_: List of &lt;a href=&#34;persistentvolumesource-quobyte.md&#34;&gt;Quobyte&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rbd

_Required_: No
_Type_: List of &lt;a href=&#34;persistentvolumesource-rbd.md&#34;&gt;Rbd&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsphereVolume

_Required_: No
_Type_: List of &lt;a href=&#34;persistentvolumesource-vspherevolume.md&#34;&gt;VsphereVolume&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

