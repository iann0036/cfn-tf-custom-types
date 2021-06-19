# TF::AzureStack::VirtualMachine

Manages a virtual machine.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureStack::VirtualMachine",
    "Properties" : {
        "<a href="#availabilitysetid" title="AvailabilitySetId">AvailabilitySetId</a>" : <i>String</i>,
        "<a href="#deletedatadisksontermination" title="DeleteDataDisksOnTermination">DeleteDataDisksOnTermination</a>" : <i>Boolean</i>,
        "<a href="#deleteosdiskontermination" title="DeleteOsDiskOnTermination">DeleteOsDiskOnTermination</a>" : <i>Boolean</i>,
        "<a href="#licensetype" title="LicenseType">LicenseType</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkinterfaceids" title="NetworkInterfaceIds">NetworkInterfaceIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#primarynetworkinterfaceid" title="PrimaryNetworkInterfaceId">PrimaryNetworkInterfaceId</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#vmsize" title="VmSize">VmSize</a>" : <i>String</i>,
        "<a href="#bootdiagnostics" title="BootDiagnostics">BootDiagnostics</a>" : <i>[ <a href="bootdiagnosticsdefinition.md">BootDiagnosticsDefinition</a>, ... ]</i>,
        "<a href="#identity" title="Identity">Identity</a>" : <i>[ <a href="identitydefinition.md">IdentityDefinition</a>, ... ]</i>,
        "<a href="#osprofile" title="OsProfile">OsProfile</a>" : <i>[ <a href="osprofiledefinition.md">OsProfileDefinition</a>, ... ]</i>,
        "<a href="#osprofilelinuxconfig" title="OsProfileLinuxConfig">OsProfileLinuxConfig</a>" : <i>[ <a href="osprofilelinuxconfigdefinition.md">OsProfileLinuxConfigDefinition</a>, ... ]</i>,
        "<a href="#osprofilesecrets" title="OsProfileSecrets">OsProfileSecrets</a>" : <i>[ <a href="osprofilesecretsdefinition.md">OsProfileSecretsDefinition</a>, ... ]</i>,
        "<a href="#osprofilewindowsconfig" title="OsProfileWindowsConfig">OsProfileWindowsConfig</a>" : <i>[ <a href="osprofilewindowsconfigdefinition.md">OsProfileWindowsConfigDefinition</a>, ... ]</i>,
        "<a href="#plan" title="Plan">Plan</a>" : <i>[ <a href="plandefinition.md">PlanDefinition</a>, ... ]</i>,
        "<a href="#storagedatadisk" title="StorageDataDisk">StorageDataDisk</a>" : <i>[ <a href="storagedatadiskdefinition.md">StorageDataDiskDefinition</a>, ... ]</i>,
        "<a href="#storageimagereference" title="StorageImageReference">StorageImageReference</a>" : <i>[ <a href="storageimagereferencedefinition.md">StorageImageReferenceDefinition</a>, ... ]</i>,
        "<a href="#storageosdisk" title="StorageOsDisk">StorageOsDisk</a>" : <i>[ <a href="storageosdiskdefinition.md">StorageOsDiskDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureStack::VirtualMachine
Properties:
    <a href="#availabilitysetid" title="AvailabilitySetId">AvailabilitySetId</a>: <i>String</i>
    <a href="#deletedatadisksontermination" title="DeleteDataDisksOnTermination">DeleteDataDisksOnTermination</a>: <i>Boolean</i>
    <a href="#deleteosdiskontermination" title="DeleteOsDiskOnTermination">DeleteOsDiskOnTermination</a>: <i>Boolean</i>
    <a href="#licensetype" title="LicenseType">LicenseType</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkinterfaceids" title="NetworkInterfaceIds">NetworkInterfaceIds</a>: <i>
      - String</i>
    <a href="#primarynetworkinterfaceid" title="PrimaryNetworkInterfaceId">PrimaryNetworkInterfaceId</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#vmsize" title="VmSize">VmSize</a>: <i>String</i>
    <a href="#bootdiagnostics" title="BootDiagnostics">BootDiagnostics</a>: <i>
      - <a href="bootdiagnosticsdefinition.md">BootDiagnosticsDefinition</a></i>
    <a href="#identity" title="Identity">Identity</a>: <i>
      - <a href="identitydefinition.md">IdentityDefinition</a></i>
    <a href="#osprofile" title="OsProfile">OsProfile</a>: <i>
      - <a href="osprofiledefinition.md">OsProfileDefinition</a></i>
    <a href="#osprofilelinuxconfig" title="OsProfileLinuxConfig">OsProfileLinuxConfig</a>: <i>
      - <a href="osprofilelinuxconfigdefinition.md">OsProfileLinuxConfigDefinition</a></i>
    <a href="#osprofilesecrets" title="OsProfileSecrets">OsProfileSecrets</a>: <i>
      - <a href="osprofilesecretsdefinition.md">OsProfileSecretsDefinition</a></i>
    <a href="#osprofilewindowsconfig" title="OsProfileWindowsConfig">OsProfileWindowsConfig</a>: <i>
      - <a href="osprofilewindowsconfigdefinition.md">OsProfileWindowsConfigDefinition</a></i>
    <a href="#plan" title="Plan">Plan</a>: <i>
      - <a href="plandefinition.md">PlanDefinition</a></i>
    <a href="#storagedatadisk" title="StorageDataDisk">StorageDataDisk</a>: <i>
      - <a href="storagedatadiskdefinition.md">StorageDataDiskDefinition</a></i>
    <a href="#storageimagereference" title="StorageImageReference">StorageImageReference</a>: <i>
      - <a href="storageimagereferencedefinition.md">StorageImageReferenceDefinition</a></i>
    <a href="#storageosdisk" title="StorageOsDisk">StorageOsDisk</a>: <i>
      - <a href="storageosdiskdefinition.md">StorageOsDiskDefinition</a></i>
</pre>

## Properties

#### AvailabilitySetId

The Id of the Availability Set in which to create the virtual machine.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteDataDisksOnTermination

Flag to enable deletion of storage data disk VHD blobs when the VM is deleted, defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteOsDiskOnTermination

Should the OS Disk be deleted when the Virtual Machine is destroyed? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseType

Specifies the Windows OS license type. If supplied, the only allowed values are `Windows_Client` and `Windows_Server`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

Specifies the supported Azure Stack Region where the resource exists. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the image from the marketplace.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInterfaceIds

Specifies the list of resource IDs for the network interfaces associated with the virtual machine.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryNetworkInterfaceId

Specifies the resource ID for the primary network interface associated with the virtual machine.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to
create the virtual machine.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmSize

Specifies the [size of the virtual machine](https://azure.microsoft.com/en-us/documentation/articles/virtual-machines-size-specs/).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootDiagnostics

_Required_: No

_Type_: List of <a href="bootdiagnosticsdefinition.md">BootDiagnosticsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identity

_Required_: No

_Type_: List of <a href="identitydefinition.md">IdentityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsProfile

_Required_: No

_Type_: List of <a href="osprofiledefinition.md">OsProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsProfileLinuxConfig

_Required_: No

_Type_: List of <a href="osprofilelinuxconfigdefinition.md">OsProfileLinuxConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsProfileSecrets

_Required_: No

_Type_: List of <a href="osprofilesecretsdefinition.md">OsProfileSecretsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsProfileWindowsConfig

_Required_: No

_Type_: List of <a href="osprofilewindowsconfigdefinition.md">OsProfileWindowsConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Plan

_Required_: No

_Type_: List of <a href="plandefinition.md">PlanDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageDataDisk

_Required_: No

_Type_: List of <a href="storagedatadiskdefinition.md">StorageDataDiskDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageImageReference

_Required_: No

_Type_: List of <a href="storageimagereferencedefinition.md">StorageImageReferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageOsDisk

_Required_: No

_Type_: List of <a href="storageosdiskdefinition.md">StorageOsDiskDefinition</a>

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

