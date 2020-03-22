# Terraform::CloudStack::StaticNat

Enables static NAT for a given IP address

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::CloudStack::StaticNat",
    "Properties" : {
        "<a href="#ipaddressid" title="IpAddressId">IpAddressId</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#virtualmachineid" title="VirtualMachineId">VirtualMachineId</a>" : <i>String</i>,
        "<a href="#vmguestip" title="VmGuestIp">VmGuestIp</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::CloudStack::StaticNat
Properties:
    <a href="#ipaddressid" title="IpAddressId">IpAddressId</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#virtualmachineid" title="VirtualMachineId">VirtualMachineId</a>: <i>String</i>
    <a href="#vmguestip" title="VmGuestIp">VmGuestIp</a>: <i>String</i>
</pre>

## Properties

#### IpAddressId

The public IP address ID for which static
NAT will be enabled. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The name or ID of the project to deploy this
instance to. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualMachineId

The virtual machine ID to enable the
static NAT feature for. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmGuestIp

The virtual machine IP address to forward the
static NAT traffic to (useful when the virtual machine has secondary
NICs or IP addresses). Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

