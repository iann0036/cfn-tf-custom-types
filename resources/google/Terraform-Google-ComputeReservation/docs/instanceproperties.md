# Terraform::Google::ComputeReservation InstanceProperties

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#machinetype" title="MachineType">MachineType</a>" : <i>String</i>,
    "<a href="#mincpuplatform" title="MinCpuPlatform">MinCpuPlatform</a>" : <i>String</i>,
    "<a href="#guestaccelerators" title="GuestAccelerators">GuestAccelerators</a>" : <i>[ <a href="instanceproperties-guestaccelerators.md">GuestAccelerators</a>, ... ]</i>,
    "<a href="#localssds" title="LocalSsds">LocalSsds</a>" : <i>[ <a href="instanceproperties-localssds.md">LocalSsds</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#machinetype" title="MachineType">MachineType</a>: <i>String</i>
<a href="#mincpuplatform" title="MinCpuPlatform">MinCpuPlatform</a>: <i>String</i>
<a href="#guestaccelerators" title="GuestAccelerators">GuestAccelerators</a>: <i>
      - <a href="instanceproperties-guestaccelerators.md">GuestAccelerators</a></i>
<a href="#localssds" title="LocalSsds">LocalSsds</a>: <i>
      - <a href="instanceproperties-localssds.md">LocalSsds</a></i>
</pre>

## Properties

#### MachineType

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinCpuPlatform

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestAccelerators

_Required_: No
_Type_: List of <a href="instanceproperties-guestaccelerators.md">GuestAccelerators</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalSsds

_Required_: No
_Type_: List of <a href="instanceproperties-localssds.md">LocalSsds</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

