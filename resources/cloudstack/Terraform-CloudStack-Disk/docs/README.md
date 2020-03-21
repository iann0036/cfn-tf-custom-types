# Terraform::CloudStack::Disk

Creates a disk volume from a disk offering. This disk volume will be attached to
a virtual machine if the optional parameters are configured.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::CloudStack::Disk",
    "Properties" : {
        "<a href="#attach" title="Attach">Attach</a>" : <i>Boolean</i>,
        "<a href="#deviceid" title="DeviceId">DeviceId</a>" : <i>Double</i>,
        "<a href="#diskoffering" title="DiskOffering">DiskOffering</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#shrinkok" title="ShrinkOk">ShrinkOk</a>" : <i>Boolean</i>,
        "<a href="#size" title="Size">Size</a>" : <i>Double</i>,
        "<a href="#virtualmachineid" title="VirtualMachineId">VirtualMachineId</a>" : <i>String</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::CloudStack::Disk
Properties:
    <a href="#attach" title="Attach">Attach</a>: <i>Boolean</i>
    <a href="#deviceid" title="DeviceId">DeviceId</a>: <i>Double</i>
    <a href="#diskoffering" title="DiskOffering">DiskOffering</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#shrinkok" title="ShrinkOk">ShrinkOk</a>: <i>Boolean</i>
    <a href="#size" title="Size">Size</a>: <i>Double</i>
    <a href="#virtualmachineid" title="VirtualMachineId">VirtualMachineId</a>: <i>String</i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
</pre>

## Properties

#### Attach

Determines whether or not to attach the disk volume to a
virtual machine (defaults false).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceId

The device ID to map the disk volume to within the guest OS.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskOffering

The name or ID of the disk offering to use for
this disk volume.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the disk volume. Changing this forces a new
resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The name or ID of the project to deploy this
instance to. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShrinkOk

Verifies if the disk volume is allowed to shrink when
resizing (defaults false).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

The size of the disk volume in gigabytes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualMachineId

The ID of the virtual machine to which you want
to attach the disk volume.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

The name or ID of the zone where this disk volume will be available.
Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

