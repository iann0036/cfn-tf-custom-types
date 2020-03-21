# Terraform::Kubernetes::Pod

CloudFormation equivalent of kubernetes_pod

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Kubernetes::Pod",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ &lt;a href=&#34;metadata.md&#34;&gt;Metadata&lt;/a&gt;, ... ]</i>,
        "<a href="#spec" title="Spec">Spec</a>" : <i>[ &lt;a href=&#34;spec.md&#34;&gt;Spec&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#affinity" title="Affinity">Affinity</a>" : <i>[ &lt;a href=&#34;affinity.md&#34;&gt;Affinity&lt;/a&gt;, ... ]</i>,
        "<a href="#container" title="Container">Container</a>" : <i>[ &lt;a href=&#34;container.md&#34;&gt;Container&lt;/a&gt;, ... ]</i>,
        "<a href="#dnsconfig" title="DnsConfig">DnsConfig</a>" : <i>[ &lt;a href=&#34;dnsconfig.md&#34;&gt;DnsConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#hostaliases" title="HostAliases">HostAliases</a>" : <i>[ &lt;a href=&#34;hostaliases.md&#34;&gt;HostAliases&lt;/a&gt;, ... ]</i>,
        "<a href="#imagepullsecrets" title="ImagePullSecrets">ImagePullSecrets</a>" : <i>[ &lt;a href=&#34;imagepullsecrets.md&#34;&gt;ImagePullSecrets&lt;/a&gt;, ... ]</i>,
        "<a href="#initcontainer" title="InitContainer">InitContainer</a>" : <i>[ &lt;a href=&#34;initcontainer.md&#34;&gt;InitContainer&lt;/a&gt;, ... ]</i>,
        "<a href="#securitycontext" title="SecurityContext">SecurityContext</a>" : <i>[ &lt;a href=&#34;securitycontext.md&#34;&gt;SecurityContext&lt;/a&gt;, ... ]</i>,
        "<a href="#toleration" title="Toleration">Toleration</a>" : <i>[ &lt;a href=&#34;toleration.md&#34;&gt;Toleration&lt;/a&gt;, ... ]</i>,
        "<a href="#volume" title="Volume">Volume</a>" : <i>[ &lt;a href=&#34;volume.md&#34;&gt;Volume&lt;/a&gt;, ... ]</i>,
        "<a href="#nodeaffinity" title="NodeAffinity">NodeAffinity</a>" : <i>[ &lt;a href=&#34;nodeaffinity.md&#34;&gt;NodeAffinity&lt;/a&gt;, ... ]</i>,
        "<a href="#podaffinity" title="PodAffinity">PodAffinity</a>" : <i>[ &lt;a href=&#34;podaffinity.md&#34;&gt;PodAffinity&lt;/a&gt;, ... ]</i>,
        "<a href="#podantiaffinity" title="PodAntiAffinity">PodAntiAffinity</a>" : <i>[ &lt;a href=&#34;podantiaffinity.md&#34;&gt;PodAntiAffinity&lt;/a&gt;, ... ]</i>,
        "<a href="#env" title="Env">Env</a>" : <i>[ &lt;a href=&#34;env.md&#34;&gt;Env&lt;/a&gt;, ... ]</i>,
        "<a href="#envfrom" title="EnvFrom">EnvFrom</a>" : <i>[ &lt;a href=&#34;envfrom.md&#34;&gt;EnvFrom&lt;/a&gt;, ... ]</i>,
        "<a href="#lifecycle" title="Lifecycle">Lifecycle</a>" : <i>[ &lt;a href=&#34;lifecycle.md&#34;&gt;Lifecycle&lt;/a&gt;, ... ]</i>,
        "<a href="#livenessprobe" title="LivenessProbe">LivenessProbe</a>" : <i>[ &lt;a href=&#34;livenessprobe.md&#34;&gt;LivenessProbe&lt;/a&gt;, ... ]</i>,
        "<a href="#port" title="Port">Port</a>" : <i>[ &lt;a href=&#34;port.md&#34;&gt;Port&lt;/a&gt;, ... ]</i>,
        "<a href="#readinessprobe" title="ReadinessProbe">ReadinessProbe</a>" : <i>[ &lt;a href=&#34;readinessprobe.md&#34;&gt;ReadinessProbe&lt;/a&gt;, ... ]</i>,
        "<a href="#resources" title="Resources">Resources</a>" : <i>[ &lt;a href=&#34;resources.md&#34;&gt;Resources&lt;/a&gt;, ... ]</i>,
        "<a href="#startupprobe" title="StartupProbe">StartupProbe</a>" : <i>[ &lt;a href=&#34;startupprobe.md&#34;&gt;StartupProbe&lt;/a&gt;, ... ]</i>,
        "<a href="#volumemount" title="VolumeMount">VolumeMount</a>" : <i>[ &lt;a href=&#34;volumemount.md&#34;&gt;VolumeMount&lt;/a&gt;, ... ]</i>,
        "<a href="#option" title="Option">Option</a>" : <i>[ &lt;a href=&#34;option.md&#34;&gt;Option&lt;/a&gt;, ... ]</i>,
        "<a href="#capabilities" title="Capabilities">Capabilities</a>" : <i>[ &lt;a href=&#34;capabilities.md&#34;&gt;Capabilities&lt;/a&gt;, ... ]</i>,
        "<a href="#selinuxoptions" title="SeLinuxOptions">SeLinuxOptions</a>" : <i>[ &lt;a href=&#34;selinuxoptions.md&#34;&gt;SeLinuxOptions&lt;/a&gt;, ... ]</i>,
        "<a href="#awselasticblockstore" title="AwsElasticBlockStore">AwsElasticBlockStore</a>" : <i>[ &lt;a href=&#34;awselasticblockstore.md&#34;&gt;AwsElasticBlockStore&lt;/a&gt;, ... ]</i>,
        "<a href="#azuredisk" title="AzureDisk">AzureDisk</a>" : <i>[ &lt;a href=&#34;azuredisk.md&#34;&gt;AzureDisk&lt;/a&gt;, ... ]</i>,
        "<a href="#azurefile" title="AzureFile">AzureFile</a>" : <i>[ &lt;a href=&#34;azurefile.md&#34;&gt;AzureFile&lt;/a&gt;, ... ]</i>,
        "<a href="#cephfs" title="CephFs">CephFs</a>" : <i>[ &lt;a href=&#34;cephfs.md&#34;&gt;CephFs&lt;/a&gt;, ... ]</i>,
        "<a href="#cinder" title="Cinder">Cinder</a>" : <i>[ &lt;a href=&#34;cinder.md&#34;&gt;Cinder&lt;/a&gt;, ... ]</i>,
        "<a href="#configmap" title="ConfigMap">ConfigMap</a>" : <i>[ &lt;a href=&#34;configmap.md&#34;&gt;ConfigMap&lt;/a&gt;, ... ]</i>,
        "<a href="#downwardapi" title="DownwardApi">DownwardApi</a>" : <i>[ &lt;a href=&#34;downwardapi.md&#34;&gt;DownwardApi&lt;/a&gt;, ... ]</i>,
        "<a href="#emptydir" title="EmptyDir">EmptyDir</a>" : <i>[ &lt;a href=&#34;emptydir.md&#34;&gt;EmptyDir&lt;/a&gt;, ... ]</i>,
        "<a href="#fc" title="Fc">Fc</a>" : <i>[ &lt;a href=&#34;fc.md&#34;&gt;Fc&lt;/a&gt;, ... ]</i>,
        "<a href="#flexvolume" title="FlexVolume">FlexVolume</a>" : <i>[ &lt;a href=&#34;flexvolume.md&#34;&gt;FlexVolume&lt;/a&gt;, ... ]</i>,
        "<a href="#flocker" title="Flocker">Flocker</a>" : <i>[ &lt;a href=&#34;flocker.md&#34;&gt;Flocker&lt;/a&gt;, ... ]</i>,
        "<a href="#gcepersistentdisk" title="GcePersistentDisk">GcePersistentDisk</a>" : <i>[ &lt;a href=&#34;gcepersistentdisk.md&#34;&gt;GcePersistentDisk&lt;/a&gt;, ... ]</i>,
        "<a href="#gitrepo" title="GitRepo">GitRepo</a>" : <i>[ &lt;a href=&#34;gitrepo.md&#34;&gt;GitRepo&lt;/a&gt;, ... ]</i>,
        "<a href="#glusterfs" title="Glusterfs">Glusterfs</a>" : <i>[ &lt;a href=&#34;glusterfs.md&#34;&gt;Glusterfs&lt;/a&gt;, ... ]</i>,
        "<a href="#hostpath" title="HostPath">HostPath</a>" : <i>[ &lt;a href=&#34;hostpath.md&#34;&gt;HostPath&lt;/a&gt;, ... ]</i>,
        "<a href="#iscsi" title="Iscsi">Iscsi</a>" : <i>[ &lt;a href=&#34;iscsi.md&#34;&gt;Iscsi&lt;/a&gt;, ... ]</i>,
        "<a href="#local" title="Local">Local</a>" : <i>[ &lt;a href=&#34;local.md&#34;&gt;Local&lt;/a&gt;, ... ]</i>,
        "<a href="#nfs" title="Nfs">Nfs</a>" : <i>[ &lt;a href=&#34;nfs.md&#34;&gt;Nfs&lt;/a&gt;, ... ]</i>,
        "<a href="#persistentvolumeclaim" title="PersistentVolumeClaim">PersistentVolumeClaim</a>" : <i>[ &lt;a href=&#34;persistentvolumeclaim.md&#34;&gt;PersistentVolumeClaim&lt;/a&gt;, ... ]</i>,
        "<a href="#photonpersistentdisk" title="PhotonPersistentDisk">PhotonPersistentDisk</a>" : <i>[ &lt;a href=&#34;photonpersistentdisk.md&#34;&gt;PhotonPersistentDisk&lt;/a&gt;, ... ]</i>,
        "<a href="#quobyte" title="Quobyte">Quobyte</a>" : <i>[ &lt;a href=&#34;quobyte.md&#34;&gt;Quobyte&lt;/a&gt;, ... ]</i>,
        "<a href="#rbd" title="Rbd">Rbd</a>" : <i>[ &lt;a href=&#34;rbd.md&#34;&gt;Rbd&lt;/a&gt;, ... ]</i>,
        "<a href="#secret" title="Secret">Secret</a>" : <i>[ &lt;a href=&#34;secret.md&#34;&gt;Secret&lt;/a&gt;, ... ]</i>,
        "<a href="#vspherevolume" title="VsphereVolume">VsphereVolume</a>" : <i>[ &lt;a href=&#34;vspherevolume.md&#34;&gt;VsphereVolume&lt;/a&gt;, ... ]</i>,
        "<a href="#preferredduringschedulingignoredduringexecution" title="PreferredDuringSchedulingIgnoredDuringExecution">PreferredDuringSchedulingIgnoredDuringExecution</a>" : <i>[ &lt;a href=&#34;preferredduringschedulingignoredduringexecution.md&#34;&gt;PreferredDuringSchedulingIgnoredDuringExecution&lt;/a&gt;, ... ]</i>,
        "<a href="#requiredduringschedulingignoredduringexecution" title="RequiredDuringSchedulingIgnoredDuringExecution">RequiredDuringSchedulingIgnoredDuringExecution</a>" : <i>[ &lt;a href=&#34;requiredduringschedulingignoredduringexecution.md&#34;&gt;RequiredDuringSchedulingIgnoredDuringExecution&lt;/a&gt;, ... ]</i>,
        "<a href="#valuefrom" title="ValueFrom">ValueFrom</a>" : <i>[ &lt;a href=&#34;valuefrom.md&#34;&gt;ValueFrom&lt;/a&gt;, ... ]</i>,
        "<a href="#configmapref" title="ConfigMapRef">ConfigMapRef</a>" : <i>[ &lt;a href=&#34;configmapref.md&#34;&gt;ConfigMapRef&lt;/a&gt;, ... ]</i>,
        "<a href="#secretref" title="SecretRef">SecretRef</a>" : <i>[ &lt;a href=&#34;secretref.md&#34;&gt;SecretRef&lt;/a&gt;, ... ]</i>,
        "<a href="#poststart" title="PostStart">PostStart</a>" : <i>[ &lt;a href=&#34;poststart.md&#34;&gt;PostStart&lt;/a&gt;, ... ]</i>,
        "<a href="#prestop" title="PreStop">PreStop</a>" : <i>[ &lt;a href=&#34;prestop.md&#34;&gt;PreStop&lt;/a&gt;, ... ]</i>,
        "<a href="#exec" title="Exec">Exec</a>" : <i>[ &lt;a href=&#34;exec.md&#34;&gt;Exec&lt;/a&gt;, ... ]</i>,
        "<a href="#httpget" title="HttpGet">HttpGet</a>" : <i>[ &lt;a href=&#34;httpget.md&#34;&gt;HttpGet&lt;/a&gt;, ... ]</i>,
        "<a href="#tcpsocket" title="TcpSocket">TcpSocket</a>" : <i>[ &lt;a href=&#34;tcpsocket.md&#34;&gt;TcpSocket&lt;/a&gt;, ... ]</i>,
        "<a href="#limits" title="Limits">Limits</a>" : <i>[ &lt;a href=&#34;limits.md&#34;&gt;Limits&lt;/a&gt;, ... ]</i>,
        "<a href="#requests" title="Requests">Requests</a>" : <i>[ &lt;a href=&#34;requests.md&#34;&gt;Requests&lt;/a&gt;, ... ]</i>,
        "<a href="#items" title="Items">Items</a>" : <i>[ &lt;a href=&#34;items.md&#34;&gt;Items&lt;/a&gt;, ... ]</i>,
        "<a href="#podaffinityterm" title="PodAffinityTerm">PodAffinityTerm</a>" : <i>[ &lt;a href=&#34;podaffinityterm.md&#34;&gt;PodAffinityTerm&lt;/a&gt;, ... ]</i>,
        "<a href="#labelselector" title="LabelSelector">LabelSelector</a>" : <i>[ &lt;a href=&#34;labelselector.md&#34;&gt;LabelSelector&lt;/a&gt;, ... ]</i>,
        "<a href="#configmapkeyref" title="ConfigMapKeyRef">ConfigMapKeyRef</a>" : <i>[ &lt;a href=&#34;configmapkeyref.md&#34;&gt;ConfigMapKeyRef&lt;/a&gt;, ... ]</i>,
        "<a href="#fieldref" title="FieldRef">FieldRef</a>" : <i>[ &lt;a href=&#34;fieldref.md&#34;&gt;FieldRef&lt;/a&gt;, ... ]</i>,
        "<a href="#resourcefieldref" title="ResourceFieldRef">ResourceFieldRef</a>" : <i>[ &lt;a href=&#34;resourcefieldref.md&#34;&gt;ResourceFieldRef&lt;/a&gt;, ... ]</i>,
        "<a href="#secretkeyref" title="SecretKeyRef">SecretKeyRef</a>" : <i>[ &lt;a href=&#34;secretkeyref.md&#34;&gt;SecretKeyRef&lt;/a&gt;, ... ]</i>,
        "<a href="#httpheader" title="HttpHeader">HttpHeader</a>" : <i>[ &lt;a href=&#34;httpheader.md&#34;&gt;HttpHeader&lt;/a&gt;, ... ]</i>,
        "<a href="#matchexpressions" title="MatchExpressions">MatchExpressions</a>" : <i>[ &lt;a href=&#34;matchexpressions.md&#34;&gt;MatchExpressions&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Kubernetes::Pod
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - &lt;a href=&#34;metadata.md&#34;&gt;Metadata&lt;/a&gt;</i>
    <a href="#spec" title="Spec">Spec</a>: <i>
      - &lt;a href=&#34;spec.md&#34;&gt;Spec&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#affinity" title="Affinity">Affinity</a>: <i>
      - &lt;a href=&#34;affinity.md&#34;&gt;Affinity&lt;/a&gt;</i>
    <a href="#container" title="Container">Container</a>: <i>
      - &lt;a href=&#34;container.md&#34;&gt;Container&lt;/a&gt;</i>
    <a href="#dnsconfig" title="DnsConfig">DnsConfig</a>: <i>
      - &lt;a href=&#34;dnsconfig.md&#34;&gt;DnsConfig&lt;/a&gt;</i>
    <a href="#hostaliases" title="HostAliases">HostAliases</a>: <i>
      - &lt;a href=&#34;hostaliases.md&#34;&gt;HostAliases&lt;/a&gt;</i>
    <a href="#imagepullsecrets" title="ImagePullSecrets">ImagePullSecrets</a>: <i>
      - &lt;a href=&#34;imagepullsecrets.md&#34;&gt;ImagePullSecrets&lt;/a&gt;</i>
    <a href="#initcontainer" title="InitContainer">InitContainer</a>: <i>
      - &lt;a href=&#34;initcontainer.md&#34;&gt;InitContainer&lt;/a&gt;</i>
    <a href="#securitycontext" title="SecurityContext">SecurityContext</a>: <i>
      - &lt;a href=&#34;securitycontext.md&#34;&gt;SecurityContext&lt;/a&gt;</i>
    <a href="#toleration" title="Toleration">Toleration</a>: <i>
      - &lt;a href=&#34;toleration.md&#34;&gt;Toleration&lt;/a&gt;</i>
    <a href="#volume" title="Volume">Volume</a>: <i>
      - &lt;a href=&#34;volume.md&#34;&gt;Volume&lt;/a&gt;</i>
    <a href="#nodeaffinity" title="NodeAffinity">NodeAffinity</a>: <i>
      - &lt;a href=&#34;nodeaffinity.md&#34;&gt;NodeAffinity&lt;/a&gt;</i>
    <a href="#podaffinity" title="PodAffinity">PodAffinity</a>: <i>
      - &lt;a href=&#34;podaffinity.md&#34;&gt;PodAffinity&lt;/a&gt;</i>
    <a href="#podantiaffinity" title="PodAntiAffinity">PodAntiAffinity</a>: <i>
      - &lt;a href=&#34;podantiaffinity.md&#34;&gt;PodAntiAffinity&lt;/a&gt;</i>
    <a href="#env" title="Env">Env</a>: <i>
      - &lt;a href=&#34;env.md&#34;&gt;Env&lt;/a&gt;</i>
    <a href="#envfrom" title="EnvFrom">EnvFrom</a>: <i>
      - &lt;a href=&#34;envfrom.md&#34;&gt;EnvFrom&lt;/a&gt;</i>
    <a href="#lifecycle" title="Lifecycle">Lifecycle</a>: <i>
      - &lt;a href=&#34;lifecycle.md&#34;&gt;Lifecycle&lt;/a&gt;</i>
    <a href="#livenessprobe" title="LivenessProbe">LivenessProbe</a>: <i>
      - &lt;a href=&#34;livenessprobe.md&#34;&gt;LivenessProbe&lt;/a&gt;</i>
    <a href="#port" title="Port">Port</a>: <i>
      - &lt;a href=&#34;port.md&#34;&gt;Port&lt;/a&gt;</i>
    <a href="#readinessprobe" title="ReadinessProbe">ReadinessProbe</a>: <i>
      - &lt;a href=&#34;readinessprobe.md&#34;&gt;ReadinessProbe&lt;/a&gt;</i>
    <a href="#resources" title="Resources">Resources</a>: <i>
      - &lt;a href=&#34;resources.md&#34;&gt;Resources&lt;/a&gt;</i>
    <a href="#startupprobe" title="StartupProbe">StartupProbe</a>: <i>
      - &lt;a href=&#34;startupprobe.md&#34;&gt;StartupProbe&lt;/a&gt;</i>
    <a href="#volumemount" title="VolumeMount">VolumeMount</a>: <i>
      - &lt;a href=&#34;volumemount.md&#34;&gt;VolumeMount&lt;/a&gt;</i>
    <a href="#option" title="Option">Option</a>: <i>
      - &lt;a href=&#34;option.md&#34;&gt;Option&lt;/a&gt;</i>
    <a href="#capabilities" title="Capabilities">Capabilities</a>: <i>
      - &lt;a href=&#34;capabilities.md&#34;&gt;Capabilities&lt;/a&gt;</i>
    <a href="#selinuxoptions" title="SeLinuxOptions">SeLinuxOptions</a>: <i>
      - &lt;a href=&#34;selinuxoptions.md&#34;&gt;SeLinuxOptions&lt;/a&gt;</i>
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
    <a href="#configmap" title="ConfigMap">ConfigMap</a>: <i>
      - &lt;a href=&#34;configmap.md&#34;&gt;ConfigMap&lt;/a&gt;</i>
    <a href="#downwardapi" title="DownwardApi">DownwardApi</a>: <i>
      - &lt;a href=&#34;downwardapi.md&#34;&gt;DownwardApi&lt;/a&gt;</i>
    <a href="#emptydir" title="EmptyDir">EmptyDir</a>: <i>
      - &lt;a href=&#34;emptydir.md&#34;&gt;EmptyDir&lt;/a&gt;</i>
    <a href="#fc" title="Fc">Fc</a>: <i>
      - &lt;a href=&#34;fc.md&#34;&gt;Fc&lt;/a&gt;</i>
    <a href="#flexvolume" title="FlexVolume">FlexVolume</a>: <i>
      - &lt;a href=&#34;flexvolume.md&#34;&gt;FlexVolume&lt;/a&gt;</i>
    <a href="#flocker" title="Flocker">Flocker</a>: <i>
      - &lt;a href=&#34;flocker.md&#34;&gt;Flocker&lt;/a&gt;</i>
    <a href="#gcepersistentdisk" title="GcePersistentDisk">GcePersistentDisk</a>: <i>
      - &lt;a href=&#34;gcepersistentdisk.md&#34;&gt;GcePersistentDisk&lt;/a&gt;</i>
    <a href="#gitrepo" title="GitRepo">GitRepo</a>: <i>
      - &lt;a href=&#34;gitrepo.md&#34;&gt;GitRepo&lt;/a&gt;</i>
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
    <a href="#persistentvolumeclaim" title="PersistentVolumeClaim">PersistentVolumeClaim</a>: <i>
      - &lt;a href=&#34;persistentvolumeclaim.md&#34;&gt;PersistentVolumeClaim&lt;/a&gt;</i>
    <a href="#photonpersistentdisk" title="PhotonPersistentDisk">PhotonPersistentDisk</a>: <i>
      - &lt;a href=&#34;photonpersistentdisk.md&#34;&gt;PhotonPersistentDisk&lt;/a&gt;</i>
    <a href="#quobyte" title="Quobyte">Quobyte</a>: <i>
      - &lt;a href=&#34;quobyte.md&#34;&gt;Quobyte&lt;/a&gt;</i>
    <a href="#rbd" title="Rbd">Rbd</a>: <i>
      - &lt;a href=&#34;rbd.md&#34;&gt;Rbd&lt;/a&gt;</i>
    <a href="#secret" title="Secret">Secret</a>: <i>
      - &lt;a href=&#34;secret.md&#34;&gt;Secret&lt;/a&gt;</i>
    <a href="#vspherevolume" title="VsphereVolume">VsphereVolume</a>: <i>
      - &lt;a href=&#34;vspherevolume.md&#34;&gt;VsphereVolume&lt;/a&gt;</i>
    <a href="#preferredduringschedulingignoredduringexecution" title="PreferredDuringSchedulingIgnoredDuringExecution">PreferredDuringSchedulingIgnoredDuringExecution</a>: <i>
      - &lt;a href=&#34;preferredduringschedulingignoredduringexecution.md&#34;&gt;PreferredDuringSchedulingIgnoredDuringExecution&lt;/a&gt;</i>
    <a href="#requiredduringschedulingignoredduringexecution" title="RequiredDuringSchedulingIgnoredDuringExecution">RequiredDuringSchedulingIgnoredDuringExecution</a>: <i>
      - &lt;a href=&#34;requiredduringschedulingignoredduringexecution.md&#34;&gt;RequiredDuringSchedulingIgnoredDuringExecution&lt;/a&gt;</i>
    <a href="#valuefrom" title="ValueFrom">ValueFrom</a>: <i>
      - &lt;a href=&#34;valuefrom.md&#34;&gt;ValueFrom&lt;/a&gt;</i>
    <a href="#configmapref" title="ConfigMapRef">ConfigMapRef</a>: <i>
      - &lt;a href=&#34;configmapref.md&#34;&gt;ConfigMapRef&lt;/a&gt;</i>
    <a href="#secretref" title="SecretRef">SecretRef</a>: <i>
      - &lt;a href=&#34;secretref.md&#34;&gt;SecretRef&lt;/a&gt;</i>
    <a href="#poststart" title="PostStart">PostStart</a>: <i>
      - &lt;a href=&#34;poststart.md&#34;&gt;PostStart&lt;/a&gt;</i>
    <a href="#prestop" title="PreStop">PreStop</a>: <i>
      - &lt;a href=&#34;prestop.md&#34;&gt;PreStop&lt;/a&gt;</i>
    <a href="#exec" title="Exec">Exec</a>: <i>
      - &lt;a href=&#34;exec.md&#34;&gt;Exec&lt;/a&gt;</i>
    <a href="#httpget" title="HttpGet">HttpGet</a>: <i>
      - &lt;a href=&#34;httpget.md&#34;&gt;HttpGet&lt;/a&gt;</i>
    <a href="#tcpsocket" title="TcpSocket">TcpSocket</a>: <i>
      - &lt;a href=&#34;tcpsocket.md&#34;&gt;TcpSocket&lt;/a&gt;</i>
    <a href="#limits" title="Limits">Limits</a>: <i>
      - &lt;a href=&#34;limits.md&#34;&gt;Limits&lt;/a&gt;</i>
    <a href="#requests" title="Requests">Requests</a>: <i>
      - &lt;a href=&#34;requests.md&#34;&gt;Requests&lt;/a&gt;</i>
    <a href="#items" title="Items">Items</a>: <i>
      - &lt;a href=&#34;items.md&#34;&gt;Items&lt;/a&gt;</i>
    <a href="#podaffinityterm" title="PodAffinityTerm">PodAffinityTerm</a>: <i>
      - &lt;a href=&#34;podaffinityterm.md&#34;&gt;PodAffinityTerm&lt;/a&gt;</i>
    <a href="#labelselector" title="LabelSelector">LabelSelector</a>: <i>
      - &lt;a href=&#34;labelselector.md&#34;&gt;LabelSelector&lt;/a&gt;</i>
    <a href="#configmapkeyref" title="ConfigMapKeyRef">ConfigMapKeyRef</a>: <i>
      - &lt;a href=&#34;configmapkeyref.md&#34;&gt;ConfigMapKeyRef&lt;/a&gt;</i>
    <a href="#fieldref" title="FieldRef">FieldRef</a>: <i>
      - &lt;a href=&#34;fieldref.md&#34;&gt;FieldRef&lt;/a&gt;</i>
    <a href="#resourcefieldref" title="ResourceFieldRef">ResourceFieldRef</a>: <i>
      - &lt;a href=&#34;resourcefieldref.md&#34;&gt;ResourceFieldRef&lt;/a&gt;</i>
    <a href="#secretkeyref" title="SecretKeyRef">SecretKeyRef</a>: <i>
      - &lt;a href=&#34;secretkeyref.md&#34;&gt;SecretKeyRef&lt;/a&gt;</i>
    <a href="#httpheader" title="HttpHeader">HttpHeader</a>: <i>
      - &lt;a href=&#34;httpheader.md&#34;&gt;HttpHeader&lt;/a&gt;</i>
    <a href="#matchexpressions" title="MatchExpressions">MatchExpressions</a>: <i>
      - &lt;a href=&#34;matchexpressions.md&#34;&gt;MatchExpressions&lt;/a&gt;</i>
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

