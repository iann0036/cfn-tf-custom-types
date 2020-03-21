# Terraform::Google::DataprocCluster WorkerConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#imageuri" title="ImageUri">ImageUri</a>" : <i>String</i>,
    "<a href="#machinetype" title="MachineType">MachineType</a>" : <i>String</i>,
    "<a href="#mincpuplatform" title="MinCpuPlatform">MinCpuPlatform</a>" : <i>String</i>,
    "<a href="#numinstances" title="NumInstances">NumInstances</a>" : <i>Double</i>,
    "<a href="#accelerators" title="Accelerators">Accelerators</a>" : <i>[ &lt;a href=&#34;workerconfig-accelerators.md&#34;&gt;Accelerators&lt;/a&gt;, ... ]</i>,
    "<a href="#diskconfig" title="DiskConfig">DiskConfig</a>" : <i>[ &lt;a href=&#34;workerconfig-diskconfig.md&#34;&gt;DiskConfig&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#imageuri" title="ImageUri">ImageUri</a>: <i>String</i>
<a href="#machinetype" title="MachineType">MachineType</a>: <i>String</i>
<a href="#mincpuplatform" title="MinCpuPlatform">MinCpuPlatform</a>: <i>String</i>
<a href="#numinstances" title="NumInstances">NumInstances</a>: <i>Double</i>
<a href="#accelerators" title="Accelerators">Accelerators</a>: <i>
      - &lt;a href=&#34;workerconfig-accelerators.md&#34;&gt;Accelerators&lt;/a&gt;</i>
<a href="#diskconfig" title="DiskConfig">DiskConfig</a>: <i>
      - &lt;a href=&#34;workerconfig-diskconfig.md&#34;&gt;DiskConfig&lt;/a&gt;</i>
</pre>

## Properties

#### ImageUri

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MachineType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinCpuPlatform

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumInstances

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Accelerators

_Required_: No
_Type_: List of &lt;a href=&#34;workerconfig-accelerators.md&#34;&gt;Accelerators&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskConfig

_Required_: No
_Type_: List of &lt;a href=&#34;workerconfig-diskconfig.md&#34;&gt;DiskConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

