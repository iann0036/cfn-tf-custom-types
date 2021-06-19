# TF::Kubernetes::Deployment VolumeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#awselasticblockstore" title="AwsElasticBlockStore">AwsElasticBlockStore</a>" : <i>[ <a href="awselasticblockstoredefinition.md">AwsElasticBlockStoreDefinition</a>, ... ]</i>,
    "<a href="#azuredisk" title="AzureDisk">AzureDisk</a>" : <i>[ <a href="azurediskdefinition.md">AzureDiskDefinition</a>, ... ]</i>,
    "<a href="#azurefile" title="AzureFile">AzureFile</a>" : <i>[ <a href="azurefiledefinition.md">AzureFileDefinition</a>, ... ]</i>,
    "<a href="#cephfs" title="CephFs">CephFs</a>" : <i>[ <a href="cephfsdefinition.md">CephFsDefinition</a>, ... ]</i>,
    "<a href="#cinder" title="Cinder">Cinder</a>" : <i>[ <a href="cinderdefinition.md">CinderDefinition</a>, ... ]</i>,
    "<a href="#configmap" title="ConfigMap">ConfigMap</a>" : <i>[ <a href="configmapdefinition.md">ConfigMapDefinition</a>, ... ]</i>,
    "<a href="#csi" title="Csi">Csi</a>" : <i>[ <a href="csidefinition.md">CsiDefinition</a>, ... ]</i>,
    "<a href="#downwardapi" title="DownwardApi">DownwardApi</a>" : <i>[ <a href="downwardapidefinition.md">DownwardApiDefinition</a>, ... ]</i>,
    "<a href="#emptydir" title="EmptyDir">EmptyDir</a>" : <i>[ <a href="emptydirdefinition.md">EmptyDirDefinition</a>, ... ]</i>,
    "<a href="#fc" title="Fc">Fc</a>" : <i>[ <a href="fcdefinition.md">FcDefinition</a>, ... ]</i>,
    "<a href="#flexvolume" title="FlexVolume">FlexVolume</a>" : <i>[ <a href="flexvolumedefinition.md">FlexVolumeDefinition</a>, ... ]</i>,
    "<a href="#flocker" title="Flocker">Flocker</a>" : <i>[ <a href="flockerdefinition.md">FlockerDefinition</a>, ... ]</i>,
    "<a href="#gcepersistentdisk" title="GcePersistentDisk">GcePersistentDisk</a>" : <i>[ <a href="gcepersistentdiskdefinition.md">GcePersistentDiskDefinition</a>, ... ]</i>,
    "<a href="#gitrepo" title="GitRepo">GitRepo</a>" : <i>[ <a href="gitrepodefinition.md">GitRepoDefinition</a>, ... ]</i>,
    "<a href="#glusterfs" title="Glusterfs">Glusterfs</a>" : <i>[ <a href="glusterfsdefinition.md">GlusterfsDefinition</a>, ... ]</i>,
    "<a href="#hostpath" title="HostPath">HostPath</a>" : <i>[ <a href="hostpathdefinition.md">HostPathDefinition</a>, ... ]</i>,
    "<a href="#iscsi" title="Iscsi">Iscsi</a>" : <i>[ <a href="iscsidefinition.md">IscsiDefinition</a>, ... ]</i>,
    "<a href="#local" title="Local">Local</a>" : <i>[ <a href="localdefinition.md">LocalDefinition</a>, ... ]</i>,
    "<a href="#nfs" title="Nfs">Nfs</a>" : <i>[ <a href="nfsdefinition.md">NfsDefinition</a>, ... ]</i>,
    "<a href="#persistentvolumeclaim" title="PersistentVolumeClaim">PersistentVolumeClaim</a>" : <i>[ <a href="persistentvolumeclaimdefinition.md">PersistentVolumeClaimDefinition</a>, ... ]</i>,
    "<a href="#photonpersistentdisk" title="PhotonPersistentDisk">PhotonPersistentDisk</a>" : <i>[ <a href="photonpersistentdiskdefinition.md">PhotonPersistentDiskDefinition</a>, ... ]</i>,
    "<a href="#projected" title="Projected">Projected</a>" : <i>[ <a href="projecteddefinition.md">ProjectedDefinition</a>, ... ]</i>,
    "<a href="#quobyte" title="Quobyte">Quobyte</a>" : <i>[ <a href="quobytedefinition.md">QuobyteDefinition</a>, ... ]</i>,
    "<a href="#rbd" title="Rbd">Rbd</a>" : <i>[ <a href="rbddefinition.md">RbdDefinition</a>, ... ]</i>,
    "<a href="#secret" title="Secret">Secret</a>" : <i>[ <a href="secretdefinition.md">SecretDefinition</a>, ... ]</i>,
    "<a href="#vspherevolume" title="VsphereVolume">VsphereVolume</a>" : <i>[ <a href="vspherevolumedefinition.md">VsphereVolumeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#awselasticblockstore" title="AwsElasticBlockStore">AwsElasticBlockStore</a>: <i>
      - <a href="awselasticblockstoredefinition.md">AwsElasticBlockStoreDefinition</a></i>
