# Terraform::VSphere::DistributedPortGroup

The `vsphere_distributed_port_group` resource can be used to manage vSphere
distributed virtual port groups. These port groups are connected to distributed
virtual switches, which can be managed by the
[`vsphere_distributed_virtual_switch`][distributed-virtual-switch] resource.

Distributed port groups can be used as networks for virtual machines, allowing
VMs to use the networking supplied by a distributed virtual switch (DVS), with
a set of policies that apply to that individual newtork, if desired.

For an overview on vSphere networking concepts, see [this
page][ref-vsphere-net-concepts]. For more information on vSphere DVS
portgroups, see [this page][ref-vsphere-dvportgroup].

[distributed-virtual-switch]: /docs/providers/vsphere/r/distributed_virtual_switch.html
[ref-vsphere-net-concepts]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.networking.doc/GUID-2B11DBB8-CB3C-4AFF-8885-EFEA0FC562F4.html
[ref-vsphere-dvportgroup]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.networking.doc/GUID-69933F6E-2442-46CF-AA17-1196CB9A0A09.html

~> **NOTE:** This resource requires vCenter and is not available on direct ESXi
connections.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VSphere::DistributedPortGroup",
    "Properties" : {
        "<a href="#activeuplinks" title="ActiveUplinks">ActiveUplinks</a>" : <i>[ String, ... ]</i>,
        "<a href="#allowforgedtransmits" title="AllowForgedTransmits">AllowForgedTransmits</a>" : <i>Boolean</i>,
        "<a href="#allowmacchanges" title="AllowMacChanges">AllowMacChanges</a>" : <i>Boolean</i>,
        "<a href="#allowpromiscuous" title="AllowPromiscuous">AllowPromiscuous</a>" : <i>Boolean</i>,
        "<a href="#autoexpand" title="AutoExpand">AutoExpand</a>" : <i>Boolean</i>,
        "<a href="#blockallports" title="BlockAllPorts">BlockAllPorts</a>" : <i>Boolean</i>,
        "<a href="#blockoverrideallowed" title="BlockOverrideAllowed">BlockOverrideAllowed</a>" : <i>Boolean</i>,
        "<a href="#checkbeacon" title="CheckBeacon">CheckBeacon</a>" : <i>Boolean</i>,
        "<a href="#customattributes" title="CustomAttributes">CustomAttributes</a>" : <i>[ <a href="customattributes.md">CustomAttributes</a>, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#directpathgen2allowed" title="DirectpathGen2Allowed">DirectpathGen2Allowed</a>" : <i>Boolean</i>,
        "<a href="#distributedvirtualswitchuuid" title="DistributedVirtualSwitchUuid">DistributedVirtualSwitchUuid</a>" : <i>String</i>,
        "<a href="#egressshapingaveragebandwidth" title="EgressShapingAverageBandwidth">EgressShapingAverageBandwidth</a>" : <i>Double</i>,
        "<a href="#egressshapingburstsize" title="EgressShapingBurstSize">EgressShapingBurstSize</a>" : <i>Double</i>,
        "<a href="#egressshapingenabled" title="EgressShapingEnabled">EgressShapingEnabled</a>" : <i>Boolean</i>,
        "<a href="#egressshapingpeakbandwidth" title="EgressShapingPeakBandwidth">EgressShapingPeakBandwidth</a>" : <i>Double</i>,
        "<a href="#failback" title="Failback">Failback</a>" : <i>Boolean</i>,
        "<a href="#ingressshapingaveragebandwidth" title="IngressShapingAverageBandwidth">IngressShapingAverageBandwidth</a>" : <i>Double</i>,
        "<a href="#ingressshapingburstsize" title="IngressShapingBurstSize">IngressShapingBurstSize</a>" : <i>Double</i>,
        "<a href="#ingressshapingenabled" title="IngressShapingEnabled">IngressShapingEnabled</a>" : <i>Boolean</i>,
        "<a href="#ingressshapingpeakbandwidth" title="IngressShapingPeakBandwidth">IngressShapingPeakBandwidth</a>" : <i>Double</i>,
        "<a href="#lacpenabled" title="LacpEnabled">LacpEnabled</a>" : <i>Boolean</i>,
        "<a href="#lacpmode" title="LacpMode">LacpMode</a>" : <i>String</i>,
        "<a href="#liveportmovingallowed" title="LivePortMovingAllowed">LivePortMovingAllowed</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#netflowenabled" title="NetflowEnabled">NetflowEnabled</a>" : <i>Boolean</i>,
        "<a href="#netflowoverrideallowed" title="NetflowOverrideAllowed">NetflowOverrideAllowed</a>" : <i>Boolean</i>,
        "<a href="#networkresourcepoolkey" title="NetworkResourcePoolKey">NetworkResourcePoolKey</a>" : <i>String</i>,
        "<a href="#networkresourcepooloverrideallowed" title="NetworkResourcePoolOverrideAllowed">NetworkResourcePoolOverrideAllowed</a>" : <i>Boolean</i>,
        "<a href="#notifyswitches" title="NotifySwitches">NotifySwitches</a>" : <i>Boolean</i>,
        "<a href="#numberofports" title="NumberOfPorts">NumberOfPorts</a>" : <i>Double</i>,
        "<a href="#portconfigresetatdisconnect" title="PortConfigResetAtDisconnect">PortConfigResetAtDisconnect</a>" : <i>Boolean</i>,
        "<a href="#portnameformat" title="PortNameFormat">PortNameFormat</a>" : <i>String</i>,
        "<a href="#portprivatesecondaryvlanid" title="PortPrivateSecondaryVlanId">PortPrivateSecondaryVlanId</a>" : <i>Double</i>,
        "<a href="#securitypolicyoverrideallowed" title="SecurityPolicyOverrideAllowed">SecurityPolicyOverrideAllowed</a>" : <i>Boolean</i>,
        "<a href="#shapingoverrideallowed" title="ShapingOverrideAllowed">ShapingOverrideAllowed</a>" : <i>Boolean</i>,
        "<a href="#standbyuplinks" title="StandbyUplinks">StandbyUplinks</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#teamingpolicy" title="TeamingPolicy">TeamingPolicy</a>" : <i>String</i>,
        "<a href="#trafficfilteroverrideallowed" title="TrafficFilterOverrideAllowed">TrafficFilterOverrideAllowed</a>" : <i>Boolean</i>,
        "<a href="#txuplink" title="TxUplink">TxUplink</a>" : <i>Boolean</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#uplinkteamingoverrideallowed" title="UplinkTeamingOverrideAllowed">UplinkTeamingOverrideAllowed</a>" : <i>Boolean</i>,
        "<a href="#vlanid" title="VlanId">VlanId</a>" : <i>Double</i>,
        "<a href="#vlanoverrideallowed" title="VlanOverrideAllowed">VlanOverrideAllowed</a>" : <i>Boolean</i>,
        "<a href="#vlanrange" title="VlanRange">VlanRange</a>" : <i>[ <a href="vlanrange.md">VlanRange</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VSphere::DistributedPortGroup
Properties:
    <a href="#activeuplinks" title="ActiveUplinks">ActiveUplinks</a>: <i>
      - String</i>
    <a href="#allowforgedtransmits" title="AllowForgedTransmits">AllowForgedTransmits</a>: <i>Boolean</i>
    <a href="#allowmacchanges" title="AllowMacChanges">AllowMacChanges</a>: <i>Boolean</i>
    <a href="#allowpromiscuous" title="AllowPromiscuous">AllowPromiscuous</a>: <i>Boolean</i>
    <a href="#autoexpand" title="AutoExpand">AutoExpand</a>: <i>Boolean</i>
    <a href="#blockallports" title="BlockAllPorts">BlockAllPorts</a>: <i>Boolean</i>
    <a href="#blockoverrideallowed" title="BlockOverrideAllowed">BlockOverrideAllowed</a>: <i>Boolean</i>
    <a href="#checkbeacon" title="CheckBeacon">CheckBeacon</a>: <i>Boolean</i>
    <a href="#customattributes" title="CustomAttributes">CustomAttributes</a>: <i>
      - <a href="customattributes.md">CustomAttributes</a></i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#directpathgen2allowed" title="DirectpathGen2Allowed">DirectpathGen2Allowed</a>: <i>Boolean</i>
    <a href="#distributedvirtualswitchuuid" title="DistributedVirtualSwitchUuid">DistributedVirtualSwitchUuid</a>: <i>String</i>
    <a href="#egressshapingaveragebandwidth" title="EgressShapingAverageBandwidth">EgressShapingAverageBandwidth</a>: <i>Double</i>
    <a href="#egressshapingburstsize" title="EgressShapingBurstSize">EgressShapingBurstSize</a>: <i>Double</i>
    <a href="#egressshapingenabled" title="EgressShapingEnabled">EgressShapingEnabled</a>: <i>Boolean</i>
    <a href="#egressshapingpeakbandwidth" title="EgressShapingPeakBandwidth">EgressShapingPeakBandwidth</a>: <i>Double</i>
    <a href="#failback" title="Failback">Failback</a>: <i>Boolean</i>
    <a href="#ingressshapingaveragebandwidth" title="IngressShapingAverageBandwidth">IngressShapingAverageBandwidth</a>: <i>Double</i>
    <a href="#ingressshapingburstsize" title="IngressShapingBurstSize">IngressShapingBurstSize</a>: <i>Double</i>
    <a href="#ingressshapingenabled" title="IngressShapingEnabled">IngressShapingEnabled</a>: <i>Boolean</i>
    <a href="#ingressshapingpeakbandwidth" title="IngressShapingPeakBandwidth">IngressShapingPeakBandwidth</a>: <i>Double</i>
    <a href="#lacpenabled" title="LacpEnabled">LacpEnabled</a>: <i>Boolean</i>
    <a href="#lacpmode" title="LacpMode">LacpMode</a>: <i>String</i>
    <a href="#liveportmovingallowed" title="LivePortMovingAllowed">LivePortMovingAllowed</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#netflowenabled" title="NetflowEnabled">NetflowEnabled</a>: <i>Boolean</i>
    <a href="#netflowoverrideallowed" title="NetflowOverrideAllowed">NetflowOverrideAllowed</a>: <i>Boolean</i>
    <a href="#networkresourcepoolkey" title="NetworkResourcePoolKey">NetworkResourcePoolKey</a>: <i>String</i>
    <a href="#networkresourcepooloverrideallowed" title="NetworkResourcePoolOverrideAllowed">NetworkResourcePoolOverrideAllowed</a>: <i>Boolean</i>
    <a href="#notifyswitches" title="NotifySwitches">NotifySwitches</a>: <i>Boolean</i>
    <a href="#numberofports" title="NumberOfPorts">NumberOfPorts</a>: <i>Double</i>
    <a href="#portconfigresetatdisconnect" title="PortConfigResetAtDisconnect">PortConfigResetAtDisconnect</a>: <i>Boolean</i>
    <a href="#portnameformat" title="PortNameFormat">PortNameFormat</a>: <i>String</i>
    <a href="#portprivatesecondaryvlanid" title="PortPrivateSecondaryVlanId">PortPrivateSecondaryVlanId</a>: <i>Double</i>
    <a href="#securitypolicyoverrideallowed" title="SecurityPolicyOverrideAllowed">SecurityPolicyOverrideAllowed</a>: <i>Boolean</i>
    <a href="#shapingoverrideallowed" title="ShapingOverrideAllowed">ShapingOverrideAllowed</a>: <i>Boolean</i>
    <a href="#standbyuplinks" title="StandbyUplinks">StandbyUplinks</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#teamingpolicy" title="TeamingPolicy">TeamingPolicy</a>: <i>String</i>
    <a href="#trafficfilteroverrideallowed" title="TrafficFilterOverrideAllowed">TrafficFilterOverrideAllowed</a>: <i>Boolean</i>
    <a href="#txuplink" title="TxUplink">TxUplink</a>: <i>Boolean</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#uplinkteamingoverrideallowed" title="UplinkTeamingOverrideAllowed">UplinkTeamingOverrideAllowed</a>: <i>Boolean</i>
    <a href="#vlanid" title="VlanId">VlanId</a>: <i>Double</i>
    <a href="#vlanoverrideallowed" title="VlanOverrideAllowed">VlanOverrideAllowed</a>: <i>Boolean</i>
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

#### AutoExpand

Allows the port group to create additional ports
past the limit specified in `number_of_ports` if necessary. Default: `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockAllPorts

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockOverrideAllowed

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckBeacon

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomAttributes

_Required_: No

_Type_: List of <a href="customattributes.md">CustomAttributes</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

An optional description for the port group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DirectpathGen2Allowed

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DistributedVirtualSwitchUuid

The ID of the DVS to add the
port group to. Forces a new resource if changed.

_Required_: Yes

_Type_: String

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

#### LacpEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LacpMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LivePortMovingAllowed

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the port group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetflowEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetflowOverrideAllowed

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkResourcePoolKey

The key of a network resource pool
to associate with this port group. The default is `-1`, which implies no
association.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkResourcePoolOverrideAllowed

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifySwitches

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumberOfPorts

The number of ports available on this port
group. Cannot be decreased below the amount of used ports on the port group.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortConfigResetAtDisconnect

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortNameFormat

An optional formatting policy for naming of
the ports in this port group. See the `portNameFormat` attribute listed
[here][ext-vsphere-portname-format] for details on the format syntax.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortPrivateSecondaryVlanId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityPolicyOverrideAllowed

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShapingOverrideAllowed

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StandbyUplinks

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TeamingPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficFilterOverrideAllowed

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TxUplink

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The port group type. Can be one of `earlyBinding` (static
binding) or `ephemeral`. Default: `earlyBinding`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UplinkTeamingOverrideAllowed

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanOverrideAllowed

_Required_: No

_Type_: Boolean

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

#### Key

Returns the <code>Key</code> value.

