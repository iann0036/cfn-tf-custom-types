# Terraform::Panos::RedistributionProfileIpv4

This resource allows you to add/update/delete IPv4 redistribution profiles
on a virtual router.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::RedistributionProfileIpv4",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#bgpcommunities" title="BgpCommunities">BgpCommunities</a>" : <i>[ String, ... ]</i>,
        "<a href="#bgpextendedcommunities" title="BgpExtendedCommunities">BgpExtendedCommunities</a>" : <i>[ String, ... ]</i>,
        "<a href="#destinations" title="Destinations">Destinations</a>" : <i>[ String, ... ]</i>,
        "<a href="#interfaces" title="Interfaces">Interfaces</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nexthops" title="NextHops">NextHops</a>" : <i>[ String, ... ]</i>,
        "<a href="#ospfareas" title="OspfAreas">OspfAreas</a>" : <i>[ String, ... ]</i>,
        "<a href="#ospfpathtypes" title="OspfPathTypes">OspfPathTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#ospftags" title="OspfTags">OspfTags</a>" : <i>[ String, ... ]</i>,
        "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
        "<a href="#types" title="Types">Types</a>" : <i>[ String, ... ]</i>,
        "<a href="#virtualrouter" title="VirtualRouter">VirtualRouter</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::RedistributionProfileIpv4
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#bgpcommunities" title="BgpCommunities">BgpCommunities</a>: <i>
      - String</i>
    <a href="#bgpextendedcommunities" title="BgpExtendedCommunities">BgpExtendedCommunities</a>: <i>
      - String</i>
    <a href="#destinations" title="Destinations">Destinations</a>: <i>
      - String</i>
    <a href="#interfaces" title="Interfaces">Interfaces</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nexthops" title="NextHops">NextHops</a>: <i>
      - String</i>
    <a href="#ospfareas" title="OspfAreas">OspfAreas</a>: <i>
      - String</i>
    <a href="#ospfpathtypes" title="OspfPathTypes">OspfPathTypes</a>: <i>
      - String</i>
    <a href="#ospftags" title="OspfTags">OspfTags</a>: <i>
      - String</i>
    <a href="#priority" title="Priority">Priority</a>: <i>Double</i>
    <a href="#types" title="Types">Types</a>: <i>
      - String</i>
    <a href="#virtualrouter" title="VirtualRouter">VirtualRouter</a>: <i>String</i>
</pre>

## Properties

#### Action

The action.  Valid values are `redist` (default) or
`no-redist`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpCommunities

BGP communities.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpExtendedCommunities

BGP extended communities.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destinations

Specify candidate routes' next-hop addresses
(subnet match).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interfaces

Specify candidate routes.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The redistribution profile's name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NextHops

Specify candidate routes' next-hop addresses
(subnet match).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OspfAreas

OSPF areas.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OspfPathTypes

OSPF path types.  Valid values are
`intra-area`, `inter-area`, `ext-1`, and `ext-2`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OspfTags

OSPF tags.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

The priority, integer from 1 to 255.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Types

The source types.  Valid values are `bgp`, `connect`,
`ospf`, `rip`, and `static`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualRouter

The virtual router to add the
redistribution profile to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

