# Terraform::Google::ContainerNodePool NodeConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#disksizegb" title="DiskSizeGb">DiskSizeGb</a>" : <i>Double</i>,
    "<a href="#disktype" title="DiskType">DiskType</a>" : <i>String</i>,
    "<a href="#guestaccelerator" title="GuestAccelerator">GuestAccelerator</a>" : <i>[ &lt;a href=&#34;nodeconfig-guestaccelerator.md&#34;&gt;GuestAccelerator&lt;/a&gt;, ... ]</i>,
    "<a href="#imagetype" title="ImageType">ImageType</a>" : <i>String</i>,
    "<a href="#labels" title="Labels">Labels</a>" : <i>[ &lt;a href=&#34;nodeconfig-labels.md&#34;&gt;Labels&lt;/a&gt;, ... ]</i>,
    "<a href="#localssdcount" title="LocalSsdCount">LocalSsdCount</a>" : <i>Double</i>,
    "<a href="#machinetype" title="MachineType">MachineType</a>" : <i>String</i>,
    "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ &lt;a href=&#34;nodeconfig-metadata.md&#34;&gt;Metadata&lt;/a&gt;, ... ]</i>,
    "<a href="#mincpuplatform" title="MinCpuPlatform">MinCpuPlatform</a>" : <i>String</i>,
    "<a href="#oauthscopes" title="OauthScopes">OauthScopes</a>" : <i>[ String, ... ]</i>,
    "<a href="#preemptible" title="Preemptible">Preemptible</a>" : <i>Boolean</i>,
    "<a href="#serviceaccount" title="ServiceAccount">ServiceAccount</a>" : <i>String</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
    "<a href="#taint" title="Taint">Taint</a>" : <i>[ &lt;a href=&#34;nodeconfig-taint.md&#34;&gt;Taint&lt;/a&gt;, ... ]</i>,
    "<a href="#sandboxconfig" title="SandboxConfig">SandboxConfig</a>" : <i>[ &lt;a href=&#34;nodeconfig-sandboxconfig.md&#34;&gt;SandboxConfig&lt;/a&gt;, ... ]</i>,
    "<a href="#shieldedinstanceconfig" title="ShieldedInstanceConfig">ShieldedInstanceConfig</a>" : <i>[ &lt;a href=&#34;nodeconfig-shieldedinstanceconfig.md&#34;&gt;ShieldedInstanceConfig&lt;/a&gt;, ... ]</i>,
    "<a href="#workloadmetadataconfig" title="WorkloadMetadataConfig">WorkloadMetadataConfig</a>" : <i>[ &lt;a href=&#34;nodeconfig-workloadmetadataconfig.md&#34;&gt;WorkloadMetadataConfig&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#disksizegb" title="DiskSizeGb">DiskSizeGb</a>: <i>Double</i>
<a href="#disktype" title="DiskType">DiskType</a>: <i>String</i>
<a href="#guestaccelerator" title="GuestAccelerator">GuestAccelerator</a>: <i>
      - &lt;a href=&#34;nodeconfig-guestaccelerator.md&#34;&gt;GuestAccelerator&lt;/a&gt;</i>
<a href="#imagetype" title="ImageType">ImageType</a>: <i>String</i>
<a href="#labels" title="Labels">Labels</a>: <i>
      - &lt;a href=&#34;nodeconfig-labels.md&#34;&gt;Labels&lt;/a&gt;</i>
<a href="#localssdcount" title="LocalSsdCount">LocalSsdCount</a>: <i>Double</i>
<a href="#machinetype" title="MachineType">MachineType</a>: <i>String</i>
<a href="#metadata" title="Metadata">Metadata</a>: <i>
      - &lt;a href=&#34;nodeconfig-metadata.md&#34;&gt;Metadata&lt;/a&gt;</i>
<a href="#mincpuplatform" title="MinCpuPlatform">MinCpuPlatform</a>: <i>String</i>
<a href="#oauthscopes" title="OauthScopes">OauthScopes</a>: <i>
      - String</i>
<a href="#preemptible" title="Preemptible">Preemptible</a>: <i>Boolean</i>
<a href="#serviceaccount" title="ServiceAccount">ServiceAccount</a>: <i>String</i>
<a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
<a href="#taint" title="Taint">Taint</a>: <i>
      - &lt;a href=&#34;nodeconfig-taint.md&#34;&gt;Taint&lt;/a&gt;</i>
<a href="#sandboxconfig" title="SandboxConfig">SandboxConfig</a>: <i>
      - &lt;a href=&#34;nodeconfig-sandboxconfig.md&#34;&gt;SandboxConfig&lt;/a&gt;</i>
<a href="#shieldedinstanceconfig" title="ShieldedInstanceConfig">ShieldedInstanceConfig</a>: <i>
      - &lt;a href=&#34;nodeconfig-shieldedinstanceconfig.md&#34;&gt;ShieldedInstanceConfig&lt;/a&gt;</i>
<a href="#workloadmetadataconfig" title="WorkloadMetadataConfig">WorkloadMetadataConfig</a>: <i>
      - &lt;a href=&#34;nodeconfig-workloadmetadataconfig.md&#34;&gt;WorkloadMetadataConfig&lt;/a&gt;</i>
</pre>

## Properties

#### DiskSizeGb

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestAccelerator

_Required_: No
_Type_: List of &lt;a href=&#34;nodeconfig-guestaccelerator.md&#34;&gt;GuestAccelerator&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No
_Type_: List of &lt;a href=&#34;nodeconfig-labels.md&#34;&gt;Labels&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalSsdCount

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MachineType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No
_Type_: List of &lt;a href=&#34;nodeconfig-metadata.md&#34;&gt;Metadata&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinCpuPlatform

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OauthScopes

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Preemptible

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccount

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Taint

_Required_: No
_Type_: List of &lt;a href=&#34;nodeconfig-taint.md&#34;&gt;Taint&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SandboxConfig

_Required_: No
_Type_: List of &lt;a href=&#34;nodeconfig-sandboxconfig.md&#34;&gt;SandboxConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShieldedInstanceConfig

_Required_: No
_Type_: List of &lt;a href=&#34;nodeconfig-shieldedinstanceconfig.md&#34;&gt;ShieldedInstanceConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkloadMetadataConfig

_Required_: No
_Type_: List of &lt;a href=&#34;nodeconfig-workloadmetadataconfig.md&#34;&gt;WorkloadMetadataConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