#### Affinity

_Required_: No

_Type_: List of &lt;a href=&#34;affinity.md&#34;&gt;Affinity&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Container

_Required_: No

_Type_: List of &lt;a href=&#34;container.md&#34;&gt;Container&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsConfig

_Required_: No

_Type_: List of &lt;a href=&#34;dnsconfig.md&#34;&gt;DnsConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostAliases

_Required_: No

_Type_: List of &lt;a href=&#34;hostaliases.md&#34;&gt;HostAliases&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImagePullSecrets

_Required_: No

_Type_: List of &lt;a href=&#34;imagepullsecrets.md&#34;&gt;ImagePullSecrets&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitContainer

_Required_: No

_Type_: List of &lt;a href=&#34;initcontainer.md&#34;&gt;InitContainer&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityContext

_Required_: No

_Type_: List of &lt;a href=&#34;securitycontext.md&#34;&gt;SecurityContext&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Toleration

_Required_: No

_Type_: List of &lt;a href=&#34;toleration.md&#34;&gt;Toleration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Volume

_Required_: No

_Type_: List of &lt;a href=&#34;volume.md&#34;&gt;Volume&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeAffinity

_Required_: No

_Type_: List of &lt;a href=&#34;nodeaffinity.md&#34;&gt;NodeAffinity&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PodAffinity

