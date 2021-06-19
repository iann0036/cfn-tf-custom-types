# TF::ACI::L3Outside

Manages ACI L3 Outside

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::L3Outside",
    "Properties" : {
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enforcertctrl" title="EnforceRtctrl">EnforceRtctrl</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#relationl3extrsectx" title="RelationL3extRsEctx">RelationL3extRsEctx</a>" : <i>String</i>,
        "<a href="#relationl3extrsinterleakpol" title="RelationL3extRsInterleakPol">RelationL3extRsInterleakPol</a>" : <i>String</i>,
        "<a href="#relationl3extrsl3domatt" title="RelationL3extRsL3DomAtt">RelationL3extRsL3DomAtt</a>" : <i>String</i>,
        "<a href="#relationl3extrsouttobdpublicsubnetholder" title="RelationL3extRsOutToBdPublicSubnetHolder">RelationL3extRsOutToBdPublicSubnetHolder</a>" : <i>[ String, ... ]</i>,
        "<a href="#targetdscp" title="TargetDscp">TargetDscp</a>" : <i>String</i>,
        "<a href="#tenantdn" title="TenantDn">TenantDn</a>" : <i>String</i>,
        "<a href="#relationl3extrsdampeningpol" title="RelationL3extRsDampeningPol">RelationL3extRsDampeningPol</a>" : <i>[ <a href="relationl3extrsdampeningpoldefinition.md">RelationL3extRsDampeningPolDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::L3Outside
Properties:
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enforcertctrl" title="EnforceRtctrl">EnforceRtctrl</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#relationl3extrsectx" title="RelationL3extRsEctx">RelationL3extRsEctx</a>: <i>String</i>
    <a href="#relationl3extrsinterleakpol" title="RelationL3extRsInterleakPol">RelationL3extRsInterleakPol</a>: <i>String</i>
    <a href="#relationl3extrsl3domatt" title="RelationL3extRsL3DomAtt">RelationL3extRsL3DomAtt</a>: <i>String</i>
    <a href="#relationl3extrsouttobdpublicsubnetholder" title="RelationL3extRsOutToBdPublicSubnetHolder">RelationL3extRsOutToBdPublicSubnetHolder</a>: <i>
      - String</i>
    <a href="#targetdscp" title="TargetDscp">TargetDscp</a>: <i>String</i>
    <a href="#tenantdn" title="TenantDn">TenantDn</a>: <i>String</i>
    <a href="#relationl3extrsdampeningpol" title="RelationL3extRsDampeningPol">RelationL3extRsDampeningPol</a>: <i>
      - <a href="relationl3extrsdampeningpoldefinition.md">RelationL3extRsDampeningPolDefinition</a></i>
</pre>

## Properties

#### Annotation

annotation for object l3_outside.
- `enforce_rtctrl` - (Optional) enforce route control type. Allowed values are "import" and "export". Default is "export".
- `name_alias` - (Optional) name_alias for object l3_outside.
- `target_dscp` - (Optional) The target differentiated services code point (DSCP) of the path attached to the layer 3 outside profile. Allowed values are "CS0", "CS1", "AF11", "AF12", "AF13", "CS2", "AF21", "AF22", "AF23", "CS3", "AF31", "AF32", "AF33", "CS4", "AF41", "AF42", "AF43", "CS5", "VA", "EF", "CS6", "CS7" and "unspecified". Default is "unspecified".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnforceRtctrl

enforce route control type. Allowed values are "import" and "export". Default is "export".
- `name_alias` - (Optional) name_alias for object l3_outside.
- `target_dscp` - (Optional) The target differentiated services code point (DSCP) of the path attached to the layer 3 outside profile. Allowed values are "CS0", "CS1", "AF11", "AF12", "AF13", "CS2", "AF21", "AF22", "AF23", "CS3", "AF31", "AF32", "AF33", "CS4", "AF41", "AF42", "AF43", "CS5", "VA", "EF", "CS6", "CS7" and "unspecified". Default is "unspecified".

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

name of Object l3_outside.
- `annotation` - (Optional) annotation for object l3_outside.
- `enforce_rtctrl` - (Optional) enforce route control type. Allowed values are "import" and "export". Default is "export".
- `name_alias` - (Optional) name_alias for object l3_outside.
- `target_dscp` - (Optional) The target differentiated services code point (DSCP) of the path attached to the layer 3 outside profile. Allowed values are "CS0", "CS1", "AF11", "AF12", "AF13", "CS2", "AF21", "AF22", "AF23", "CS3", "AF31", "AF32", "AF33", "CS4", "AF41", "AF42", "AF43", "CS5", "VA", "EF", "CS6", "CS7" and "unspecified". Default is "unspecified".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameAlias

name_alias for object l3_outside.
- `target_dscp` - (Optional) The target differentiated services code point (DSCP) of the path attached to the layer 3 outside profile. Allowed values are "CS0", "CS1", "AF11", "AF12", "AF13", "CS2", "AF21", "AF22", "AF23", "CS3", "AF31", "AF32", "AF33", "CS4", "AF41", "AF42", "AF43", "CS5", "VA", "EF", "CS6", "CS7" and "unspecified". Default is "unspecified".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationL3extRsEctx

Relation to class fvCtx. Cardinality - N_TO_ONE. Type - String.
- `relation_l3ext_rs_out_to_bd_public_subnet_holder` - (Optional) Relation to class fvBDPublicSubnetHolder. Cardinality - N_TO_M. Type - Set of String.
- `relation_l3ext_rs_interleak_pol` - (Optional) Relation to class rtctrlProfile. Cardinality - N_TO_ONE. Type - String.
- `relation_l3ext_rs_l3_dom_att` - (Optional) Relation to class extnwDomP. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationL3extRsInterleakPol

Relation to class rtctrlProfile. Cardinality - N_TO_ONE. Type - String.
- `relation_l3ext_rs_l3_dom_att` - (Optional) Relation to class extnwDomP. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationL3extRsL3DomAtt

Relation to class extnwDomP. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationL3extRsOutToBdPublicSubnetHolder

Relation to class fvBDPublicSubnetHolder. Cardinality - N_TO_M. Type - Set of String.
- `relation_l3ext_rs_interleak_pol` - (Optional) Relation to class rtctrlProfile. Cardinality - N_TO_ONE. Type - String.
- `relation_l3ext_rs_l3_dom_att` - (Optional) Relation to class extnwDomP. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetDscp

The target differentiated services code point (DSCP) of the path attached to the layer 3 outside profile. Allowed values are "CS0", "CS1", "AF11", "AF12", "AF13", "CS2", "AF21", "AF22", "AF23", "CS3", "AF31", "AF32", "AF33", "CS4", "AF41", "AF42", "AF43", "CS5", "VA", "EF", "CS6", "CS7" and "unspecified". Default is "unspecified".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantDn

Distinguished name of parent Tenant object.
- `name` - (Required) name of Object l3_outside.
- `annotation` - (Optional) annotation for object l3_outside.
- `enforce_rtctrl` - (Optional) enforce route control type. Allowed values are "import" and "export". Default is "export".
- `name_alias` - (Optional) name_alias for object l3_outside.
- `target_dscp` - (Optional) The target differentiated services code point (DSCP) of the path attached to the layer 3 outside profile. Allowed values are "CS0", "CS1", "AF11", "AF12", "AF13", "CS2", "AF21", "AF22", "AF23", "CS3", "AF31", "AF32", "AF33", "CS4", "AF41", "AF42", "AF43", "CS5", "VA", "EF", "CS6", "CS7" and "unspecified". Default is "unspecified".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationL3extRsDampeningPol

_Required_: No

_Type_: List of <a href="relationl3extrsdampeningpoldefinition.md">RelationL3extRsDampeningPolDefinition</a>

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

