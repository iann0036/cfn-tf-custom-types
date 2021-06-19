# TF::VRA::Deployment

This resource provides a way to create a deployment in vRealize Automation(vRA) by either using a blueprint, or catalog item, or an inline blueprint.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::VRA::Deployment",
    "Properties" : {
        "<a href="#blueprintcontent" title="BlueprintContent">BlueprintContent</a>" : <i>String</i>,
        "<a href="#blueprintid" title="BlueprintId">BlueprintId</a>" : <i>String</i>,
        "<a href="#blueprintversion" title="BlueprintVersion">BlueprintVersion</a>" : <i>String</i>,
        "<a href="#catalogitemid" title="CatalogItemId">CatalogItemId</a>" : <i>String</i>,
        "<a href="#catalogitemversion" title="CatalogItemVersion">CatalogItemVersion</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#expandlastrequest" title="ExpandLastRequest">ExpandLastRequest</a>" : <i>Boolean</i>,
        "<a href="#expandproject" title="ExpandProject">ExpandProject</a>" : <i>Boolean</i>,
        "<a href="#expandresources" title="ExpandResources">ExpandResources</a>" : <i>Boolean</i>,
        "<a href="#inputs" title="Inputs">Inputs</a>" : <i>[ <a href="inputsdefinition.md">InputsDefinition</a>, ... ]</i>,
        "<a href="#leaseexpireat" title="LeaseExpireAt">LeaseExpireAt</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#owner" title="Owner">Owner</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::VRA::Deployment
Properties:
    <a href="#blueprintcontent" title="BlueprintContent">BlueprintContent</a>: <i>String</i>
    <a href="#blueprintid" title="BlueprintId">BlueprintId</a>: <i>String</i>
    <a href="#blueprintversion" title="BlueprintVersion">BlueprintVersion</a>: <i>String</i>
    <a href="#catalogitemid" title="CatalogItemId">CatalogItemId</a>: <i>String</i>
    <a href="#catalogitemversion" title="CatalogItemVersion">CatalogItemVersion</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#expandlastrequest" title="ExpandLastRequest">ExpandLastRequest</a>: <i>Boolean</i>
    <a href="#expandproject" title="ExpandProject">ExpandProject</a>: <i>Boolean</i>
    <a href="#expandresources" title="ExpandResources">ExpandResources</a>: <i>Boolean</i>
    <a href="#inputs" title="Inputs">Inputs</a>: <i>
      - <a href="inputsdefinition.md">InputsDefinition</a></i>
    <a href="#leaseexpireat" title="LeaseExpireAt">LeaseExpireAt</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#owner" title="Owner">Owner</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### BlueprintContent

vRA Cloud template content. Conflicts with `blueprint_id` and `catalog_item_id`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlueprintId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlueprintVersion

The version of the vRA cloud template to request the deployment. Used only when `blueprint_id` is provided.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CatalogItemId

The id of the vRA catalog item to request the deployment. Conflicts with `blueprint_id` and `blueprint_content`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CatalogItemVersion

The version of the vRA catalog item to request the deployment. Used only when `catalog_item_id` is provided.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A human-friendly description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpandLastRequest

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpandProject

Flag to indicate whether to expand project information.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpandResources

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Inputs

Inputs provided by the user. For inputs including those with default values, refer to `inputs_including_defaults`.

_Required_: No

_Type_: List of <a href="inputsdefinition.md">InputsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LeaseExpireAt

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A human-friendly name used as an identifier in APIs that support this option.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Owner

The user this deployment belongs to. At create, the owner is ignored but is used to update during next apply.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The id of the project this entity belongs to.

_Required_: Yes

_Type_: String

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

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### CreatedBy

Returns the <code>CreatedBy</code> value.

#### Expense

Returns the <code>Expense</code> value.

#### Id

Returns the <code>Id</code> value.

#### InputsIncludingDefaults

Returns the <code>InputsIncludingDefaults</code> value.

#### LastRequest

Returns the <code>LastRequest</code> value.

#### LastUpdatedAt

Returns the <code>LastUpdatedAt</code> value.

#### LastUpdatedBy

Returns the <code>LastUpdatedBy</code> value.

#### OrgId

The ID of the organization this deployment belongs to.

#### Project

Returns the <code>Project</code> value.

#### Resources

Returns the <code>Resources</code> value.

#### Status

Returns the <code>Status</code> value.

