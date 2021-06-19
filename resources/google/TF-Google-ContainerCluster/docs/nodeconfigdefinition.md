# TF::Google::ContainerCluster NodeConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#disksizegb" title="DiskSizeGb">DiskSizeGb</a>" : <i>Double</i>,
    "<a href="#disktype" title="DiskType">DiskType</a>" : <i>String</i>,
    "<a href="#guestaccelerator" title="GuestAccelerator">GuestAccelerator</a>" : <i>[ <a href="guestacceleratordefinition2.md">GuestAcceleratorDefinition2</a>, ... ]</i>,
    "<a href="#imagetype" title="ImageType">ImageType</a>" : <i>String</i>,
    "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition2.md">LabelsDefinition2</a>, ... ]</i>,
    "<a href="#localssdcount" title="LocalSsdCount">LocalSsdCount</a>" : <i>Double</i>,
    "<a href="#machinetype" title="MachineType">MachineType</a>" : <i>String</i>,
    "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadatadefinition2.md">MetadataDefinition2</a>, ... ]</i>,
    "<a href="#mincpuplatform" title="MinCpuPlatform">MinCpuPlatform</a>" : <i>String</i>,
    "<a href="#oauthscopes" title="OauthScopes">OauthScopes</a>" : <i>[ String, ... ]</i>,
    "<a href="#preemptible" title="Preemptible">Preemptible</a>" : <i>Boolean</i>,
    "<a href="#serviceaccount" title="ServiceAccount">ServiceAccount</a>" : <i>String</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
    "<a href="#taint" title="Taint">Taint</a>" : <i>[ <a href="taintdefinition2.md">TaintDefinition2</a>, ... ]</i>,
    "<a href="#shieldedinstanceconfig" title="ShieldedInstanceConfig">ShieldedInstanceConfig</a>" : <i>[ <a href="shieldedinstanceconfigdefinition.md">ShieldedInstanceConfigDefinition</a>, ... ]</i>,
    "<a href="#workloadmetadataconfig" title="WorkloadMetadataConfig">WorkloadMetadataConfig</a>" : <i>[ <a href="workloadmetadataconfigdefinition.md">WorkloadMetadataConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#disksizegb" title="DiskSizeGb">DiskSizeGb</a>: <i>Double</i>
<a href="#disktype" title="DiskType">DiskType</a>: <i>String</i>
<a href="#guestaccelerator" title="GuestAccelerator">GuestAccelerator</a>: <i>
      - <a href="guestacceleratordefinition2.md">GuestAcceleratorDefinition2</a></i>
<a href="#imagetype" title="ImageType">ImageType</a>: <i>String</i>
<a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition2.md">LabelsDefinition2</a></i>
<a href="#localssdcount" title="LocalSsdCount">LocalSsdCount</a>: <i>Double</i>
<a href="#machinetype" title="MachineType">MachineType</a>: <i>String</i>
<a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadatadefinition2.md">MetadataDefinition2</a></i>
<a href="#mincpuplatform" title="MinCpuPlatform">MinCpuPlatform</a>: <i>String</i>
<a href="#oauthscopes" title="OauthScopes">OauthScopes</a>: <i>
      - String</i>
<a href="#preemptible" title="Preemptible">Preemptible</a>: <i>Boolean</i>
<a href="#serviceaccount" title="ServiceAccount">ServiceAccount</a>: <i>String</i>
<a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
<a href="#taint" title="Taint">Taint</a>: <i>
      - <a href="taintdefinition2.md">TaintDefinition2</a></i>
<a href="#shieldedinstanceconfig" title="ShieldedInstanceConfig">ShieldedInstanceConfig</a>: <i>
      - <a href="shieldedinstanceconfigdefinition.md">ShieldedInstanceConfigDefinition</a></i>
<a href="#workloadmetadataconfig" title="WorkloadMetadataConfig">WorkloadMetadataConfig</a>: <i>
      - <a href="workloadmetadataconfigdefinition.md">WorkloadMetadataConfigDefinition</a></i>
</pre>

## Properties

#### DiskSizeGb

Size of the disk attached to each node, specified
in GB. The smallest allowed disk size is 10GB. Defaults to 100GB.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskType

Type of the disk attached to each node
(e.g. 'pd-standard', 'pd-balanced' or 'pd-ssd'). If unspecified, the default disk type is 'pd-standard'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestAccelerator

List of the type and count of accelerator cards attached to the instance.
Structure documented below.
To support removal of guest_accelerators in Terraform 0.12 this field is an
[Attribute as Block](/docs/configuration/attr-as-blocks.html).

_Required_: No

_Type_: List of <a href="guestacceleratordefinition2.md">GuestAcceleratorDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageType

The image type to use for this node. Note that changing the image type
will delete and recreate all nodes in the node pool.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

The Kubernetes labels (key/value pairs) to be applied to each node. The kubernetes.io/ and k8s.io/ prefixes are
reserved by Kubernetes Core components and cannot be specified.

_Required_: No

_Type_: List of <a href="labelsdefinition2.md">LabelsDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalSsdCount

The amount of local SSD disks that will be
attached to each cluster node. Defaults to 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MachineType

The name of a Google Compute Engine machine type.
Defaults to `e2-medium`. To create a custom machine type, value should be set as specified
[here](https://cloud.google.com/compute/docs/reference/latest/instances#machineType).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

The metadata key/value pairs assigned to instances in
the cluster. From GKE `1.12` onwards, `disable-legacy-endpoints` is set to
`true` by the API; if `metadata` is set but that default value is not
included, Terraform will attempt to unset the value. To avoid this, set the
value in your config.

_Required_: No

_Type_: List of <a href="metadatadefinition2.md">MetadataDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinCpuPlatform

Minimum CPU platform to be used by this instance.
The instance may be scheduled on the specified or newer CPU platform. Applicable
values are the friendly names of CPU platforms, such as `Intel Haswell`. See the
[official documentation](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform)
for more information.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OauthScopes

The set of Google API scopes to be made available
on all of the node VMs under the "default" service account.
Use the "https://www.googleapis.com/auth/cloud-platform" scope to grant access to all APIs. It is recommended that you set `service_account` to a non-default service account and grant IAM roles to that service account for only the resources that it needs.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Preemptible

A boolean that represents whether or not the underlying node VMs
are preemptible. See the [official documentation](https://cloud.google.com/container-engine/docs/preemptible-vm)
for more information. Defaults to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccount

The service account to be used by the Node VMs.
If not specified, the "default" service account is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

The list of instance tags applied to all nodes. Tags are used to identify
valid sources or targets for network firewalls.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Taint

A list of [Kubernetes taints](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/)
to apply to nodes. GKE's API can only set this field on cluster creation.
However, GKE will add taints to your nodes if you enable certain features such
as GPUs. If this field is set, any diffs on this field will cause Terraform to
recreate the underlying resource. Taint values can be updated safely in
Kubernetes (eg. through `kubectl`), and it's recommended that you do not use
this field to manage taints. If you do, `lifecycle.ignore_changes` is
recommended. Structure is documented below.

_Required_: No

_Type_: List of <a href="taintdefinition2.md">TaintDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShieldedInstanceConfig

_Required_: No

_Type_: List of <a href="shieldedinstanceconfigdefinition.md">ShieldedInstanceConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkloadMetadataConfig

_Required_: No

_Type_: List of <a href="workloadmetadataconfigdefinition.md">WorkloadMetadataConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

