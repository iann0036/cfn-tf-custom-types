# TF::VSphere::HostPortGroup

The `vsphere_host_port_group` resource can be used to manage vSphere standard
port groups on an ESXi host. These port groups are connected to standard
virtual switches, which can be managed by the
[`vsphere_host_virtual_switch`][host-virtual-switch] resource.

For an overview on vSphere networking concepts, see [this page][ref-vsphere-net-concepts].

[host-virtual-switch]: /docs/providers/vsphere/r/host_virtual_switch.html
[ref-vsphere-net-concepts]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.networking.doc/GUID-2B11DBB8-CB3C-4AFF-8885-EFEA0FC562F4.html

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::VSphere::HostPortGroup",
    "Properties" : {
        "<a href="#activenics" title="ActiveNics">ActiveNics</a>" : <i>[ String, ... ]</i>,
        "<a href="#allowforgedtransmits" title="AllowForgedTransmits">AllowForgedTransmits</a>" : <i>Boolean</i>,
        "<a href="#allowmacchanges" title="AllowMacChanges">AllowMacChanges</a>" : <i>Boolean</i>,
        "<a href="#allowpromiscuous" title="AllowPromiscuous">AllowPromiscuous</a>" : <i>Boolean</i>,
        "<a href="#checkbeacon" title="CheckBeacon">CheckBeacon</a>" : <i>Boolean</i>,
        "<a href="#failback" title="Failback">Failback</a>" : <i>Boolean</i>,
        "<a href="#hostsystemid" title="HostSystemId">HostSystemId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#notifyswitches" title="NotifySwitches">NotifySwitches</a>" : <i>Boolean</i>,
        "<a href="#shapingaveragebandwidth" title="ShapingAverageBandwidth">ShapingAverageBandwidth</a>" : <i>Double</i>,
        "<a href="#shapingburstsize" title="ShapingBurstSize">ShapingBurstSize</a>" : <i>Double</i>,
        "<a href="#shapingenabled" title="ShapingEnabled">ShapingEnabled</a>" : <i>Boolean</i>,
        "<a href="#shapingpeakbandwidth" title="ShapingPeakBandwidth">ShapingPeakBandwidth</a>" : <i>Double</i>,
        "<a href="#standbynics" title="StandbyNics">StandbyNics</a>" : <i>[ String, ... ]</i>,
        "<a href="#teamingpolicy" title="TeamingPolicy">TeamingPolicy</a>" : <i>String</i>,
        "<a href="#virtualswitchname" title="VirtualSwitchName">VirtualSwitchName</a>" : <i>String</i>,
        "<a href="#vlanid" title="VlanId">VlanId</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::VSphere::HostPortGroup
Properties:
    <a href="#activenics" title="ActiveNics">ActiveNics</a>: <i>
      - String</i>
    <a href="#allowforgedtransmits" title="AllowForgedTransmits">AllowForgedTransmits</a>: <i>Boolean</i>
    <a href="#allowmacchanges" title="AllowMacChanges">AllowMacChanges</a>: <i>Boolean</i>
    <a href="#allowpromiscuous" title="AllowPromiscuous">AllowPromiscuous</a>: <i>Boolean</i>
    <a href="#checkbeacon" title="CheckBeacon">CheckBeacon</a>: <i>Boolean</i>
    <a href="#failback" title="Failback">Failback</a>: <i>Boolean</i>
    <a href="#hostsystemid" title="HostSystemId">HostSystemId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#notifyswitches" title="NotifySwitches">NotifySwitches</a>: <i>Boolean</i>
    <a href="#shapingaveragebandwidth" title="ShapingAverageBandwidth">ShapingAverageBandwidth</a>: <i>Double</i>
    <a href="#shapingburstsize" title="ShapingBurstSize">ShapingBurstSize</a>: <i>Double</i>
    <a href="#shapingenabled" title="ShapingEnabled">ShapingEnabled</a>: <i>Boolean</i>
    <a href="#shapingpeakbandwidth" title="ShapingPeakBandwidth">ShapingPeakBandwidth</a>: <i>Double</i>
    <a href="#standbynics" title="StandbyNics">StandbyNics</a>: <i>
      - String</i>
    <a href="#teamingpolicy" title="TeamingPolicy">TeamingPolicy</a>: <i>String</i>
    <a href="#virtualswitchname" title="VirtualSwitchName">VirtualSwitchName</a>: <i>String</i>
    <a href="#vlanid" title="VlanId">VlanId</a>: <i>Double</i>
</pre>

## Properties

#### ActiveNics

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

#### CheckBeacon

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Failback

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostSystemId

The [managed object ID][docs-about-morefs] of
the host to set the port group up on. Forces a new resource if changed.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the port group.  Forces a new resource if
changed.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifySwitches

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShapingAverageBandwidth

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShapingBurstSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShapingEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShapingPeakBandwidth

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StandbyNics

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TeamingPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualSwitchName

The name of the virtual switch to bind
this port group to. Forces a new resource if changed.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanId

The VLAN ID/trunk mode for this port group.  An ID of
`0` denotes no tagging, an ID of `1`-`4094` tags with the specific ID, and an
ID of `4095` enables trunk mode, allowing the guest to manage its own
tagging. Default: `0`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ComputedPolicy

Returns the <code>ComputedPolicy</code> value.

#### Id

Returns the <code>Id</code> value.

#### Key

Returns the <code>Key</code> value.

#### Ports

Returns the <code>Ports</code> value.

