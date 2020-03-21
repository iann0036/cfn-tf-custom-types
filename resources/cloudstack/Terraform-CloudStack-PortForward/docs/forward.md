# Terraform::CloudStack::PortForward Forward

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#privateport" title="PrivatePort">PrivatePort</a>" : <i>Double</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#publicport" title="PublicPort">PublicPort</a>" : <i>Double</i>,
    "<a href="#virtualmachineid" title="VirtualMachineId">VirtualMachineId</a>" : <i>String</i>,
    "<a href="#vmguestip" title="VmGuestIp">VmGuestIp</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#privateport" title="PrivatePort">PrivatePort</a>: <i>Double</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#publicport" title="PublicPort">PublicPort</a>: <i>Double</i>
<a href="#virtualmachineid" title="VirtualMachineId">VirtualMachineId</a>: <i>String</i>
<a href="#vmguestip" title="VmGuestIp">VmGuestIp</a>: <i>String</i>
</pre>

## Properties

#### PrivatePort

The private port to forward to.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

The name of the protocol to allow. Valid options are:
`tcp` and `udp`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicPort

The public port to forward from.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualMachineId

The ID of the virtual machine to forward to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmGuestIp

The virtual machine IP address for the port
forwarding rule (useful when the virtual machine has secondairy NICs
or IP addresses).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

