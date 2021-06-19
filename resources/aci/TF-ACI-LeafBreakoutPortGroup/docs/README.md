# TF::ACI::LeafBreakoutPortGroup

Manages ACI Leaf Breakout Port Group

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::LeafBreakoutPortGroup",
    "Properties" : {
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#brkoutmap" title="BrkoutMap">BrkoutMap</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#relationinfrarsmonbrkoutinfrapol" title="RelationInfraRsMonBrkoutInfraPol">RelationInfraRsMonBrkoutInfraPol</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::LeafBreakoutPortGroup
Properties:
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#brkoutmap" title="BrkoutMap">BrkoutMap</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#relationinfrarsmonbrkoutinfrapol" title="RelationInfraRsMonBrkoutInfraPol">RelationInfraRsMonBrkoutInfraPol</a>: <i>String</i>
</pre>

## Properties

#### Annotation

Annotation for leaf breakout port group object.
- `brkout_map` - (Optional) Breakout map for leaf breakout port group object. Allowed values are "100g-2x", "100g-4x", "10g-4x", "25g-4x", "50g-8x" and "none". Default value is "none".
- `name_alias` - (Optional) Name alias for leaf breakout port group object.
- `description` - (Optional) Description for leaf breakout port group object.
- `relation_infra_rs_mon_brkout_infra_pol` - (Optional) Relation to class monInfraPol. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BrkoutMap

Breakout map for leaf breakout port group object. Allowed values are "100g-2x", "100g-4x", "10g-4x", "25g-4x", "50g-8x" and "none". Default value is "none".
- `name_alias` - (Optional) Name alias for leaf breakout port group object.
- `description` - (Optional) Description for leaf breakout port group object.
- `relation_infra_rs_mon_brkout_infra_pol` - (Optional) Relation to class monInfraPol. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description for leaf breakout port group object.
- `relation_infra_rs_mon_brkout_infra_pol` - (Optional) Relation to class monInfraPol. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of leaf breakout port group object.
- `annotation` - (Optional) Annotation for leaf breakout port group object.
- `brkout_map` - (Optional) Breakout map for leaf breakout port group object. Allowed values are "100g-2x", "100g-4x", "10g-4x", "25g-4x", "50g-8x" and "none". Default value is "none".
- `name_alias` - (Optional) Name alias for leaf breakout port group object.
- `description` - (Optional) Description for leaf breakout port group object.
- `relation_infra_rs_mon_brkout_infra_pol` - (Optional) Relation to class monInfraPol. Cardinality - N_TO_ONE. Type - String.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameAlias

Name alias for leaf breakout port group object.
- `description` - (Optional) Description for leaf breakout port group object.
- `relation_infra_rs_mon_brkout_infra_pol` - (Optional) Relation to class monInfraPol. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationInfraRsMonBrkoutInfraPol

Relation to class monInfraPol. Cardinality - N_TO_ONE. Type - String.

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

