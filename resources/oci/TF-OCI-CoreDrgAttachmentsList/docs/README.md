# TF::OCI::CoreDrgAttachmentsList

This resource provides the Drg Attachments List resource in Oracle Cloud Infrastructure Core service.

Returns a complete list of DRG attachments that belong to a particular DRG.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::CoreDrgAttachmentsList",
    "Properties" : {
        "<a href="#attachmenttype" title="AttachmentType">AttachmentType</a>" : <i>String</i>,
        "<a href="#drgid" title="DrgId">DrgId</a>" : <i>String</i>,
        "<a href="#iscrosstenancy" title="IsCrossTenancy">IsCrossTenancy</a>" : <i>Boolean</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::CoreDrgAttachmentsList
Properties:
    <a href="#attachmenttype" title="AttachmentType">AttachmentType</a>: <i>String</i>
    <a href="#drgid" title="DrgId">DrgId</a>: <i>String</i>
    <a href="#iscrosstenancy" title="IsCrossTenancy">IsCrossTenancy</a>: <i>Boolean</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AttachmentType

The type for the network resource attached to the DRG.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DrgId

The [[OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsCrossTenancy

Whether the DRG attachment lives in a different tenancy than the DRG.

_Required_: No

_Type_: Boolean

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

#### DrgAllAttachments

Returns the <code>DrgAllAttachments</code> value.

#### Id

Returns the <code>Id</code> value.

