# TF::FortiOS::SwitchcontrollerManagedswitch SnmpTrapThresholdDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#traphighcputhreshold" title="TrapHighCpuThreshold">TrapHighCpuThreshold</a>" : <i>Double</i>,
    "<a href="#traplogfullthreshold" title="TrapLogFullThreshold">TrapLogFullThreshold</a>" : <i>Double</i>,
    "<a href="#traplowmemorythreshold" title="TrapLowMemoryThreshold">TrapLowMemoryThreshold</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#traphighcputhreshold" title="TrapHighCpuThreshold">TrapHighCpuThreshold</a>: <i>Double</i>
<a href="#traplogfullthreshold" title="TrapLogFullThreshold">TrapLogFullThreshold</a>: <i>Double</i>
<a href="#traplowmemorythreshold" title="TrapLowMemoryThreshold">TrapLowMemoryThreshold</a>: <i>Double</i>
</pre>

## Properties

#### TrapHighCpuThreshold

CPU usage when trap is sent.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrapLogFullThreshold

Log disk usage when trap is sent.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrapLowMemoryThreshold

Memory usage when trap is sent.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

