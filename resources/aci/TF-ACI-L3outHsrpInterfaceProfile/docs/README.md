# TF::ACI::L3outHsrpInterfaceProfile

Manages ACI L3-out HSRP interface profile

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::L3outHsrpInterfaceProfile",
    "Properties" : {
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#logicalinterfaceprofiledn" title="LogicalInterfaceProfileDn">LogicalInterfaceProfileDn</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#relationhsrprsifpol" title="RelationHsrpRsIfPol">RelationHsrpRsIfPol</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::L3outHsrpInterfaceProfile
Properties:
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#logicalinterfaceprofiledn" title="LogicalInterfaceProfileDn">LogicalInterfaceProfileDn</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#relationhsrprsifpol" title="RelationHsrpRsIfPol">RelationHsrpRsIfPol</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
</pre>

## Properties

#### Annotation

Annotation for object L3-out HSRP interface profile.
- `description` - (Optional) Description for object L3-out HSRP interface profile.
- `name_alias` - (Optional) Name alias for object L3-out HSRP interface profile.
- `version` - (Optional) Compatibility catalog version.
Allowed values: "v1", "v2". Default value: "v1".
- `relation_hsrp_rs_if_pol` - (Optional) Relation to class hsrpIfPol. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description for object L3-out HSRP interface profile.
- `name_alias` - (Optional) Name alias for object L3-out HSRP interface profile.
- `version` - (Optional) Compatibility catalog version.
Allowed values: "v1", "v2". Default value: "v1".
- `relation_hsrp_rs_if_pol` - (Optional) Relation to class hsrpIfPol. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogicalInterfaceProfileDn

Distinguished name of parent logical interface profile object.
- `annotation` - (Optional) Annotation for object L3-out HSRP interface profile.
- `description` - (Optional) Description for object L3-out HSRP interface profile.
- `name_alias` - (Optional) Name alias for object L3-out HSRP interface profile.
- `version` - (Optional) Compatibility catalog version.
Allowed values: "v1", "v2". Default value: "v1".
- `relation_hsrp_rs_if_pol` - (Optional) Relation to class hsrpIfPol. Cardinality - N_TO_ONE. Type - String.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameAlias

Name alias for object L3-out HSRP interface profile.
- `version` - (Optional) Compatibility catalog version.
Allowed values: "v1", "v2". Default value: "v1".
- `relation_hsrp_rs_if_pol` - (Optional) Relation to class hsrpIfPol. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationHsrpRsIfPol

Relation to class hsrpIfPol. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

Compatibility catalog version.
Allowed values: "v1", "v2". Default value: "v1".
- `relation_hsrp_rs_if_pol` - (Optional) Relation to class hsrpIfPol. Cardinality - N_TO_ONE. Type - String.

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