_Required_: No

_Type_: List of &lt;a href=&#34;podaffinity.md&#34;&gt;PodAffinity&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PodAntiAffinity

_Required_: No

_Type_: List of &lt;a href=&#34;podantiaffinity.md&#34;&gt;PodAntiAffinity&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Env

_Required_: No

_Type_: List of &lt;a href=&#34;env.md&#34;&gt;Env&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvFrom

_Required_: No

_Type_: List of &lt;a href=&#34;envfrom.md&#34;&gt;EnvFrom&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lifecycle

_Required_: No

_Type_: List of &lt;a href=&#34;lifecycle.md&#34;&gt;Lifecycle&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LivenessProbe

_Required_: No

_Type_: List of &lt;a href=&#34;livenessprobe.md&#34;&gt;LivenessProbe&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: List of &lt;a href=&#34;port.md&#34;&gt;Port&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadinessProbe

_Required_: No

_Type_: List of &lt;a href=&#34;readinessprobe.md&#34;&gt;ReadinessProbe&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resources

_Required_: No

_Type_: List of &lt;a href=&#34;resources.md&#34;&gt;Resources&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartupProbe

_Required_: No

_Type_: List of &lt;a href=&#34;startupprobe.md&#34;&gt;StartupProbe&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeMount

_Required_: No

