# TF::FortiOS::RouterMulticast InterfaceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bfd" title="Bfd">Bfd</a>" : <i>String</i>,
    "<a href="#ciscoexcludegenid" title="CiscoExcludeGenid">CiscoExcludeGenid</a>" : <i>String</i>,
    "<a href="#drpriority" title="DrPriority">DrPriority</a>" : <i>Double</i>,
    "<a href="#helloholdtime" title="HelloHoldtime">HelloHoldtime</a>" : <i>Double</i>,
    "<a href="#hellointerval" title="HelloInterval">HelloInterval</a>" : <i>Double</i>,
    "<a href="#multicastflow" title="MulticastFlow">MulticastFlow</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#neighbourfilter" title="NeighbourFilter">NeighbourFilter</a>" : <i>String</i>,
    "<a href="#passive" title="Passive">Passive</a>" : <i>String</i>,
    "<a href="#pimmode" title="PimMode">PimMode</a>" : <i>String</i>,
    "<a href="#propagationdelay" title="PropagationDelay">PropagationDelay</a>" : <i>Double</i>,
    "<a href="#rpcandidate" title="RpCandidate">RpCandidate</a>" : <i>String</i>,
    "<a href="#rpcandidategroup" title="RpCandidateGroup">RpCandidateGroup</a>" : <i>String</i>,
    "<a href="#rpcandidateinterval" title="RpCandidateInterval">RpCandidateInterval</a>" : <i>Double</i>,
    "<a href="#rpcandidatepriority" title="RpCandidatePriority">RpCandidatePriority</a>" : <i>Double</i>,
    "<a href="#rpfnbrfailback" title="RpfNbrFailBack">RpfNbrFailBack</a>" : <i>String</i>,
    "<a href="#rpfnbrfailbackfilter" title="RpfNbrFailBackFilter">RpfNbrFailBackFilter</a>" : <i>String</i>,
    "<a href="#staterefreshinterval" title="StateRefreshInterval">StateRefreshInterval</a>" : <i>Double</i>,
    "<a href="#staticgroup" title="StaticGroup">StaticGroup</a>" : <i>String</i>,
    "<a href="#ttlthreshold" title="TtlThreshold">TtlThreshold</a>" : <i>Double</i>,
    "<a href="#igmp" title="Igmp">Igmp</a>" : <i>[ <a href="igmpdefinition.md">IgmpDefinition</a>, ... ]</i>,
    "<a href="#joingroup" title="JoinGroup">JoinGroup</a>" : <i>[ <a href="joingroupdefinition.md">JoinGroupDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#bfd" title="Bfd">Bfd</a>: <i>String</i>
<a href="#ciscoexcludegenid" title="CiscoExcludeGenid">CiscoExcludeGenid</a>: <i>String</i>
<a href="#drpriority" title="DrPriority">DrPriority</a>: <i>Double</i>
<a href="#helloholdtime" title="HelloHoldtime">HelloHoldtime</a>: <i>Double</i>
<a href="#hellointerval" title="HelloInterval">HelloInterval</a>: <i>Double</i>
<a href="#multicastflow" title="MulticastFlow">MulticastFlow</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#neighbourfilter" title="NeighbourFilter">NeighbourFilter</a>: <i>String</i>
<a href="#passive" title="Passive">Passive</a>: <i>String</i>
<a href="#pimmode" title="PimMode">PimMode</a>: <i>String</i>
<a href="#propagationdelay" title="PropagationDelay">PropagationDelay</a>: <i>Double</i>
<a href="#rpcandidate" title="RpCandidate">RpCandidate</a>: <i>String</i>
<a href="#rpcandidategroup" title="RpCandidateGroup">RpCandidateGroup</a>: <i>String</i>
<a href="#rpcandidateinterval" title="RpCandidateInterval">RpCandidateInterval</a>: <i>Double</i>
<a href="#rpcandidatepriority" title="RpCandidatePriority">RpCandidatePriority</a>: <i>Double</i>
<a href="#rpfnbrfailback" title="RpfNbrFailBack">RpfNbrFailBack</a>: <i>String</i>
<a href="#rpfnbrfailbackfilter" title="RpfNbrFailBackFilter">RpfNbrFailBackFilter</a>: <i>String</i>
<a href="#staterefreshinterval" title="StateRefreshInterval">StateRefreshInterval</a>: <i>Double</i>
<a href="#staticgroup" title="StaticGroup">StaticGroup</a>: <i>String</i>
<a href="#ttlthreshold" title="TtlThreshold">TtlThreshold</a>: <i>Double</i>
<a href="#igmp" title="Igmp">Igmp</a>: <i>
      - <a href="igmpdefinition.md">IgmpDefinition</a></i>
<a href="#joingroup" title="JoinGroup">JoinGroup</a>: <i>
      - <a href="joingroupdefinition.md">JoinGroupDefinition</a></i>
</pre>

## Properties

#### Bfd

Enable/disable Protocol Independent Multicast (PIM) Bidirectional Forwarding Detection (BFD). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CiscoExcludeGenid

Exclude GenID from hello packets (compatibility with old Cisco IOS). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DrPriority

DR election priority.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HelloHoldtime

Time before old neighbor information expires (0 - 65535 sec, default = 105).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HelloInterval

Interval between sending PIM hello messages (0 - 65535 sec, default = 30).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MulticastFlow

Acceptable source for multicast group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Interface name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NeighbourFilter

Routers acknowledged as neighbor routers.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Passive

Enable/disable listening to IGMP but not participating in PIM. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PimMode

PIM operation mode. Valid values: `sparse-mode`, `dense-mode`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PropagationDelay

Delay flooding packets on this interface (100 - 5000 msec, default = 500).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RpCandidate

Enable/disable compete to become RP in elections. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RpCandidateGroup

Multicast groups managed by this RP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RpCandidateInterval

RP candidate advertisement interval (1 - 16383 sec, default = 60).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RpCandidatePriority

Router's priority as RP.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RpfNbrFailBack

Enable/disable fail back for RPF neighbor query. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RpfNbrFailBackFilter

Filter for fail back RPF neighbors.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StateRefreshInterval

Interval between sending state-refresh packets (1 - 100 sec, default = 60).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticGroup

Statically set multicast groups to forward out.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TtlThreshold

Minimum TTL of multicast packets that will be forwarded (applied only to new multicast routes) (1 - 255, default = 1).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Igmp

_Required_: No

_Type_: List of <a href="igmpdefinition.md">IgmpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JoinGroup

_Required_: No

_Type_: List of <a href="joingroupdefinition.md">JoinGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

