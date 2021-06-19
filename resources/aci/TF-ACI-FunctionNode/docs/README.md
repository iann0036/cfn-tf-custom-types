# TF::ACI::FunctionNode

Manages ACI Function Node

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::FunctionNode",
    "Properties" : {
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#connconsumerdn" title="ConnConsumerDn">ConnConsumerDn</a>" : <i>String</i>,
        "<a href="#connproviderdn" title="ConnProviderDn">ConnProviderDn</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#functemplatetype" title="FuncTemplateType">FuncTemplateType</a>" : <i>String</i>,
        "<a href="#functype" title="FuncType">FuncType</a>" : <i>String</i>,
        "<a href="#iscopy" title="IsCopy">IsCopy</a>" : <i>String</i>,
        "<a href="#l4l7servicegraphtemplatedn" title="L4L7ServiceGraphTemplateDn">L4L7ServiceGraphTemplateDn</a>" : <i>String</i>,
        "<a href="#managed" title="Managed">Managed</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#relationvnsrsdefaultscopetoterm" title="RelationVnsRsDefaultScopeToTerm">RelationVnsRsDefaultScopeToTerm</a>" : <i>String</i>,
        "<a href="#relationvnsrsnodetoabsfuncprof" title="RelationVnsRsNodeToAbsFuncProf">RelationVnsRsNodeToAbsFuncProf</a>" : <i>String</i>,
        "<a href="#relationvnsrsnodetocloudldev" title="RelationVnsRsNodeToCloudLDev">RelationVnsRsNodeToCloudLDev</a>" : <i>String</i>,
        "<a href="#relationvnsrsnodetoldev" title="RelationVnsRsNodeToLDev">RelationVnsRsNodeToLDev</a>" : <i>String</i>,
        "<a href="#relationvnsrsnodetomfunc" title="RelationVnsRsNodeToMFunc">RelationVnsRsNodeToMFunc</a>" : <i>String</i>,
        "<a href="#routingmode" title="RoutingMode">RoutingMode</a>" : <i>String</i>,
        "<a href="#sequencenumber" title="SequenceNumber">SequenceNumber</a>" : <i>String</i>,
        "<a href="#shareencap" title="ShareEncap">ShareEncap</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::FunctionNode
Properties:
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#connconsumerdn" title="ConnConsumerDn">ConnConsumerDn</a>: <i>String</i>
    <a href="#connproviderdn" title="ConnProviderDn">ConnProviderDn</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#functemplatetype" title="FuncTemplateType">FuncTemplateType</a>: <i>String</i>
    <a href="#functype" title="FuncType">FuncType</a>: <i>String</i>
    <a href="#iscopy" title="IsCopy">IsCopy</a>: <i>String</i>
    <a href="#l4l7servicegraphtemplatedn" title="L4L7ServiceGraphTemplateDn">L4L7ServiceGraphTemplateDn</a>: <i>String</i>
    <a href="#managed" title="Managed">Managed</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#relationvnsrsdefaultscopetoterm" title="RelationVnsRsDefaultScopeToTerm">RelationVnsRsDefaultScopeToTerm</a>: <i>String</i>
    <a href="#relationvnsrsnodetoabsfuncprof" title="RelationVnsRsNodeToAbsFuncProf">RelationVnsRsNodeToAbsFuncProf</a>: <i>String</i>
    <a href="#relationvnsrsnodetocloudldev" title="RelationVnsRsNodeToCloudLDev">RelationVnsRsNodeToCloudLDev</a>: <i>String</i>
    <a href="#relationvnsrsnodetoldev" title="RelationVnsRsNodeToLDev">RelationVnsRsNodeToLDev</a>: <i>String</i>
    <a href="#relationvnsrsnodetomfunc" title="RelationVnsRsNodeToMFunc">RelationVnsRsNodeToMFunc</a>: <i>String</i>
    <a href="#routingmode" title="RoutingMode">RoutingMode</a>: <i>String</i>
    <a href="#sequencenumber" title="SequenceNumber">SequenceNumber</a>: <i>String</i>
    <a href="#shareencap" title="ShareEncap">ShareEncap</a>: <i>String</i>
</pre>

## Properties

#### Annotation

Annotation for object function_node.
- `func_template_type` - (Optional) func_template_type for object function_node.
Allowed values: "OTHER", "FW_TRANS", "FW_ROUTED", "CLOUD_VENDOR_LB", "CLOUD_VENDOR_FW", "CLOUD_NATIVE_LB", "CLOUD_NATIVE_FW", "ADC_TWO_ARM", "ADC_ONE_ARM". Default value: "OTHER".
- `func_type` - (Optional) A function type. A GoThrough node is a transparent device, where a packet goes through without being addressed to the device, and the endpoints are not aware of that device. A GoTo device has a specific destination.
Allowed values: "GoThrough", "GoTo", "L1", "L2", "None". Default value: "GoTo".
- `is_copy` - (Optional) if the device is a copy device.
Allowed values: "yes", "no". Default value: "no".
- `managed` - (Optional) Specified if the function is using a managed device.
Allowed values: "yes", "no". Default value: "yes".
- `name_alias` - (Optional) name_alias for object function_node.
- `routing_mode` - (Optional) Routing_mode for object function_node.
Allowed values: "Redirect", "unspecified". Default value: "unspecified".
- `sequence_number` - (Optional) Internal property incremented when aaa user logs in.
- `share_encap` - (Optional) Enables encap sharing on node.
Allowed values: "yes", "no". Default value: "no".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnConsumerDn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnProviderDn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FuncTemplateType

func_template_type for object function_node.
Allowed values: "OTHER", "FW_TRANS", "FW_ROUTED", "CLOUD_VENDOR_LB", "CLOUD_VENDOR_FW", "CLOUD_NATIVE_LB", "CLOUD_NATIVE_FW", "ADC_TWO_ARM", "ADC_ONE_ARM". Default value: "OTHER".
- `func_type` - (Optional) A function type. A GoThrough node is a transparent device, where a packet goes through without being addressed to the device, and the endpoints are not aware of that device. A GoTo device has a specific destination.
Allowed values: "GoThrough", "GoTo", "L1", "L2", "None". Default value: "GoTo".
- `is_copy` - (Optional) if the device is a copy device.
Allowed values: "yes", "no". Default value: "no".
- `managed` - (Optional) Specified if the function is using a managed device.
Allowed values: "yes", "no". Default value: "yes".
- `name_alias` - (Optional) name_alias for object function_node.
- `routing_mode` - (Optional) Routing_mode for object function_node.
Allowed values: "Redirect", "unspecified". Default value: "unspecified".
- `sequence_number` - (Optional) Internal property incremented when aaa user logs in.
- `share_encap` - (Optional) Enables encap sharing on node.
Allowed values: "yes", "no". Default value: "no".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FuncType

A function type. A GoThrough node is a transparent device, where a packet goes through without being addressed to the device, and the endpoints are not aware of that device. A GoTo device has a specific destination.
Allowed values: "GoThrough", "GoTo", "L1", "L2", "None". Default value: "GoTo".
- `is_copy` - (Optional) if the device is a copy device.
Allowed values: "yes", "no". Default value: "no".
- `managed` - (Optional) Specified if the function is using a managed device.
Allowed values: "yes", "no". Default value: "yes".
- `name_alias` - (Optional) name_alias for object function_node.
- `routing_mode` - (Optional) Routing_mode for object function_node.
Allowed values: "Redirect", "unspecified". Default value: "unspecified".
- `sequence_number` - (Optional) Internal property incremented when aaa user logs in.
- `share_encap` - (Optional) Enables encap sharing on node.
Allowed values: "yes", "no". Default value: "no".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsCopy

if the device is a copy device.
Allowed values: "yes", "no". Default value: "no".
- `managed` - (Optional) Specified if the function is using a managed device.
Allowed values: "yes", "no". Default value: "yes".
- `name_alias` - (Optional) name_alias for object function_node.
- `routing_mode` - (Optional) Routing_mode for object function_node.
Allowed values: "Redirect", "unspecified". Default value: "unspecified".
- `sequence_number` - (Optional) Internal property incremented when aaa user logs in.
- `share_encap` - (Optional) Enables encap sharing on node.
Allowed values: "yes", "no". Default value: "no".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L4L7ServiceGraphTemplateDn

Distinguished name of parent L4-L7 Service Graph Template object.
- `name` - (Required) name of Object function_node.
- `annotation` - (Optional) Annotation for object function_node.
- `func_template_type` - (Optional) func_template_type for object function_node.
Allowed values: "OTHER", "FW_TRANS", "FW_ROUTED", "CLOUD_VENDOR_LB", "CLOUD_VENDOR_FW", "CLOUD_NATIVE_LB", "CLOUD_NATIVE_FW", "ADC_TWO_ARM", "ADC_ONE_ARM". Default value: "OTHER".
- `func_type` - (Optional) A function type. A GoThrough node is a transparent device, where a packet goes through without being addressed to the device, and the endpoints are not aware of that device. A GoTo device has a specific destination.
Allowed values: "GoThrough", "GoTo", "L1", "L2", "None". Default value: "GoTo".
- `is_copy` - (Optional) if the device is a copy device.
Allowed values: "yes", "no". Default value: "no".
- `managed` - (Optional) Specified if the function is using a managed device.
Allowed values: "yes", "no". Default value: "yes".
- `name_alias` - (Optional) name_alias for object function_node.
- `routing_mode` - (Optional) Routing_mode for object function_node.
Allowed values: "Redirect", "unspecified". Default value: "unspecified".
- `sequence_number` - (Optional) Internal property incremented when aaa user logs in.
- `share_encap` - (Optional) Enables encap sharing on node.
Allowed values: "yes", "no". Default value: "no".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Managed

Specified if the function is using a managed device.
Allowed values: "yes", "no". Default value: "yes".
- `name_alias` - (Optional) name_alias for object function_node.
- `routing_mode` - (Optional) Routing_mode for object function_node.
Allowed values: "Redirect", "unspecified". Default value: "unspecified".
- `sequence_number` - (Optional) Internal property incremented when aaa user logs in.
- `share_encap` - (Optional) Enables encap sharing on node.
Allowed values: "yes", "no". Default value: "no".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

name of Object function_node.
- `annotation` - (Optional) Annotation for object function_node.
- `func_template_type` - (Optional) func_template_type for object function_node.
Allowed values: "OTHER", "FW_TRANS", "FW_ROUTED", "CLOUD_VENDOR_LB", "CLOUD_VENDOR_FW", "CLOUD_NATIVE_LB", "CLOUD_NATIVE_FW", "ADC_TWO_ARM", "ADC_ONE_ARM". Default value: "OTHER".
- `func_type` - (Optional) A function type. A GoThrough node is a transparent device, where a packet goes through without being addressed to the device, and the endpoints are not aware of that device. A GoTo device has a specific destination.
Allowed values: "GoThrough", "GoTo", "L1", "L2", "None". Default value: "GoTo".
- `is_copy` - (Optional) if the device is a copy device.
Allowed values: "yes", "no". Default value: "no".
- `managed` - (Optional) Specified if the function is using a managed device.
Allowed values: "yes", "no". Default value: "yes".
- `name_alias` - (Optional) name_alias for object function_node.
- `routing_mode` - (Optional) Routing_mode for object function_node.
Allowed values: "Redirect", "unspecified". Default value: "unspecified".
- `sequence_number` - (Optional) Internal property incremented when aaa user logs in.
- `share_encap` - (Optional) Enables encap sharing on node.
Allowed values: "yes", "no". Default value: "no".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameAlias

name_alias for object function_node.
- `routing_mode` - (Optional) Routing_mode for object function_node.
Allowed values: "Redirect", "unspecified". Default value: "unspecified".
- `sequence_number` - (Optional) Internal property incremented when aaa user logs in.
- `share_encap` - (Optional) Enables encap sharing on node.
Allowed values: "yes", "no". Default value: "no".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVnsRsDefaultScopeToTerm

Relation to class vnsATerm. Cardinality - ONE_TO_ONE. Type - String.
- `relation_vns_rs_node_to_cloud_l_dev` - (Optional) Relation to class cloudALDev. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVnsRsNodeToAbsFuncProf

Relation to class vnsAbsFuncProf. Cardinality - N_TO_ONE. Type - String.
- `relation_vns_rs_node_to_l_dev` - (Optional) Relation to class vnsALDevIf. Cardinality - N_TO_ONE. Type - String.
- `relation_vns_rs_node_to_m_func` - (Optional) Relation to class vnsMFunc. Cardinality - N_TO_ONE. Type - String.
- `relation_vns_rs_default_scope_to_term` - (Optional) Relation to class vnsATerm. Cardinality - ONE_TO_ONE. Type - String.
- `relation_vns_rs_node_to_cloud_l_dev` - (Optional) Relation to class cloudALDev. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVnsRsNodeToCloudLDev

Relation to class cloudALDev. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVnsRsNodeToLDev

Relation to class vnsALDevIf. Cardinality - N_TO_ONE. Type - String.
- `relation_vns_rs_node_to_m_func` - (Optional) Relation to class vnsMFunc. Cardinality - N_TO_ONE. Type - String.
- `relation_vns_rs_default_scope_to_term` - (Optional) Relation to class vnsATerm. Cardinality - ONE_TO_ONE. Type - String.
- `relation_vns_rs_node_to_cloud_l_dev` - (Optional) Relation to class cloudALDev. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationVnsRsNodeToMFunc

Relation to class vnsMFunc. Cardinality - N_TO_ONE. Type - String.
- `relation_vns_rs_default_scope_to_term` - (Optional) Relation to class vnsATerm. Cardinality - ONE_TO_ONE. Type - String.
- `relation_vns_rs_node_to_cloud_l_dev` - (Optional) Relation to class cloudALDev. Cardinality - N_TO_ONE. Type - String.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoutingMode

Routing_mode for object function_node.
Allowed values: "Redirect", "unspecified". Default value: "unspecified".
- `sequence_number` - (Optional) Internal property incremented when aaa user logs in.
- `share_encap` - (Optional) Enables encap sharing on node.
Allowed values: "yes", "no". Default value: "no".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SequenceNumber

Internal property incremented when aaa user logs in.
- `share_encap` - (Optional) Enables encap sharing on node.
Allowed values: "yes", "no". Default value: "no".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShareEncap

Enables encap sharing on node.
Allowed values: "yes", "no". Default value: "no".

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

