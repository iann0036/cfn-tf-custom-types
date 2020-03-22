# Terraform::AzureRM::LinuxVirtualMachineScaleSet

Manages a Linux Virtual Machine Scale Set.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::LinuxVirtualMachineScaleSet",
    "Properties" : {
        "<a href="#adminpassword" title="AdminPassword">AdminPassword</a>" : <i>String</i>,
        "<a href="#adminusername" title="AdminUsername">AdminUsername</a>" : <i>String</i>,
        "<a href="#computernameprefix" title="ComputerNamePrefix">ComputerNamePrefix</a>" : <i>String</i>,
        "<a href="#customdata" title="CustomData">CustomData</a>" : <i>String</i>,
        "<a href="#disablepasswordauthentication" title="DisablePasswordAuthentication">DisablePasswordAuthentication</a>" : <i>Boolean</i>,
        "<a href="#donotrunextensionsonoverprovisionedmachines" title="DoNotRunExtensionsOnOverprovisionedMachines">DoNotRunExtensionsOnOverprovisionedMachines</a>" : <i>Boolean</i>,
        "<a href="#evictionpolicy" title="EvictionPolicy">EvictionPolicy</a>" : <i>String</i>,
        "<a href="#healthprobeid" title="HealthProbeId">HealthProbeId</a>" : <i>String</i>,
        "<a href="#instances" title="Instances">Instances</a>" : <i>Double</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#maxbidprice" title="MaxBidPrice">MaxBidPrice</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#overprovision" title="Overprovision">Overprovision</a>" : <i>Boolean</i>,
        "<a href="#priority" title="Priority">Priority</a>" : <i>String</i>,
        "<a href="#provisionvmagent" title="ProvisionVmAgent">ProvisionVmAgent</a>" : <i>Boolean</i>,
        "<a href="#proximityplacementgroupid" title="ProximityPlacementGroupId">ProximityPlacementGroupId</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#scaleinpolicy" title="ScaleInPolicy">ScaleInPolicy</a>" : <i>String</i>,
        "<a href="#singleplacementgroup" title="SinglePlacementGroup">SinglePlacementGroup</a>" : <i>Boolean</i>,
        "<a href="#sku" title="Sku">Sku</a>" : <i>String</i>,
        "<a href="#sourceimageid" title="SourceImageId">SourceImageId</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#upgrademode" title="UpgradeMode">UpgradeMode</a>" : <i>String</i>,
        "<a href="#zonebalance" title="ZoneBalance">ZoneBalance</a>" : <i>Boolean</i>,
        "<a href="#zones" title="Zones">Zones</a>" : <i>[ String, ... ]</i>,
        "<a href="#additionalcapabilities" title="AdditionalCapabilities">AdditionalCapabilities</a>" : <i>[ <a href="additionalcapabilities.md">AdditionalCapabilities</a>, ... ]</i>,
        "<a href="#adminsshkey" title="AdminSshKey">AdminSshKey</a>" : <i>[ <a href="adminsshkey.md">AdminSshKey</a>, ... ]</i>,
        "<a href="#automaticosupgradepolicy" title="AutomaticOsUpgradePolicy">AutomaticOsUpgradePolicy</a>" : <i>[ <a href="automaticosupgradepolicy.md">AutomaticOsUpgradePolicy</a>, ... ]</i>,
        "<a href="#bootdiagnostics" title="BootDiagnostics">BootDiagnostics</a>" : <i>[ <a href="bootdiagnostics.md">BootDiagnostics</a>, ... ]</i>,
        "<a href="#datadisk" title="DataDisk">DataDisk</a>" : <i>[ <a href="datadisk.md">DataDisk</a>, ... ]</i>,
        "<a href="#identity" title="Identity">Identity</a>" : <i>[ <a href="identity.md">Identity</a>, ... ]</i>,
        "<a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>" : <i>[ <a href="networkinterface.md">NetworkInterface</a>, ... ]</i>,
        "<a href="#osdisk" title="OsDisk">OsDisk</a>" : <i>[ <a href="osdisk.md">OsDisk</a>, ... ]</i>,
        "<a href="#plan" title="Plan">Plan</a>" : <i>[ <a href="plan.md">Plan</a>, ... ]</i>,
        "<a href="#rollingupgradepolicy" title="RollingUpgradePolicy">RollingUpgradePolicy</a>" : <i>[ <a href="rollingupgradepolicy.md">RollingUpgradePolicy</a>, ... ]</i>,
        "<a href="#secret" title="Secret">Secret</a>" : <i>[ <a href="secret.md">Secret</a>, ... ]</i>,
        "<a href="#sourceimagereference" title="SourceImageReference">SourceImageReference</a>" : <i>[ <a href="sourceimagereference.md">SourceImageReference</a>, ... ]</i>,
        "<a href="#terminatenotification" title="TerminateNotification">TerminateNotification</a>" : <i>[ <a href="terminatenotification.md">TerminateNotification</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#ipconfiguration" title="IpConfiguration">IpConfiguration</a>" : <i>[ <a href="ipconfiguration.md">IpConfiguration</a>, ... ]</i>,
        "<a href="#diffdisksettings" title="DiffDiskSettings">DiffDiskSettings</a>" : <i>[ <a href="diffdisksettings.md">DiffDiskSettings</a>, ... ]</i>,
        "<a href="#certificate" title="Certificate">Certificate</a>" : <i>[ <a href="certificate.md">Certificate</a>, ... ]</i>,
        "<a href="#publicipaddress" title="PublicIpAddress">PublicIpAddress</a>" : <i>[ <a href="publicipaddress.md">PublicIpAddress</a>, ... ]</i>,
        "<a href="#iptag" title="IpTag">IpTag</a>" : <i>[ <a href="iptag.md">IpTag</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::LinuxVirtualMachineScaleSet
Properties:
    <a href="#adminpassword" title="AdminPassword">AdminPassword</a>: <i>String</i>
    <a href="#adminusername" title="AdminUsername">AdminUsername</a>: <i>String</i>
    <a href="#computernameprefix" title="ComputerNamePrefix">ComputerNamePrefix</a>: <i>String</i>
    <a href="#customdata" title="CustomData">CustomData</a>: <i>String</i>
    <a href="#disablepasswordauthentication" title="DisablePasswordAuthentication">DisablePasswordAuthentication</a>: <i>Boolean</i>
    <a href="#donotrunextensionsonoverprovisionedmachines" title="DoNotRunExtensionsOnOverprovisionedMachines">DoNotRunExtensionsOnOverprovisionedMachines</a>: <i>Boolean</i>
    <a href="#evictionpolicy" title="EvictionPolicy">EvictionPolicy</a>: <i>String</i>
    <a href="#healthprobeid" title="HealthProbeId">HealthProbeId</a>: <i>String</i>
    <a href="#instances" title="Instances">Instances</a>: <i>Double</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#maxbidprice" title="MaxBidPrice">MaxBidPrice</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#overprovision" title="Overprovision">Overprovision</a>: <i>Boolean</i>
    <a href="#priority" title="Priority">Priority</a>: <i>String</i>
    <a href="#provisionvmagent" title="ProvisionVmAgent">ProvisionVmAgent</a>: <i>Boolean</i>
    <a href="#proximityplacementgroupid" title="ProximityPlacementGroupId">ProximityPlacementGroupId</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#scaleinpolicy" title="ScaleInPolicy">ScaleInPolicy</a>: <i>String</i>
    <a href="#singleplacementgroup" title="SinglePlacementGroup">SinglePlacementGroup</a>: <i>Boolean</i>
    <a href="#sku" title="Sku">Sku</a>: <i>String</i>
    <a href="#sourceimageid" title="SourceImageId">SourceImageId</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#upgrademode" title="UpgradeMode">UpgradeMode</a>: <i>String</i>
    <a href="#zonebalance" title="ZoneBalance">ZoneBalance</a>: <i>Boolean</i>
    <a href="#zones" title="Zones">Zones</a>: <i>
      - String</i>
    <a href="#additionalcapabilities" title="AdditionalCapabilities">AdditionalCapabilities</a>: <i>
      - <a href="additionalcapabilities.md">AdditionalCapabilities</a></i>
    <a href="#adminsshkey" title="AdminSshKey">AdminSshKey</a>: <i>
      - <a href="adminsshkey.md">AdminSshKey</a></i>
    <a href="#automaticosupgradepolicy" title="AutomaticOsUpgradePolicy">AutomaticOsUpgradePolicy</a>: <i>
      - <a href="automaticosupgradepolicy.md">AutomaticOsUpgradePolicy</a></i>
    <a href="#bootdiagnostics" title="BootDiagnostics">BootDiagnostics</a>: <i>
      - <a href="bootdiagnostics.md">BootDiagnostics</a></i>
    <a href="#datadisk" title="DataDisk">DataDisk</a>: <i>
      - <a href="datadisk.md">DataDisk</a></i>
    <a href="#identity" title="Identity">Identity</a>: <i>
      - <a href="identity.md">Identity</a></i>
    <a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>: <i>
      - <a href="networkinterface.md">NetworkInterface</a></i>
    <a href="#osdisk" title="OsDisk">OsDisk</a>: <i>
      - <a href="osdisk.md">OsDisk</a></i>
    <a href="#plan" title="Plan">Plan</a>: <i>
      - <a href="plan.md">Plan</a></i>
    <a href="#rollingupgradepolicy" title="RollingUpgradePolicy">RollingUpgradePolicy</a>: <i>
      - <a href="rollingupgradepolicy.md">RollingUpgradePolicy</a></i>
    <a href="#secret" title="Secret">Secret</a>: <i>
      - <a href="secret.md">Secret</a></i>
    <a href="#sourceimagereference" title="SourceImageReference">SourceImageReference</a>: <i>
      - <a href="sourceimagereference.md">SourceImageReference</a></i>
    <a href="#terminatenotification" title="TerminateNotification">TerminateNotification</a>: <i>
      - <a href="terminatenotification.md">TerminateNotification</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#ipconfiguration" title="IpConfiguration">IpConfiguration</a>: <i>
      - <a href="ipconfiguration.md">IpConfiguration</a></i>
    <a href="#diffdisksettings" title="DiffDiskSettings">DiffDiskSettings</a>: <i>
      - <a href="diffdisksettings.md">DiffDiskSettings</a></i>
    <a href="#certificate" title="Certificate">Certificate</a>: <i>
      - <a href="certificate.md">Certificate</a></i>
    <a href="#publicipaddress" title="PublicIpAddress">PublicIpAddress</a>: <i>
      - <a href="publicipaddress.md">PublicIpAddress</a></i>
    <a href="#iptag" title="IpTag">IpTag</a>: <i>
      - <a href="iptag.md">IpTag</a></i>
</pre>

## Properties

#### AdminPassword

The Password which should be used for the local-administrator on this Virtual Machine. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminUsername

The username of the local administrator on each Virtual Machine Scale Set instance. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComputerNamePrefix

The prefix which should be used for the name of the Virtual Machines in this Scale Set. If unspecified this defaults to the value for the `name` field.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomData

The Base64-Encoded Custom Data which should be used for this Virtual Machine Scale Set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisablePasswordAuthentication

Should Password Authentication be disabled on this Virtual Machine Scale Set? Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DoNotRunExtensionsOnOverprovisionedMachines

Should Virtual Machine Extensions be run on Overprovisioned Virtual Machines in the Scale Set? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EvictionPolicy

The Policy which should be used Virtual Machines are Evicted from the Scale Set. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthProbeId

The ID of a Load Balancer Probe which should be used to determine the health of an instance. Changing this forces a new resource to be created. This is Required and can only be specified when `upgrade_mode` is set to `Automatic` or `Rolling`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Instances

The number of Virtual Machines in the Scale Set.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

The Azure location where the Linux Virtual Machine Scale Set should exist. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxBidPrice

The maximum price you're willing to pay for each Virtual Machine in this Scale Set, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machines in the Scale Set will be evicted using the `eviction_policy`. Defaults to `-1`, which means that each Virtual Machine in this Scale Set should not be evicted for price reasons.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Linux Virtual Machine Scale Set. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Overprovision

Should Azure over-provision Virtual Machines in this Scale Set? This means that multiple Virtual Machines will be provisioned and Azure will keep the instances which become available first - which improves provisioning success rates and improves deployment time. You're not billed for these over-provisioned VM's and they don't count towards the Subscription Quota. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

The Priority of this Virtual Machine Scale Set. Possible values are `Regular` and `Spot`. Defaults to `Regular`. Changing this value forces a new resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProvisionVmAgent

Should the Azure VM Agent be provisioned on each Virtual Machine in the Scale Set? Defaults to `true`. Changing this value forces a new resource to be created.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProximityPlacementGroupId

The ID of the Proximity Placement Group in which the Virtual Machine Scale Set should be assigned to. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the Resource Group in which the Linux Virtual Machine Scale Set should be exist. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleInPolicy

The scale-in policy rule that decides which virtual machines are chosen for removal when a Virtual Machine Scale Set is scaled in. Possible values for the scale-in policy rules are `Default`, `NewestVM` and `OldestVM`, defaults to `Default`. For more information about scale in policy, please [refer to this doc](https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-scale-in-policy).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SinglePlacementGroup

Should this Virtual Machine Scale Set be limited to a Single Placement Group, which means the number of instances will be capped at 100 Virtual Machines. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sku

The Virtual Machine SKU for the Scale Set, such as `Standard_F2`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceImageId

The ID of an Image which each Virtual Machine in this Scale Set should be based on.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags which should be assigned to this Virtual Machine Scale Set.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpgradeMode

Specifies how Upgrades (e.g. changing the Image/SKU) should be performed to Virtual Machine Instances. Possible values are `Automatic`, `Manual` and `Rolling`. Defaults to `Manual`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneBalance

Should the Virtual Machines in this Scale Set be strictly evenly distributed across Availability Zones? Defaults to `false`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zones

A list of Availability Zones in which the Virtual Machines in this Scale Set should be created in. Changing this forces a new resource to be created.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalCapabilities

_Required_: No

_Type_: List of <a href="additionalcapabilities.md">AdditionalCapabilities</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminSshKey

_Required_: No

_Type_: List of <a href="adminsshkey.md">AdminSshKey</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutomaticOsUpgradePolicy

_Required_: No

_Type_: List of <a href="automaticosupgradepolicy.md">AutomaticOsUpgradePolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootDiagnostics

_Required_: No

_Type_: List of <a href="bootdiagnostics.md">BootDiagnostics</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataDisk

_Required_: No

_Type_: List of <a href="datadisk.md">DataDisk</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identity

_Required_: No

_Type_: List of <a href="identity.md">Identity</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInterface

_Required_: No

_Type_: List of <a href="networkinterface.md">NetworkInterface</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsDisk

_Required_: No

_Type_: List of <a href="osdisk.md">OsDisk</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Plan

_Required_: No

_Type_: List of <a href="plan.md">Plan</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RollingUpgradePolicy

_Required_: No

_Type_: List of <a href="rollingupgradepolicy.md">RollingUpgradePolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Secret

_Required_: No

_Type_: List of <a href="secret.md">Secret</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceImageReference

_Required_: No

_Type_: List of <a href="sourceimagereference.md">SourceImageReference</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TerminateNotification

_Required_: No

_Type_: List of <a href="terminatenotification.md">TerminateNotification</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpConfiguration

_Required_: No

_Type_: List of <a href="ipconfiguration.md">IpConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiffDiskSettings

_Required_: No

_Type_: List of <a href="diffdisksettings.md">DiffDiskSettings</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Certificate

_Required_: No

_Type_: List of <a href="certificate.md">Certificate</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIpAddress

_Required_: No

_Type_: List of <a href="publicipaddress.md">PublicIpAddress</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpTag

_Required_: No

_Type_: List of <a href="iptag.md">IpTag</a>

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

#### UniqueId

Returns the <code>UniqueId</code> value.

