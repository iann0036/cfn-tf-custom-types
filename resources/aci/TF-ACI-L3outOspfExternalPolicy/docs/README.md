# TF::ACI::L3outOspfExternalPolicy

Manages ACI L3-out OSPF External Policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::L3outOspfExternalPolicy",
    "Properties" : {
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#areacost" title="AreaCost">AreaCost</a>" : <i>String</i>,
        "<a href="#areactrl" title="AreaCtrl">AreaCtrl</a>" : <i>String</i>,
        "<a href="#areaid" title="AreaId">AreaId</a>" : <i>String</i>,
        "<a href="#areatype" title="AreaType">AreaType</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#l3outsidedn" title="L3OutsideDn">L3OutsideDn</a>" : <i>String</i>,
        "<a href="#multipodinternal" title="MultipodInternal">MultipodInternal</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::L3outOspfExternalPolicy
Properties:
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#areacost" title="AreaCost">AreaCost</a>: <i>String</i>
    <a href="#areactrl" title="AreaCtrl">AreaCtrl</a>: <i>String</i>
    <a href="#areaid" title="AreaId">AreaId</a>: <i>String</i>
    <a href="#areatype" title="AreaType">AreaType</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#l3outsidedn" title="L3OutsideDn">L3OutsideDn</a>: <i>String</i>
    <a href="#multipodinternal" title="MultipodInternal">MultipodInternal</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
</pre>

## Properties

#### Annotation

Annotation for object L3-out OSPF External Policy.
- `area_cost` - (Optional) The OSPF Area cost.
- `area_ctrl` - (Optional) The controls of redistribution and summary LSA generation into NSSA and Stub areas.
Allowed values: "redistribute", "summary", "suppress-fa", "unspecified" (Multiple Comma-Delimited values are allowed. E.g., "redistribute,summary"). Default value: "redistribute,summary".
- `area_id` - (Optional) The OSPF Area ID.
- `area_type` - (Optional) The area type.
Allowed values: "nssa", "regular", "stub". Default value: "nssa".
- `multipod_internal` - (Optional) Start OSPF in WAN instance instead of default.
Allowed values: "no", "yes". Default value: "no".
- `name_alias` - (Optional) Name alias for object L3-out OSPF External Policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AreaCost

The OSPF Area cost.
- `area_ctrl` - (Optional) The controls of redistribution and summary LSA generation into NSSA and Stub areas.
Allowed values: "redistribute", "summary", "suppress-fa", "unspecified" (Multiple Comma-Delimited values are allowed. E.g., "redistribute,summary"). Default value: "redistribute,summary".
- `area_id` - (Optional) The OSPF Area ID.
- `area_type` - (Optional) The area type.
Allowed values: "nssa", "regular", "stub". Default value: "nssa".
- `multipod_internal` - (Optional) Start OSPF in WAN instance instead of default.
Allowed values: "no", "yes". Default value: "no".
- `name_alias` - (Optional) Name alias for object L3-out OSPF External Policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AreaCtrl

The controls of redistribution and summary LSA generation into NSSA and Stub areas.
Allowed values: "redistribute", "summary", "suppress-fa", "unspecified" (Multiple Comma-Delimited values are allowed. E.g., "redistribute,summary"). Default value: "redistribute,summary".
- `area_id` - (Optional) The OSPF Area ID.
- `area_type` - (Optional) The area type.
Allowed values: "nssa", "regular", "stub". Default value: "nssa".
- `multipod_internal` - (Optional) Start OSPF in WAN instance instead of default.
Allowed values: "no", "yes". Default value: "no".
- `name_alias` - (Optional) Name alias for object L3-out OSPF External Policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AreaId

The OSPF Area ID.
- `area_type` - (Optional) The area type.
Allowed values: "nssa", "regular", "stub". Default value: "nssa".
- `multipod_internal` - (Optional) Start OSPF in WAN instance instead of default.
Allowed values: "no", "yes". Default value: "no".
- `name_alias` - (Optional) Name alias for object L3-out OSPF External Policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AreaType

The area type.
Allowed values: "nssa", "regular", "stub". Default value: "nssa".
- `multipod_internal` - (Optional) Start OSPF in WAN instance instead of default.
Allowed values: "no", "yes". Default value: "no".
- `name_alias` - (Optional) Name alias for object L3-out OSPF External Policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L3OutsideDn

Distinguished name of parent l3 outside object.
- `annotation` - (Optional) Annotation for object L3-out OSPF External Policy.
- `area_cost` - (Optional) The OSPF Area cost.
- `area_ctrl` - (Optional) The controls of redistribution and summary LSA generation into NSSA and Stub areas.
Allowed values: "redistribute", "summary", "suppress-fa", "unspecified" (Multiple Comma-Delimited values are allowed. E.g., "redistribute,summary"). Default value: "redistribute,summary".
- `area_id` - (Optional) The OSPF Area ID.
- `area_type` - (Optional) The area type.
Allowed values: "nssa", "regular", "stub". Default value: "nssa".
- `multipod_internal` - (Optional) Start OSPF in WAN instance instead of default.
Allowed values: "no", "yes". Default value: "no".
- `name_alias` - (Optional) Name alias for object L3-out OSPF External Policy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MultipodInternal

Start OSPF in WAN instance instead of default.
Allowed values: "no", "yes". Default value: "no".
- `name_alias` - (Optional) Name alias for object L3-out OSPF External Policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameAlias

Name alias for object L3-out OSPF External Policy.

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

