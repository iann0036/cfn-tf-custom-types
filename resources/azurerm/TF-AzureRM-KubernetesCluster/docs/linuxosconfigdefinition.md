# TF::AzureRM::KubernetesCluster LinuxOsConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#swapfilesizemb" title="SwapFileSizeMb">SwapFileSizeMb</a>" : <i>Double</i>,
    "<a href="#transparenthugepagedefrag" title="TransparentHugePageDefrag">TransparentHugePageDefrag</a>" : <i>String</i>,
    "<a href="#transparenthugepageenabled" title="TransparentHugePageEnabled">TransparentHugePageEnabled</a>" : <i>String</i>,
    "<a href="#sysctlconfig" title="SysctlConfig">SysctlConfig</a>" : <i>[ <a href="sysctlconfigdefinition.md">SysctlConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#swapfilesizemb" title="SwapFileSizeMb">SwapFileSizeMb</a>: <i>Double</i>
<a href="#transparenthugepagedefrag" title="TransparentHugePageDefrag">TransparentHugePageDefrag</a>: <i>String</i>
<a href="#transparenthugepageenabled" title="TransparentHugePageEnabled">TransparentHugePageEnabled</a>: <i>String</i>
<a href="#sysctlconfig" title="SysctlConfig">SysctlConfig</a>: <i>
      - <a href="sysctlconfigdefinition.md">SysctlConfigDefinition</a></i>
</pre>

## Properties

#### SwapFileSizeMb

Specifies the size of swap file on each node in MB. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransparentHugePageDefrag

specifies the defrag configuration for Transparent Huge Page. Possible values are `always`, `defer`, `defer+madvise`, `madvise` and `never`. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransparentHugePageEnabled

Specifies the Transparent Huge Page enabled configuration. Possible values are `always`, `madvise` and `never`. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SysctlConfig

_Required_: No

_Type_: List of <a href="sysctlconfigdefinition.md">SysctlConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

