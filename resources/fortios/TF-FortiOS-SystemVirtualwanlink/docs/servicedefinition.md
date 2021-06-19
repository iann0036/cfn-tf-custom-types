# TF::FortiOS::SystemVirtualwanlink ServiceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#addrmode" title="AddrMode">AddrMode</a>" : <i>String</i>,
    "<a href="#bandwidthweight" title="BandwidthWeight">BandwidthWeight</a>" : <i>Double</i>,
    "<a href="#default" title="Default">Default</a>" : <i>String</i>,
    "<a href="#dscpforward" title="DscpForward">DscpForward</a>" : <i>String</i>,
    "<a href="#dscpforwardtag" title="DscpForwardTag">DscpForwardTag</a>" : <i>String</i>,
    "<a href="#dscpreverse" title="DscpReverse">DscpReverse</a>" : <i>String</i>,
    "<a href="#dscpreversetag" title="DscpReverseTag">DscpReverseTag</a>" : <i>String</i>,
    "<a href="#dstnegate" title="DstNegate">DstNegate</a>" : <i>String</i>,
    "<a href="#endport" title="EndPort">EndPort</a>" : <i>Double</i>,
    "<a href="#gateway" title="Gateway">Gateway</a>" : <i>String</i>,
    "<a href="#healthcheck" title="HealthCheck">HealthCheck</a>" : <i>[ <a href="healthcheckdefinition.md">HealthCheckDefinition</a>, ... ]</i>,
    "<a href="#holddowntime" title="HoldDownTime">HoldDownTime</a>" : <i>Double</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#inputdevicenegate" title="InputDeviceNegate">InputDeviceNegate</a>" : <i>String</i>,
    "<a href="#internetservice" title="InternetService">InternetService</a>" : <i>String</i>,
    "<a href="#jitterweight" title="JitterWeight">JitterWeight</a>" : <i>Double</i>,
    "<a href="#latencyweight" title="LatencyWeight">LatencyWeight</a>" : <i>Double</i>,
    "<a href="#linkcostfactor" title="LinkCostFactor">LinkCostFactor</a>" : <i>String</i>,
    "<a href="#linkcostthreshold" title="LinkCostThreshold">LinkCostThreshold</a>" : <i>Double</i>,
    "<a href="#member" title="Member">Member</a>" : <i>Double</i>,
    "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#packetlossweight" title="PacketLossWeight">PacketLossWeight</a>" : <i>Double</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>Double</i>,
    "<a href="#qualitylink" title="QualityLink">QualityLink</a>" : <i>Double</i>,
    "<a href="#role" title="Role">Role</a>" : <i>String</i>,
    "<a href="#routetag" title="RouteTag">RouteTag</a>" : <i>Double</i>,
    "<a href="#slacomparemethod" title="SlaCompareMethod">SlaCompareMethod</a>" : <i>String</i>,
    "<a href="#srcnegate" title="SrcNegate">SrcNegate</a>" : <i>String</i>,
    "<a href="#standaloneaction" title="StandaloneAction">StandaloneAction</a>" : <i>String</i>,
    "<a href="#startport" title="StartPort">StartPort</a>" : <i>Double</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#tos" title="Tos">Tos</a>" : <i>String</i>,
    "<a href="#tosmask" title="TosMask">TosMask</a>" : <i>String</i>,
    "<a href="#dst" title="Dst">Dst</a>" : <i>[ <a href="dstdefinition.md">DstDefinition</a>, ... ]</i>,
    "<a href="#dst6" title="Dst6">Dst6</a>" : <i>[ <a href="dst6definition.md">Dst6Definition</a>, ... ]</i>,
    "<a href="#groups" title="Groups">Groups</a>" : <i>[ <a href="groupsdefinition.md">GroupsDefinition</a>, ... ]</i>,
    "<a href="#inputdevice" title="InputDevice">InputDevice</a>" : <i>[ <a href="inputdevicedefinition.md">InputDeviceDefinition</a>, ... ]</i>,
    "<a href="#internetserviceappctrl" title="InternetServiceAppCtrl">InternetServiceAppCtrl</a>" : <i>[ <a href="internetserviceappctrldefinition.md">InternetServiceAppCtrlDefinition</a>, ... ]</i>,
    "<a href="#internetserviceappctrlgroup" title="InternetServiceAppCtrlGroup">InternetServiceAppCtrlGroup</a>" : <i>[ <a href="internetserviceappctrlgroupdefinition.md">InternetServiceAppCtrlGroupDefinition</a>, ... ]</i>,
    "<a href="#internetservicectrl" title="InternetServiceCtrl">InternetServiceCtrl</a>" : <i>[ <a href="internetservicectrldefinition.md">InternetServiceCtrlDefinition</a>, ... ]</i>,
    "<a href="#internetservicectrlgroup" title="InternetServiceCtrlGroup">InternetServiceCtrlGroup</a>" : <i>[ <a href="internetservicectrlgroupdefinition.md">InternetServiceCtrlGroupDefinition</a>, ... ]</i>,
    "<a href="#internetservicecustom" title="InternetServiceCustom">InternetServiceCustom</a>" : <i>[ <a href="internetservicecustomdefinition.md">InternetServiceCustomDefinition</a>, ... ]</i>,
    "<a href="#internetservicecustomgroup" title="InternetServiceCustomGroup">InternetServiceCustomGroup</a>" : <i>[ <a href="internetservicecustomgroupdefinition.md">InternetServiceCustomGroupDefinition</a>, ... ]</i>,
    "<a href="#internetservicegroup" title="InternetServiceGroup">InternetServiceGroup</a>" : <i>[ <a href="internetservicegroupdefinition.md">InternetServiceGroupDefinition</a>, ... ]</i>,
    "<a href="#internetserviceid" title="InternetServiceId">InternetServiceId</a>" : <i>[ <a href="internetserviceiddefinition.md">InternetServiceIdDefinition</a>, ... ]</i>,
    "<a href="#internetservicename" title="InternetServiceName">InternetServiceName</a>" : <i>[ <a href="internetservicenamedefinition.md">InternetServiceNameDefinition</a>, ... ]</i>,
    "<a href="#prioritymembers" title="PriorityMembers">PriorityMembers</a>" : <i>[ <a href="prioritymembersdefinition.md">PriorityMembersDefinition</a>, ... ]</i>,
    "<a href="#sla" title="Sla">Sla</a>" : <i>[ <a href="sladefinition.md">SlaDefinition</a>, ... ]</i>,
    "<a href="#src" title="Src">Src</a>" : <i>[ <a href="srcdefinition.md">SrcDefinition</a>, ... ]</i>,
    "<a href="#src6" title="Src6">Src6</a>" : <i>[ <a href="src6definition.md">Src6Definition</a>, ... ]</i>,
    "<a href="#users" title="Users">Users</a>" : <i>[ <a href="usersdefinition.md">UsersDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#addrmode" title="AddrMode">AddrMode</a>: <i>String</i>
