# Terraform::VSphere::DistributedVirtualSwitch

The `vsphere_distributed_virtual_switch` resource can be used to manage VMware
Distributed Virtual Switches.

An essential component of a distributed, scalable VMware datacenter, the
vSphere Distributed Virtual Switch (DVS) provides centralized management and
monitoring of the networking configuration of all the hosts that are associated
with the switch. In addition to adding port groups (see the
[`vsphere_distributed_port_group`][distributed-port-group] resource) that can
be used as networks for virtual machines, a DVS can be configured to perform
advanced high availability, traffic shaping, network monitoring, and more.

For an overview on vSphere networking concepts, see [this
page][ref-vsphere-net-concepts]. For more information on vSphere DVS, see [this
page][ref-vsphere-dvs].

[distributed-port-group]: /docs/providers/vsphere/r/distributed_port_group.html
[ref-vsphere-net-concepts]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.networking.doc/GUID-2B11DBB8-CB3C-4AFF-8885-EFEA0FC562F4.html
[ref-vsphere-dvs]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.networking.doc/GUID-375B45C7-684C-4C51-BA3C-70E48DFABF04.html

~> **NOTE:** This resource requires vCenter and is not available on direct ESXi
connections.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VSphere::DistributedVirtualSwitch",
    "Properties" : {
        "<a href="#activeuplinks" title="ActiveUplinks">ActiveUplinks</a>" : <i>[ String, ... ]</i>,
        "<a href="#allowforgedtransmits" title="AllowForgedTransmits">AllowForgedTransmits</a>" : <i>Boolean</i>,
        "<a href="#allowmacchanges" title="AllowMacChanges">AllowMacChanges</a>" : <i>Boolean</i>,
        "<a href="#allowpromiscuous" title="AllowPromiscuous">AllowPromiscuous</a>" : <i>Boolean</i>,
        "<a href="#blockallports" title="BlockAllPorts">BlockAllPorts</a>" : <i>Boolean</i>,
        "<a href="#checkbeacon" title="CheckBeacon">CheckBeacon</a>" : <i>Boolean</i>,
        "<a href="#contactdetail" title="ContactDetail">ContactDetail</a>" : <i>String</i>,
        "<a href="#contactname" title="ContactName">ContactName</a>" : <i>String</i>,
        "<a href="#customattributes" title="CustomAttributes">CustomAttributes</a>" : <i>[ <a href="customattributes.md">CustomAttributes</a>, ... ]</i>,
        "<a href="#datacenterid" title="DatacenterId">DatacenterId</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#directpathgen2allowed" title="DirectpathGen2Allowed">DirectpathGen2Allowed</a>" : <i>Boolean</i>,
        "<a href="#egressshapingaveragebandwidth" title="EgressShapingAverageBandwidth">EgressShapingAverageBandwidth</a>" : <i>Double</i>,
        "<a href="#egressshapingburstsize" title="EgressShapingBurstSize">EgressShapingBurstSize</a>" : <i>Double</i>,
        "<a href="#egressshapingenabled" title="EgressShapingEnabled">EgressShapingEnabled</a>" : <i>Boolean</i>,
        "<a href="#egressshapingpeakbandwidth" title="EgressShapingPeakBandwidth">EgressShapingPeakBandwidth</a>" : <i>Double</i>,
        "<a href="#failback" title="Failback">Failback</a>" : <i>Boolean</i>,
        "<a href="#faulttolerancemaximummbit" title="FaulttoleranceMaximumMbit">FaulttoleranceMaximumMbit</a>" : <i>Double</i>,
        "<a href="#faulttolerancereservationmbit" title="FaulttoleranceReservationMbit">FaulttoleranceReservationMbit</a>" : <i>Double</i>,
        "<a href="#faulttolerancesharecount" title="FaulttoleranceShareCount">FaulttoleranceShareCount</a>" : <i>Double</i>,
        "<a href="#faulttolerancesharelevel" title="FaulttoleranceShareLevel">FaulttoleranceShareLevel</a>" : <i>String</i>,
        "<a href="#folder" title="Folder">Folder</a>" : <i>String</i>,
        "<a href="#hbrmaximummbit" title="HbrMaximumMbit">HbrMaximumMbit</a>" : <i>Double</i>,
        "<a href="#hbrreservationmbit" title="HbrReservationMbit">HbrReservationMbit</a>" : <i>Double</i>,
        "<a href="#hbrsharecount" title="HbrShareCount">HbrShareCount</a>" : <i>Double</i>,
        "<a href="#hbrsharelevel" title="HbrShareLevel">HbrShareLevel</a>" : <i>String</i>,
        "<a href="#ingressshapingaveragebandwidth" title="IngressShapingAverageBandwidth">IngressShapingAverageBandwidth</a>" : <i>Double</i>,
        "<a href="#ingressshapingburstsize" title="IngressShapingBurstSize">IngressShapingBurstSize</a>" : <i>Double</i>,
        "<a href="#ingressshapingenabled" title="IngressShapingEnabled">IngressShapingEnabled</a>" : <i>Boolean</i>,
        "<a href="#ingressshapingpeakbandwidth" title="IngressShapingPeakBandwidth">IngressShapingPeakBandwidth</a>" : <i>Double</i>,
        "<a href="#ipv4address" title="Ipv4Address">Ipv4Address</a>" : <i>String</i>,
        "<a href="#iscsimaximummbit" title="IscsiMaximumMbit">IscsiMaximumMbit</a>" : <i>Double</i>,
        "<a href="#iscsireservationmbit" title="IscsiReservationMbit">IscsiReservationMbit</a>" : <i>Double</i>,
        "<a href="#iscsisharecount" title="IscsiShareCount">IscsiShareCount</a>" : <i>Double</i>,
        "<a href="#iscsisharelevel" title="IscsiShareLevel">IscsiShareLevel</a>" : <i>String</i>,
        "<a href="#lacpapiversion" title="LacpApiVersion">LacpApiVersion</a>" : <i>String</i>,
        "<a href="#lacpenabled" title="LacpEnabled">LacpEnabled</a>" : <i>Boolean</i>,
        "<a href="#lacpmode" title="LacpMode">LacpMode</a>" : <i>String</i>,
        "<a href="#linkdiscoveryoperation" title="LinkDiscoveryOperation">LinkDiscoveryOperation</a>" : <i>String</i>,
        "<a href="#linkdiscoveryprotocol" title="LinkDiscoveryProtocol">LinkDiscoveryProtocol</a>" : <i>String</i>,
        "<a href="#managementmaximummbit" title="ManagementMaximumMbit">ManagementMaximumMbit</a>" : <i>Double</i>,
        "<a href="#managementreservationmbit" title="ManagementReservationMbit">ManagementReservationMbit</a>" : <i>Double</i>,
        "<a href="#managementsharecount" title="ManagementShareCount">ManagementShareCount</a>" : <i>Double</i>,
        "<a href="#managementsharelevel" title="ManagementShareLevel">ManagementShareLevel</a>" : <i>String</i>,
        "<a href="#maxmtu" title="MaxMtu">MaxMtu</a>" : <i>Double</i>,
        "<a href="#multicastfilteringmode" title="MulticastFilteringMode">MulticastFilteringMode</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#netflowactiveflowtimeout" title="NetflowActiveFlowTimeout">NetflowActiveFlowTimeout</a>" : <i>Double</i>,
        "<a href="#netflowcollectoripaddress" title="NetflowCollectorIpAddress">NetflowCollectorIpAddress</a>" : <i>String</i>,
        "<a href="#netflowcollectorport" title="NetflowCollectorPort">NetflowCollectorPort</a>" : <i>Double</i>,
        "<a href="#netflowenabled" title="NetflowEnabled">NetflowEnabled</a>" : <i>Boolean</i>,
        "<a href="#netflowidleflowtimeout" title="NetflowIdleFlowTimeout">NetflowIdleFlowTimeout</a>" : <i>Double</i>,
        "<a href="#netflowinternalflowsonly" title="NetflowInternalFlowsOnly">NetflowInternalFlowsOnly</a>" : <i>Boolean</i>,
        "<a href="#netflowobservationdomainid" title="NetflowObservationDomainId">NetflowObservationDomainId</a>" : <i>Double</i>,
        "<a href="#netflowsamplingrate" title="NetflowSamplingRate">NetflowSamplingRate</a>" : <i>Double</i>,
        "<a href="#networkresourcecontrolenabled" title="NetworkResourceControlEnabled">NetworkResourceControlEnabled</a>" : <i>Boolean</i>,
        "<a href="#networkresourcecontrolversion" title="NetworkResourceControlVersion">NetworkResourceControlVersion</a>" : <i>String</i>,
        "<a href="#nfsmaximummbit" title="NfsMaximumMbit">NfsMaximumMbit</a>" : <i>Double</i>,
        "<a href="#nfsreservationmbit" title="NfsReservationMbit">NfsReservationMbit</a>" : <i>Double</i>,
        "<a href="#nfssharecount" title="NfsShareCount">NfsShareCount</a>" : <i>Double</i>,
        "<a href="#nfssharelevel" title="NfsShareLevel">NfsShareLevel</a>" : <i>String</i>,
        "<a href="#notifyswitches" title="NotifySwitches">NotifySwitches</a>" : <i>Boolean</i>,
        "<a href="#portprivatesecondaryvlanid" title="PortPrivateSecondaryVlanId">PortPrivateSecondaryVlanId</a>" : <i>Double</i>,
        "<a href="#standbyuplinks" title="StandbyUplinks">StandbyUplinks</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#teamingpolicy" title="TeamingPolicy">TeamingPolicy</a>" : <i>String</i>,
        "<a href="#txuplink" title="TxUplink">TxUplink</a>" : <i>Boolean</i>,
        "<a href="#uplinks" title="Uplinks">Uplinks</a>" : <i>[ String, ... ]</i>,
        "<a href="#vdpmaximummbit" title="VdpMaximumMbit">VdpMaximumMbit</a>" : <i>Double</i>,
        "<a href="#vdpreservationmbit" title="VdpReservationMbit">VdpReservationMbit</a>" : <i>Double</i>,
        "<a href="#vdpsharecount" title="VdpShareCount">VdpShareCount</a>" : <i>Double</i>,
        "<a href="#vdpsharelevel" title="VdpShareLevel">VdpShareLevel</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>,
        "<a href="#virtualmachinemaximummbit" title="VirtualmachineMaximumMbit">VirtualmachineMaximumMbit</a>" : <i>Double</i>,
        "<a href="#virtualmachinereservationmbit" title="VirtualmachineReservationMbit">VirtualmachineReservationMbit</a>" : <i>Double</i>,
        "<a href="#virtualmachinesharecount" title="VirtualmachineShareCount">VirtualmachineShareCount</a>" : <i>Double</i>,
        "<a href="#virtualmachinesharelevel" title="VirtualmachineShareLevel">VirtualmachineShareLevel</a>" : <i>String</i>,
        "<a href="#vlanid" title="VlanId">VlanId</a>" : <i>Double</i>,
        "<a href="#vmotionmaximummbit" title="VmotionMaximumMbit">VmotionMaximumMbit</a>" : <i>Double</i>,
        "<a href="#vmotionreservationmbit" title="VmotionReservationMbit">VmotionReservationMbit</a>" : <i>Double</i>,
        "<a href="#vmotionsharecount" title="VmotionShareCount">VmotionShareCount</a>" : <i>Double</i>,
        "<a href="#vmotionsharelevel" title="VmotionShareLevel">VmotionShareLevel</a>" : <i>String</i>,
        "<a href="#vsanmaximummbit" title="VsanMaximumMbit">VsanMaximumMbit</a>" : <i>Double</i>,
        "<a href="#vsanreservationmbit" title="VsanReservationMbit">VsanReservationMbit</a>" : <i>Double</i>,
        "<a href="#vsansharecount" title="VsanShareCount">VsanShareCount</a>" : <i>Double</i>,
        "<a href="#vsansharelevel" title="VsanShareLevel">VsanShareLevel</a>" : <i>String</i>,
        "<a href="#host" title="Host">Host</a>" : <i>[ <a href="host.md">Host</a>, ... ]</i>,
        "<a href="#vlanrange" title="VlanRange">VlanRange</a>" : <i>[ <a href="vlanrange.md">VlanRange</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VSphere::DistributedVirtualSwitch
Properties:
    <a href="#activeuplinks" title="ActiveUplinks">ActiveUplinks</a>: <i>
      - String</i>
    <a href="#allowforgedtransmits" title="AllowForgedTransmits">AllowForgedTransmits</a>: <i>Boolean</i>
    <a href="#allowmacchanges" title="AllowMacChanges">AllowMacChanges</a>: <i>Boolean</i>
    <a href="#allowpromiscuous" title="AllowPromiscuous">AllowPromiscuous</a>: <i>Boolean</i>
    <a href="#blockallports" title="BlockAllPorts">BlockAllPorts</a>: <i>Boolean</i>
    <a href="#checkbeacon" title="CheckBeacon">CheckBeacon</a>: <i>Boolean</i>
    <a href="#contactdetail" title="ContactDetail">ContactDetail</a>: <i>String</i>
    <a href="#contactname" title="ContactName">ContactName</a>: <i>String</i>
    <a href="#customattributes" title="CustomAttributes">CustomAttributes</a>: <i>
      - <a href="customattributes.md">CustomAttributes</a></i>
    <a href="#datacenterid" title="DatacenterId">DatacenterId</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#directpathgen2allowed" title="DirectpathGen2Allowed">DirectpathGen2Allowed</a>: <i>Boolean</i>
    <a href="#egressshapingaveragebandwidth" title="EgressShapingAverageBandwidth">EgressShapingAverageBandwidth</a>: <i>Double</i>
    <a href="#egressshapingburstsize" title="EgressShapingBurstSize">EgressShapingBurstSize</a>: <i>Double</i>
    <a href="#egressshapingenabled" title="EgressShapingEnabled">EgressShapingEnabled</a>: <i>Boolean</i>
    <a href="#egressshapingpeakbandwidth" title="EgressShapingPeakBandwidth">EgressShapingPeakBandwidth</a>: <i>Double</i>
    <a href="#failback" title="Failback">Failback</a>: <i>Boolean</i>
    <a href="#faulttolerancemaximummbit" title="FaulttoleranceMaximumMbit">FaulttoleranceMaximumMbit</a>: <i>Double</i>
    <a href="#faulttolerancereservationmbit" title="FaulttoleranceReservationMbit">FaulttoleranceReservationMbit</a>: <i>Double</i>
    <a href="#faulttolerancesharecount" title="FaulttoleranceShareCount">FaulttoleranceShareCount</a>: <i>Double</i>
    <a href="#faulttolerancesharelevel" title="FaulttoleranceShareLevel">FaulttoleranceShareLevel</a>: <i>String</i>
    <a href="#folder" title="Folder">Folder</a>: <i>String</i>
    <a href="#hbrmaximummbit" title="HbrMaximumMbit">HbrMaximumMbit</a>: <i>Double</i>
    <a href="#hbrreservationmbit" title="HbrReservationMbit">HbrReservationMbit</a>: <i>Double</i>
    <a href="#hbrsharecount" title="HbrShareCount">HbrShareCount</a>: <i>Double</i>
    <a href="#hbrsharelevel" title="HbrShareLevel">HbrShareLevel</a>: <i>String</i>
    <a href="#ingressshapingaveragebandwidth" title="IngressShapingAverageBandwidth">IngressShapingAverageBandwidth</a>: <i>Double</i>
    <a href="#ingressshapingburstsize" title="IngressShapingBurstSize">IngressShapingBurstSize</a>: <i>Double</i>
    <a href="#ingressshapingenabled" title="IngressShapingEnabled">IngressShapingEnabled</a>: <i>Boolean</i>
    <a href="#ingressshapingpeakbandwidth" title="IngressShapingPeakBandwidth">IngressShapingPeakBandwidth</a>: <i>Double</i>
    <a href="#ipv4address" title="Ipv4Address">Ipv4Address</a>: <i>String</i>
    <a href="#iscsimaximummbit" title="IscsiMaximumMbit">IscsiMaximumMbit</a>: <i>Double</i>
    <a href="#iscsireservationmbit" title="IscsiReservationMbit">IscsiReservationMbit</a>: <i>Double</i>
    <a href="#iscsisharecount" title="IscsiShareCount">IscsiShareCount</a>: <i>Double</i>
    <a href="#iscsisharelevel" title="IscsiShareLevel">IscsiShareLevel</a>: <i>String</i>
    <a href="#lacpapiversion" title="LacpApiVersion">LacpApiVersion</a>: <i>String</i>
    <a href="#lacpenabled" title="LacpEnabled">LacpEnabled</a>: <i>Boolean</i>
    <a href="#lacpmode" title="LacpMode">LacpMode</a>: <i>String</i>
    <a href="#linkdiscoveryoperation" title="LinkDiscoveryOperation">LinkDiscoveryOperation</a>: <i>String</i>
    <a href="#linkdiscoveryprotocol" title="LinkDiscoveryProtocol">LinkDiscoveryProtocol</a>: <i>String</i>
    <a href="#managementmaximummbit" title="ManagementMaximumMbit">ManagementMaximumMbit</a>: <i>Double</i>
    <a href="#managementreservationmbit" title="ManagementReservationMbit">ManagementReservationMbit</a>: <i>Double</i>
    <a href="#managementsharecount" title="ManagementShareCount">ManagementShareCount</a>: <i>Double</i>
    <a href="#managementsharelevel" title="ManagementShareLevel">ManagementShareLevel</a>: <i>String</i>
    <a href="#maxmtu" title="MaxMtu">MaxMtu</a>: <i>Double</i>
    <a href="#multicastfilteringmode" title="MulticastFilteringMode">MulticastFilteringMode</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#netflowactiveflowtimeout" title="NetflowActiveFlowTimeout">NetflowActiveFlowTimeout</a>: <i>Double</i>
    <a href="#netflowcollectoripaddress" title="NetflowCollectorIpAddress">NetflowCollectorIpAddress</a>: <i>String</i>
    <a href="#netflowcollectorport" title="NetflowCollectorPort">NetflowCollectorPort</a>: <i>Double</i>
    <a href="#netflowenabled" title="NetflowEnabled">NetflowEnabled</a>: <i>Boolean</i>
    <a href="#netflowidleflowtimeout" title="NetflowIdleFlowTimeout">NetflowIdleFlowTimeout</a>: <i>Double</i>
    <a href="#netflowinternalflowsonly" title="NetflowInternalFlowsOnly">NetflowInternalFlowsOnly</a>: <i>Boolean</i>
    <a href="#netflowobservationdomainid" title="NetflowObservationDomainId">NetflowObservationDomainId</a>: <i>Double</i>
    <a href="#netflowsamplingrate" title="NetflowSamplingRate">NetflowSamplingRate</a>: <i>Double</i>
    <a href="#networkresourcecontrolenabled" title="NetworkResourceControlEnabled">NetworkResourceControlEnabled</a>: <i>Boolean</i>
    <a href="#networkresourcecontrolversion" title="NetworkResourceControlVersion">NetworkResourceControlVersion</a>: <i>String</i>
    <a href="#nfsmaximummbit" title="NfsMaximumMbit">NfsMaximumMbit</a>: <i>Double</i>
    <a href="#nfsreservationmbit" title="NfsReservationMbit">NfsReservationMbit</a>: <i>Double</i>
    <a href="#nfssharecount" title="NfsShareCount">NfsShareCount</a>: <i>Double</i>
    <a href="#nfssharelevel" title="NfsShareLevel">NfsShareLevel</a>: <i>String</i>
    <a href="#notifyswitches" title="NotifySwitches">NotifySwitches</a>: <i>Boolean</i>
    <a href="#portprivatesecondaryvlanid" title="PortPrivateSecondaryVlanId">PortPrivateSecondaryVlanId</a>: <i>Double</i>
    <a href="#standbyuplinks" title="StandbyUplinks">StandbyUplinks</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#teamingpolicy" title="TeamingPolicy">TeamingPolicy</a>: <i>String</i>
    <a href="#txuplink" title="TxUplink">TxUplink</a>: <i>Boolean</i>
    <a href="#uplinks" title="Uplinks">Uplinks</a>: <i>
      - String</i>
    <a href="#vdpmaximummbit" title="VdpMaximumMbit">VdpMaximumMbit</a>: <i>Double</i>
    <a href="#vdpreservationmbit" title="VdpReservationMbit">VdpReservationMbit</a>: <i>Double</i>
    <a href="#vdpsharecount" title="VdpShareCount">VdpShareCount</a>: <i>Double</i>
    <a href="#vdpsharelevel" title="VdpShareLevel">VdpShareLevel</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
    <a href="#virtualmachinemaximummbit" title="VirtualmachineMaximumMbit">VirtualmachineMaximumMbit</a>: <i>Double</i>
    <a href="#virtualmachinereservationmbit" title="VirtualmachineReservationMbit">VirtualmachineReservationMbit</a>: <i>Double</i>
    <a href="#virtualmachinesharecount" title="VirtualmachineShareCount">VirtualmachineShareCount</a>: <i>Double</i>
    <a href="#virtualmachinesharelevel" title="VirtualmachineShareLevel">VirtualmachineShareLevel</a>: <i>String</i>
    <a href="#vlanid" title="VlanId">VlanId</a>: <i>Double</i>
    <a href="#vmotionmaximummbit" title="VmotionMaximumMbit">VmotionMaximumMbit</a>: <i>Double</i>
    <a href="#vmotionreservationmbit" title="VmotionReservationMbit">VmotionReservationMbit</a>: <i>Double</i>
    <a href="#vmotionsharecount" title="VmotionShareCount">VmotionShareCount</a>: <i>Double</i>
    <a href="#vmotionsharelevel" title="VmotionShareLevel">VmotionShareLevel</a>: <i>String</i>
    <a href="#vsanmaximummbit" title="VsanMaximumMbit">VsanMaximumMbit</a>: <i>Double</i>
    <a href="#vsanreservationmbit" title="VsanReservationMbit">VsanReservationMbit</a>: <i>Double</i>
    <a href="#vsansharecount" title="VsanShareCount">VsanShareCount</a>: <i>Double</i>
    <a href="#vsansharelevel" title="VsanShareLevel">VsanShareLevel</a>: <i>String</i>
    <a href="#host" title="Host">Host</a>: <i>
      - <a href="host.md">Host</a></i>
    <a href="#vlanrange" title="VlanRange">VlanRange</a>: <i>
      - <a href="vlanrange.md">VlanRange</a></i>
</pre>

## Properties

#### ActiveUplinks

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowForgedTransmits

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowMacChanges

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowPromiscuous

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockAllPorts

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckBeacon

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContactDetail

The detailed contact information for the person
who is responsible for the DVS.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContactName

The name of the person who is responsible for the
DVS.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomAttributes

Map of custom attribute ids to attribute
value strings to set for virtual switch. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.

_Required_: No

_Type_: List of <a href="customattributes.md">CustomAttributes</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatacenterId

The ID of the datacenter where the distributed
virtual switch will be created. Forces a new resource if changed.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A detailed description for the DVS.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DirectpathGen2Allowed

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EgressShapingAverageBandwidth

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EgressShapingBurstSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EgressShapingEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EgressShapingPeakBandwidth

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Failback

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FaulttoleranceMaximumMbit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FaulttoleranceReservationMbit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FaulttoleranceShareCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FaulttoleranceShareLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Folder

The folder to create the DVS in. Forces a new resource
if changed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HbrMaximumMbit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HbrReservationMbit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HbrShareCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HbrShareLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IngressShapingAverageBandwidth

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IngressShapingBurstSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IngressShapingEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IngressShapingPeakBandwidth

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4Address

An IPv4 address to identify the switch. This is
mostly useful when used with the [Netflow arguments](#netflow-arguments) found
below.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IscsiMaximumMbit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IscsiReservationMbit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IscsiShareCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IscsiShareLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LacpApiVersion

The Link Aggregation Control Protocol group
version to use with the switch. Possible values are `singleLag` and
`multipleLag`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LacpEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LacpMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinkDiscoveryOperation

Whether to `advertise` or `listen`
for link discovery traffic.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinkDiscoveryProtocol

The discovery protocol type. Valid
types are `cdp` and `lldp`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagementMaximumMbit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagementReservationMbit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagementShareCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagementShareLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxMtu

The maximum transmission unit (MTU) for the virtual
switch.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MulticastFilteringMode

The multicast filtering mode to use
with the switch. Can be one of `legacyFiltering` or `snooping`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the distributed virtual switch.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetflowActiveFlowTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetflowCollectorIpAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetflowCollectorPort

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetflowEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetflowIdleFlowTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetflowInternalFlowsOnly

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetflowObservationDomainId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetflowSamplingRate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkResourceControlEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkResourceControlVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NfsMaximumMbit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NfsReservationMbit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NfsShareCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NfsShareLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifySwitches

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortPrivateSecondaryVlanId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StandbyUplinks

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TeamingPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TxUplink

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uplinks

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VdpMaximumMbit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VdpReservationMbit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VdpShareCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VdpShareLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

- The version of the DVS to create. The default is to
create the DVS at the latest version supported by the version of vSphere
being used. A DVS can be upgraded to another version, but cannot be
downgraded.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualmachineMaximumMbit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualmachineReservationMbit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualmachineShareCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualmachineShareLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmotionMaximumMbit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmotionReservationMbit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmotionShareCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmotionShareLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsanMaximumMbit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsanReservationMbit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsanShareCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsanShareLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Host

_Required_: No

_Type_: List of <a href="host.md">Host</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanRange

_Required_: No

_Type_: List of <a href="vlanrange.md">VlanRange</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ConfigVersion

Returns the <code>ConfigVersion</code> value.

#### Id

Returns the <code>Id</code> value.

