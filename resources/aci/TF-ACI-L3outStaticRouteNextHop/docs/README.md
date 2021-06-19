# TF::ACI::L3outStaticRouteNextHop

Manages ACI L3out Static Route Next Hop

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::L3outStaticRouteNextHop",
    "Properties" : {
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#nexthopprofiletype" title="NexthopProfileType">NexthopProfileType</a>" : <i>String</i>,
        "<a href="#nhaddr" title="NhAddr">NhAddr</a>" : <i>String</i>,
        "<a href="#pref" title="Pref">Pref</a>" : <i>String</i>,
        "<a href="#relationiprsnexthoproutetrack" title="RelationIpRsNexthopRouteTrack">RelationIpRsNexthopRouteTrack</a>" : <i>String</i>,
        "<a href="#relationiprsnhtrackmember" title="RelationIpRsNhTrackMember">RelationIpRsNhTrackMember</a>" : <i>String</i>,
        "<a href="#staticroutedn" title="StaticRouteDn">StaticRouteDn</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::L3outStaticRouteNextHop
Properties:
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#nexthopprofiletype" title="NexthopProfileType">NexthopProfileType</a>: <i>String</i>
    <a href="#nhaddr" title="NhAddr">NhAddr</a>: <i>String</i>
    <a href="#pref" title="Pref">Pref</a>: <i>String</i>
    <a href="#relationiprsnexthoproutetrack" title="RelationIpRsNexthopRouteTrack">RelationIpRsNexthopRouteTrack</a>: <i>String</i>
    <a href="#relationiprsnhtrackmember" title="RelationIpRsNhTrackMember">RelationIpRsNhTrackMember</a>: <i>String</i>
    <a href="#staticroutedn" title="StaticRouteDn">StaticRouteDn</a>: <i>String</i>
</pre>

## Properties

#### Annotation

Annotation for object l3out static route next hop.
- `description` - (Optional) Description for object l3out static route next hop.
- `name_alias` - (Optional) Name alias for object l3out static route next hop.
- `pref` - (Optional) Administrative preference value for this route.
Allowed values: "unspecified". Default value: "unspecified".
- `nexthop_profile_type` - (Optional) Component type.
Allowed values: "none", "prefix". Default value: "prefix".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description for object l3out static route next hop.
- `name_alias` - (Optional) Name alias for object l3out static route next hop.
- `pref` - (Optional) Administrative preference value for this route.
Allowed values: "unspecified". Default value: "unspecified".
- `nexthop_profile_type` - (Optional) Component type.
Allowed values: "none", "prefix". Default value: "prefix".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameAlias

Name alias for object l3out static route next hop.
- `pref` - (Optional) Administrative preference value for this route.
Allowed values: "unspecified". Default value: "unspecified".
- `nexthop_profile_type` - (Optional) Component type.
Allowed values: "none", "prefix". Default value: "prefix".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NexthopProfileType

Component type.
Allowed values: "none", "prefix". Default value: "prefix".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NhAddr

The nexthop IP address for the static route to the outside network.
- `annotation` - (Optional) Annotation for object l3out static route next hop.
- `description` - (Optional) Description for object l3out static route next hop.
- `name_alias` - (Optional) Name alias for object l3out static route next hop.
- `pref` - (Optional) Administrative preference value for this route.
Allowed values: "unspecified". Default value: "unspecified".
- `nexthop_profile_type` - (Optional) Component type.
Allowed values: "none", "prefix". Default value: "prefix".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pref

Administrative preference value for this route.
Allowed values: "unspecified". Default value: "unspecified".
- `nexthop_profile_type` - (Optional) Component type.
Allowed values: "none", "prefix". Default value: "prefix".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationIpRsNexthopRouteTrack

Relation to class fvTrackList. Cardinality - N_TO_ONE. Type - String.
- `relation_ip_rs_nh_track_member` - (Optional) Relation to class fvTrackMember. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationIpRsNhTrackMember

Relation to class fvTrackMember. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticRouteDn

Distinguished name of parent static route object.
- `nh_addr` - (Required) The nexthop IP address for the static route to the outside network.
- `annotation` - (Optional) Annotation for object l3out static route next hop.
- `description` - (Optional) Description for object l3out static route next hop.
- `name_alias` - (Optional) Name alias for object l3out static route next hop.
- `pref` - (Optional) Administrative preference value for this route.
Allowed values: "unspecified". Default value: "unspecified".
- `nexthop_profile_type` - (Optional) Component type.
Allowed values: "none", "prefix". Default value: "prefix".

_Required_: Yes

_Type_: String

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

