# Terraform::Skytap::Vm

Provides a Skytap Virtual Machine (VM) resource. The environment VM resource represents an image of a single virtual machine.

~> **NOTE:**
* VMs do not exist outside of environments or templates.
* An environment or template can have multiple VMs.
* Each VM is a unique resource. Therefore, a VM in a template will have a different ID than a VM in an environment created from that template.
* The VM will be run immediately after creation.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Skytap::Vm",
    "Properties" : {
        "<a href="#cpus" title="Cpus">Cpus</a>" : <i>Double</i>,
        "<a href="#environmentid" title="EnvironmentId">EnvironmentId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#osdisksize" title="OsDiskSize">OsDiskSize</a>" : <i>Double</i>,
        "<a href="#ram" title="Ram">Ram</a>" : <i>Double</i>,
        "<a href="#templateid" title="TemplateId">TemplateId</a>" : <i>String</i>,
        "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
        "<a href="#vmid" title="VmId">VmId</a>" : <i>String</i>,
        "<a href="#disk" title="Disk">Disk</a>" : <i>[ <a href="disk.md">Disk</a>, ... ]</i>,
        "<a href="#label" title="Label">Label</a>" : <i>[ <a href="label.md">Label</a>, ... ]</i>,
        "<a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>" : <i>[ <a href="networkinterface.md">NetworkInterface</a>, ... ]</i>,
        "<a href="#publishedservice" title="PublishedService">PublishedService</a>" : <i>[ <a href="publishedservice.md">PublishedService</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Skytap::Vm
Properties:
    <a href="#cpus" title="Cpus">Cpus</a>: <i>Double</i>
    <a href="#environmentid" title="EnvironmentId">EnvironmentId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#osdisksize" title="OsDiskSize">OsDiskSize</a>: <i>Double</i>
    <a href="#ram" title="Ram">Ram</a>: <i>Double</i>
    <a href="#templateid" title="TemplateId">TemplateId</a>: <i>String</i>
    <a href="#userdata" title="UserData">UserData</a>: <i>String</i>
    <a href="#vmid" title="VmId">VmId</a>: <i>String</i>
    <a href="#disk" title="Disk">Disk</a>: <i>
      - <a href="disk.md">Disk</a></i>
    <a href="#label" title="Label">Label</a>: <i>
      - <a href="label.md">Label</a></i>
    <a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>: <i>
      - <a href="networkinterface.md">NetworkInterface</a></i>
    <a href="#publishedservice" title="PublishedService">PublishedService</a>: <i>
      - <a href="publishedservice.md">PublishedService</a></i>
</pre>

## Properties

#### Cpus

Number of CPUs allocated to this virtual machine. Valid range is 1 to 12. Maximum limit depends on the `max_cpus` setting.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvironmentId

ID of the environment you want to add the VM to. If updating with a new one then the VM will be recreated.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A unique name for the published service.
* `internal_port` - (Required, Force New) The port that is exposed on the interface. Typically this will be dictated by standard usage (e.g., port 80 for http traffic, port 22 for SSH).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsDiskSize

The size of the OS disk. The disk size is in MiB; it will be converted to GiB in the Skytap UI. The maximum disk size is 2,096,128 MiB (1.999 TiB).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ram

Amount of RAM allocated to this VM. Valid range is 256 and 131,072 (MB). Maximum limit depends on `max_ram` setting.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateId

ID of the template you want to create the vm from. If updating with a new one then the VM will be recreated.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

VM user data, available from the metadata server and the skytap api.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmId

ID of the VM you want to create the VM from. If updating with a new one then the VM will be recreated.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disk

_Required_: No

_Type_: List of <a href="disk.md">Disk</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

_Required_: No

_Type_: List of <a href="label.md">Label</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInterface

_Required_: No

_Type_: List of <a href="networkinterface.md">NetworkInterface</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublishedService

_Required_: No

_Type_: List of <a href="publishedservice.md">PublishedService</a>

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

#### MaxCpus

Returns the <code>MaxCpus</code> value.

#### MaxRam

Returns the <code>MaxRam</code> value.

#### ServiceIps

Returns the <code>ServiceIps</code> value.

#### ServicePorts

Returns the <code>ServicePorts</code> value.

