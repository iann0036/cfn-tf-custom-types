# Terraform::VSphere::VirtualDisk

The `vsphere_virtual_disk` resource can be used to create virtual disks outside
of any given [`vsphere_virtual_machine`][docs-vsphere-virtual-machine]
resource. These disks can be attached to a virtual machine by creating a disk
block with the [`attach`][docs-vsphere-virtual-machine-disk-attach] parameter.

[docs-vsphere-virtual-machine]: /docs/providers/vsphere/r/virtual_machine.html
[docs-vsphere-virtual-machine-disk-attach]: /docs/providers/vsphere/r/virtual_machine.html#attach

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VSphere::VirtualDisk",
    "Properties" : {
        "<a href="#adaptertype" title="AdapterType">AdapterType</a>" : <i>String</i>,
        "<a href="#createdirectories" title="CreateDirectories">CreateDirectories</a>" : <i>Boolean</i>,
        "<a href="#datacenter" title="Datacenter">Datacenter</a>" : <i>String</i>,
        "<a href="#datastore" title="Datastore">Datastore</a>" : <i>String</i>,
        "<a href="#size" title="Size">Size</a>" : <i>Double</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#vmdkpath" title="VmdkPath">VmdkPath</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VSphere::VirtualDisk
Properties:
    <a href="#adaptertype" title="AdapterType">AdapterType</a>: <i>String</i>
    <a href="#createdirectories" title="CreateDirectories">CreateDirectories</a>: <i>Boolean</i>
    <a href="#datacenter" title="Datacenter">Datacenter</a>: <i>String</i>
    <a href="#datastore" title="Datastore">Datastore</a>: <i>String</i>
    <a href="#size" title="Size">Size</a>: <i>Double</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#vmdkpath" title="VmdkPath">VmdkPath</a>: <i>String</i>
</pre>

## Properties

#### AdapterType

The adapter type for this virtual disk. Can be
one of `ide`, `lsiLogic`, or `busLogic`.  Default: `lsiLogic`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateDirectories

Tells the resource to create any
directories that are a part of the `vmdk_path` parameter if they are missing.
Default: `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Datacenter

The name of the datacenter in which to create the
disk. Can be omitted when when ESXi or if there is only one datacenter in
your infrastructure.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Datastore

The name of the datastore in which to create the
disk.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

Size of the disk (in GB).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of disk to create. Can be one of
`eagerZeroedThick`, `lazy`, or `thin`. Default: `eagerZeroedThick`. For
information on what each kind of disk provisioning policy means, click
[here][docs-vmware-vm-disk-provisioning].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmdkPath

The path, including filename, of the virtual disk to
be created.  This needs to end in `.vmdk`.

_Required_: Yes

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

