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
    "<a href="#accelerators" title="Accelerators">Accelerators</a>" : <i>[ <a href="workerconfig-accelerators.md">Accelerators</a>, ... ]</i>,
    "<a href="#diskconfig" title="DiskConfig">DiskConfig</a>" : <i>[ <a href="workerconfig-diskconfig.md">DiskConfig</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#imageuri" title="ImageUri">ImageUri</a>: <i>String</i>
<a href="#machinetype" title="MachineType">MachineType</a>: <i>String</i>
<a href="#mincpuplatform" title="MinCpuPlatform">MinCpuPlatform</a>: <i>String</i>
<a href="#numinstances" title="NumInstances">NumInstances</a>: <i>Double</i>
<a href="#accelerators" title="Accelerators">Accelerators</a>: <i>
      - <a href="workerconfig-accelerators.md">Accelerators</a></i>
<a href="#diskconfig" title="DiskConfig">DiskConfig</a>: <i>
      - <a href="workerconfig-diskconfig.md">DiskConfig</a></i>
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

_Type_: List of <a href="workerconfig-accelerators.md">Accelerators</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskConfig

_Required_: No

_Type_: List of <a href="workerconfig-diskconfig.md">DiskConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

