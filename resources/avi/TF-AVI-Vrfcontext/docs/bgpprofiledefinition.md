# TF::AVI::Vrfcontext BgpProfileDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#community" title="Community">Community</a>" : <i>[ String, ... ]</i>,
    "<a href="#holdtime" title="HoldTime">HoldTime</a>" : <i>Double</i>,
    "<a href="#ibgp" title="Ibgp">Ibgp</a>" : <i>Boolean</i>,
    "<a href="#keepaliveinterval" title="KeepaliveInterval">KeepaliveInterval</a>" : <i>Double</i>,
    "<a href="#localas" title="LocalAs">LocalAs</a>" : <i>Double</i>,
    "<a href="#localpreference" title="LocalPreference">LocalPreference</a>" : <i>Double</i>,
    "<a href="#numaspathprepend" title="NumAsPathPrepend">NumAsPathPrepend</a>" : <i>Double</i>,
    "<a href="#sendcommunity" title="SendCommunity">SendCommunity</a>" : <i>Boolean</i>,
    "<a href="#shutdown" title="Shutdown">Shutdown</a>" : <i>Boolean</i>,
    "<a href="#ipcommunities" title="IpCommunities">IpCommunities</a>" : <i>[ <a href="ipcommunitiesdefinition.md">IpCommunitiesDefinition</a>, ... ]</i>,
    "<a href="#peers" title="Peers">Peers</a>" : <i>[ <a href="peersdefinition.md">PeersDefinition</a>, ... ]</i>,
    "<a href="#routingoptions" title="RoutingOptions">RoutingOptions</a>" : <i>[ <a href="routingoptionsdefinition.md">RoutingOptionsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#community" title="Community">Community</a>: <i>
      - String</i>
<a href="#holdtime" title="HoldTime">HoldTime</a>: <i>Double</i>
<a href="#ibgp" title="Ibgp">Ibgp</a>: <i>Boolean</i>
<a href="#keepaliveinterval" title="KeepaliveInterval">KeepaliveInterval</a>: <i>Double</i>
<a href="#localas" title="LocalAs">LocalAs</a>: <i>Double</i>
<a href="#localpreference" title="LocalPreference">LocalPreference</a>: <i>Double</i>
<a href="#numaspathprepend" title="NumAsPathPrepend">NumAsPathPrepend</a>: <i>Double</i>
<a href="#sendcommunity" title="SendCommunity">SendCommunity</a>: <i>Boolean</i>
<a href="#shutdown" title="Shutdown">Shutdown</a>: <i>Boolean</i>
<a href="#ipcommunities" title="IpCommunities">IpCommunities</a>: <i>
      - <a href="ipcommunitiesdefinition.md">IpCommunitiesDefinition</a></i>
<a href="#peers" title="Peers">Peers</a>: <i>
      - <a href="peersdefinition.md">PeersDefinition</a></i>
<a href="#routingoptions" title="RoutingOptions">RoutingOptions</a>: <i>
      - <a href="routingoptionsdefinition.md">RoutingOptionsDefinition</a></i>
</pre>

## Properties

#### Community

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HoldTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ibgp

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepaliveInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalAs

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalPreference

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumAsPathPrepend

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendCommunity

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shutdown

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpCommunities

_Required_: No

_Type_: List of <a href="ipcommunitiesdefinition.md">IpCommunitiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Peers

_Required_: No

_Type_: List of <a href="peersdefinition.md">PeersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoutingOptions

_Required_: No

_Type_: List of <a href="routingoptionsdefinition.md">RoutingOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

