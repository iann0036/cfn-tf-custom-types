# Terraform::AzureRM::VirtualMachine

CloudFormation equivalent of azurerm_virtual_machine

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::VirtualMachine",
    "Properties" : {
        "<a href="#availabilitysetid" title="AvailabilitySetId">AvailabilitySetId</a>" : <i>String</i>,
        "<a href="#deletedatadisksontermination" title="DeleteDataDisksOnTermination">DeleteDataDisksOnTermination</a>" : <i>Boolean</i>,
        "<a href="#deleteosdiskontermination" title="DeleteOsDiskOnTermination">DeleteOsDiskOnTermination</a>" : <i>Boolean</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#licensetype" title="LicenseType">LicenseType</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkinterfaceids" title="NetworkInterfaceIds">NetworkInterfaceIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#primarynetworkinterfaceid" title="PrimaryNetworkInterfaceId">PrimaryNetworkInterfaceId</a>" : <i>String</i>,
        "<a href="#proximityplacementgroupid" title="ProximityPlacementGroupId">ProximityPlacementGroupId</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#vmsize" title="VmSize">VmSize</a>" : <i>String</i>,
        "<a href="#zones" title="Zones">Zones</a>" : <i>[ String, ... ]</i>,
        "<a href="#additionalcapabilities" title="AdditionalCapabilities">AdditionalCapabilities</a>" : <i>[ &lt;a href=&#34;additionalcapabilities.md&#34;&gt;AdditionalCapabilities&lt;/a&gt;, ... ]</i>,
        "<a href="#bootdiagnostics" title="BootDiagnostics">BootDiagnostics</a>" : <i>[ &lt;a href=&#34;bootdiagnostics.md&#34;&gt;BootDiagnostics&lt;/a&gt;, ... ]</i>,
        "<a href="#identity" title="Identity">Identity</a>" : <i>[ &lt;a href=&#34;identity.md&#34;&gt;Identity&lt;/a&gt;, ... ]</i>,
        "<a href="#osprofile" title="OsProfile">OsProfile</a>" : <i>[ &lt;a href=&#34;osprofile.md&#34;&gt;OsProfile&lt;/a&gt;, ... ]</i>,
        "<a href="#osprofilelinuxconfig" title="OsProfileLinuxConfig">OsProfileLinuxConfig</a>" : <i>[ &lt;a href=&#34;osprofilelinuxconfig.md&#34;&gt;OsProfileLinuxConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#osprofilesecrets" title="OsProfileSecrets">OsProfileSecrets</a>" : <i>[ &lt;a href=&#34;osprofilesecrets.md&#34;&gt;OsProfileSecrets&lt;/a&gt;, ... ]</i>,
        "<a href="#osprofilewindowsconfig" title="OsProfileWindowsConfig">OsProfileWindowsConfig</a>" : <i>[ &lt;a href=&#34;osprofilewindowsconfig.md&#34;&gt;OsProfileWindowsConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#plan" title="Plan">Plan</a>" : <i>[ &lt;a href=&#34;plan.md&#34;&gt;Plan&lt;/a&gt;, ... ]</i>,
        "<a href="#storagedatadisk" title="StorageDataDisk">StorageDataDisk</a>" : <i>[ &lt;a href=&#34;storagedatadisk.md&#34;&gt;StorageDataDisk&lt;/a&gt;, ... ]</i>,
        "<a href="#storageimagereference" title="StorageImageReference">StorageImageReference</a>" : <i>[ &lt;a href=&#34;storageimagereference.md&#34;&gt;StorageImageReference&lt;/a&gt;, ... ]</i>,
        "<a href="#storageosdisk" title="StorageOsDisk">StorageOsDisk</a>" : <i>[ &lt;a href=&#34;storageosdisk.md&#34;&gt;StorageOsDisk&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#sshkeys" title="SshKeys">SshKeys</a>" : <i>[ &lt;a href=&#34;sshkeys.md&#34;&gt;SshKeys&lt;/a&gt;, ... ]</i>,
        "<a href="#vaultcertificates" title="VaultCertificates">VaultCertificates</a>" : <i>[ &lt;a href=&#34;vaultcertificates.md&#34;&gt;VaultCertificates&lt;/a&gt;, ... ]</i>,
        "<a href="#additionalunattendconfig" title="AdditionalUnattendConfig">AdditionalUnattendConfig</a>" : <i>[ &lt;a href=&#34;additionalunattendconfig.md&#34;&gt;AdditionalUnattendConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#winrm" title="Winrm">Winrm</a>" : <i>[ &lt;a href=&#34;winrm.md&#34;&gt;Winrm&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::VirtualMachine
Properties:
    <a href="#availabilitysetid" title="AvailabilitySetId">AvailabilitySetId</a>: <i>String</i>
    <a href="#deletedatadisksontermination" title="DeleteDataDisksOnTermination">DeleteDataDisksOnTermination</a>: <i>Boolean</i>
    <a href="#deleteosdiskontermination" title="DeleteOsDiskOnTermination">DeleteOsDiskOnTermination</a>: <i>Boolean</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#licensetype" title="LicenseType">LicenseType</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkinterfaceids" title="NetworkInterfaceIds">NetworkInterfaceIds</a>: <i>
      - String</i>
    <a href="#primarynetworkinterfaceid" title="PrimaryNetworkInterfaceId">PrimaryNetworkInterfaceId</a>: <i>String</i>
    <a href="#proximityplacementgroupid" title="ProximityPlacementGroupId">ProximityPlacementGroupId</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#vmsize" title="VmSize">VmSize</a>: <i>String</i>
    <a href="#zones" title="Zones">Zones</a>: <i>
      - String</i>
    <a href="#additionalcapabilities" title="AdditionalCapabilities">AdditionalCapabilities</a>: <i>
      - &lt;a href=&#34;additionalcapabilities.md&#34;&gt;AdditionalCapabilities&lt;/a&gt;</i>
    <a href="#bootdiagnostics" title="BootDiagnostics">BootDiagnostics</a>: <i>
      - &lt;a href=&#34;bootdiagnostics.md&#34;&gt;BootDiagnostics&lt;/a&gt;</i>
    <a href="#identity" title="Identity">Identity</a>: <i>
      - &lt;a href=&#34;identity.md&#34;&gt;Identity&lt;/a&gt;</i>
    <a href="#osprofile" title="OsProfile">OsProfile</a>: <i>
      - &lt;a href=&#34;osprofile.md&#34;&gt;OsProfile&lt;/a&gt;</i>
    <a href="#osprofilelinuxconfig" title="OsProfileLinuxConfig">OsProfileLinuxConfig</a>: <i>
      - &lt;a href=&#34;osprofilelinuxconfig.md&#34;&gt;OsProfileLinuxConfig&lt;/a&gt;</i>
    <a href="#osprofilesecrets" title="OsProfileSecrets">OsProfileSecrets</a>: <i>
      - &lt;a href=&#34;osprofilesecrets.md&#34;&gt;OsProfileSecrets&lt;/a&gt;</i>
    <a href="#osprofilewindowsconfig" title="OsProfileWindowsConfig">OsProfileWindowsConfig</a>: <i>
      - &lt;a href=&#34;osprofilewindowsconfig.md&#34;&gt;OsProfileWindowsConfig&lt;/a&gt;</i>
    <a href="#plan" title="Plan">Plan</a>: <i>
      - &lt;a href=&#34;plan.md&#34;&gt;Plan&lt;/a&gt;</i>
    <a href="#storagedatadisk" title="StorageDataDisk">StorageDataDisk</a>: <i>
      - &lt;a href=&#34;storagedatadisk.md&#34;&gt;StorageDataDisk&lt;/a&gt;</i>
    <a href="#storageimagereference" title="StorageImageReference">StorageImageReference</a>: <i>
      - &lt;a href=&#34;storageimagereference.md&#34;&gt;StorageImageReference&lt;/a&gt;</i>
    <a href="#storageosdisk" title="StorageOsDisk">StorageOsDisk</a>: <i>
      - &lt;a href=&#34;storageosdisk.md&#34;&gt;StorageOsDisk&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#sshkeys" title="SshKeys">SshKeys</a>: <i>
      - &lt;a href=&#34;sshkeys.md&#34;&gt;SshKeys&lt;/a&gt;</i>
    <a href="#vaultcertificates" title="VaultCertificates">VaultCertificates</a>: <i>
      - &lt;a href=&#34;vaultcertificates.md&#34;&gt;VaultCertificates&lt;/a&gt;</i>
    <a href="#additionalunattendconfig" title="AdditionalUnattendConfig">AdditionalUnattendConfig</a>: <i>
      - &lt;a href=&#34;additionalunattendconfig.md&#34;&gt;AdditionalUnattendConfig&lt;/a&gt;</i>
    <a href="#winrm" title="Winrm">Winrm</a>: <i>
      - &lt;a href=&#34;winrm.md&#34;&gt;Winrm&lt;/a&gt;</i>
</pre>

## Properties

#### AvailabilitySetId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteDataDisksOnTermination

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteOsDiskOnTermination

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInterfaceIds

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryNetworkInterfaceId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProximityPlacementGroupId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmSize

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zones

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalCapabilities

_Required_: No

_Type_: List of &lt;a href=&#34;additionalcapabilities.md&#34;&gt;AdditionalCapabilities&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootDiagnostics

_Required_: No

_Type_: List of &lt;a href=&#34;bootdiagnostics.md&#34;&gt;BootDiagnostics&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identity

_Required_: No

_Type_: List of &lt;a href=&#34;identity.md&#34;&gt;Identity&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsProfile

_Required_: No

_Type_: List of &lt;a href=&#34;osprofile.md&#34;&gt;OsProfile&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsProfileLinuxConfig

_Required_: No

_Type_: List of &lt;a href=&#34;osprofilelinuxconfig.md&#34;&gt;OsProfileLinuxConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsProfileSecrets

_Required_: No

_Type_: List of &lt;a href=&#34;osprofilesecrets.md&#34;&gt;OsProfileSecrets&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsProfileWindowsConfig

_Required_: No

_Type_: List of &lt;a href=&#34;osprofilewindowsconfig.md&#34;&gt;OsProfileWindowsConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Plan

_Required_: No

_Type_: List of &lt;a href=&#34;plan.md&#34;&gt;Plan&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageDataDisk

_Required_: No

_Type_: List of &lt;a href=&#34;storagedatadisk.md&#34;&gt;StorageDataDisk&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageImageReference

_Required_: No

_Type_: List of &lt;a href=&#34;storageimagereference.md&#34;&gt;StorageImageReference&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageOsDisk

_Required_: No

_Type_: List of &lt;a href=&#34;storageosdisk.md&#34;&gt;StorageOsDisk&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKeys

_Required_: No

_Type_: List of &lt;a href=&#34;sshkeys.md&#34;&gt;SshKeys&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VaultCertificates

_Required_: No

_Type_: List of &lt;a href=&#34;vaultcertificates.md&#34;&gt;VaultCertificates&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalUnattendConfig

_Required_: No

_Type_: List of &lt;a href=&#34;additionalunattendconfig.md&#34;&gt;AdditionalUnattendConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Winrm

_Required_: No

_Type_: List of &lt;a href=&#34;winrm.md&#34;&gt;Winrm&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