_Type_: List of &lt;a href=&#34;volumemount.md&#34;&gt;VolumeMount&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Option

_Required_: No

_Type_: List of &lt;a href=&#34;option.md&#34;&gt;Option&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Capabilities

_Required_: No

_Type_: List of &lt;a href=&#34;capabilities.md&#34;&gt;Capabilities&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeLinuxOptions

_Required_: No

_Type_: List of &lt;a href=&#34;selinuxoptions.md&#34;&gt;SeLinuxOptions&lt;/a&gt;

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

#### ConfigMap

_Required_: No

_Type_: List of &lt;a href=&#34;configmap.md&#34;&gt;ConfigMap&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DownwardApi

_Required_: No

_Type_: List of &lt;a href=&#34;downwardapi.md&#34;&gt;DownwardApi&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmptyDir

_Required_: No

_Type_: List of &lt;a href=&#34;emptydir.md&#34;&gt;EmptyDir&lt;/a&gt;

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

#### GitRepo

_Required_: No

_Type_: List of &lt;a href=&#34;gitrepo.md&#34;&gt;GitRepo&lt;/a&gt;

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

#### PersistentVolumeClaim

_Required_: No

_Type_: List of &lt;a href=&#34;persistentvolumeclaim.md&#34;&gt;PersistentVolumeClaim&lt;/a&gt;

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

