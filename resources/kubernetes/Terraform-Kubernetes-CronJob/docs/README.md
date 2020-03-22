# Terraform::Kubernetes::CronJob

A Cron Job creates Jobs on a time-based schedule.

  One CronJob object is like one line of a crontab (cron table) file. It runs a job periodically on a given schedule, written in Cron format.

  Note: All CronJob `schedule` times are based on the timezone of the master where the job is initiated.
  For instructions on creating and working with cron jobs, and for an example of a spec file for a cron job, see Running automated tasks with cron jobs.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Kubernetes::CronJob",
    "Properties" : {
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadata.md">Metadata</a>, ... ]</i>,
        "<a href="#spec" title="Spec">Spec</a>" : <i>[ <a href="spec.md">Spec</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#jobtemplate" title="JobTemplate">JobTemplate</a>" : <i>[ <a href="jobtemplate.md">JobTemplate</a>, ... ]</i>,
        "<a href="#selector" title="Selector">Selector</a>" : <i>[ <a href="selector.md">Selector</a>, ... ]</i>,
        "<a href="#template" title="Template">Template</a>" : <i>[ <a href="template.md">Template</a>, ... ]</i>,
        "<a href="#matchexpressions" title="MatchExpressions">MatchExpressions</a>" : <i>[ <a href="matchexpressions.md">MatchExpressions</a>, ... ]</i>,
        "<a href="#affinity" title="Affinity">Affinity</a>" : <i>[ <a href="affinity.md">Affinity</a>, ... ]</i>,
        "<a href="#container" title="Container">Container</a>" : <i>[ <a href="container.md">Container</a>, ... ]</i>,
        "<a href="#dnsconfig" title="DnsConfig">DnsConfig</a>" : <i>[ <a href="dnsconfig.md">DnsConfig</a>, ... ]</i>,
        "<a href="#hostaliases" title="HostAliases">HostAliases</a>" : <i>[ <a href="hostaliases.md">HostAliases</a>, ... ]</i>,
        "<a href="#imagepullsecrets" title="ImagePullSecrets">ImagePullSecrets</a>" : <i>[ <a href="imagepullsecrets.md">ImagePullSecrets</a>, ... ]</i>,
        "<a href="#initcontainer" title="InitContainer">InitContainer</a>" : <i>[ <a href="initcontainer.md">InitContainer</a>, ... ]</i>,
        "<a href="#securitycontext" title="SecurityContext">SecurityContext</a>" : <i>[ <a href="securitycontext.md">SecurityContext</a>, ... ]</i>,
        "<a href="#toleration" title="Toleration">Toleration</a>" : <i>[ <a href="toleration.md">Toleration</a>, ... ]</i>,
        "<a href="#volume" title="Volume">Volume</a>" : <i>[ <a href="volume.md">Volume</a>, ... ]</i>,
        "<a href="#nodeaffinity" title="NodeAffinity">NodeAffinity</a>" : <i>[ <a href="nodeaffinity.md">NodeAffinity</a>, ... ]</i>,
        "<a href="#podaffinity" title="PodAffinity">PodAffinity</a>" : <i>[ <a href="podaffinity.md">PodAffinity</a>, ... ]</i>,
        "<a href="#podantiaffinity" title="PodAntiAffinity">PodAntiAffinity</a>" : <i>[ <a href="podantiaffinity.md">PodAntiAffinity</a>, ... ]</i>,
        "<a href="#env" title="Env">Env</a>" : <i>[ <a href="env.md">Env</a>, ... ]</i>,
        "<a href="#envfrom" title="EnvFrom">EnvFrom</a>" : <i>[ <a href="envfrom.md">EnvFrom</a>, ... ]</i>,
        "<a href="#lifecycle" title="Lifecycle">Lifecycle</a>" : <i>[ <a href="lifecycle.md">Lifecycle</a>, ... ]</i>,
        "<a href="#livenessprobe" title="LivenessProbe">LivenessProbe</a>" : <i>[ <a href="livenessprobe.md">LivenessProbe</a>, ... ]</i>,
        "<a href="#port" title="Port">Port</a>" : <i>[ <a href="port.md">Port</a>, ... ]</i>,
        "<a href="#readinessprobe" title="ReadinessProbe">ReadinessProbe</a>" : <i>[ <a href="readinessprobe.md">ReadinessProbe</a>, ... ]</i>,
        "<a href="#resources" title="Resources">Resources</a>" : <i>[ <a href="resources.md">Resources</a>, ... ]</i>,
        "<a href="#startupprobe" title="StartupProbe">StartupProbe</a>" : <i>[ <a href="startupprobe.md">StartupProbe</a>, ... ]</i>,
        "<a href="#volumemount" title="VolumeMount">VolumeMount</a>" : <i>[ <a href="volumemount.md">VolumeMount</a>, ... ]</i>,
        "<a href="#option" title="Option">Option</a>" : <i>[ <a href="option.md">Option</a>, ... ]</i>,
        "<a href="#capabilities" title="Capabilities">Capabilities</a>" : <i>[ <a href="capabilities.md">Capabilities</a>, ... ]</i>,
        "<a href="#selinuxoptions" title="SeLinuxOptions">SeLinuxOptions</a>" : <i>[ <a href="selinuxoptions.md">SeLinuxOptions</a>, ... ]</i>,
        "<a href="#awselasticblockstore" title="AwsElasticBlockStore">AwsElasticBlockStore</a>" : <i>[ <a href="awselasticblockstore.md">AwsElasticBlockStore</a>, ... ]</i>,
        "<a href="#azuredisk" title="AzureDisk">AzureDisk</a>" : <i>[ <a href="azuredisk.md">AzureDisk</a>, ... ]</i>,
        "<a href="#azurefile" title="AzureFile">AzureFile</a>" : <i>[ <a href="azurefile.md">AzureFile</a>, ... ]</i>,
        "<a href="#cephfs" title="CephFs">CephFs</a>" : <i>[ <a href="cephfs.md">CephFs</a>, ... ]</i>,
        "<a href="#cinder" title="Cinder">Cinder</a>" : <i>[ <a href="cinder.md">Cinder</a>, ... ]</i>,
        "<a href="#configmap" title="ConfigMap">ConfigMap</a>" : <i>[ <a href="configmap.md">ConfigMap</a>, ... ]</i>,
        "<a href="#downwardapi" title="DownwardApi">DownwardApi</a>" : <i>[ <a href="downwardapi.md">DownwardApi</a>, ... ]</i>,
        "<a href="#emptydir" title="EmptyDir">EmptyDir</a>" : <i>[ <a href="emptydir.md">EmptyDir</a>, ... ]</i>,
        "<a href="#fc" title="Fc">Fc</a>" : <i>[ <a href="fc.md">Fc</a>, ... ]</i>,
        "<a href="#flexvolume" title="FlexVolume">FlexVolume</a>" : <i>[ <a href="flexvolume.md">FlexVolume</a>, ... ]</i>,
        "<a href="#flocker" title="Flocker">Flocker</a>" : <i>[ <a href="flocker.md">Flocker</a>, ... ]</i>,
        "<a href="#gcepersistentdisk" title="GcePersistentDisk">GcePersistentDisk</a>" : <i>[ <a href="gcepersistentdisk.md">GcePersistentDisk</a>, ... ]</i>,
        "<a href="#gitrepo" title="GitRepo">GitRepo</a>" : <i>[ <a href="gitrepo.md">GitRepo</a>, ... ]</i>,
        "<a href="#glusterfs" title="Glusterfs">Glusterfs</a>" : <i>[ <a href="glusterfs.md">Glusterfs</a>, ... ]</i>,
        "<a href="#hostpath" title="HostPath">HostPath</a>" : <i>[ <a href="hostpath.md">HostPath</a>, ... ]</i>,
        "<a href="#iscsi" title="Iscsi">Iscsi</a>" : <i>[ <a href="iscsi.md">Iscsi</a>, ... ]</i>,
        "<a href="#local" title="Local">Local</a>" : <i>[ <a href="local.md">Local</a>, ... ]</i>,
        "<a href="#nfs" title="Nfs">Nfs</a>" : <i>[ <a href="nfs.md">Nfs</a>, ... ]</i>,
        "<a href="#persistentvolumeclaim" title="PersistentVolumeClaim">PersistentVolumeClaim</a>" : <i>[ <a href="persistentvolumeclaim.md">PersistentVolumeClaim</a>, ... ]</i>,
        "<a href="#photonpersistentdisk" title="PhotonPersistentDisk">PhotonPersistentDisk</a>" : <i>[ <a href="photonpersistentdisk.md">PhotonPersistentDisk</a>, ... ]</i>,
        "<a href="#quobyte" title="Quobyte">Quobyte</a>" : <i>[ <a href="quobyte.md">Quobyte</a>, ... ]</i>,
        "<a href="#rbd" title="Rbd">Rbd</a>" : <i>[ <a href="rbd.md">Rbd</a>, ... ]</i>,
        "<a href="#secret" title="Secret">Secret</a>" : <i>[ <a href="secret.md">Secret</a>, ... ]</i>,
        "<a href="#vspherevolume" title="VsphereVolume">VsphereVolume</a>" : <i>[ <a href="vspherevolume.md">VsphereVolume</a>, ... ]</i>,
        "<a href="#preferredduringschedulingignoredduringexecution" title="PreferredDuringSchedulingIgnoredDuringExecution">PreferredDuringSchedulingIgnoredDuringExecution</a>" : <i>[ <a href="preferredduringschedulingignoredduringexecution.md">PreferredDuringSchedulingIgnoredDuringExecution</a>, ... ]</i>,
        "<a href="#requiredduringschedulingignoredduringexecution" title="RequiredDuringSchedulingIgnoredDuringExecution">RequiredDuringSchedulingIgnoredDuringExecution</a>" : <i>[ <a href="requiredduringschedulingignoredduringexecution.md">RequiredDuringSchedulingIgnoredDuringExecution</a>, ... ]</i>,
        "<a href="#valuefrom" title="ValueFrom">ValueFrom</a>" : <i>[ <a href="valuefrom.md">ValueFrom</a>, ... ]</i>,
        "<a href="#configmapref" title="ConfigMapRef">ConfigMapRef</a>" : <i>[ <a href="configmapref.md">ConfigMapRef</a>, ... ]</i>,
        "<a href="#secretref" title="SecretRef">SecretRef</a>" : <i>[ <a href="secretref.md">SecretRef</a>, ... ]</i>,
        "<a href="#poststart" title="PostStart">PostStart</a>" : <i>[ <a href="poststart.md">PostStart</a>, ... ]</i>,
        "<a href="#prestop" title="PreStop">PreStop</a>" : <i>[ <a href="prestop.md">PreStop</a>, ... ]</i>,
        "<a href="#exec" title="Exec">Exec</a>" : <i>[ <a href="exec.md">Exec</a>, ... ]</i>,
        "<a href="#httpget" title="HttpGet">HttpGet</a>" : <i>[ <a href="httpget.md">HttpGet</a>, ... ]</i>,
        "<a href="#tcpsocket" title="TcpSocket">TcpSocket</a>" : <i>[ <a href="tcpsocket.md">TcpSocket</a>, ... ]</i>,
        "<a href="#limits" title="Limits">Limits</a>" : <i>[ <a href="limits.md">Limits</a>, ... ]</i>,
        "<a href="#requests" title="Requests">Requests</a>" : <i>[ <a href="requests.md">Requests</a>, ... ]</i>,
        "<a href="#items" title="Items">Items</a>" : <i>[ <a href="items.md">Items</a>, ... ]</i>,
        "<a href="#podaffinityterm" title="PodAffinityTerm">PodAffinityTerm</a>" : <i>[ <a href="podaffinityterm.md">PodAffinityTerm</a>, ... ]</i>,
        "<a href="#labelselector" title="LabelSelector">LabelSelector</a>" : <i>[ <a href="labelselector.md">LabelSelector</a>, ... ]</i>,
        "<a href="#configmapkeyref" title="ConfigMapKeyRef">ConfigMapKeyRef</a>" : <i>[ <a href="configmapkeyref.md">ConfigMapKeyRef</a>, ... ]</i>,
        "<a href="#fieldref" title="FieldRef">FieldRef</a>" : <i>[ <a href="fieldref.md">FieldRef</a>, ... ]</i>,
        "<a href="#resourcefieldref" title="ResourceFieldRef">ResourceFieldRef</a>" : <i>[ <a href="resourcefieldref.md">ResourceFieldRef</a>, ... ]</i>,
        "<a href="#secretkeyref" title="SecretKeyRef">SecretKeyRef</a>" : <i>[ <a href="secretkeyref.md">SecretKeyRef</a>, ... ]</i>,
        "<a href="#httpheader" title="HttpHeader">HttpHeader</a>" : <i>[ <a href="httpheader.md">HttpHeader</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Kubernetes::CronJob
Properties:
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadata.md">Metadata</a></i>
    <a href="#spec" title="Spec">Spec</a>: <i>
      - <a href="spec.md">Spec</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#jobtemplate" title="JobTemplate">JobTemplate</a>: <i>
      - <a href="jobtemplate.md">JobTemplate</a></i>
    <a href="#selector" title="Selector">Selector</a>: <i>
      - <a href="selector.md">Selector</a></i>
    <a href="#template" title="Template">Template</a>: <i>
      - <a href="template.md">Template</a></i>
    <a href="#matchexpressions" title="MatchExpressions">MatchExpressions</a>: <i>
      - <a href="matchexpressions.md">MatchExpressions</a></i>
    <a href="#affinity" title="Affinity">Affinity</a>: <i>
      - <a href="affinity.md">Affinity</a></i>
    <a href="#container" title="Container">Container</a>: <i>
      - <a href="container.md">Container</a></i>
    <a href="#dnsconfig" title="DnsConfig">DnsConfig</a>: <i>
      - <a href="dnsconfig.md">DnsConfig</a></i>
    <a href="#hostaliases" title="HostAliases">HostAliases</a>: <i>
      - <a href="hostaliases.md">HostAliases</a></i>
    <a href="#imagepullsecrets" title="ImagePullSecrets">ImagePullSecrets</a>: <i>
      - <a href="imagepullsecrets.md">ImagePullSecrets</a></i>
    <a href="#initcontainer" title="InitContainer">InitContainer</a>: <i>
      - <a href="initcontainer.md">InitContainer</a></i>
    <a href="#securitycontext" title="SecurityContext">SecurityContext</a>: <i>
      - <a href="securitycontext.md">SecurityContext</a></i>
    <a href="#toleration" title="Toleration">Toleration</a>: <i>
      - <a href="toleration.md">Toleration</a></i>
    <a href="#volume" title="Volume">Volume</a>: <i>
      - <a href="volume.md">Volume</a></i>
    <a href="#nodeaffinity" title="NodeAffinity">NodeAffinity</a>: <i>
      - <a href="nodeaffinity.md">NodeAffinity</a></i>
    <a href="#podaffinity" title="PodAffinity">PodAffinity</a>: <i>
      - <a href="podaffinity.md">PodAffinity</a></i>
    <a href="#podantiaffinity" title="PodAntiAffinity">PodAntiAffinity</a>: <i>
      - <a href="podantiaffinity.md">PodAntiAffinity</a></i>
    <a href="#env" title="Env">Env</a>: <i>
      - <a href="env.md">Env</a></i>
    <a href="#envfrom" title="EnvFrom">EnvFrom</a>: <i>
      - <a href="envfrom.md">EnvFrom</a></i>
    <a href="#lifecycle" title="Lifecycle">Lifecycle</a>: <i>
      - <a href="lifecycle.md">Lifecycle</a></i>
    <a href="#livenessprobe" title="LivenessProbe">LivenessProbe</a>: <i>
      - <a href="livenessprobe.md">LivenessProbe</a></i>
    <a href="#port" title="Port">Port</a>: <i>
      - <a href="port.md">Port</a></i>
    <a href="#readinessprobe" title="ReadinessProbe">ReadinessProbe</a>: <i>
      - <a href="readinessprobe.md">ReadinessProbe</a></i>
    <a href="#resources" title="Resources">Resources</a>: <i>
      - <a href="resources.md">Resources</a></i>
    <a href="#startupprobe" title="StartupProbe">StartupProbe</a>: <i>
      - <a href="startupprobe.md">StartupProbe</a></i>
    <a href="#volumemount" title="VolumeMount">VolumeMount</a>: <i>
      - <a href="volumemount.md">VolumeMount</a></i>
    <a href="#option" title="Option">Option</a>: <i>
      - <a href="option.md">Option</a></i>
    <a href="#capabilities" title="Capabilities">Capabilities</a>: <i>
      - <a href="capabilities.md">Capabilities</a></i>
    <a href="#selinuxoptions" title="SeLinuxOptions">SeLinuxOptions</a>: <i>
      - <a href="selinuxoptions.md">SeLinuxOptions</a></i>
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
    <a href="#configmap" title="ConfigMap">ConfigMap</a>: <i>
      - <a href="configmap.md">ConfigMap</a></i>
    <a href="#downwardapi" title="DownwardApi">DownwardApi</a>: <i>
      - <a href="downwardapi.md">DownwardApi</a></i>
    <a href="#emptydir" title="EmptyDir">EmptyDir</a>: <i>
      - <a href="emptydir.md">EmptyDir</a></i>
    <a href="#fc" title="Fc">Fc</a>: <i>
      - <a href="fc.md">Fc</a></i>
    <a href="#flexvolume" title="FlexVolume">FlexVolume</a>: <i>
      - <a href="flexvolume.md">FlexVolume</a></i>
    <a href="#flocker" title="Flocker">Flocker</a>: <i>
      - <a href="flocker.md">Flocker</a></i>
    <a href="#gcepersistentdisk" title="GcePersistentDisk">GcePersistentDisk</a>: <i>
      - <a href="gcepersistentdisk.md">GcePersistentDisk</a></i>
    <a href="#gitrepo" title="GitRepo">GitRepo</a>: <i>
      - <a href="gitrepo.md">GitRepo</a></i>
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
    <a href="#persistentvolumeclaim" title="PersistentVolumeClaim">PersistentVolumeClaim</a>: <i>
      - <a href="persistentvolumeclaim.md">PersistentVolumeClaim</a></i>
    <a href="#photonpersistentdisk" title="PhotonPersistentDisk">PhotonPersistentDisk</a>: <i>
      - <a href="photonpersistentdisk.md">PhotonPersistentDisk</a></i>
    <a href="#quobyte" title="Quobyte">Quobyte</a>: <i>
      - <a href="quobyte.md">Quobyte</a></i>
    <a href="#rbd" title="Rbd">Rbd</a>: <i>
      - <a href="rbd.md">Rbd</a></i>
    <a href="#secret" title="Secret">Secret</a>: <i>
      - <a href="secret.md">Secret</a></i>
    <a href="#vspherevolume" title="VsphereVolume">VsphereVolume</a>: <i>
      - <a href="vspherevolume.md">VsphereVolume</a></i>
    <a href="#preferredduringschedulingignoredduringexecution" title="PreferredDuringSchedulingIgnoredDuringExecution">PreferredDuringSchedulingIgnoredDuringExecution</a>: <i>
      - <a href="preferredduringschedulingignoredduringexecution.md">PreferredDuringSchedulingIgnoredDuringExecution</a></i>
    <a href="#requiredduringschedulingignoredduringexecution" title="RequiredDuringSchedulingIgnoredDuringExecution">RequiredDuringSchedulingIgnoredDuringExecution</a>: <i>
      - <a href="requiredduringschedulingignoredduringexecution.md">RequiredDuringSchedulingIgnoredDuringExecution</a></i>
    <a href="#valuefrom" title="ValueFrom">ValueFrom</a>: <i>
      - <a href="valuefrom.md">ValueFrom</a></i>
    <a href="#configmapref" title="ConfigMapRef">ConfigMapRef</a>: <i>
      - <a href="configmapref.md">ConfigMapRef</a></i>
    <a href="#secretref" title="SecretRef">SecretRef</a>: <i>
      - <a href="secretref.md">SecretRef</a></i>
    <a href="#poststart" title="PostStart">PostStart</a>: <i>
      - <a href="poststart.md">PostStart</a></i>
    <a href="#prestop" title="PreStop">PreStop</a>: <i>
      - <a href="prestop.md">PreStop</a></i>
    <a href="#exec" title="Exec">Exec</a>: <i>
      - <a href="exec.md">Exec</a></i>
    <a href="#httpget" title="HttpGet">HttpGet</a>: <i>
      - <a href="httpget.md">HttpGet</a></i>
    <a href="#tcpsocket" title="TcpSocket">TcpSocket</a>: <i>
      - <a href="tcpsocket.md">TcpSocket</a></i>
    <a href="#limits" title="Limits">Limits</a>: <i>
      - <a href="limits.md">Limits</a></i>
    <a href="#requests" title="Requests">Requests</a>: <i>
      - <a href="requests.md">Requests</a></i>
    <a href="#items" title="Items">Items</a>: <i>
      - <a href="items.md">Items</a></i>
    <a href="#podaffinityterm" title="PodAffinityTerm">PodAffinityTerm</a>: <i>
      - <a href="podaffinityterm.md">PodAffinityTerm</a></i>
    <a href="#labelselector" title="LabelSelector">LabelSelector</a>: <i>
      - <a href="labelselector.md">LabelSelector</a></i>
    <a href="#configmapkeyref" title="ConfigMapKeyRef">ConfigMapKeyRef</a>: <i>
      - <a href="configmapkeyref.md">ConfigMapKeyRef</a></i>
    <a href="#fieldref" title="FieldRef">FieldRef</a>: <i>
      - <a href="fieldref.md">FieldRef</a></i>
    <a href="#resourcefieldref" title="ResourceFieldRef">ResourceFieldRef</a>: <i>
      - <a href="resourcefieldref.md">ResourceFieldRef</a></i>
    <a href="#secretkeyref" title="SecretKeyRef">SecretKeyRef</a>: <i>
      - <a href="secretkeyref.md">SecretKeyRef</a></i>
    <a href="#httpheader" title="HttpHeader">HttpHeader</a>: <i>
      - <a href="httpheader.md">HttpHeader</a></i>
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

#### JobTemplate

_Required_: No

_Type_: List of <a href="jobtemplate.md">JobTemplate</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Selector

_Required_: No

_Type_: List of <a href="selector.md">Selector</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

_Required_: No

_Type_: List of <a href="template.md">Template</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchExpressions

_Required_: No

_Type_: List of <a href="matchexpressions.md">MatchExpressions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Affinity

_Required_: No

_Type_: List of <a href="affinity.md">Affinity</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Container

_Required_: No

_Type_: List of <a href="container.md">Container</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsConfig

_Required_: No

_Type_: List of <a href="dnsconfig.md">DnsConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostAliases

_Required_: No

_Type_: List of <a href="hostaliases.md">HostAliases</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImagePullSecrets

_Required_: No

_Type_: List of <a href="imagepullsecrets.md">ImagePullSecrets</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitContainer

_Required_: No

_Type_: List of <a href="initcontainer.md">InitContainer</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityContext

_Required_: No

_Type_: List of <a href="securitycontext.md">SecurityContext</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Toleration

_Required_: No

_Type_: List of <a href="toleration.md">Toleration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Volume

_Required_: No

_Type_: List of <a href="volume.md">Volume</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeAffinity

_Required_: No

_Type_: List of <a href="nodeaffinity.md">NodeAffinity</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PodAffinity

_Required_: No

_Type_: List of <a href="podaffinity.md">PodAffinity</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PodAntiAffinity

_Required_: No

_Type_: List of <a href="podantiaffinity.md">PodAntiAffinity</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Env

_Required_: No

_Type_: List of <a href="env.md">Env</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvFrom

_Required_: No

_Type_: List of <a href="envfrom.md">EnvFrom</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lifecycle

_Required_: No

_Type_: List of <a href="lifecycle.md">Lifecycle</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LivenessProbe

_Required_: No

_Type_: List of <a href="livenessprobe.md">LivenessProbe</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: List of <a href="port.md">Port</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadinessProbe

_Required_: No

_Type_: List of <a href="readinessprobe.md">ReadinessProbe</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resources

_Required_: No

_Type_: List of <a href="resources.md">Resources</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartupProbe

_Required_: No

_Type_: List of <a href="startupprobe.md">StartupProbe</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeMount

_Required_: No

_Type_: List of <a href="volumemount.md">VolumeMount</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Option

_Required_: No

_Type_: List of <a href="option.md">Option</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Capabilities

_Required_: No

_Type_: List of <a href="capabilities.md">Capabilities</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeLinuxOptions

_Required_: No

_Type_: List of <a href="selinuxoptions.md">SeLinuxOptions</a>

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

#### ConfigMap

_Required_: No

_Type_: List of <a href="configmap.md">ConfigMap</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DownwardApi

_Required_: No

_Type_: List of <a href="downwardapi.md">DownwardApi</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmptyDir

_Required_: No

_Type_: List of <a href="emptydir.md">EmptyDir</a>

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

#### GitRepo

_Required_: No

_Type_: List of <a href="gitrepo.md">GitRepo</a>

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

#### PersistentVolumeClaim

_Required_: No

_Type_: List of <a href="persistentvolumeclaim.md">PersistentVolumeClaim</a>

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

#### Secret

_Required_: No

_Type_: List of <a href="secret.md">Secret</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsphereVolume

_Required_: No

_Type_: List of <a href="vspherevolume.md">VsphereVolume</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreferredDuringSchedulingIgnoredDuringExecution

_Required_: No

_Type_: List of <a href="preferredduringschedulingignoredduringexecution.md">PreferredDuringSchedulingIgnoredDuringExecution</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequiredDuringSchedulingIgnoredDuringExecution

_Required_: No

_Type_: List of <a href="requiredduringschedulingignoredduringexecution.md">RequiredDuringSchedulingIgnoredDuringExecution</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValueFrom

_Required_: No

_Type_: List of <a href="valuefrom.md">ValueFrom</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigMapRef

_Required_: No

_Type_: List of <a href="configmapref.md">ConfigMapRef</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretRef

_Required_: No

_Type_: List of <a href="secretref.md">SecretRef</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PostStart

_Required_: No

_Type_: List of <a href="poststart.md">PostStart</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreStop

_Required_: No

_Type_: List of <a href="prestop.md">PreStop</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Exec

_Required_: No

_Type_: List of <a href="exec.md">Exec</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpGet

_Required_: No

_Type_: List of <a href="httpget.md">HttpGet</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpSocket

_Required_: No

_Type_: List of <a href="tcpsocket.md">TcpSocket</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Limits

_Required_: No

_Type_: List of <a href="limits.md">Limits</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Requests

_Required_: No

_Type_: List of <a href="requests.md">Requests</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Items

_Required_: No

_Type_: List of <a href="items.md">Items</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PodAffinityTerm

_Required_: No

_Type_: List of <a href="podaffinityterm.md">PodAffinityTerm</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LabelSelector

_Required_: No

_Type_: List of <a href="labelselector.md">LabelSelector</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigMapKeyRef

_Required_: No

_Type_: List of <a href="configmapkeyref.md">ConfigMapKeyRef</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FieldRef

_Required_: No

_Type_: List of <a href="fieldref.md">FieldRef</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceFieldRef

_Required_: No

_Type_: List of <a href="resourcefieldref.md">ResourceFieldRef</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretKeyRef

_Required_: No

_Type_: List of <a href="secretkeyref.md">SecretKeyRef</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpHeader

_Required_: No

_Type_: List of <a href="httpheader.md">HttpHeader</a>

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

