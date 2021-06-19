# TF::PrismaCloud::ComplianceStandardRequirement

Manage a compliance standard requirement.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::PrismaCloud::ComplianceStandardRequirement",
    "Properties" : {
        "<a href="#csid" title="CsId">CsId</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#requirementid" title="RequirementId">RequirementId</a>" : <i>String</i>,
        "<a href="#vieworder" title="ViewOrder">ViewOrder</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::PrismaCloud::ComplianceStandardRequirement
Properties:
    <a href="#csid" title="CsId">CsId</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#requirementid" title="RequirementId">RequirementId</a>: <i>String</i>
    <a href="#vieworder" title="ViewOrder">ViewOrder</a>: <i>Double</i>
</pre>

## Properties

#### CsId

Compliance standard ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Compliance standard requirement name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequirementId

Compliance requirement number.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ViewOrder

View order.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreatedBy

Returns the <code>CreatedBy</code> value.

#### CreatedOn

Returns the <code>CreatedOn</code> value.

#### CsrId

Returns the <code>CsrId</code> value.

#### Id

Returns the <code>Id</code> value.

#### LastModifiedBy

Returns the <code>LastModifiedBy</code> value.

#### LastModifiedOn

Returns the <code>LastModifiedOn</code> value.

#### PoliciesAssignedCount

Returns the <code>PoliciesAssignedCount</code> value.

#### StandardName

Returns the <code>StandardName</code> value.

#### SystemDefault

Returns the <code>SystemDefault</code> value.