#### Secret

_Required_: No

_Type_: List of &lt;a href=&#34;secret.md&#34;&gt;Secret&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsphereVolume

_Required_: No

_Type_: List of &lt;a href=&#34;vspherevolume.md&#34;&gt;VsphereVolume&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreferredDuringSchedulingIgnoredDuringExecution

_Required_: No

_Type_: List of &lt;a href=&#34;preferredduringschedulingignoredduringexecution.md&#34;&gt;PreferredDuringSchedulingIgnoredDuringExecution&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequiredDuringSchedulingIgnoredDuringExecution

_Required_: No

_Type_: List of &lt;a href=&#34;requiredduringschedulingignoredduringexecution.md&#34;&gt;RequiredDuringSchedulingIgnoredDuringExecution&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValueFrom

_Required_: No

_Type_: List of &lt;a href=&#34;valuefrom.md&#34;&gt;ValueFrom&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigMapRef

_Required_: No

_Type_: List of &lt;a href=&#34;configmapref.md&#34;&gt;ConfigMapRef&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretRef

_Required_: No

_Type_: List of &lt;a href=&#34;secretref.md&#34;&gt;SecretRef&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PostStart

_Required_: No

_Type_: List of &lt;a href=&#34;poststart.md&#34;&gt;PostStart&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreStop

