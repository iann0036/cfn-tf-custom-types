# TF::AzureRM::KubernetesClusterNodePool KubeletConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowedunsafesysctls" title="AllowedUnsafeSysctls">AllowedUnsafeSysctls</a>" : <i>[ String, ... ]</i>,
    "<a href="#containerlogmaxline" title="ContainerLogMaxLine">ContainerLogMaxLine</a>" : <i>Double</i>,
    "<a href="#containerlogmaxsizemb" title="ContainerLogMaxSizeMb">ContainerLogMaxSizeMb</a>" : <i>Double</i>,
    "<a href="#cpucfsquotaenabled" title="CpuCfsQuotaEnabled">CpuCfsQuotaEnabled</a>" : <i>Boolean</i>,
    "<a href="#cpucfsquotaperiod" title="CpuCfsQuotaPeriod">CpuCfsQuotaPeriod</a>" : <i>String</i>,
    "<a href="#cpumanagerpolicy" title="CpuManagerPolicy">CpuManagerPolicy</a>" : <i>String</i>,
    "<a href="#imagegchighthreshold" title="ImageGcHighThreshold">ImageGcHighThreshold</a>" : <i>Double</i>,
    "<a href="#imagegclowthreshold" title="ImageGcLowThreshold">ImageGcLowThreshold</a>" : <i>Double</i>,
    "<a href="#podmaxpid" title="PodMaxPid">PodMaxPid</a>" : <i>Double</i>,
    "<a href="#topologymanagerpolicy" title="TopologyManagerPolicy">TopologyManagerPolicy</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#allowedunsafesysctls" title="AllowedUnsafeSysctls">AllowedUnsafeSysctls</a>: <i>
      - String</i>
<a href="#containerlogmaxline" title="ContainerLogMaxLine">ContainerLogMaxLine</a>: <i>Double</i>
<a href="#containerlogmaxsizemb" title="ContainerLogMaxSizeMb">ContainerLogMaxSizeMb</a>: <i>Double</i>
<a href="#cpucfsquotaenabled" title="CpuCfsQuotaEnabled">CpuCfsQuotaEnabled</a>: <i>Boolean</i>
<a href="#cpucfsquotaperiod" title="CpuCfsQuotaPeriod">CpuCfsQuotaPeriod</a>: <i>String</i>
<a href="#cpumanagerpolicy" title="CpuManagerPolicy">CpuManagerPolicy</a>: <i>String</i>
<a href="#imagegchighthreshold" title="ImageGcHighThreshold">ImageGcHighThreshold</a>: <i>Double</i>
<a href="#imagegclowthreshold" title="ImageGcLowThreshold">ImageGcLowThreshold</a>: <i>Double</i>
<a href="#podmaxpid" title="PodMaxPid">PodMaxPid</a>: <i>Double</i>
<a href="#topologymanagerpolicy" title="TopologyManagerPolicy">TopologyManagerPolicy</a>: <i>String</i>
</pre>

## Properties

#### AllowedUnsafeSysctls

Specifies the allow list of unsafe sysctls command or patterns (ending in `*`). Changing this forces a new resource to be created.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContainerLogMaxLine

Specifies the maximum number of container log files that can be present for a container. must be at least 2. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContainerLogMaxSizeMb

Specifies the maximum size (e.g. 10MB) of container log file before it is rotated. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuCfsQuotaEnabled

Is CPU CFS quota enforcement for containers enabled? Changing this forces a new resource to be created.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuCfsQuotaPeriod

Specifies the CPU CFS quota period value. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuManagerPolicy

Specifies the CPU Manager policy to use. Possible values are `none` and `static`, Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageGcHighThreshold

Specifies the percent of disk usage above which image garbage collection is always run. Must be between `0` and `100`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageGcLowThreshold

Specifies the percent of disk usage lower than which image garbage collection is never run. Must be between `0` and `100`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PodMaxPid

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopologyManagerPolicy

Specifies the Topology Manager policy to use. Possible values are `none`, `best-effort`, `restricted` or `single-numa-node`. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

