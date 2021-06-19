# TF::VCD::Vm

Provides a VMware Cloud Director standalone VM resource. This can be used to create, modify, and delete Standalone VMs.

Supported in provider *v3.2+*

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::VCD::Vm",
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
Type: TF::VCD::Vm
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

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootImage

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CatalogName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComputerName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuCores

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuHotAddEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cpus

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExposeHardwareVirtualization

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestProperties

_Required_: No

_Type_: List of <a href="guestpropertiesdefinition.md">GuestPropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HardwareVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Href

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Memory

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryHotAddEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of <a href="metadatadefinition.md">MetadataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkDhcpWaitSeconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Org

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PowerOn

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreventUpdatePowerOff

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

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VappName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdc

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmNameInTemplate

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

