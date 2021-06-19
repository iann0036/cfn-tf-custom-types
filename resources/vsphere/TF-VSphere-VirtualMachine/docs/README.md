# TF::VSphere::VirtualMachine

The `vsphere_virtual_machine` resource can be used to manage the complex
lifecycle of a virtual machine. It supports management of disk, network
interface, and CDROM devices, creation from scratch or cloning from template,
and migration through both host and storage vMotion.

For more details on working with virtual machines in vSphere, see [this
page][vmware-docs-vm-management].

[vmware-docs-vm-management]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vm_admin.doc/GUID-55238059-912E-411F-A0E9-A7A536972A91.html

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::VSphere::VirtualMachine",
    "Properties" : {
        "<a href="#alternateguestname" title="AlternateGuestName">AlternateGuestName</a>" : <i>String</i>,
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#bootdelay" title="BootDelay">BootDelay</a>" : <i>Double</i>,
        "<a href="#bootretrydelay" title="BootRetryDelay">BootRetryDelay</a>" : <i>Double</i>,
        "<a href="#bootretryenabled" title="BootRetryEnabled">BootRetryEnabled</a>" : <i>Boolean</i>,
        "<a href="#cpuhotaddenabled" title="CpuHotAddEnabled">CpuHotAddEnabled</a>" : <i>Boolean</i>,
        "<a href="#cpuhotremoveenabled" title="CpuHotRemoveEnabled">CpuHotRemoveEnabled</a>" : <i>Boolean</i>,
        "<a href="#cpulimit" title="CpuLimit">CpuLimit</a>" : <i>Double</i>,
        "<a href="#cpuperformancecountersenabled" title="CpuPerformanceCountersEnabled">CpuPerformanceCountersEnabled</a>" : <i>Boolean</i>,
        "<a href="#cpureservation" title="CpuReservation">CpuReservation</a>" : <i>Double</i>,
        "<a href="#cpusharecount" title="CpuShareCount">CpuShareCount</a>" : <i>Double</i>,
        "<a href="#cpusharelevel" title="CpuShareLevel">CpuShareLevel</a>" : <i>String</i>,
        "<a href="#customattributes" title="CustomAttributes">CustomAttributes</a>" : <i>[ <a href="customattributesdefinition.md">CustomAttributesDefinition</a>, ... ]</i>,
        "<a href="#datacenterid" title="DatacenterId">DatacenterId</a>" : <i>String</i>,
        "<a href="#datastoreclusterid" title="DatastoreClusterId">DatastoreClusterId</a>" : <i>String</i>,
        "<a href="#datastoreid" title="DatastoreId">DatastoreId</a>" : <i>String</i>,
        "<a href="#efisecurebootenabled" title="EfiSecureBootEnabled">EfiSecureBootEnabled</a>" : <i>Boolean</i>,
        "<a href="#enablediskuuid" title="EnableDiskUuid">EnableDiskUuid</a>" : <i>Boolean</i>,
        "<a href="#enablelogging" title="EnableLogging">EnableLogging</a>" : <i>Boolean</i>,
        "<a href="#eptrvimode" title="EptRviMode">EptRviMode</a>" : <i>String</i>,
        "<a href="#extraconfig" title="ExtraConfig">ExtraConfig</a>" : <i>[ <a href="extraconfigdefinition.md">ExtraConfigDefinition</a>, ... ]</i>,
        "<a href="#firmware" title="Firmware">Firmware</a>" : <i>String</i>,
        "<a href="#folder" title="Folder">Folder</a>" : <i>String</i>,
        "<a href="#forcepoweroff" title="ForcePowerOff">ForcePowerOff</a>" : <i>Boolean</i>,
        "<a href="#guestid" title="GuestId">GuestId</a>" : <i>String</i>,
        "<a href="#hardwareversion" title="HardwareVersion">HardwareVersion</a>" : <i>Double</i>,
        "<a href="#hostsystemid" title="HostSystemId">HostSystemId</a>" : <i>String</i>,
        "<a href="#hvmode" title="HvMode">HvMode</a>" : <i>String</i>,
        "<a href="#idecontrollercount" title="IdeControllerCount">IdeControllerCount</a>" : <i>Double</i>,
        "<a href="#ignoredguestips" title="IgnoredGuestIps">IgnoredGuestIps</a>" : <i>[ String, ... ]</i>,
        "<a href="#latencysensitivity" title="LatencySensitivity">LatencySensitivity</a>" : <i>String</i>,
        "<a href="#memory" title="Memory">Memory</a>" : <i>Double</i>,
        "<a href="#memoryhotaddenabled" title="MemoryHotAddEnabled">MemoryHotAddEnabled</a>" : <i>Boolean</i>,
        "<a href="#memorylimit" title="MemoryLimit">MemoryLimit</a>" : <i>Double</i>,
        "<a href="#memoryreservation" title="MemoryReservation">MemoryReservation</a>" : <i>Double</i>,
        "<a href="#memorysharecount" title="MemoryShareCount">MemoryShareCount</a>" : <i>Double</i>,
        "<a href="#memorysharelevel" title="MemoryShareLevel">MemoryShareLevel</a>" : <i>String</i>,
        "<a href="#migratewaittimeout" title="MigrateWaitTimeout">MigrateWaitTimeout</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nestedhvenabled" title="NestedHvEnabled">NestedHvEnabled</a>" : <i>Boolean</i>,
        "<a href="#numcorespersocket" title="NumCoresPerSocket">NumCoresPerSocket</a>" : <i>Double</i>,
        "<a href="#numcpus" title="NumCpus">NumCpus</a>" : <i>Double</i>,
        "<a href="#pcideviceid" title="PciDeviceId">PciDeviceId</a>" : <i>[ String, ... ]</i>,
        "<a href="#powerontimeout" title="PoweronTimeout">PoweronTimeout</a>" : <i>Double</i>,
        "<a href="#replacetrigger" title="ReplaceTrigger">ReplaceTrigger</a>" : <i>String</i>,
        "<a href="#resourcepoolid" title="ResourcePoolId">ResourcePoolId</a>" : <i>String</i>,
        "<a href="#runtoolsscriptsafterpoweron" title="RunToolsScriptsAfterPowerOn">RunToolsScriptsAfterPowerOn</a>" : <i>Boolean</i>,
        "<a href="#runtoolsscriptsafterresume" title="RunToolsScriptsAfterResume">RunToolsScriptsAfterResume</a>" : <i>Boolean</i>,
        "<a href="#runtoolsscriptsbeforeguestreboot" title="RunToolsScriptsBeforeGuestReboot">RunToolsScriptsBeforeGuestReboot</a>" : <i>Boolean</i>,
        "<a href="#runtoolsscriptsbeforeguestshutdown" title="RunToolsScriptsBeforeGuestShutdown">RunToolsScriptsBeforeGuestShutdown</a>" : <i>Boolean</i>,
        "<a href="#runtoolsscriptsbeforegueststandby" title="RunToolsScriptsBeforeGuestStandby">RunToolsScriptsBeforeGuestStandby</a>" : <i>Boolean</i>,
        "<a href="#satacontrollercount" title="SataControllerCount">SataControllerCount</a>" : <i>Double</i>,
        "<a href="#scsibussharing" title="ScsiBusSharing">ScsiBusSharing</a>" : <i>String</i>,
        "<a href="#scsicontrollercount" title="ScsiControllerCount">ScsiControllerCount</a>" : <i>Double</i>,
        "<a href="#scsitype" title="ScsiType">ScsiType</a>" : <i>String</i>,
        "<a href="#shutdownwaittimeout" title="ShutdownWaitTimeout">ShutdownWaitTimeout</a>" : <i>Double</i>,
        "<a href="#storagepolicyid" title="StoragePolicyId">StoragePolicyId</a>" : <i>String</i>,
        "<a href="#swapplacementpolicy" title="SwapPlacementPolicy">SwapPlacementPolicy</a>" : <i>String</i>,
        "<a href="#synctimewithhost" title="SyncTimeWithHost">SyncTimeWithHost</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#vbsenabled" title="VbsEnabled">VbsEnabled</a>" : <i>Boolean</i>,
        "<a href="#vvtdenabled" title="VvtdEnabled">VvtdEnabled</a>" : <i>Boolean</i>,
        "<a href="#waitforguestiptimeout" title="WaitForGuestIpTimeout">WaitForGuestIpTimeout</a>" : <i>Double</i>,
        "<a href="#waitforguestnetroutable" title="WaitForGuestNetRoutable">WaitForGuestNetRoutable</a>" : <i>Boolean</i>,
        "<a href="#waitforguestnettimeout" title="WaitForGuestNetTimeout">WaitForGuestNetTimeout</a>" : <i>Double</i>,
        "<a href="#cdrom" title="Cdrom">Cdrom</a>" : <i>[ <a href="cdromdefinition.md">CdromDefinition</a>, ... ]</i>,
        "<a href="#clone" title="Clone">Clone</a>" : <i>[ <a href="clonedefinition.md">CloneDefinition</a>, ... ]</i>,
        "<a href="#disk" title="Disk">Disk</a>" : <i>[ <a href="diskdefinition.md">DiskDefinition</a>, ... ]</i>,
        "<a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>" : <i>[ <a href="networkinterfacedefinition.md">NetworkInterfaceDefinition</a>, ... ]</i>,
        "<a href="#ovfdeploy" title="OvfDeploy">OvfDeploy</a>" : <i>[ <a href="ovfdeploydefinition.md">OvfDeployDefinition</a>, ... ]</i>,
        "<a href="#vapp" title="Vapp">Vapp</a>" : <i>[ <a href="vappdefinition.md">VappDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::VSphere::VirtualMachine
Properties:
    <a href="#alternateguestname" title="AlternateGuestName">AlternateGuestName</a>: <i>String</i>
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#bootdelay" title="BootDelay">BootDelay</a>: <i>Double</i>
    <a href="#bootretrydelay" title="BootRetryDelay">BootRetryDelay</a>: <i>Double</i>
    <a href="#bootretryenabled" title="BootRetryEnabled">BootRetryEnabled</a>: <i>Boolean</i>
    <a href="#cpuhotaddenabled" title="CpuHotAddEnabled">CpuHotAddEnabled</a>: <i>Boolean</i>
    <a href="#cpuhotremoveenabled" title="CpuHotRemoveEnabled">CpuHotRemoveEnabled</a>: <i>Boolean</i>
    <a href="#cpulimit" title="CpuLimit">CpuLimit</a>: <i>Double</i>
    <a href="#cpuperformancecountersenabled" title="CpuPerformanceCountersEnabled">CpuPerformanceCountersEnabled</a>: <i>Boolean</i>
    <a href="#cpureservation" title="CpuReservation">CpuReservation</a>: <i>Double</i>
    <a href="#cpusharecount" title="CpuShareCount">CpuShareCount</a>: <i>Double</i>
    <a href="#cpusharelevel" title="CpuShareLevel">CpuShareLevel</a>: <i>String</i>
    <a href="#customattributes" title="CustomAttributes">CustomAttributes</a>: <i>
      - <a href="customattributesdefinition.md">CustomAttributesDefinition</a></i>
    <a href="#datacenterid" title="DatacenterId">DatacenterId</a>: <i>String</i>
    <a href="#datastoreclusterid" title="DatastoreClusterId">DatastoreClusterId</a>: <i>String</i>
    <a href="#datastoreid" title="DatastoreId">DatastoreId</a>: <i>String</i>
    <a href="#efisecurebootenabled" title="EfiSecureBootEnabled">EfiSecureBootEnabled</a>: <i>Boolean</i>
    <a href="#enablediskuuid" title="EnableDiskUuid">EnableDiskUuid</a>: <i>Boolean</i>
    <a href="#enablelogging" title="EnableLogging">EnableLogging</a>: <i>Boolean</i>
    <a href="#eptrvimode" title="EptRviMode">EptRviMode</a>: <i>String</i>
    <a href="#extraconfig" title="ExtraConfig">ExtraConfig</a>: <i>
      - <a href="extraconfigdefinition.md">ExtraConfigDefinition</a></i>
    <a href="#firmware" title="Firmware">Firmware</a>: <i>String</i>
    <a href="#folder" title="Folder">Folder</a>: <i>String</i>
    <a href="#forcepoweroff" title="ForcePowerOff">ForcePowerOff</a>: <i>Boolean</i>
    <a href="#guestid" title="GuestId">GuestId</a>: <i>String</i>
    <a href="#hardwareversion" title="HardwareVersion">HardwareVersion</a>: <i>Double</i>
    <a href="#hostsystemid" title="HostSystemId">HostSystemId</a>: <i>String</i>
    <a href="#hvmode" title="HvMode">HvMode</a>: <i>String</i>
    <a href="#idecontrollercount" title="IdeControllerCount">IdeControllerCount</a>: <i>Double</i>
    <a href="#ignoredguestips" title="IgnoredGuestIps">IgnoredGuestIps</a>: <i>
      - String</i>
    <a href="#latencysensitivity" title="LatencySensitivity">LatencySensitivity</a>: <i>String</i>
    <a href="#memory" title="Memory">Memory</a>: <i>Double</i>
    <a href="#memoryhotaddenabled" title="MemoryHotAddEnabled">MemoryHotAddEnabled</a>: <i>Boolean</i>
    <a href="#memorylimit" title="MemoryLimit">MemoryLimit</a>: <i>Double</i>
    <a href="#memoryreservation" title="MemoryReservation">MemoryReservation</a>: <i>Double</i>
    <a href="#memorysharecount" title="MemoryShareCount">MemoryShareCount</a>: <i>Double</i>
    <a href="#memorysharelevel" title="MemoryShareLevel">MemoryShareLevel</a>: <i>String</i>
    <a href="#migratewaittimeout" title="MigrateWaitTimeout">MigrateWaitTimeout</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nestedhvenabled" title="NestedHvEnabled">NestedHvEnabled</a>: <i>Boolean</i>
    <a href="#numcorespersocket" title="NumCoresPerSocket">NumCoresPerSocket</a>: <i>Double</i>
    <a href="#numcpus" title="NumCpus">NumCpus</a>: <i>Double</i>
    <a href="#pcideviceid" title="PciDeviceId">PciDeviceId</a>: <i>
      - String</i>
    <a href="#powerontimeout" title="PoweronTimeout">PoweronTimeout</a>: <i>Double</i>
    <a href="#replacetrigger" title="ReplaceTrigger">ReplaceTrigger</a>: <i>String</i>
    <a href="#resourcepoolid" title="ResourcePoolId">ResourcePoolId</a>: <i>String</i>
    <a href="#runtoolsscriptsafterpoweron" title="RunToolsScriptsAfterPowerOn">RunToolsScriptsAfterPowerOn</a>: <i>Boolean</i>
    <a href="#runtoolsscriptsafterresume" title="RunToolsScriptsAfterResume">RunToolsScriptsAfterResume</a>: <i>Boolean</i>
    <a href="#runtoolsscriptsbeforeguestreboot" title="RunToolsScriptsBeforeGuestReboot">RunToolsScriptsBeforeGuestReboot</a>: <i>Boolean</i>
    <a href="#runtoolsscriptsbeforeguestshutdown" title="RunToolsScriptsBeforeGuestShutdown">RunToolsScriptsBeforeGuestShutdown</a>: <i>Boolean</i>
    <a href="#runtoolsscriptsbeforegueststandby" title="RunToolsScriptsBeforeGuestStandby">RunToolsScriptsBeforeGuestStandby</a>: <i>Boolean</i>
    <a href="#satacontrollercount" title="SataControllerCount">SataControllerCount</a>: <i>Double</i>
    <a href="#scsibussharing" title="ScsiBusSharing">ScsiBusSharing</a>: <i>String</i>
    <a href="#scsicontrollercount" title="ScsiControllerCount">ScsiControllerCount</a>: <i>Double</i>
    <a href="#scsitype" title="ScsiType">ScsiType</a>: <i>String</i>
    <a href="#shutdownwaittimeout" title="ShutdownWaitTimeout">ShutdownWaitTimeout</a>: <i>Double</i>
    <a href="#storagepolicyid" title="StoragePolicyId">StoragePolicyId</a>: <i>String</i>
    <a href="#swapplacementpolicy" title="SwapPlacementPolicy">SwapPlacementPolicy</a>: <i>String</i>
    <a href="#synctimewithhost" title="SyncTimeWithHost">SyncTimeWithHost</a>: <i>Boolean</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#vbsenabled" title="VbsEnabled">VbsEnabled</a>: <i>Boolean</i>
    <a href="#vvtdenabled" title="VvtdEnabled">VvtdEnabled</a>: <i>Boolean</i>
    <a href="#waitforguestiptimeout" title="WaitForGuestIpTimeout">WaitForGuestIpTimeout</a>: <i>Double</i>
    <a href="#waitforguestnetroutable" title="WaitForGuestNetRoutable">WaitForGuestNetRoutable</a>: <i>Boolean</i>
    <a href="#waitforguestnettimeout" title="WaitForGuestNetTimeout">WaitForGuestNetTimeout</a>: <i>Double</i>
    <a href="#cdrom" title="Cdrom">Cdrom</a>: <i>
      - <a href="cdromdefinition.md">CdromDefinition</a></i>
    <a href="#clone" title="Clone">Clone</a>: <i>
      - <a href="clonedefinition.md">CloneDefinition</a></i>
    <a href="#disk" title="Disk">Disk</a>: <i>
      - <a href="diskdefinition.md">DiskDefinition</a></i>
    <a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>: <i>
      - <a href="networkinterfacedefinition.md">NetworkInterfaceDefinition</a></i>
    <a href="#ovfdeploy" title="OvfDeploy">OvfDeploy</a>: <i>
      - <a href="ovfdeploydefinition.md">OvfDeployDefinition</a></i>
    <a href="#vapp" title="Vapp">Vapp</a>: <i>
      - <a href="vappdefinition.md">VappDefinition</a></i>
</pre>

## Properties

#### AlternateGuestName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Annotation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootDelay

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootRetryDelay

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootRetryEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuHotAddEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuHotRemoveEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuPerformanceCountersEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuReservation

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuShareCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuShareLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomAttributes

_Required_: No

_Type_: List of <a href="customattributesdefinition.md">CustomAttributesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatacenterId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatastoreClusterId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatastoreId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EfiSecureBootEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableDiskUuid

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableLogging

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EptRviMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtraConfig

_Required_: No

_Type_: List of <a href="extraconfigdefinition.md">ExtraConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Firmware

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Folder

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForcePowerOff

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HardwareVersion

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostSystemId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HvMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdeControllerCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoredGuestIps

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LatencySensitivity

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

#### MemoryLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryReservation

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryShareCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryShareLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MigrateWaitTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NestedHvEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumCoresPerSocket

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumCpus

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PciDeviceId

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PoweronTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplaceTrigger

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourcePoolId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunToolsScriptsAfterPowerOn

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunToolsScriptsAfterResume

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunToolsScriptsBeforeGuestReboot

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunToolsScriptsBeforeGuestShutdown

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunToolsScriptsBeforeGuestStandby

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SataControllerCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScsiBusSharing

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScsiControllerCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScsiType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShutdownWaitTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StoragePolicyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwapPlacementPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SyncTimeWithHost

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VbsEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VvtdEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForGuestIpTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForGuestNetRoutable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForGuestNetTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cdrom

_Required_: No

_Type_: List of <a href="cdromdefinition.md">CdromDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Clone

_Required_: No

_Type_: List of <a href="clonedefinition.md">CloneDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disk

_Required_: No

_Type_: List of <a href="diskdefinition.md">DiskDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInterface

_Required_: No

_Type_: List of <a href="networkinterfacedefinition.md">NetworkInterfaceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OvfDeploy

_Required_: No

_Type_: List of <a href="ovfdeploydefinition.md">OvfDeployDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vapp

_Required_: No

_Type_: List of <a href="vappdefinition.md">VappDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ChangeVersion

Returns the <code>ChangeVersion</code> value.

#### DefaultIpAddress

Returns the <code>DefaultIpAddress</code> value.

#### GuestIpAddresses

Returns the <code>GuestIpAddresses</code> value.

#### Id

Returns the <code>Id</code> value.

#### Imported

Returns the <code>Imported</code> value.

#### Moid

Returns the <code>Moid</code> value.

#### RebootRequired

Returns the <code>RebootRequired</code> value.

#### Uuid

Returns the <code>Uuid</code> value.

#### VappTransport

Returns the <code>VappTransport</code> value.

#### VmwareToolsStatus

Returns the <code>VmwareToolsStatus</code> value.

#### VmxPath

Returns the <code>VmxPath</code> value.

