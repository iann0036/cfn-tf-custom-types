# TF::ACI::L3outStaticRoute

Manages ACI L3out Static Route

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::L3outStaticRoute",
    "Properties" : {
        "<a href="#aggregate" title="Aggregate">Aggregate</a>" : <i>String</i>,
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#fabricnodedn" title="FabricNodeDn">FabricNodeDn</a>" : <i>String</i>,
        "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#pref" title="Pref">Pref</a>" : <i>String</i>,
        "<a href="#relationiprsroutetrack" title="RelationIpRsRouteTrack">RelationIpRsRouteTrack</a>" : <i>String</i>,
        "<a href="#rtctrl" title="RtCtrl">RtCtrl</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::L3outStaticRoute
Properties:
    <a href="#aggregate" title="Aggregate">Aggregate</a>: <i>String</i>
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#fabricnodedn" title="FabricNodeDn">FabricNodeDn</a>: <i>String</i>
    <a href="#ip" title="Ip">Ip</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#pref" title="Pref">Pref</a>: <i>String</i>
    <a href="#relationiprsroutetrack" title="RelationIpRsRouteTrack">RelationIpRsRouteTrack</a>: <i>String</i>
    <a href="#rtctrl" title="RtCtrl">RtCtrl</a>: <i>String</i>
</pre>

## Properties

#### Aggregate

Aggregated Route for object l3out static route.
Allowed values: "no", "yes". Default value: "no".
- `annotation` - (Optional) Annotation for object l3out static route.
- `description` - (Optional) Description for object l3out static route.
- `name_alias` - (Optional) Name alias for object l3out static route.
- `pref` - (Optional) The administrative preference value for this route. This value is useful for resolving routes advertised from different protocols. Default value: "1".
- `rt_ctrl` - (Optional) Route control for object l3out static route.
Allowed values: "bfd", "unspecified". Default value: "unspecified".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Annotation

Annotation for object l3out static route.
- `description` - (Optional) Description for object l3out static route.
- `name_alias` - (Optional) Name alias for object l3out static route.
- `pref` - (Optional) The administrative preference value for this route. This value is useful for resolving routes advertised from different protocols. Default value: "1".
- `rt_ctrl` - (Optional) Route control for object l3out static route.
Allowed values: "bfd", "unspecified". Default value: "unspecified".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description for object l3out static route.
- `name_alias` - (Optional) Name alias for object l3out static route.
- `pref` - (Optional) The administrative preference value for this route. This value is useful for resolving routes advertised from different protocols. Default value: "1".
- `rt_ctrl` - (Optional) Route control for object l3out static route.
Allowed values: "bfd", "unspecified". Default value: "unspecified".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FabricNodeDn

Distinguished name of parent fabric node object.
- `ip` - (Required) The static route IP address assigned to the outside network.
- `aggregate` - (Optional) Aggregated Route for object l3out static route.
Allowed values: "no", "yes". Default value: "no".
- `annotation` - (Optional) Annotation for object l3out static route.
- `description` - (Optional) Description for object l3out static route.
- `name_alias` - (Optional) Name alias for object l3out static route.
- `pref` - (Optional) The administrative preference value for this route. This value is useful for resolving routes advertised from different protocols. Default value: "1".
- `rt_ctrl` - (Optional) Route control for object l3out static route.
Allowed values: "bfd", "unspecified". Default value: "unspecified".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

The static route IP address assigned to the outside network.
- `aggregate` - (Optional) Aggregated Route for object l3out static route.
Allowed values: "no", "yes". Default value: "no".
- `annotation` - (Optional) Annotation for object l3out static route.
- `description` - (Optional) Description for object l3out static route.
- `name_alias` - (Optional) Name alias for object l3out static route.
- `pref` - (Optional) The administrative preference value for this route. This value is useful for resolving routes advertised from different protocols. Default value: "1".
- `rt_ctrl` - (Optional) Route control for object l3out static route.
Allowed values: "bfd", "unspecified". Default value: "unspecified".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameAlias

Name alias for object l3out static route.
- `pref` - (Optional) The administrative preference value for this route. This value is useful for resolving routes advertised from different protocols. Default value: "1".
- `rt_ctrl` - (Optional) Route control for object l3out static route.
Allowed values: "bfd", "unspecified". Default value: "unspecified".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pref

The administrative preference value for this route. This value is useful for resolving routes advertised from different protocols. Default value: "1".
- `rt_ctrl` - (Optional) Route control for object l3out static route.
Allowed values: "bfd", "unspecified". Default value: "unspecified".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationIpRsRouteTrack

Relation to class fvTrackList. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RtCtrl

Route control for object l3out static route.
Allowed values: "bfd", "unspecified". Default value: "unspecified".

_Required_: No

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

