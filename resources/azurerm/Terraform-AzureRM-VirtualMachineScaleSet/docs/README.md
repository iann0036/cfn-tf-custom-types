# Terraform::AzureRM::VirtualMachineScaleSet

Manages a virtual machine scale set.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::VirtualMachineScaleSet",
    "Properties" : {
        "<a href="#automaticosupgrade" title="AutomaticOsUpgrade">AutomaticOsUpgrade</a>" : <i>Boolean</i>,
        "<a href="#evictionpolicy" title="EvictionPolicy">EvictionPolicy</a>" : <i>String</i>,
        "<a href="#healthprobeid" title="HealthProbeId">HealthProbeId</a>" : <i>String</i>,
        "<a href="#licensetype" title="LicenseType">LicenseType</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#overprovision" title="Overprovision">Overprovision</a>" : <i>Boolean</i>,
        "<a href="#priority" title="Priority">Priority</a>" : <i>String</i>,
        "<a href="#proximityplacementgroupid" title="ProximityPlacementGroupId">ProximityPlacementGroupId</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#singleplacementgroup" title="SinglePlacementGroup">SinglePlacementGroup</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#upgradepolicymode" title="UpgradePolicyMode">UpgradePolicyMode</a>" : <i>String</i>,
        "<a href="#zones" title="Zones">Zones</a>" : <i>[ String, ... ]</i>,
        "<a href="#bootdiagnostics" title="BootDiagnostics">BootDiagnostics</a>" : <i>[ <a href="bootdiagnostics.md">BootDiagnostics</a>, ... ]</i>,
        "<a href="#extension" title="Extension">Extension</a>" : <i>[ <a href="extension.md">Extension</a>, ... ]</i>,
        "<a href="#identity" title="Identity">Identity</a>" : <i>[ <a href="identity.md">Identity</a>, ... ]</i>,
        "<a href="#networkprofile" title="NetworkProfile">NetworkProfile</a>" : <i>[ <a href="networkprofile.md">NetworkProfile</a>, ... ]</i>,
        "<a href="#osprofile" title="OsProfile">OsProfile</a>" : <i>[ <a href="osprofile.md">OsProfile</a>, ... ]</i>,
        "<a href="#osprofilelinuxconfig" title="OsProfileLinuxConfig">OsProfileLinuxConfig</a>" : <i>[ <a href="osprofilelinuxconfig.md">OsProfileLinuxConfig</a>, ... ]</i>,
        "<a href="#osprofilesecrets" title="OsProfileSecrets">OsProfileSecrets</a>" : <i>[ <a href="osprofilesecrets.md">OsProfileSecrets</a>, ... ]</i>,
        "<a href="#osprofilewindowsconfig" title="OsProfileWindowsConfig">OsProfileWindowsConfig</a>" : <i>[ <a href="osprofilewindowsconfig.md">OsProfileWindowsConfig</a>, ... ]</i>,
        "<a href="#plan" title="Plan">Plan</a>" : <i>[ <a href="plan.md">Plan</a>, ... ]</i>,
        "<a href="#rollingupgradepolicy" title="RollingUpgradePolicy">RollingUpgradePolicy</a>" : <i>[ <a href="rollingupgradepolicy.md">RollingUpgradePolicy</a>, ... ]</i>,
        "<a href="#sku" title="Sku">Sku</a>" : <i>[ <a href="sku.md">Sku</a>, ... ]</i>,
        "<a href="#storageprofiledatadisk" title="StorageProfileDataDisk">StorageProfileDataDisk</a>" : <i>[ <a href="storageprofiledatadisk.md">StorageProfileDataDisk</a>, ... ]</i>,
        "<a href="#storageprofileimagereference" title="StorageProfileImageReference">StorageProfileImageReference</a>" : <i>[ <a href="storageprofileimagereference.md">StorageProfileImageReference</a>, ... ]</i>,
        "<a href="#storageprofileosdisk" title="StorageProfileOsDisk">StorageProfileOsDisk</a>" : <i>[ <a href="storageprofileosdisk.md">StorageProfileOsDisk</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#dnssettings" title="DnsSettings">DnsSettings</a>" : <i>[ <a href="dnssettings.md">DnsSettings</a>, ... ]</i>,
        "<a href="#ipconfiguration" title="IpConfiguration">IpConfiguration</a>" : <i>[ <a href="ipconfiguration.md">IpConfiguration</a>, ... ]</i>,
        "<a href="#sshkeys" title="SshKeys">SshKeys</a>" : <i>[ <a href="sshkeys.md">SshKeys</a>, ... ]</i>,
        "<a href="#vaultcertificates" title="VaultCertificates">VaultCertificates</a>" : <i>[ <a href="vaultcertificates.md">VaultCertificates</a>, ... ]</i>,
        "<a href="#additionalunattendconfig" title="AdditionalUnattendConfig">AdditionalUnattendConfig</a>" : <i>[ <a href="additionalunattendconfig.md">AdditionalUnattendConfig</a>, ... ]</i>,
        "<a href="#winrm" title="Winrm">Winrm</a>" : <i>[ <a href="winrm.md">Winrm</a>, ... ]</i>,
        "<a href="#publicipaddressconfiguration" title="PublicIpAddressConfiguration">PublicIpAddressConfiguration</a>" : <i>[ <a href="publicipaddressconfiguration.md">PublicIpAddressConfiguration</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::VirtualMachineScaleSet
Properties:
    <a href="#automaticosupgrade" title="AutomaticOsUpgrade">AutomaticOsUpgrade</a>: <i>Boolean</i>
    <a href="#evictionpolicy" title="EvictionPolicy">EvictionPolicy</a>: <i>String</i>
    <a href="#healthprobeid" title="HealthProbeId">HealthProbeId</a>: <i>String</i>
    <a href="#licensetype" title="LicenseType">LicenseType</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#overprovision" title="Overprovision">Overprovision</a>: <i>Boolean</i>
    <a href="#priority" title="Priority">Priority</a>: <i>String</i>
    <a href="#proximityplacementgroupid" title="ProximityPlacementGroupId">ProximityPlacementGroupId</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#singleplacementgroup" title="SinglePlacementGroup">SinglePlacementGroup</a>: <i>Boolean</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#upgradepolicymode" title="UpgradePolicyMode">UpgradePolicyMode</a>: <i>String</i>
    <a href="#zones" title="Zones">Zones</a>: <i>
      - String</i>
    <a href="#bootdiagnostics" title="BootDiagnostics">BootDiagnostics</a>: <i>
      - <a href="bootdiagnostics.md">BootDiagnostics</a></i>
    <a href="#extension" title="Extension">Extension</a>: <i>
      - <a href="extension.md">Extension</a></i>
    <a href="#identity" title="Identity">Identity</a>: <i>
      - <a href="identity.md">Identity</a></i>
    <a href="#networkprofile" title="NetworkProfile">NetworkProfile</a>: <i>
      - <a href="networkprofile.md">NetworkProfile</a></i>
    <a href="#osprofile" title="OsProfile">OsProfile</a>: <i>
      - <a href="osprofile.md">OsProfile</a></i>
    <a href="#osprofilelinuxconfig" title="OsProfileLinuxConfig">OsProfileLinuxConfig</a>: <i>
      - <a href="osprofilelinuxconfig.md">OsProfileLinuxConfig</a></i>
    <a href="#osprofilesecrets" title="OsProfileSecrets">OsProfileSecrets</a>: <i>
      - <a href="osprofilesecrets.md">OsProfileSecrets</a></i>
    <a href="#osprofilewindowsconfig" title="OsProfileWindowsConfig">OsProfileWindowsConfig</a>: <i>
      - <a href="osprofilewindowsconfig.md">OsProfileWindowsConfig</a></i>
    <a href="#plan" title="Plan">Plan</a>: <i>
      - <a href="plan.md">Plan</a></i>
    <a href="#rollingupgradepolicy" title="RollingUpgradePolicy">RollingUpgradePolicy</a>: <i>
      - <a href="rollingupgradepolicy.md">RollingUpgradePolicy</a></i>
    <a href="#sku" title="Sku">Sku</a>: <i>
      - <a href="sku.md">Sku</a></i>
    <a href="#storageprofiledatadisk" title="StorageProfileDataDisk">StorageProfileDataDisk</a>: <i>
      - <a href="storageprofiledatadisk.md">StorageProfileDataDisk</a></i>
    <a href="#storageprofileimagereference" title="StorageProfileImageReference">StorageProfileImageReference</a>: <i>
      - <a href="storageprofileimagereference.md">StorageProfileImageReference</a></i>
    <a href="#storageprofileosdisk" title="StorageProfileOsDisk">StorageProfileOsDisk</a>: <i>
      - <a href="storageprofileosdisk.md">StorageProfileOsDisk</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#dnssettings" title="DnsSettings">DnsSettings</a>: <i>
      - <a href="dnssettings.md">DnsSettings</a></i>
    <a href="#ipconfiguration" title="IpConfiguration">IpConfiguration</a>: <i>
      - <a href="ipconfiguration.md">IpConfiguration</a></i>
    <a href="#sshkeys" title="SshKeys">SshKeys</a>: <i>
      - <a href="sshkeys.md">SshKeys</a></i>
    <a href="#vaultcertificates" title="VaultCertificates">VaultCertificates</a>: <i>
      - <a href="vaultcertificates.md">VaultCertificates</a></i>
    <a href="#additionalunattendconfig" title="AdditionalUnattendConfig">AdditionalUnattendConfig</a>: <i>
      - <a href="additionalunattendconfig.md">AdditionalUnattendConfig</a></i>
    <a href="#winrm" title="Winrm">Winrm</a>: <i>
      - <a href="winrm.md">Winrm</a></i>
    <a href="#publicipaddressconfiguration" title="PublicIpAddressConfiguration">PublicIpAddressConfiguration</a>: <i>
      - <a href="publicipaddressconfiguration.md">PublicIpAddressConfiguration</a></i>
</pre>

## Properties

#### AutomaticOsUpgrade

Automatic OS patches can be applied by Azure to your scaleset. This is particularly useful when `upgrade_policy_mode` is set to `Rolling`. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EvictionPolicy

Specifies the eviction policy for Virtual Machines in this Scale Set. Possible values are `Deallocate` and `Delete`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthProbeId

Specifies the identifier for the load balancer health probe. Required when using `Rolling` as your `upgrade_policy_mode`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseType

Specifies the Windows OS license type. If supplied, the only allowed values are `Windows_Client` and `Windows_Server`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the virtual machine scale set resource. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Overprovision

Specifies whether the virtual machine scale set should be overprovisioned.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

Specifies the priority for the Virtual Machines in the Scale Set. Defaults to `Regular`. Possible values are `Low` and `Regular`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProximityPlacementGroupId

The ID of the Proximity Placement Group to which this Virtual Machine should be assigned. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to create the virtual machine scale set. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SinglePlacementGroup

Specifies whether the scale set is limited to a single placement group with a maximum size of 100 virtual machines. If set to false, managed disks must be used. Default is true. Changing this forces a new resource to be created. See [documentation](http://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-placement-groups) for more information.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpgradePolicyMode

Specifies the mode of an upgrade to virtual machines in the scale set. Possible values, `Rolling`, `Manual`, or `Automatic`. When choosing `Rolling`, you will need to set a health probe.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zones

A collection of availability zones to spread the Virtual Machines over.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootDiagnostics

_Required_: No

_Type_: List of <a href="bootdiagnostics.md">BootDiagnostics</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Extension

_Required_: No

_Type_: List of <a href="extension.md">Extension</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identity

_Required_: No

_Type_: List of <a href="identity.md">Identity</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkProfile

_Required_: No

_Type_: List of <a href="networkprofile.md">NetworkProfile</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsProfile

_Required_: No

_Type_: List of <a href="osprofile.md">OsProfile</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsProfileLinuxConfig

_Required_: No

_Type_: List of <a href="osprofilelinuxconfig.md">OsProfileLinuxConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsProfileSecrets

_Required_: No

_Type_: List of <a href="osprofilesecrets.md">OsProfileSecrets</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsProfileWindowsConfig

_Required_: No

_Type_: List of <a href="osprofilewindowsconfig.md">OsProfileWindowsConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Plan

_Required_: No

_Type_: List of <a href="plan.md">Plan</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RollingUpgradePolicy

_Required_: No

_Type_: List of <a href="rollingupgradepolicy.md">RollingUpgradePolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sku

_Required_: No

_Type_: List of <a href="sku.md">Sku</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageProfileDataDisk

_Required_: No

_Type_: List of <a href="storageprofiledatadisk.md">StorageProfileDataDisk</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageProfileImageReference

_Required_: No

_Type_: List of <a href="storageprofileimagereference.md">StorageProfileImageReference</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageProfileOsDisk

_Required_: No

_Type_: List of <a href="storageprofileosdisk.md">StorageProfileOsDisk</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsSettings

_Required_: No

_Type_: List of <a href="dnssettings.md">DnsSettings</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpConfiguration

_Required_: No

_Type_: List of <a href="ipconfiguration.md">IpConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKeys

_Required_: No

_Type_: List of <a href="sshkeys.md">SshKeys</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VaultCertificates

_Required_: No

_Type_: List of <a href="vaultcertificates.md">VaultCertificates</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalUnattendConfig

_Required_: No

_Type_: List of <a href="additionalunattendconfig.md">AdditionalUnattendConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Winrm

_Required_: No

_Type_: List of <a href="winrm.md">Winrm</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIpAddressConfiguration

_Required_: No

_Type_: List of <a href="publicipaddressconfiguration.md">PublicIpAddressConfiguration</a>

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