<a href="#bandwidthweight" title="BandwidthWeight">BandwidthWeight</a>: <i>Double</i>
<a href="#default" title="Default">Default</a>: <i>String</i>
<a href="#dscpforward" title="DscpForward">DscpForward</a>: <i>String</i>
<a href="#dscpforwardtag" title="DscpForwardTag">DscpForwardTag</a>: <i>String</i>
<a href="#dscpreverse" title="DscpReverse">DscpReverse</a>: <i>String</i>
<a href="#dscpreversetag" title="DscpReverseTag">DscpReverseTag</a>: <i>String</i>
<a href="#dstnegate" title="DstNegate">DstNegate</a>: <i>String</i>
<a href="#endport" title="EndPort">EndPort</a>: <i>Double</i>
<a href="#gateway" title="Gateway">Gateway</a>: <i>String</i>
<a href="#healthcheck" title="HealthCheck">HealthCheck</a>: <i>
      - <a href="healthcheckdefinition.md">HealthCheckDefinition</a></i>
<a href="#holddowntime" title="HoldDownTime">HoldDownTime</a>: <i>Double</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#inputdevicenegate" title="InputDeviceNegate">InputDeviceNegate</a>: <i>String</i>
<a href="#internetservice" title="InternetService">InternetService</a>: <i>String</i>
<a href="#jitterweight" title="JitterWeight">JitterWeight</a>: <i>Double</i>
<a href="#latencyweight" title="LatencyWeight">LatencyWeight</a>: <i>Double</i>
<a href="#linkcostfactor" title="LinkCostFactor">LinkCostFactor</a>: <i>String</i>
<a href="#linkcostthreshold" title="LinkCostThreshold">LinkCostThreshold</a>: <i>Double</i>
<a href="#member" title="Member">Member</a>: <i>Double</i>
<a href="#mode" title="Mode">Mode</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#packetlossweight" title="PacketLossWeight">PacketLossWeight</a>: <i>Double</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>Double</i>
<a href="#qualitylink" title="QualityLink">QualityLink</a>: <i>Double</i>
<a href="#role" title="Role">Role</a>: <i>String</i>
<a href="#routetag" title="RouteTag">RouteTag</a>: <i>Double</i>
<a href="#slacomparemethod" title="SlaCompareMethod">SlaCompareMethod</a>: <i>String</i>
<a href="#srcnegate" title="SrcNegate">SrcNegate</a>: <i>String</i>
<a href="#standaloneaction" title="StandaloneAction">StandaloneAction</a>: <i>String</i>
<a href="#startport" title="StartPort">StartPort</a>: <i>Double</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#tos" title="Tos">Tos</a>: <i>String</i>
<a href="#tosmask" title="TosMask">TosMask</a>: <i>String</i>
<a href="#dst" title="Dst">Dst</a>: <i>
      - <a href="dstdefinition.md">DstDefinition</a></i>
