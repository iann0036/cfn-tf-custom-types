# Terraform::Google::ComputeReservation InstanceProperties

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#machinetype" title="MachineType">MachineType</a>" : <i>String</i>,
    "<a href="#mincpuplatform" title="MinCpuPlatform">MinCpuPlatform</a>" : <i>String</i>,
    "<a href="#guestaccelerators" title="GuestAccelerators">GuestAccelerators</a>" : <i>[ &lt;a href=&#34;instanceproperties-guestaccelerators.md&#34;&gt;GuestAccelerators&lt;/a&gt;, ... ]</i>,
    "<a href="#localssds" title="LocalSsds">LocalSsds</a>" : <i>[ &lt;a href=&#34;instanceproperties-localssds.md&#34;&gt;LocalSsds&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#machinetype" title="MachineType">MachineType</a>: <i>String</i>
<a href="#mincpuplatform" title="MinCpuPlatform">MinCpuPlatform</a>: <i>String</i>
<a href="#guestaccelerators" title="GuestAccelerators">GuestAccelerators</a>: <i>
      - &lt;a href=&#34;instanceproperties-guestaccelerators.md&#34;&gt;GuestAccelerators&lt;/a&gt;</i>
<a href="#localssds" title="LocalSsds">LocalSsds</a>: <i>
      - &lt;a href=&#34;instanceproperties-localssds.md&#34;&gt;LocalSsds&lt;/a&gt;</i>
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
_Type_: List of &lt;a href=&#34;instanceproperties-guestaccelerators.md&#34;&gt;GuestAccelerators&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalSsds

_Required_: No
_Type_: List of &lt;a href=&#34;instanceproperties-localssds.md&#34;&gt;LocalSsds&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

