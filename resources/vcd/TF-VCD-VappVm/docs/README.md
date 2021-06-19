# TF::VCD::VappVm

Provides a vCloud Director VM resource. This can be used to create,
modify, and delete VMs within a vApp.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::VCD::VappVm",
    "Properties" : {
        "<a href="#acceptalleulas" title="AcceptAllEulas">AcceptAllEulas</a>" : <i>Boolean</i>,
        "<a href="#bootimage" title="BootImage">BootImage</a>" : <i>String</i>,
        "<a href="#catalogname" title="CatalogName">CatalogName</a>" : <i>String</i>,
        "<a href="#computername" title="ComputerName">ComputerName</a>" : <i>String</i>,
        "<a href="#cpucores" title="CpuCores">CpuCores</a>" : <i>Double</i>,
        "<a href="#cpuhotaddenabled" title="CpuHotAddEnabled">CpuHotAddEnabled</a>" : <i>Boolean</i>,
        "<a href="#cpus" title="Cpus">Cpus</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#exposehardwarevirtualization" title="ExposeHardwareVirtualization">ExposeHardwareVirtualization</a>" : <i>Boolean</i>,
        "<a href="#guestproperties" title="GuestProperties">GuestProperties</a>" : <i>[ <a href="guestpropertiesdefinition.md">GuestPropertiesDefinition</a>, ... ]</i>,
        "<a href="#hardwareversion" title="HardwareVersion">HardwareVersion</a>" : <i>String</i>,
        "<a href="#href" title="Href">Href</a>" : <i>String</i>,
        "<a href="#memory" title="Memory">Memory</a>" : <i>Double</i>,
        "<a href="#memoryhotaddenabled" title="MemoryHotAddEnabled">MemoryHotAddEnabled</a>" : <i>Boolean</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadatadefinition.md">MetadataDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkdhcpwaitseconds" title="NetworkDhcpWaitSeconds">NetworkDhcpWaitSeconds</a>" : <i>Double</i>,
        "<a href="#org" title="Org">Org</a>" : <i>String</i>,
        "<a href="#ostype" title="OsType">OsType</a>" : <i>String</i>,
        "<a href="#poweron" title="PowerOn">PowerOn</a>" : <i>Boolean</i>,
        "<a href="#preventupdatepoweroff" title="PreventUpdatePowerOff">PreventUpdatePowerOff</a>" : <i>Boolean</i>,
        "<a href="#sizingpolicyid" title="SizingPolicyId">SizingPolicyId</a>" : <i>String</i>,
        "<a href="#storageprofile" title="StorageProfile">StorageProfile</a>" : <i>String</i>,
        "<a href="#templatename" title="TemplateName">TemplateName</a>" : <i>String</i>,
        "<a href="#vappname" title="VappName">VappName</a>" : <i>String</i>,
        "<a href="#vdc" title="Vdc">Vdc</a>" : <i>String</i>,
        "<a href="#vmnameintemplate" title="VmNameInTemplate">VmNameInTemplate</a>" : <i>String</i>,
        "<a href="#customization" title="Customization">Customization</a>" : <i>[ <a href="customizationdefinition.md">CustomizationDefinition</a>, ... ]</i>,
        "<a href="#disk" title="Disk">Disk</a>" : <i>[ <a href="diskdefinition.md">DiskDefinition</a>, ... ]</i>,
        "<a href="#network" title="Network">Network</a>" : <i>[ <a href="networkdefinition.md">NetworkDefinition</a>, ... ]</i>,
        "<a href="#overridetemplatedisk" title="OverrideTemplateDisk">OverrideTemplateDisk</a>" : <i>[ <a href="overridetemplatediskdefinition.md">OverrideTemplateDiskDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::VCD::VappVm
Properties:
    <a href="#acceptalleulas" title="AcceptAllEulas">AcceptAllEulas</a>: <i>Boolean</i>
    <a href="#bootimage" title="BootImage">BootImage</a>: <i>String</i>
    <a href="#catalogname" title="CatalogName">CatalogName</a>: <i>String</i>
    <a href="#computername" title="ComputerName">ComputerName</a>: <i>String</i>
    <a href="#cpucores" title="CpuCores">CpuCores</a>: <i>Double</i>
    <a href="#cpuhotaddenabled" title="CpuHotAddEnabled">CpuHotAddEnabled</a>: <i>Boolean</i>
    <a href="#cpus" title="Cpus">Cpus</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#exposehardwarevirtualization" title="ExposeHardwareVirtualization">ExposeHardwareVirtualization</a>: <i>Boolean</i>
    <a href="#guestproperties" title="GuestProperties">GuestProperties</a>: <i>
      - <a href="guestpropertiesdefinition.md">GuestPropertiesDefinition</a></i>
    <a href="#hardwareversion" title="HardwareVersion">HardwareVersion</a>: <i>String</i>
    <a href="#href" title="Href">Href</a>: <i>String</i>
    <a href="#memory" title="Memory">Memory</a>: <i>Double</i>
    <a href="#memoryhotaddenabled" title="MemoryHotAddEnabled">MemoryHotAddEnabled</a>: <i>Boolean</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadatadefinition.md">MetadataDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkdhcpwaitseconds" title="NetworkDhcpWaitSeconds">NetworkDhcpWaitSeconds</a>: <i>Double</i>
    <a href="#org" title="Org">Org</a>: <i>String</i>
    <a href="#ostype" title="OsType">OsType</a>: <i>String</i>
    <a href="#poweron" title="PowerOn">PowerOn</a>: <i>Boolean</i>
    <a href="#preventupdatepoweroff" title="PreventUpdatePowerOff">PreventUpdatePowerOff</a>: <i>Boolean</i>
    <a href="#sizingpolicyid" title="SizingPolicyId">SizingPolicyId</a>: <i>String</i>
    <a href="#storageprofile" title="StorageProfile">StorageProfile</a>: <i>String</i>
    <a href="#templatename" title="TemplateName">TemplateName</a>: <i>String</i>
    <a href="#vappname" title="VappName">VappName</a>: <i>String</i>
    <a href="#vdc" title="Vdc">Vdc</a>: <i>String</i>
    <a href="#vmnameintemplate" title="VmNameInTemplate">VmNameInTemplate</a>: <i>String</i>
    <a href="#customization" title="Customization">Customization</a>: <i>
      - <a href="customizationdefinition.md">CustomizationDefinition</a></i>
    <a href="#disk" title="Disk">Disk</a>: <i>
      - <a href="diskdefinition.md">DiskDefinition</a></i>
    <a href="#network" title="Network">Network</a>: <i>
      - <a href="networkdefinition.md">NetworkDefinition</a></i>
    <a href="#overridetemplatedisk" title="OverrideTemplateDisk">OverrideTemplateDisk</a>: <i>
      - <a href="overridetemplatediskdefinition.md">OverrideTemplateDiskDefinition</a></i>
</pre>

## Properties

#### AcceptAllEulas

Automatically accept EULA if OVA has it. Default is `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootImage

Media name to mount as boot image. Image is mounted only during VM creation. On update if value is changed to empty it will eject the mounted media. If you want to mount an image later, please use [vcd_inserted_media](/docs/providers/vcd/r/inserted_media.html).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CatalogName

The catalog name in which to find the given vApp Template or media for `boot_image`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComputerName

Computer name to assign to this virtual machine.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuCores

The number of cores per socket.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuHotAddEnabled

True if the virtual machine supports addition of virtual CPUs while powered on. Default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cpus

The number of virtual CPUs to allocate to the VM. Socket count is a result of: virtual logical processors/cores per socket. If `cpu_hot_add_enabled` is true, then cpus will be increased without VM power off.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The VM description. Note: for VM from Template `description` is read only. Currently, this field has
the description of the OVA used to create the VM.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExposeHardwareVirtualization

Boolean for exposing full CPU virtualization to the
guest operating system so that applications that require hardware virtualization can run on virtual machines without binary
translation or paravirtualization. Useful for hypervisor nesting provided underlying hardware supports it. Default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestProperties

Key value map of guest properties.

_Required_: No

_Type_: List of <a href="guestpropertiesdefinition.md">GuestPropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HardwareVersion

Virtual Hardware Version (e.g.`vmx-14`, `vmx-13`, `vmx-12`, etc.). Required when creating empty VM.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Href

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Memory

The amount of RAM (in MB) to allocate to the VM. If `memory_hot_add_enabled` is true, then memory will be increased without VM power off.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryHotAddEnabled

True if the virtual machine supports addition of memory while powered on. Default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

Key value map of metadata to assign to this VM.

_Required_: No

_Type_: List of <a href="metadatadefinition.md">MetadataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A name for the VM, unique within the vApp.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkDhcpWaitSeconds

Optional number of seconds to try and wait for DHCP IP (only valid
for adapters in `network` block with `ip_allocation_mode=DHCP`). It constantly checks if IP is present so the time given
is a maximum. VM must be powered on and _at least one_ of the following _must be true_:
* VM has Guest Tools. It waits for IP address to be reported by Guest Tools. This is a slower option, but
does not require for the VM to use Edge Gateways DHCP service.
* VM DHCP interface is connected to routed Org network and is using Edge Gateways DHCP service (not
relayed). It works by querying DHCP leases on Edge Gateway. In general it is quicker than waiting
until Guest Tools report IP addresses, but is more constrained. However this is the only option if Guest
Tools are not present on the VM.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Org

The name of organization to use, optional if defined at provider level. Useful when connected as sysadmin working across different organisations.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsType

Operating System type. Possible values can be found in [Os Types](#os-types). Required when creating empty VM.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PowerOn

A boolean value stating if this VM should be powered on. Default is `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreventUpdatePowerOff

True if the update of resource should fail when virtual machine power off needed. Default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SizingPolicyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageProfile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateName

The name of the vApp Template to use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VappName

The vApp this VM belongs to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdc

The name of VDC to use, optional if defined at provider level.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmNameInTemplate

The name of the VM in vApp Template to use. For cases when vApp template has more than one VM.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Customization

_Required_: No

_Type_: List of <a href="customizationdefinition.md">CustomizationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disk

_Required_: No

_Type_: List of <a href="diskdefinition.md">DiskDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

_Required_: No

_Type_: List of <a href="networkdefinition.md">NetworkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideTemplateDisk

_Required_: No

_Type_: List of <a href="overridetemplatediskdefinition.md">OverrideTemplateDiskDefinition</a>

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

#### InternalDisk

Returns the <code>InternalDisk</code> value.

#### VmType

Returns the <code>VmType</code> value.

