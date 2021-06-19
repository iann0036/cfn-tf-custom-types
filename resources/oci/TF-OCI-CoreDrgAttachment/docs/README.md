# TF::OCI::CoreDrgAttachment

This resource provides the Drg Attachment resource in Oracle Cloud Infrastructure Core service.

Attaches the specified DRG to the specified network resource. A VCN can be attached to only one DRG
at a time, but a DRG can be attached to more than one VCN. The response includes a `DrgAttachment`
object with its own [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm). For more information about DRGs, see
[Dynamic Routing Gateways (DRGs)](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingDRGs.htm).

You may optionally specify a *display name* for the attachment, otherwise a default is provided.
It does not have to be unique, and you can change it. Avoid entering confidential information.

For the purposes of access control, the DRG attachment is automatically placed into the currently selected compartment.
For more information about compartments and access control, see
[Overview of the IAM Service](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/ove...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::CoreDrgAttachment",
    "Properties" : {
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#drgid" title="DrgId">DrgId</a>" : <i>String</i>,
        "<a href="#drgroutetableid" title="DrgRouteTableId">DrgRouteTableId</a>" : <i>String</i>,
        "<a href="#exportdrgroutedistributionid" title="ExportDrgRouteDistributionId">ExportDrgRouteDistributionId</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>, ... ]</i>,
        "<a href="#removeexportdrgroutedistributiontrigger" title="RemoveExportDrgRouteDistributionTrigger">RemoveExportDrgRouteDistributionTrigger</a>" : <i>Boolean</i>,
        "<a href="#routetableid" title="RouteTableId">RouteTableId</a>" : <i>String</i>,
        "<a href="#vcnid" title="VcnId">VcnId</a>" : <i>String</i>,
        "<a href="#networkdetails" title="NetworkDetails">NetworkDetails</a>" : <i>[ <a href="networkdetailsdefinition.md">NetworkDetailsDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::CoreDrgAttachment
Properties:
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtagsdefinition.md">DefinedTagsDefinition</a></i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#drgid" title="DrgId">DrgId</a>: <i>String</i>
    <a href="#drgroutetableid" title="DrgRouteTableId">DrgRouteTableId</a>: <i>String</i>
    <a href="#exportdrgroutedistributionid" title="ExportDrgRouteDistributionId">ExportDrgRouteDistributionId</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a></i>
    <a href="#removeexportdrgroutedistributiontrigger" title="RemoveExportDrgRouteDistributionTrigger">RemoveExportDrgRouteDistributionTrigger</a>: <i>Boolean</i>
    <a href="#routetableid" title="RouteTableId">RouteTableId</a>: <i>String</i>
    <a href="#vcnid" title="VcnId">VcnId</a>: <i>String</i>
    <a href="#networkdetails" title="NetworkDetails">NetworkDetails</a>: <i>
      - <a href="networkdetailsdefinition.md">NetworkDetailsDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### DefinedTags

(Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

_Required_: No

_Type_: List of <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

(Updatable) A user-friendly name. Does not have to be unique. Avoid entering confidential information.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DrgId

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DrgRouteTableId

(Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG route table that is assigned to this attachment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExportDrgRouteDistributionId

(Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the export route distribution used to specify how routes in the assigned DRG route table are advertised to the attachment. If this value is null, no routes are advertised through this attachment.
This field cannot be set by the user while creating the resource and gets a default value on creation. This can be only be updated to its default value. If this fields needs to be set to null, remove_export_drg_route_distribution_trigger needs to be used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

(Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

_Required_: No

_Type_: List of <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoveExportDrgRouteDistributionTrigger

(Updatable) An optional property when set to true during update disables the export of route Distribution by setting export_drg_route_distribution_id to null.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteTableId

(Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the route table used by the DRG attachment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VcnId

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN. This field is deprecated. Instead, use the `networkDetails` field to specify the [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the attached resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkDetails

_Required_: No

_Type_: List of <a href="networkdetailsdefinition.md">NetworkDetailsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CompartmentId

Returns the <code>CompartmentId</code> value.

#### Id

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the network attached to the DRG.
* `route_table_id` - (Optional) (Updatable) This is the [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the route table that is used to route the traffic as it enters a VCN through this attachment.

#### IsCrossTenancy

Returns the <code>IsCrossTenancy</code> value.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