_Required_: No

_Type_: List of &lt;a href=&#34;prestop.md&#34;&gt;PreStop&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Exec

_Required_: No

_Type_: List of &lt;a href=&#34;exec.md&#34;&gt;Exec&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpGet

_Required_: No

_Type_: List of &lt;a href=&#34;httpget.md&#34;&gt;HttpGet&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpSocket

_Required_: No

_Type_: List of &lt;a href=&#34;tcpsocket.md&#34;&gt;TcpSocket&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Limits

_Required_: No

_Type_: List of &lt;a href=&#34;limits.md&#34;&gt;Limits&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Requests

_Required_: No

_Type_: List of &lt;a href=&#34;requests.md&#34;&gt;Requests&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Items

_Required_: No

_Type_: List of &lt;a href=&#34;items.md&#34;&gt;Items&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PodAffinityTerm

_Required_: No

_Type_: List of &lt;a href=&#34;podaffinityterm.md&#34;&gt;PodAffinityTerm&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LabelSelector

_Required_: No

_Type_: List of &lt;a href=&#34;labelselector.md&#34;&gt;LabelSelector&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigMapKeyRef

_Required_: No

_Type_: List of &lt;a href=&#34;configmapkeyref.md&#34;&gt;ConfigMapKeyRef&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FieldRef

_Required_: No

_Type_: List of &lt;a href=&#34;fieldref.md&#34;&gt;FieldRef&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceFieldRef

_Required_: No

_Type_: List of &lt;a href=&#34;resourcefieldref.md&#34;&gt;ResourceFieldRef&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretKeyRef

_Required_: No

_Type_: List of &lt;a href=&#34;secretkeyref.md&#34;&gt;SecretKeyRef&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpHeader

_Required_: No

_Type_: List of &lt;a href=&#34;httpheader.md&#34;&gt;HttpHeader&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchExpressions

_Required_: No

_Type_: List of &lt;a href=&#34;matchexpressions.md&#34;&gt;MatchExpressions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

