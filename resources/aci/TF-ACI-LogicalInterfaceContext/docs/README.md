# TF::ACI::LogicalInterfaceContext

Manages ACI Logical Interface Context

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::LogicalInterfaceContext",
    "Properties" : {
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#connnameorlbl" title="ConnNameOrLbl">ConnNameOrLbl</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#l3dest" title="L3Dest">L3Dest</a>" : <i>String</i>,
        "<a href="#logicaldevicecontextdn" title="LogicalDeviceContextDn">LogicalDeviceContextDn</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#permitlog" title="PermitLog">PermitLog</a>" : <i>String</i>,
        "<a href="#relationvnsrslifctxtobd" title="RelationVnsRsLIfCtxToBd">RelationVnsRsLIfCtxToBd</a>" : <i>String</i>,
        "<a href="#relationvnsrslifctxtocustqospol" title="RelationVnsRsLIfCtxToCustQosPol">RelationVnsRsLIfCtxToCustQosPol</a>" : <i>String</i>,
        "<a href="#relationvnsrslifctxtoinstp" title="RelationVnsRsLIfCtxToInstP">RelationVnsRsLIfCtxToInstP</a>" : <i>String</i>,
        "<a href="#relationvnsrslifctxtolif" title="RelationVnsRsLIfCtxToLIf">RelationVnsRsLIfCtxToLIf</a>" : <i>String</i>,
        "<a href="#relationvnsrslifctxtoout" title="RelationVnsRsLIfCtxToOut">RelationVnsRsLIfCtxToOut</a>" : <i>String</i>,
        "<a href="#relationvnsrslifctxtooutdef" title="RelationVnsRsLIfCtxToOutDef">RelationVnsRsLIfCtxToOutDef</a>" : <i>String</i>,
        "<a href="#relationvnsrslifctxtosvcepgpol" title="RelationVnsRsLIfCtxToSvcEPgPol">RelationVnsRsLIfCtxToSvcEPgPol</a>" : <i>String</i>,
        "<a href="#relationvnsrslifctxtosvcredirectpol" title="RelationVnsRsLIfCtxToSvcRedirectPol">RelationVnsRsLIfCtxToSvcRedirectPol</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::LogicalInterfaceContext
Properties:
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#connnameorlbl" title="ConnNameOrLbl">ConnNameOrLbl</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#l3dest" title="L3Dest">L3Dest</a>: <i>String</i>
    <a href="#logicaldevicecontextdn" title="LogicalDeviceContextDn">LogicalDeviceContextDn</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#permitlog" title="PermitLog">PermitLog</a>: <i>String</i>
    <a href="#relationvnsrslifctxtobd" title="RelationVnsRsLIfCtxToBd">RelationVnsRsLIfCtxToBd</a>: <i>String</i>
    <a href="#relationvnsrslifctxtocustqospol" title="RelationVnsRsLIfCtxToCustQosPol">RelationVnsRsLIfCtxToCustQosPol</a>: <i>String</i>
    <a href="#relationvnsrslifctxtoinstp" title="RelationVnsRsLIfCtxToInstP">RelationVnsRsLIfCtxToInstP</a>: <i>String</i>
    <a href="#relationvnsrslifctxtolif" title="RelationVnsRsLIfCtxToLIf">RelationVnsRsLIfCtxToLIf</a>: <i>String</i>
    <a href="#relationvnsrslifctxtoout" title="RelationVnsRsLIfCtxToOut">RelationVnsRsLIfCtxToOut</a>: <i>String</i>
    <a href="#relationvnsrslifctxtooutdef" title="RelationVnsRsLIfCtxToOutDef">RelationVnsRsLIfCtxToOutDef</a>: <i>String</i>
    <a href="#relationvnsrslifctxtosvcepgpol" title="RelationVnsRsLIfCtxToSvcEPgPol">RelationVnsRsLIfCtxToSvcEPgPol</a>: <i>String</i>
    <a href="#relationvnsrslifctxtosvcredirectpol" title="RelationVnsRsLIfCtxToSvcRedirectPol">RelationVnsRsLIfCtxToSvcRedirectPol</a>: <i>String</i>
</pre>

## Properties

#### Annotation

Annotation for object logical_interface_context.
- `l3_dest` - (Optional) Is this LIF a L3 Destination.
Allowed values: "yes", "no". Default is "yes".
- `name_alias` - (Optional) Name alias for object logical_interface_context.
- `permit_log` - (Optional) Permit logging action for object logical_interface_context.
Allowed values: "yes", "no". Default is "no".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnNameOrLbl

The connector name or label for the logical interface context.
- `annotation` - (Optional) Annotation for object logical_interface_context.
- `l3_dest` - (Optional) Is this LIF a L3 Destination.
Allowed values: "yes", "no". Default is "yes".
- `name_alias` - (Optional) Name alias for object logical_interface_context.
- `permit_log` - (Optional) Permit logging action for object logical_interface_context.
Allowed values: "yes", "no". Default is "no".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L3Dest

Is this LIF a L3 Destination.
Allowed values: "yes", "no". Default is "yes".
- `name_alias` - (Optional) Name alias for object logical_interface_context.
- `permit_log` - (Optional) Permit logging action for object logical_interface_context.
Allowed values: "yes", "no". Default is "no".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogicalDeviceContextDn

Distinguished name of parent LogicalDeviceContext object.
- `conn_name_or_lbl` - (Required) The connector name or label for the logical interface context.
- `annotation` - (Optional) Annotation for object logical_interface_context.
- `l3_dest` - (Optional) Is this LIF a L3 Destination.
Allowed values: "yes", "no". Default is "yes".
- `name_alias` - (Optional) Name alias for object logical_interface_context.
- `permit_log` - (Optional) Permit logging action for object logical_interface_context.
Allowed values: "yes", "no". Default is "no".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameAlias

Name alias for object logical_interface_context.
- `permit_log` - (Optional) Permit logging action for object logical_interface_context.
Allowed values: "yes", "no". Default is "no".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermitLog

Permit logging action for object logical_interface_context.
Allowed values: "yes", "no". Default is "no".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVnsRsLIfCtxToBd

Relation to class fvBD. Cardinality - N_TO_ONE. Type - String.
- `relation_vns_rs_l_if_ctx_to_out` - (Optional) Relation to class l3extOut. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVnsRsLIfCtxToCustQosPol

Relation to class qosCustomPol. Cardinality - N_TO_ONE. Type - String.
- `relation_vns_rs_l_if_ctx_to_svc_e_pg_pol` - (Optional) Relation to class vnsSvcEPgPol. Cardinality - N_TO_ONE. Type - String.
- `relation_vns_rs_l_if_ctx_to_svc_redirect_pol` - (Optional) Relation to class vnsSvcRedirectPol. Cardinality - N_TO_ONE. Type - String.
- `relation_vns_rs_l_if_ctx_to_l_if` - (Optional) Relation to class vnsALDevLIf. Cardinality - N_TO_ONE. Type - String.
- `relation_vns_rs_l_if_ctx_to_out_def` - (Optional) Relation to class l3extOutDef. Cardinality - N_TO_ONE. Type - String.
- `relation_vns_rs_l_if_ctx_to_inst_p` - (Optional) Relation to class fvEPg. Cardinality - N_TO_ONE. Type - String.
- `relation_vns_rs_l_if_ctx_to_bd` - (Optional) Relation to class fvBD. Cardinality - N_TO_ONE. Type - String.
- `relation_vns_rs_l_if_ctx_to_out` - (Optional) Relation to class l3extOut. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVnsRsLIfCtxToInstP

Relation to class fvEPg. Cardinality - N_TO_ONE. Type - String.
- `relation_vns_rs_l_if_ctx_to_bd` - (Optional) Relation to class fvBD. Cardinality - N_TO_ONE. Type - String.
- `relation_vns_rs_l_if_ctx_to_out` - (Optional) Relation to class l3extOut. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVnsRsLIfCtxToLIf

Relation to class vnsALDevLIf. Cardinality - N_TO_ONE. Type - String.
- `relation_vns_rs_l_if_ctx_to_out_def` - (Optional) Relation to class l3extOutDef. Cardinality - N_TO_ONE. Type - String.
- `relation_vns_rs_l_if_ctx_to_inst_p` - (Optional) Relation to class fvEPg. Cardinality - N_TO_ONE. Type - String.
- `relation_vns_rs_l_if_ctx_to_bd` - (Optional) Relation to class fvBD. Cardinality - N_TO_ONE. Type - String.
- `relation_vns_rs_l_if_ctx_to_out` - (Optional) Relation to class l3extOut. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVnsRsLIfCtxToOut

Relation to class l3extOut. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVnsRsLIfCtxToOutDef

Relation to class l3extOutDef. Cardinality - N_TO_ONE. Type - String.
- `relation_vns_rs_l_if_ctx_to_inst_p` - (Optional) Relation to class fvEPg. Cardinality - N_TO_ONE. Type - String.
- `relation_vns_rs_l_if_ctx_to_bd` - (Optional) Relation to class fvBD. Cardinality - N_TO_ONE. Type - String.
- `relation_vns_rs_l_if_ctx_to_out` - (Optional) Relation to class l3extOut. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVnsRsLIfCtxToSvcEPgPol

Relation to class vnsSvcEPgPol. Cardinality - N_TO_ONE. Type - String.
- `relation_vns_rs_l_if_ctx_to_svc_redirect_pol` - (Optional) Relation to class vnsSvcRedirectPol. Cardinality - N_TO_ONE. Type - String.
- `relation_vns_rs_l_if_ctx_to_l_if` - (Optional) Relation to class vnsALDevLIf. Cardinality - N_TO_ONE. Type - String.
- `relation_vns_rs_l_if_ctx_to_out_def` - (Optional) Relation to class l3extOutDef. Cardinality - N_TO_ONE. Type - String.
- `relation_vns_rs_l_if_ctx_to_inst_p` - (Optional) Relation to class fvEPg. Cardinality - N_TO_ONE. Type - String.
- `relation_vns_rs_l_if_ctx_to_bd` - (Optional) Relation to class fvBD. Cardinality - N_TO_ONE. Type - String.
- `relation_vns_rs_l_if_ctx_to_out` - (Optional) Relation to class l3extOut. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVnsRsLIfCtxToSvcRedirectPol

Relation to class vnsSvcRedirectPol. Cardinality - N_TO_ONE. Type - String.
- `relation_vns_rs_l_if_ctx_to_l_if` - (Optional) Relation to class vnsALDevLIf. Cardinality - N_TO_ONE. Type - String.
- `relation_vns_rs_l_if_ctx_to_out_def` - (Optional) Relation to class l3extOutDef. Cardinality - N_TO_ONE. Type - String.
- `relation_vns_rs_l_if_ctx_to_inst_p` - (Optional) Relation to class fvEPg. Cardinality - N_TO_ONE. Type - String.
- `relation_vns_rs_l_if_ctx_to_bd` - (Optional) Relation to class fvBD. Cardinality - N_TO_ONE. Type - String.
- `relation_vns_rs_l_if_ctx_to_out` - (Optional) Relation to class l3extOut. Cardinality - N_TO_ONE. Type - String.

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

