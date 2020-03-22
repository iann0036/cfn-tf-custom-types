# Terraform::VCD::VmInternalDisk

This can be used to create, update and delete VM internal disks on already created VMs.

~> **Note:** To adjust disk parameters when creating a new VM, please use [override_template_disk](/docs/providers/vcd/r/vapp_vm.html#override-template-disk).

To manage disks which already exist inside a VM, please [import](#importing) them first.

~> **Note:** Managing disks in VM is possible only when VDC fast provisioned is disabled.

Supported in provider *v2.7+*

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VCD::VmInternalDisk",
    "Properties" : {
        "<a href="#allowvmreboot" title="AllowVmReboot">AllowVmReboot</a>" : <i>Boolean</i>,
        "<a href="#busnumber" title="BusNumber">BusNumber</a>" : <i>Double</i>,
        "<a href="#bustype" title="BusType">BusType</a>" : <i>String</i>,
        "<a href="#iops" title="Iops">Iops</a>" : <i>Double</i>,
        "<a href="#org" title="Org">Org</a>" : <i>String</i>,
        "<a href="#sizeinmb" title="SizeInMb">SizeInMb</a>" : <i>Double</i>,
        "<a href="#storageprofile" title="StorageProfile">StorageProfile</a>" : <i>String</i>,
        "<a href="#unitnumber" title="UnitNumber">UnitNumber</a>" : <i>Double</i>,
        "<a href="#vappname" title="VappName">VappName</a>" : <i>String</i>,
        "<a href="#vdc" title="Vdc">Vdc</a>" : <i>String</i>,
        "<a href="#vmname" title="VmName">VmName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VCD::VmInternalDisk
Properties:
    <a href="#allowvmreboot" title="AllowVmReboot">AllowVmReboot</a>: <i>Boolean</i>
    <a href="#busnumber" title="BusNumber">BusNumber</a>: <i>Double</i>
    <a href="#bustype" title="BusType">BusType</a>: <i>String</i>
    <a href="#iops" title="Iops">Iops</a>: <i>Double</i>
    <a href="#org" title="Org">Org</a>: <i>String</i>
    <a href="#sizeinmb" title="SizeInMb">SizeInMb</a>: <i>Double</i>
    <a href="#storageprofile" title="StorageProfile">StorageProfile</a>: <i>String</i>
    <a href="#unitnumber" title="UnitNumber">UnitNumber</a>: <i>Double</i>
    <a href="#vappname" title="VappName">VappName</a>: <i>String</i>
    <a href="#vdc" title="Vdc">Vdc</a>: <i>String</i>
    <a href="#vmname" title="VmName">VmName</a>: <i>String</i>
</pre>

## Properties

#### AllowVmReboot

Powers off VM when changing any attribute of an IDE disk or unit/bus number of other disk types, after the change is complete VM is powered back on. Without this setting enabled, such changes on a powered-on VM would fail. Defaults to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BusNumber

The number of the SCSI or IDE controller itself.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BusType

The type of disk controller. Possible values: `ide`, `parallel`( LSI Logic Parallel SCSI), `sas`(LSI Logic SAS (SCSI)), `paravirtual`(Paravirtual (SCSI)), `sata`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Iops

Specifies the IOPS for the disk. Default is 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Org

The name of organization to use, optional if defined at provider level. Useful when connected as sysadmin working across different organisations.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SizeInMb

The size of the disk in MB.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageProfile

Storage profile which overrides the VM default one.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnitNumber

The device number on the SCSI or IDE controller of the disk.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VappName

The vAPP this VM internal disk belongs to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdc

The name of VDC to use, optional if defined at provider level.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmName

VM in vAPP in which internal disk is created.

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

#### ThinProvisioned

Returns the <code>ThinProvisioned</code> value.

