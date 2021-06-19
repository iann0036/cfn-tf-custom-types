# TF::ACI::L2Outside

Manages ACI L2 Outside

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::L2Outside",
    "Properties" : {
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#relationl2extrsebd" title="RelationL2extRsEBd">RelationL2extRsEBd</a>" : <i>String</i>,
        "<a href="#relationl2extrsl2domatt" title="RelationL2extRsL2DomAtt">RelationL2extRsL2DomAtt</a>" : <i>String</i>,
        "<a href="#targetdscp" title="TargetDscp">TargetDscp</a>" : <i>String</i>,
        "<a href="#tenantdn" title="TenantDn">TenantDn</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::L2Outside
Properties:
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#relationl2extrsebd" title="RelationL2extRsEBd">RelationL2extRsEBd</a>: <i>String</i>
    <a href="#relationl2extrsl2domatt" title="RelationL2extRsL2DomAtt">RelationL2extRsL2DomAtt</a>: <i>String</i>
    <a href="#targetdscp" title="TargetDscp">TargetDscp</a>: <i>String</i>
    <a href="#tenantdn" title="TenantDn">TenantDn</a>: <i>String</i>
</pre>

## Properties

#### Annotation

Annotation for object l2 outside.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of object l2 outside.
- `annotation` - (Optional) Annotation for object l2 outside.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameAlias

Name alias for object l2 outside.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationL2extRsEBd

Relation to class fvBD. Cardinality - N_TO_ONE. Type - String.
- `relation_l2ext_rs_l2_dom_att` - (Optional) Relation to class l2extDomP. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationL2extRsL2DomAtt

Relation to class l2extDomP. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetDscp

Target dscp.
Allowed values: "AF11", "AF12", "AF13", "AF21", "AF22", "AF23", "AF31", "AF32", "AF33", "AF41", "AF42", "AF43", "CS0", "CS1", "CS2", "CS3", "CS4", "CS5", "CS6", "CS7", "EF", "VA", "unspecified". Default value: "unspecified".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantDn

Distinguished name of parent tenant object.
- `name` - (Required) Name of object l2 outside.
- `annotation` - (Optional) Annotation for object l2 outside.

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