<a href="#azuredisk" title="AzureDisk">AzureDisk</a>: <i>
      - <a href="azurediskdefinition.md">AzureDiskDefinition</a></i>
<a href="#azurefile" title="AzureFile">AzureFile</a>: <i>
      - <a href="azurefiledefinition.md">AzureFileDefinition</a></i>
<a href="#cephfs" title="CephFs">CephFs</a>: <i>
      - <a href="cephfsdefinition.md">CephFsDefinition</a></i>
<a href="#cinder" title="Cinder">Cinder</a>: <i>
      - <a href="cinderdefinition.md">CinderDefinition</a></i>
<a href="#configmap" title="ConfigMap">ConfigMap</a>: <i>
      - <a href="configmapdefinition.md">ConfigMapDefinition</a></i>
<a href="#csi" title="Csi">Csi</a>: <i>
      - <a href="csidefinition.md">CsiDefinition</a></i>
<a href="#downwardapi" title="DownwardApi">DownwardApi</a>: <i>
      - <a href="downwardapidefinition.md">DownwardApiDefinition</a></i>
<a href="#emptydir" title="EmptyDir">EmptyDir</a>: <i>
      - <a href="emptydirdefinition.md">EmptyDirDefinition</a></i>
<a href="#fc" title="Fc">Fc</a>: <i>
      - <a href="fcdefinition.md">FcDefinition</a></i>
<a href="#flexvolume" title="FlexVolume">FlexVolume</a>: <i>
      - <a href="flexvolumedefinition.md">FlexVolumeDefinition</a></i>
<a href="#flocker" title="Flocker">Flocker</a>: <i>
      - <a href="flockerdefinition.md">FlockerDefinition</a></i>
<a href="#gcepersistentdisk" title="GcePersistentDisk">GcePersistentDisk</a>: <i>
      - <a href="gcepersistentdiskdefinition.md">GcePersistentDiskDefinition</a></i>
<a href="#gitrepo" title="GitRepo">GitRepo</a>: <i>
      - <a href="gitrepodefinition.md">GitRepoDefinition</a></i>
<a href="#glusterfs" title="Glusterfs">Glusterfs</a>: <i>
      - <a href="glusterfsdefinition.md">GlusterfsDefinition</a></i>
<a href="#hostpath" title="HostPath">HostPath</a>: <i>
      - <a href="hostpathdefinition.md">HostPathDefinition</a></i>
<a href="#iscsi" title="Iscsi">Iscsi</a>: <i>
      - <a href="iscsidefinition.md">IscsiDefinition</a></i>
<a href="#local" title="Local">Local</a>: <i>
      - <a href="localdefinition.md">LocalDefinition</a></i>
<a href="#nfs" title="Nfs">Nfs</a>: <i>
      - <a href="nfsdefinition.md">NfsDefinition</a></i>