<a href="#dst6" title="Dst6">Dst6</a>: <i>
      - <a href="dst6definition.md">Dst6Definition</a></i>
<a href="#groups" title="Groups">Groups</a>: <i>
      - <a href="groupsdefinition.md">GroupsDefinition</a></i>
<a href="#inputdevice" title="InputDevice">InputDevice</a>: <i>
      - <a href="inputdevicedefinition.md">InputDeviceDefinition</a></i>
<a href="#internetserviceappctrl" title="InternetServiceAppCtrl">InternetServiceAppCtrl</a>: <i>
      - <a href="internetserviceappctrldefinition.md">InternetServiceAppCtrlDefinition</a></i>
<a href="#internetserviceappctrlgroup" title="InternetServiceAppCtrlGroup">InternetServiceAppCtrlGroup</a>: <i>
      - <a href="internetserviceappctrlgroupdefinition.md">InternetServiceAppCtrlGroupDefinition</a></i>
<a href="#internetservicectrl" title="InternetServiceCtrl">InternetServiceCtrl</a>: <i>
      - <a href="internetservicectrldefinition.md">InternetServiceCtrlDefinition</a></i>
<a href="#internetservicectrlgroup" title="InternetServiceCtrlGroup">InternetServiceCtrlGroup</a>: <i>
      - <a href="internetservicectrlgroupdefinition.md">InternetServiceCtrlGroupDefinition</a></i>
<a href="#internetservicecustom" title="InternetServiceCustom">InternetServiceCustom</a>: <i>
      - <a href="internetservicecustomdefinition.md">InternetServiceCustomDefinition</a></i>
<a href="#internetservicecustomgroup" title="InternetServiceCustomGroup">InternetServiceCustomGroup</a>: <i>
      - <a href="internetservicecustomgroupdefinition.md">InternetServiceCustomGroupDefinition</a></i>
<a href="#internetservicegroup" title="InternetServiceGroup">InternetServiceGroup</a>: <i>
      - <a href="internetservicegroupdefinition.md">InternetServiceGroupDefinition</a></i>
<a href="#internetserviceid" title="InternetServiceId">InternetServiceId</a>: <i>
      - <a href="internetserviceiddefinition.md">InternetServiceIdDefinition</a></i>
<a href="#internetservicename" title="InternetServiceName">InternetServiceName</a>: <i>
      - <a href="internetservicenamedefinition.md">InternetServiceNameDefinition</a></i>
<a href="#prioritymembers" title="PriorityMembers">PriorityMembers</a>: <i>
      - <a href="prioritymembersdefinition.md">PriorityMembersDefinition</a></i>
<a href="#sla" title="Sla">Sla</a>: <i>
      - <a href="sladefinition.md">SlaDefinition</a></i>
<a href="#src" title="Src">Src</a>: <i>
      - <a href="srcdefinition.md">SrcDefinition</a></i>
<a href="#src6" title="Src6">Src6</a>: <i>
      - <a href="src6definition.md">Src6Definition</a></i>
<a href="#users" title="Users">Users</a>: <i>
      - <a href="usersdefinition.md">UsersDefinition</a></i>
</pre>

