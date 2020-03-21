# Terraform::AzureStack::VirtualMachineScaleSet

CloudFormation equivalent of azurestack_virtual_machine_scale_set

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureStack::VirtualMachineScaleSet",
    "Properties" : {
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#licensetype" title="LicenseType">LicenseType</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#overprovision" title="Overprovision">Overprovision</a>" : <i>Boolean</i>,
        "<a href="#priority" title="Priority">Priority</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#singleplacementgroup" title="SinglePlacementGroup">SinglePlacementGroup</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#upgradepolicymode" title="UpgradePolicyMode">UpgradePolicyMode</a>" : <i>String</i>,
        "<a href="#extension" title="Extension">Extension</a>" : <i>[ &lt;a href=&#34;extension.md&#34;&gt;Extension&lt;/a&gt;, ... ]</i>,
        "<a href="#identity" title="Identity">Identity</a>" : <i>[ &lt;a href=&#34;identity.md&#34;&gt;Identity&lt;/a&gt;, ... ]</i>,
        "<a href="#networkprofile" title="NetworkProfile">NetworkProfile</a>" : <i>[ &lt;a href=&#34;networkprofile.md&#34;&gt;NetworkProfile&lt;/a&gt;, ... ]</i>,
        "<a href="#osprofile" title="OsProfile">OsProfile</a>" : <i>[ &lt;a href=&#34;osprofile.md&#34;&gt;OsProfile&lt;/a&gt;, ... ]</i>,
        "<a href="#osprofilelinuxconfig" title="OsProfileLinuxConfig">OsProfileLinuxConfig</a>" : <i>[ &lt;a href=&#34;osprofilelinuxconfig.md&#34;&gt;OsProfileLinuxConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#osprofilesecrets" title="OsProfileSecrets">OsProfileSecrets</a>" : <i>[ &lt;a href=&#34;osprofilesecrets.md&#34;&gt;OsProfileSecrets&lt;/a&gt;, ... ]</i>,
        "<a href="#osprofilewindowsconfig" title="OsProfileWindowsConfig">OsProfileWindowsConfig</a>" : <i>[ &lt;a href=&#34;osprofilewindowsconfig.md&#34;&gt;OsProfileWindowsConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#plan" title="Plan">Plan</a>" : <i>[ &lt;a href=&#34;plan.md&#34;&gt;Plan&lt;/a&gt;, ... ]</i>,
        "<a href="#sku" title="Sku">Sku</a>" : <i>[ &lt;a href=&#34;sku.md&#34;&gt;Sku&lt;/a&gt;, ... ]</i>,
        "<a href="#storageprofiledatadisk" title="StorageProfileDataDisk">StorageProfileDataDisk</a>" : <i>[ &lt;a href=&#34;storageprofiledatadisk.md&#34;&gt;StorageProfileDataDisk&lt;/a&gt;, ... ]</i>,
        "<a href="#storageprofileimagereference" title="StorageProfileImageReference">StorageProfileImageReference</a>" : <i>[ &lt;a href=&#34;storageprofileimagereference.md&#34;&gt;StorageProfileImageReference&lt;/a&gt;, ... ]</i>,
        "<a href="#storageprofileosdisk" title="StorageProfileOsDisk">StorageProfileOsDisk</a>" : <i>[ &lt;a href=&#34;storageprofileosdisk.md&#34;&gt;StorageProfileOsDisk&lt;/a&gt;, ... ]</i>,
        "<a href="#ipconfiguration" title="IpConfiguration">IpConfiguration</a>" : <i>[ &lt;a href=&#34;ipconfiguration.md&#34;&gt;IpConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#sshkeys" title="SshKeys">SshKeys</a>" : <i>[ &lt;a href=&#34;sshkeys.md&#34;&gt;SshKeys&lt;/a&gt;, ... ]</i>,
        "<a href="#vaultcertificates" title="VaultCertificates">VaultCertificates</a>" : <i>[ &lt;a href=&#34;vaultcertificates.md&#34;&gt;VaultCertificates&lt;/a&gt;, ... ]</i>,
        "<a href="#additionalunattendconfig" title="AdditionalUnattendConfig">AdditionalUnattendConfig</a>" : <i>[ &lt;a href=&#34;additionalunattendconfig.md&#34;&gt;AdditionalUnattendConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#winrm" title="Winrm">Winrm</a>" : <i>[ &lt;a href=&#34;winrm.md&#34;&gt;Winrm&lt;/a&gt;, ... ]</i>,
        "<a href="#publicipaddressconfiguration" title="PublicIpAddressConfiguration">PublicIpAddressConfiguration</a>" : <i>[ &lt;a href=&#34;publicipaddressconfiguration.md&#34;&gt;PublicIpAddressConfiguration&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureStack::VirtualMachineScaleSet
Properties:
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#licensetype" title="LicenseType">LicenseType</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#overprovision" title="Overprovision">Overprovision</a>: <i>Boolean</i>
    <a href="#priority" title="Priority">Priority</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#singleplacementgroup" title="SinglePlacementGroup">SinglePlacementGroup</a>: <i>Boolean</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#upgradepolicymode" title="UpgradePolicyMode">UpgradePolicyMode</a>: <i>String</i>
    <a href="#extension" title="Extension">Extension</a>: <i>
      - &lt;a href=&#34;extension.md&#34;&gt;Extension&lt;/a&gt;</i>
    <a href="#identity" title="Identity">Identity</a>: <i>
      - &lt;a href=&#34;identity.md&#34;&gt;Identity&lt;/a&gt;</i>
    <a href="#networkprofile" title="NetworkProfile">NetworkProfile</a>: <i>
      - &lt;a href=&#34;networkprofile.md&#34;&gt;NetworkProfile&lt;/a&gt;</i>
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
    <a href="#sku" title="Sku">Sku</a>: <i>
      - &lt;a href=&#34;sku.md&#34;&gt;Sku&lt;/a&gt;</i>
    <a href="#storageprofiledatadisk" title="StorageProfileDataDisk">StorageProfileDataDisk</a>: <i>
      - &lt;a href=&#34;storageprofiledatadisk.md&#34;&gt;StorageProfileDataDisk&lt;/a&gt;</i>
    <a href="#storageprofileimagereference" title="StorageProfileImageReference">StorageProfileImageReference</a>: <i>
      - &lt;a href=&#34;storageprofileimagereference.md&#34;&gt;StorageProfileImageReference&lt;/a&gt;</i>
    <a href="#storageprofileosdisk" title="StorageProfileOsDisk">StorageProfileOsDisk</a>: <i>
      - &lt;a href=&#34;storageprofileosdisk.md&#34;&gt;StorageProfileOsDisk&lt;/a&gt;</i>
    <a href="#ipconfiguration" title="IpConfiguration">IpConfiguration</a>: <i>
      - &lt;a href=&#34;ipconfiguration.md&#34;&gt;IpConfiguration&lt;/a&gt;</i>
    <a href="#sshkeys" title="SshKeys">SshKeys</a>: <i>
      - &lt;a href=&#34;sshkeys.md&#34;&gt;SshKeys&lt;/a&gt;</i>
    <a href="#vaultcertificates" title="VaultCertificates">VaultCertificates</a>: <i>
      - &lt;a href=&#34;vaultcertificates.md&#34;&gt;VaultCertificates&lt;/a&gt;</i>
    <a href="#additionalunattendconfig" title="AdditionalUnattendConfig">AdditionalUnattendConfig</a>: <i>
      - &lt;a href=&#34;additionalunattendconfig.md&#34;&gt;AdditionalUnattendConfig&lt;/a&gt;</i>
    <a href="#winrm" title="Winrm">Winrm</a>: <i>
      - &lt;a href=&#34;winrm.md&#34;&gt;Winrm&lt;/a&gt;</i>
    <a href="#publicipaddressconfiguration" title="PublicIpAddressConfiguration">PublicIpAddressConfiguration</a>: <i>
      - &lt;a href=&#34;publicipaddressconfiguration.md&#34;&gt;PublicIpAddressConfiguration&lt;/a&gt;</i>
</pre>

## Properties

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

#### Overprovision

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SinglePlacementGroup

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpgradePolicyMode

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Extension

_Required_: No

_Type_: List of &lt;a href=&#34;extension.md&#34;&gt;Extension&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identity

_Required_: No

_Type_: List of &lt;a href=&#34;identity.md&#34;&gt;Identity&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkProfile

_Required_: No

_Type_: List of &lt;a href=&#34;networkprofile.md&#34;&gt;NetworkProfile&lt;/a&gt;

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

#### Sku

_Required_: No

_Type_: List of &lt;a href=&#34;sku.md&#34;&gt;Sku&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageProfileDataDisk

_Required_: No

_Type_: List of &lt;a href=&#34;storageprofiledatadisk.md&#34;&gt;StorageProfileDataDisk&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageProfileImageReference

_Required_: No

_Type_: List of &lt;a href=&#34;storageprofileimagereference.md&#34;&gt;StorageProfileImageReference&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageProfileOsDisk

_Required_: No

_Type_: List of &lt;a href=&#34;storageprofileosdisk.md&#34;&gt;StorageProfileOsDisk&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;ipconfiguration.md&#34;&gt;IpConfiguration&lt;/a&gt;

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

#### PublicIpAddressConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;publicipaddressconfiguration.md&#34;&gt;PublicIpAddressConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