<a href="#persistentvolumeclaim" title="PersistentVolumeClaim">PersistentVolumeClaim</a>: <i>
      - <a href="persistentvolumeclaimdefinition.md">PersistentVolumeClaimDefinition</a></i>
<a href="#photonpersistentdisk" title="PhotonPersistentDisk">PhotonPersistentDisk</a>: <i>
      - <a href="photonpersistentdiskdefinition.md">PhotonPersistentDiskDefinition</a></i>
<a href="#projected" title="Projected">Projected</a>: <i>
      - <a href="projecteddefinition.md">ProjectedDefinition</a></i>
<a href="#quobyte" title="Quobyte">Quobyte</a>: <i>
      - <a href="quobytedefinition.md">QuobyteDefinition</a></i>
<a href="#rbd" title="Rbd">Rbd</a>: <i>
      - <a href="rbddefinition.md">RbdDefinition</a></i>
<a href="#secret" title="Secret">Secret</a>: <i>
      - <a href="secretdefinition.md">SecretDefinition</a></i>
<a href="#vspherevolume" title="VsphereVolume">VsphereVolume</a>: <i>
      - <a href="vspherevolumedefinition.md">VsphereVolumeDefinition</a></i>
</pre>

## Properties

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsElasticBlockStore

_Required_: No

_Type_: List of <a href="awselasticblockstoredefinition.md">AwsElasticBlockStoreDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureDisk

_Required_: No

_Type_: List of <a href="azurediskdefinition.md">AzureDiskDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureFile

_Required_: No

_Type_: List of <a href="azurefiledefinition.md">AzureFileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CephFs

_Required_: No

_Type_: List of <a href="cephfsdefinition.md">CephFsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cinder

_Required_: No

_Type_: List of <a href="cinderdefinition.md">CinderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigMap

_Required_: No

_Type_: List of <a href="configmapdefinition.md">ConfigMapDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Csi

_Required_: No

_Type_: List of <a href="csidefinition.md">CsiDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DownwardApi

_Required_: No

_Type_: List of <a href="downwardapidefinition.md">DownwardApiDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmptyDir

_Required_: No

_Type_: List of <a href="emptydirdefinition.md">EmptyDirDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fc

_Required_: No

_Type_: List of <a href="fcdefinition.md">FcDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlexVolume

_Required_: No

_Type_: List of <a href="flexvolumedefinition.md">FlexVolumeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Flocker

_Required_: No

_Type_: List of <a href="flockerdefinition.md">FlockerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcePersistentDisk

_Required_: No

_Type_: List of <a href="gcepersistentdiskdefinition.md">GcePersistentDiskDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GitRepo

_Required_: No

_Type_: List of <a href="gitrepodefinition.md">GitRepoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Glusterfs

_Required_: No

_Type_: List of <a href="glusterfsdefinition.md">GlusterfsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostPath

_Required_: No

_Type_: List of <a href="hostpathdefinition.md">HostPathDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Iscsi

_Required_: No

_Type_: List of <a href="iscsidefinition.md">IscsiDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Local

_Required_: No

_Type_: List of <a href="localdefinition.md">LocalDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nfs

_Required_: No

_Type_: List of <a href="nfsdefinition.md">NfsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PersistentVolumeClaim

_Required_: No

_Type_: List of <a href="persistentvolumeclaimdefinition.md">PersistentVolumeClaimDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PhotonPersistentDisk

_Required_: No

_Type_: List of <a href="photonpersistentdiskdefinition.md">PhotonPersistentDiskDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Projected

_Required_: No

_Type_: List of <a href="projecteddefinition.md">ProjectedDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Quobyte

_Required_: No

_Type_: List of <a href="quobytedefinition.md">QuobyteDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rbd

_Required_: No

_Type_: List of <a href="rbddefinition.md">RbdDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Secret

_Required_: No

_Type_: List of <a href="secretdefinition.md">SecretDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsphereVolume

_Required_: No

_Type_: List of <a href="vspherevolumedefinition.md">VsphereVolumeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