## Properties

#### AddrMode

Address mode (IPv4 or IPv6). Valid values: `ipv4`, `ipv6`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BandwidthWeight

Coefficient of reciprocal of available bidirectional bandwidth in the formula of custom-profile-1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Default

Enable/disable use of SD-WAN as default service. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DscpForward

Enable/disable forward traffic DSCP tag. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DscpForwardTag

Forward traffic DSCP tag.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DscpReverse

Enable/disable reverse traffic DSCP tag. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DscpReverseTag

Reverse traffic DSCP tag.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DstNegate

Enable/disable negation of destination address match. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndPort

End destination port number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gateway

Enable/disable SD-WAN service gateway. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheck

_Required_: No

_Type_: List of <a href="healthcheckdefinition.md">HealthCheckDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HoldDownTime

Waiting period in seconds when switching from the back-up member to the primary member (0 - 10000000, default = 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

Priority rule ID (1 - 4000).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InputDeviceNegate

Enable/disable negation of input device match. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetService

Enable/disable use of Internet service for application-based load balancing. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JitterWeight

Coefficient of jitter in the formula of custom-profile-1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LatencyWeight

Coefficient of latency in the formula of custom-profile-1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinkCostFactor

Link cost factor. Valid values: `latency`, `jitter`, `packet-loss`, `inbandwidth`, `outbandwidth`, `bibandwidth`, `custom-profile-1`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinkCostThreshold

Percentage threshold change of link cost values that will result in policy route regeneration (0 - 10000000, default = 10).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Member

Member sequence number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

Control how the priority rule sets the priority of interfaces in the SD-WAN. Valid values: `auto`, `manual`, `priority`, `sla`, `load-balance`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Priority rule name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PacketLossWeight

Coefficient of packet-loss in the formula of custom-profile-1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Protocol number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QualityLink

Quality grade.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

Service role to work with neighbor. Valid values: `standalone`, `primary`, `secondary`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteTag

IPv4 route map route-tag.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlaCompareMethod

Method to compare SLA value for sla and load balance mode.  Valid values: `order`, `number`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcNegate

Enable/disable negation of source address match. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StandaloneAction

Enable/disable service when selected neighbor role is standalone while service role is not standalone. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartPort

Start destination port number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable SD-WAN service. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tos

Type of service bit pattern.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TosMask

Type of service evaluated bits.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dst

_Required_: No

_Type_: List of <a href="dstdefinition.md">DstDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dst6

_Required_: No

_Type_: List of <a href="dst6definition.md">Dst6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Groups

_Required_: No

_Type_: List of <a href="groupsdefinition.md">GroupsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InputDevice

_Required_: No

_Type_: List of <a href="inputdevicedefinition.md">InputDeviceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceAppCtrl

_Required_: No

_Type_: List of <a href="internetserviceappctrldefinition.md">InternetServiceAppCtrlDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceAppCtrlGroup

_Required_: No

_Type_: List of <a href="internetserviceappctrlgroupdefinition.md">InternetServiceAppCtrlGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceCtrl

_Required_: No

_Type_: List of <a href="internetservicectrldefinition.md">InternetServiceCtrlDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceCtrlGroup

_Required_: No

_Type_: List of <a href="internetservicectrlgroupdefinition.md">InternetServiceCtrlGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceCustom

_Required_: No

_Type_: List of <a href="internetservicecustomdefinition.md">InternetServiceCustomDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceCustomGroup

_Required_: No

_Type_: List of <a href="internetservicecustomgroupdefinition.md">InternetServiceCustomGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceGroup

_Required_: No

_Type_: List of <a href="internetservicegroupdefinition.md">InternetServiceGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceId

_Required_: No

_Type_: List of <a href="internetserviceiddefinition.md">InternetServiceIdDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceName

_Required_: No

_Type_: List of <a href="internetservicenamedefinition.md">InternetServiceNameDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PriorityMembers

_Required_: No

_Type_: List of <a href="prioritymembersdefinition.md">PriorityMembersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sla

_Required_: No

_Type_: List of <a href="sladefinition.md">SlaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Src

_Required_: No

_Type_: List of <a href="srcdefinition.md">SrcDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Src6

_Required_: No

_Type_: List of <a href="src6definition.md">Src6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Users

_Required_: No

_Type_: List of <a href="usersdefinition.md">UsersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

