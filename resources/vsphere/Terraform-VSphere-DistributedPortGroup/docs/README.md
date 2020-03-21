# Terraform::VSphere::DistributedPortGroup

CloudFormation equivalent of vsphere_distributed_port_group

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VSphere::DistributedPortGroup",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#activeuplinks" title="ActiveUplinks">ActiveUplinks</a>" : <i>[ String, ... ]</i>,
        "<a href="#allowforgedtransmits" title="AllowForgedTransmits">AllowForgedTransmits</a>" : <i>Boolean</i>,
        "<a href="#allowmacchanges" title="AllowMacChanges">AllowMacChanges</a>" : <i>Boolean</i>,
        "<a href="#allowpromiscuous" title="AllowPromiscuous">AllowPromiscuous</a>" : <i>Boolean</i>,
        "<a href="#autoexpand" title="AutoExpand">AutoExpand</a>" : <i>Boolean</i>,
        "<a href="#blockallports" title="BlockAllPorts">BlockAllPorts</a>" : <i>Boolean</i>,
        "<a href="#blockoverrideallowed" title="BlockOverrideAllowed">BlockOverrideAllowed</a>" : <i>Boolean</i>,
        "<a href="#checkbeacon" title="CheckBeacon">CheckBeacon</a>" : <i>Boolean</i>,
        "<a href="#configversion" title="ConfigVersion">ConfigVersion</a>" : <i>String</i>,
        "<a href="#customattributes" title="CustomAttributes">CustomAttributes</a>" : <i>[ &lt;a href=&#34;customattributes.md&#34;&gt;CustomAttributes&lt;/a&gt;, ... ]</i>,
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
        "<a href="#key" title="Key">Key</a>" : <i>String</i>,
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
        "<a href="#vlanrange" title="VlanRange">VlanRange</a>" : <i>[ &lt;a href=&#34;vlanrange.md&#34;&gt;VlanRange&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VSphere::DistributedPortGroup
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#activeuplinks" title="ActiveUplinks">ActiveUplinks</a>: <i>
      - String</i>
    <a href="#allowforgedtransmits" title="AllowForgedTransmits">AllowForgedTransmits</a>: <i>Boolean</i>
    <a href="#allowmacchanges" title="AllowMacChanges">AllowMacChanges</a>: <i>Boolean</i>
    <a href="#allowpromiscuous" title="AllowPromiscuous">AllowPromiscuous</a>: <i>Boolean</i>
    <a href="#autoexpand" title="AutoExpand">AutoExpand</a>: <i>Boolean</i>
    <a href="#blockallports" title="BlockAllPorts">BlockAllPorts</a>: <i>Boolean</i>
    <a href="#blockoverrideallowed" title="BlockOverrideAllowed">BlockOverrideAllowed</a>: <i>Boolean</i>
    <a href="#checkbeacon" title="CheckBeacon">CheckBeacon</a>: <i>Boolean</i>
    <a href="#configversion" title="ConfigVersion">ConfigVersion</a>: <i>String</i>
    <a href="#customattributes" title="CustomAttributes">CustomAttributes</a>: <i>
      - &lt;a href=&#34;customattributes.md&#34;&gt;CustomAttributes&lt;/a&gt;</i>
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
    <a href="#key" title="Key">Key</a>: <i>String</i>
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
      - &lt;a href=&#34;vlanrange.md&#34;&gt;VlanRange&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

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

#### ConfigVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomAttributes

_Required_: No

_Type_: List of &lt;a href=&#34;customattributes.md&#34;&gt;CustomAttributes&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DirectpathGen2Allowed

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DistributedVirtualSwitchUuid

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

#### Key

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

#### LivePortMovingAllowed

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

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

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortConfigResetAtDisconnect

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortNameFormat

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

_Type_: List of &lt;a href=&#34;vlanrange.md&#34;&gt;VlanRange&lt;/a&gt;

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

Returns the &lt;code&gt;ConfigVersion&lt;/code&gt; value.

#### Key

Returns the &lt;code&gt;Key&lt;/code&gt; value.

