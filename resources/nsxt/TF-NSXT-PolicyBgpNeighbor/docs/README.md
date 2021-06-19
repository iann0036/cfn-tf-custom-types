# TF::NSXT::PolicyBgpNeighbor

This resource provides a method for the management of a BGP Neighbor.

This resource is applicable to NSX Global Manager and NSX Policy Manager.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NSXT::PolicyBgpNeighbor",
    "Properties" : {
        "<a href="#allowasin" title="AllowAsIn">AllowAsIn</a>" : <i>Boolean</i>,
        "<a href="#bgppath" title="BgpPath">BgpPath</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#gracefulrestartmode" title="GracefulRestartMode">GracefulRestartMode</a>" : <i>String</i>,
        "<a href="#holddowntime" title="HoldDownTime">HoldDownTime</a>" : <i>Double</i>,
        "<a href="#keepalivetime" title="KeepAliveTime">KeepAliveTime</a>" : <i>Double</i>,
        "<a href="#maximumhoplimit" title="MaximumHopLimit">MaximumHopLimit</a>" : <i>Double</i>,
        "<a href="#neighboraddress" title="NeighborAddress">NeighborAddress</a>" : <i>String</i>,
        "<a href="#nsxid" title="NsxId">NsxId</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#remoteasnum" title="RemoteAsNum">RemoteAsNum</a>" : <i>String</i>,
        "<a href="#sourceaddresses" title="SourceAddresses">SourceAddresses</a>" : <i>[ String, ... ]</i>,
        "<a href="#bfdconfig" title="BfdConfig">BfdConfig</a>" : <i>[ <a href="bfdconfigdefinition.md">BfdConfigDefinition</a>, ... ]</i>,
        "<a href="#routefiltering" title="RouteFiltering">RouteFiltering</a>" : <i>[ <a href="routefilteringdefinition.md">RouteFilteringDefinition</a>, ... ]</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tagdefinition.md">TagDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NSXT::PolicyBgpNeighbor
Properties:
    <a href="#allowasin" title="AllowAsIn">AllowAsIn</a>: <i>Boolean</i>
    <a href="#bgppath" title="BgpPath">BgpPath</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#gracefulrestartmode" title="GracefulRestartMode">GracefulRestartMode</a>: <i>String</i>
    <a href="#holddowntime" title="HoldDownTime">HoldDownTime</a>: <i>Double</i>
    <a href="#keepalivetime" title="KeepAliveTime">KeepAliveTime</a>: <i>Double</i>
    <a href="#maximumhoplimit" title="MaximumHopLimit">MaximumHopLimit</a>: <i>Double</i>
    <a href="#neighboraddress" title="NeighborAddress">NeighborAddress</a>: <i>String</i>
    <a href="#nsxid" title="NsxId">NsxId</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#remoteasnum" title="RemoteAsNum">RemoteAsNum</a>: <i>String</i>
    <a href="#sourceaddresses" title="SourceAddresses">SourceAddresses</a>: <i>
      - String</i>
    <a href="#bfdconfig" title="BfdConfig">BfdConfig</a>: <i>
      - <a href="bfdconfigdefinition.md">BfdConfigDefinition</a></i>
    <a href="#routefiltering" title="RouteFiltering">RouteFiltering</a>: <i>
      - <a href="routefilteringdefinition.md">RouteFilteringDefinition</a></i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tagdefinition.md">TagDefinition</a></i>
</pre>

## Properties

#### AllowAsIn

Flag to enable allowas_in option for BGP neighbor. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpPath

The policy path to the BGP configuration for this neighbor.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of the resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

Display name of the resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GracefulRestartMode

BGP Graceful Restart Configuration Mode. One of `DISABLE`, `GR_AND_HELPER` or `HELPER_ONLY`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HoldDownTime

Wait time in seconds before declaring peer dead. Defaults to `180`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepAliveTime

Interval between keep alive messages sent to peer. Defaults to `60`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumHopLimit

Maximum number of hops allowed to reach BGP neighbor. Defaults to `1`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NeighborAddress

Neighbor IP Address.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsxId

The NSX ID of this resource. If set, this ID will be used to create the resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Password for BGP neighbor authentication. Set to the empty string to clear out the password.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteAsNum

ASN of the neighbor in ASPLAIN/ASDOT Format.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceAddresses

A list of up to 8 source IP Addresses for BGP peering. `ip_addresses` field of an existing `nsxt_policy_tier0_gateway_interface` can be used here.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BfdConfig

_Required_: No

_Type_: List of <a href="bfdconfigdefinition.md">BfdConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteFiltering

_Required_: No

_Type_: List of <a href="routefilteringdefinition.md">RouteFilteringDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tagdefinition.md">TagDefinition</a>

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

#### Path

Returns the <code>Path</code> value.

#### Revision

Returns the <code>Revision</code> value.

