# TF::ACI::L2outExtepg

Manages ACI L2-Out External EPG

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::L2outExtepg",
    "Properties" : {
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#exceptiontag" title="ExceptionTag">ExceptionTag</a>" : <i>String</i>,
        "<a href="#floodonencap" title="FloodOnEncap">FloodOnEncap</a>" : <i>String</i>,
        "<a href="#l2outsidedn" title="L2OutsideDn">L2OutsideDn</a>" : <i>String</i>,
        "<a href="#matcht" title="MatchT">MatchT</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#prefgrmemb" title="PrefGrMemb">PrefGrMemb</a>" : <i>String</i>,
        "<a href="#prio" title="Prio">Prio</a>" : <i>String</i>,
        "<a href="#relationfvrscons" title="RelationFvRsCons">RelationFvRsCons</a>" : <i>[ String, ... ]</i>,
        "<a href="#relationfvrsconsif" title="RelationFvRsConsIf">RelationFvRsConsIf</a>" : <i>[ String, ... ]</i>,
        "<a href="#relationfvrscustqospol" title="RelationFvRsCustQosPol">RelationFvRsCustQosPol</a>" : <i>String</i>,
        "<a href="#relationfvrsintraepg" title="RelationFvRsIntraEpg">RelationFvRsIntraEpg</a>" : <i>[ String, ... ]</i>,
        "<a href="#relationfvrsprotby" title="RelationFvRsProtBy">RelationFvRsProtBy</a>" : <i>[ String, ... ]</i>,
        "<a href="#relationfvrsprov" title="RelationFvRsProv">RelationFvRsProv</a>" : <i>[ String, ... ]</i>,
        "<a href="#relationfvrssecinherited" title="RelationFvRsSecInherited">RelationFvRsSecInherited</a>" : <i>[ String, ... ]</i>,
        "<a href="#relationl2extrsl2instptodomp" title="RelationL2extRsL2InstPToDomP">RelationL2extRsL2InstPToDomP</a>" : <i>String</i>,
        "<a href="#targetdscp" title="TargetDscp">TargetDscp</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::L2outExtepg
Properties:
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#exceptiontag" title="ExceptionTag">ExceptionTag</a>: <i>String</i>
    <a href="#floodonencap" title="FloodOnEncap">FloodOnEncap</a>: <i>String</i>
    <a href="#l2outsidedn" title="L2OutsideDn">L2OutsideDn</a>: <i>String</i>
    <a href="#matcht" title="MatchT">MatchT</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#prefgrmemb" title="PrefGrMemb">PrefGrMemb</a>: <i>String</i>
    <a href="#prio" title="Prio">Prio</a>: <i>String</i>
    <a href="#relationfvrscons" title="RelationFvRsCons">RelationFvRsCons</a>: <i>
      - String</i>
    <a href="#relationfvrsconsif" title="RelationFvRsConsIf">RelationFvRsConsIf</a>: <i>
      - String</i>
    <a href="#relationfvrscustqospol" title="RelationFvRsCustQosPol">RelationFvRsCustQosPol</a>: <i>String</i>
    <a href="#relationfvrsintraepg" title="RelationFvRsIntraEpg">RelationFvRsIntraEpg</a>: <i>
      - String</i>
    <a href="#relationfvrsprotby" title="RelationFvRsProtBy">RelationFvRsProtBy</a>: <i>
      - String</i>
    <a href="#relationfvrsprov" title="RelationFvRsProv">RelationFvRsProv</a>: <i>
      - String</i>
    <a href="#relationfvrssecinherited" title="RelationFvRsSecInherited">RelationFvRsSecInherited</a>: <i>
      - String</i>
    <a href="#relationl2extrsl2instptodomp" title="RelationL2extRsL2InstPToDomP">RelationL2extRsL2InstPToDomP</a>: <i>String</i>
    <a href="#targetdscp" title="TargetDscp">TargetDscp</a>: <i>String</i>
</pre>

## Properties

#### Annotation

annotation for object L2-Out External EPG.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionTag

Exception tag for object L2-Out External EPG.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FloodOnEncap

Control at EPG level if the traffic L2 Multicast/Broadcast and Link Local Layer should be flooded only on ENCAP or based on bridg-domain settings.
Allowed values: "disabled", "enabled". Default value: "disabled".
- `match_t` - (Optional) The provider label match criteria.
Allowed values: "All", "AtleastOne", "AtmostOne", "None". Default value: "AtleastOne".
- `name_alias` - (Optional) name_alias for object L2-Out External EPG.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L2OutsideDn

Distinguished name of parent L2-Outside object.
- `name` - (Required) The name of the layer 2 L2-Out External EPG. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
- `annotation` - (Optional) annotation for object L2-Out External EPG.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchT

The provider label match criteria.
Allowed values: "All", "AtleastOne", "AtmostOne", "None". Default value: "AtleastOne".
- `name_alias` - (Optional) name_alias for object L2-Out External EPG.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the layer 2 L2-Out External EPG. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
- `annotation` - (Optional) annotation for object L2-Out External EPG.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameAlias

name_alias for object L2-Out External EPG.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefGrMemb

Represents parameter used to determine if EPg is part of a group that does not a contract for communication.
Allowed values: "exclude", "include". Default value: "exclude".
- `prio` - (Optional) The QoS priority class identifier.
Allowed values: "level1", "level2", "level3", "level4", "level5", "level6", "unspecified".
- `target_dscp` - (Optional) The target differentiated services code point (DSCP) of the path attached to the layer 3 outside profile.
Allowed values: "AF11", "AF12", "AF13", "AF21", "AF22", "AF23", "AF31", "AF32", "AF33", "AF41", "AF42", "AF43", "CS0", "CS1", "CS2", "CS3", "CS4", "CS5", "CS6", "CS7", "EF", "VA", "unspecified".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prio

The QoS priority class identifier.
Allowed values: "level1", "level2", "level3", "level4", "level5", "level6", "unspecified".
- `target_dscp` - (Optional) The target differentiated services code point (DSCP) of the path attached to the layer 3 outside profile.
Allowed values: "AF11", "AF12", "AF13", "AF21", "AF22", "AF23", "AF31", "AF32", "AF33", "AF41", "AF42", "AF43", "CS0", "CS1", "CS2", "CS3", "CS4", "CS5", "CS6", "CS7", "EF", "VA", "unspecified".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsCons

Relation to class vzBrCP. Cardinality - N_TO_M. Type - Set of String.
- `relation_l2ext_rs_l2_inst_p_to_dom_p` - (Optional) Relation to class l2extDomP. Cardinality - N_TO_ONE. Type - String.
- `relation_fv_rs_prot_by` - (Optional) Relation to class vzTaboo. Cardinality - N_TO_M. Type - Set of String.
- `relation_fv_rs_intra_epg` - (Optional) Relation to class vzBrCP. Cardinality - N_TO_M. Type - Set of String.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsConsIf

Relation to class vzCPIf. Cardinality - N_TO_M. Type - Set of String.
- `relation_fv_rs_cust_qos_pol` - (Optional) Relation to class qosCustomPol. Cardinality - N_TO_ONE. Type - String.
- `relation_fv_rs_cons` - (Optional) Relation to class vzBrCP. Cardinality - N_TO_M. Type - Set of String.
- `relation_l2ext_rs_l2_inst_p_to_dom_p` - (Optional) Relation to class l2extDomP. Cardinality - N_TO_ONE. Type - String.
- `relation_fv_rs_prot_by` - (Optional) Relation to class vzTaboo. Cardinality - N_TO_M. Type - Set of String.
- `relation_fv_rs_intra_epg` - (Optional) Relation to class vzBrCP. Cardinality - N_TO_M. Type - Set of String.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsCustQosPol

Relation to class qosCustomPol. Cardinality - N_TO_ONE. Type - String.
- `relation_fv_rs_cons` - (Optional) Relation to class vzBrCP. Cardinality - N_TO_M. Type - Set of String.
- `relation_l2ext_rs_l2_inst_p_to_dom_p` - (Optional) Relation to class l2extDomP. Cardinality - N_TO_ONE. Type - String.
- `relation_fv_rs_prot_by` - (Optional) Relation to class vzTaboo. Cardinality - N_TO_M. Type - Set of String.
- `relation_fv_rs_intra_epg` - (Optional) Relation to class vzBrCP. Cardinality - N_TO_M. Type - Set of String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsIntraEpg

Relation to class vzBrCP. Cardinality - N_TO_M. Type - Set of String.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsProtBy

Relation to class vzTaboo. Cardinality - N_TO_M. Type - Set of String.
- `relation_fv_rs_intra_epg` - (Optional) Relation to class vzBrCP. Cardinality - N_TO_M. Type - Set of String.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsProv

Relation to class vzBrCP. Cardinality - N_TO_M. Type - Set of String.
- `relation_fv_rs_cons_if` - (Optional) Relation to class vzCPIf. Cardinality - N_TO_M. Type - Set of String.
- `relation_fv_rs_cust_qos_pol` - (Optional) Relation to class qosCustomPol. Cardinality - N_TO_ONE. Type - String.
- `relation_fv_rs_cons` - (Optional) Relation to class vzBrCP. Cardinality - N_TO_M. Type - Set of String.
- `relation_l2ext_rs_l2_inst_p_to_dom_p` - (Optional) Relation to class l2extDomP. Cardinality - N_TO_ONE. Type - String.
- `relation_fv_rs_prot_by` - (Optional) Relation to class vzTaboo. Cardinality - N_TO_M. Type - Set of String.
- `relation_fv_rs_intra_epg` - (Optional) Relation to class vzBrCP. Cardinality - N_TO_M. Type - Set of String.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationFvRsSecInherited

Relation to class fvEPg. Cardinality - N_TO_M. Type - Set of String.
- `relation_fv_rs_prov` - (Optional) Relation to class vzBrCP. Cardinality - N_TO_M. Type - Set of String.
- `relation_fv_rs_cons_if` - (Optional) Relation to class vzCPIf. Cardinality - N_TO_M. Type - Set of String.
- `relation_fv_rs_cust_qos_pol` - (Optional) Relation to class qosCustomPol. Cardinality - N_TO_ONE. Type - String.
- `relation_fv_rs_cons` - (Optional) Relation to class vzBrCP. Cardinality - N_TO_M. Type - Set of String.
- `relation_l2ext_rs_l2_inst_p_to_dom_p` - (Optional) Relation to class l2extDomP. Cardinality - N_TO_ONE. Type - String.
- `relation_fv_rs_prot_by` - (Optional) Relation to class vzTaboo. Cardinality - N_TO_M. Type - Set of String.
- `relation_fv_rs_intra_epg` - (Optional) Relation to class vzBrCP. Cardinality - N_TO_M. Type - Set of String.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationL2extRsL2InstPToDomP

Relation to class l2extDomP. Cardinality - N_TO_ONE. Type - String.
- `relation_fv_rs_prot_by` - (Optional) Relation to class vzTaboo. Cardinality - N_TO_M. Type - Set of String.
- `relation_fv_rs_intra_epg` - (Optional) Relation to class vzBrCP. Cardinality - N_TO_M. Type - Set of String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetDscp

The target differentiated services code point (DSCP) of the path attached to the layer 3 outside profile.
Allowed values: "AF11", "AF12", "AF13", "AF21", "AF22", "AF23", "AF31", "AF32", "AF33", "AF41", "AF42", "AF43", "CS0", "CS1", "CS2", "CS3", "CS4", "CS5", "CS6", "CS7", "EF", "VA", "unspecified".

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

