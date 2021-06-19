# TF::AzureRM::VirtualMachineScaleSet

Manages a virtual machine scale set.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::VirtualMachineScaleSet",
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
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#upgradepolicymode" title="UpgradePolicyMode">UpgradePolicyMode</a>" : <i>String</i>,
        "<a href="#zones" title="Zones">Zones</a>" : <i>[ String, ... ]</i>,
        "<a href="#bootdiagnostics" title="BootDiagnostics">BootDiagnostics</a>" : <i>[ <a href="bootdiagnosticsdefinition.md">BootDiagnosticsDefinition</a>, ... ]</i>,
        "<a href="#extension" title="Extension">Extension</a>" : <i>[ <a href="extensiondefinition.md">ExtensionDefinition</a>, ... ]</i>,
        "<a href="#identity" title="Identity">Identity</a>" : <i>[ <a href="identitydefinition.md">IdentityDefinition</a>, ... ]</i>,
        "<a href="#networkprofile" title="NetworkProfile">NetworkProfile</a>" : <i>[ <a href="networkprofiledefinition.md">NetworkProfileDefinition</a>, ... ]</i>,
        "<a href="#osprofile" title="OsProfile">OsProfile</a>" : <i>[ <a href="osprofiledefinition.md">OsProfileDefinition</a>, ... ]</i>,
        "<a href="#osprofilelinuxconfig" title="OsProfileLinuxConfig">OsProfileLinuxConfig</a>" : <i>[ <a href="osprofilelinuxconfigdefinition.md">OsProfileLinuxConfigDefinition</a>, ... ]</i>,
        "<a href="#osprofilesecrets" title="OsProfileSecrets">OsProfileSecrets</a>" : <i>[ <a href="osprofilesecretsdefinition.md">OsProfileSecretsDefinition</a>, ... ]</i>,
        "<a href="#osprofilewindowsconfig" title="OsProfileWindowsConfig">OsProfileWindowsConfig</a>" : <i>[ <a href="osprofilewindowsconfigdefinition.md">OsProfileWindowsConfigDefinition</a>, ... ]</i>,
        "<a href="#plan" title="Plan">Plan</a>" : <i>[ <a href="plandefinition.md">PlanDefinition</a>, ... ]</i>,
        "<a href="#rollingupgradepolicy" title="RollingUpgradePolicy">RollingUpgradePolicy</a>" : <i>[ <a href="rollingupgradepolicydefinition.md">RollingUpgradePolicyDefinition</a>, ... ]</i>,
        "<a href="#sku" title="Sku">Sku</a>" : <i>[ <a href="skudefinition.md">SkuDefinition</a>, ... ]</i>,
        "<a href="#storageprofiledatadisk" title="StorageProfileDataDisk">StorageProfileDataDisk</a>" : <i>[ <a href="storageprofiledatadiskdefinition.md">StorageProfileDataDiskDefinition</a>, ... ]</i>,
        "<a href="#storageprofileimagereference" title="StorageProfileImageReference">StorageProfileImageReference</a>" : <i>[ <a href="storageprofileimagereferencedefinition.md">StorageProfileImageReferenceDefinition</a>, ... ]</i>,
        "<a href="#storageprofileosdisk" title="StorageProfileOsDisk">StorageProfileOsDisk</a>" : <i>[ <a href="storageprofileosdiskdefinition.md">StorageProfileOsDiskDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::VirtualMachineScaleSet
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
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#upgradepolicymode" title="UpgradePolicyMode">UpgradePolicyMode</a>: <i>String</i>
    <a href="#zones" title="Zones">Zones</a>: <i>
      - String</i>
    <a href="#bootdiagnostics" title="BootDiagnostics">BootDiagnostics</a>: <i>
      - <a href="bootdiagnosticsdefinition.md">BootDiagnosticsDefinition</a></i>
    <a href="#extension" title="Extension">Extension</a>: <i>
      - <a href="extensiondefinition.md">ExtensionDefinition</a></i>
    <a href="#identity" title="Identity">Identity</a>: <i>
      - <a href="identitydefinition.md">IdentityDefinition</a></i>
    <a href="#networkprofile" title="NetworkProfile">NetworkProfile</a>: <i>
      - <a href="networkprofiledefinition.md">NetworkProfileDefinition</a></i>
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
    <a href="#rollingupgradepolicy" title="RollingUpgradePolicy">RollingUpgradePolicy</a>: <i>
      - <a href="rollingupgradepolicydefinition.md">RollingUpgradePolicyDefinition</a></i>
    <a href="#sku" title="Sku">Sku</a>: <i>
      - <a href="skudefinition.md">SkuDefinition</a></i>
    <a href="#storageprofiledatadisk" title="StorageProfileDataDisk">StorageProfileDataDisk</a>: <i>
      - <a href="storageprofiledatadiskdefinition.md">StorageProfileDataDiskDefinition</a></i>
    <a href="#storageprofileimagereference" title="StorageProfileImageReference">StorageProfileImageReference</a>: <i>
      - <a href="storageprofileimagereferencedefinition.md">StorageProfileImageReferenceDefinition</a></i>
    <a href="#storageprofileosdisk" title="StorageProfileOsDisk">StorageProfileOsDisk</a>: <i>
      - <a href="storageprofileosdiskdefinition.md">StorageProfileOsDiskDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
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

Specifies whether the virtual machine scale set should be overprovisioned. Defaults to `true`.

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

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

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

_Type_: List of <a href="bootdiagnosticsdefinition.md">BootDiagnosticsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Extension

_Required_: No

_Type_: List of <a href="extensiondefinition.md">ExtensionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identity

_Required_: No

_Type_: List of <a href="identitydefinition.md">IdentityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkProfile

_Required_: No

_Type_: List of <a href="networkprofiledefinition.md">NetworkProfileDefinition</a>

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

#### RollingUpgradePolicy

_Required_: No

_Type_: List of <a href="rollingupgradepolicydefinition.md">RollingUpgradePolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sku

_Required_: No

_Type_: List of <a href="skudefinition.md">SkuDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageProfileDataDisk

_Required_: No

_Type_: List of <a href="storageprofiledatadiskdefinition.md">StorageProfileDataDiskDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageProfileImageReference

_Required_: No

_Type_: List of <a href="storageprofileimagereferencedefinition.md">StorageProfileImageReferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageProfileOsDisk

_Required_: No

_Type_: List of <a href="storageprofileosdiskdefinition.md">StorageProfileOsDiskDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

