# Terraform::VSphere::VirtualMachineSnapshot

The `vsphere_virtual_machine_snapshot` resource can be used to manage snapshots
for a virtual machine.

For more information on managing snapshots and how they work in VMware, see
[here][ext-vm-snapshot-management].

[ext-vm-snapshot-management]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vm_admin.doc/GUID-CA948C69-7F58-4519-AEB1-739545EA94E5.html

~> **NOTE:** A snapshot in VMware differs from traditional disk snapshots, and
can contain the actual running state of the virtual machine, data for all disks
that have not been set to be independent from the snapshot (including ones that
have been attached via the [attach][docs-vsphere-virtual-machine-disk-attach]
parameter to the `vsphere_virtual_machine` `disk` block), and even the
configuration of the virtual machine at the time of the snapshot. Virtual
machine, disk activity, and configuration changes post-snapshot are not
included in the original state. Use this resource with care! Neither VMware nor
HashiCorp recommends retaining snapshots for a extended period of time and does
NOT recommend using them as as backup feature. For more information on the
limitation of virtual machine snapshots, see [here][ext-vm-snap-limitations].

[docs-vsphere-virtual-machine-disk-attach]: /docs/providers/vsphere/r/virtual_machine.html#attach
[ext-vm-snap-limitations]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vm_admin.doc/GUID-53F65726-A23B-4CF0-A7D5-48E584B88613.html

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VSphere::VirtualMachineSnapshot",
    "Properties" : {
        "<a href="#consolidate" title="Consolidate">Consolidate</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#memory" title="Memory">Memory</a>" : <i>Boolean</i>,
        "<a href="#quiesce" title="Quiesce">Quiesce</a>" : <i>Boolean</i>,
        "<a href="#removechildren" title="RemoveChildren">RemoveChildren</a>" : <i>Boolean</i>,
        "<a href="#snapshotname" title="SnapshotName">SnapshotName</a>" : <i>String</i>,
        "<a href="#virtualmachineuuid" title="VirtualMachineUuid">VirtualMachineUuid</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VSphere::VirtualMachineSnapshot
Properties:
    <a href="#consolidate" title="Consolidate">Consolidate</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#memory" title="Memory">Memory</a>: <i>Boolean</i>
    <a href="#quiesce" title="Quiesce">Quiesce</a>: <i>Boolean</i>
    <a href="#removechildren" title="RemoveChildren">RemoveChildren</a>: <i>Boolean</i>
    <a href="#snapshotname" title="SnapshotName">SnapshotName</a>: <i>String</i>
    <a href="#virtualmachineuuid" title="VirtualMachineUuid">VirtualMachineUuid</a>: <i>String</i>
</pre>

## Properties

#### Consolidate

If set to `true`, the delta disks involved in this
snapshot will be consolidated into the parent when this resource is
destroyed.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A description for the snapshot.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Memory

If set to `true`, a dump of the internal state of the
virtual machine is included in the snapshot.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Quiesce

If set to `true`, and the virtual machine is powered
on when the snapshot is taken, VMware Tools is used to quiesce the file
system in the virtual machine.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoveChildren

If set to `true`, the entire snapshot subtree
is removed when this resource is destroyed.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotName

The name of the snapshot.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualMachineUuid

The virtual machine UUID.

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

#### Id

Returns the <code>Id</code> value.

