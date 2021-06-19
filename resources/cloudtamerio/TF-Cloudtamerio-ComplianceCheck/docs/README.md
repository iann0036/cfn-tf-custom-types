# TF::Cloudtamerio::ComplianceCheck

CloudFormation equivalent of cloudtamerio_compliance_check

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Cloudtamerio::ComplianceCheck",
    "Properties" : {
        "<a href="#azurepolicyid" title="AzurePolicyId">AzurePolicyId</a>" : <i>Double</i>,
        "<a href="#body" title="Body">Body</a>" : <i>String</i>,
        "<a href="#cloudproviderid" title="CloudProviderId">CloudProviderId</a>" : <i>Double</i>,
        "<a href="#compliancechecktypeid" title="ComplianceCheckTypeId">ComplianceCheckTypeId</a>" : <i>Double</i>,
        "<a href="#createdbyuserid" title="CreatedByUserId">CreatedByUserId</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#frequencyminutes" title="FrequencyMinutes">FrequencyMinutes</a>" : <i>Double</i>,
        "<a href="#frequencytypeid" title="FrequencyTypeId">FrequencyTypeId</a>" : <i>Double</i>,
        "<a href="#isallregions" title="IsAllRegions">IsAllRegions</a>" : <i>Boolean</i>,
        "<a href="#isautoarchived" title="IsAutoArchived">IsAutoArchived</a>" : <i>Boolean</i>,
        "<a href="#lastupdated" title="LastUpdated">LastUpdated</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#regions" title="Regions">Regions</a>" : <i>[ String, ... ]</i>,
        "<a href="#severitytypeid" title="SeverityTypeId">SeverityTypeId</a>" : <i>Double</i>,
        "<a href="#ownerusergroups" title="OwnerUserGroups">OwnerUserGroups</a>" : <i>[ <a href="ownerusergroupsdefinition.md">OwnerUserGroupsDefinition</a>, ... ]</i>,
        "<a href="#ownerusers" title="OwnerUsers">OwnerUsers</a>" : <i>[ <a href="ownerusersdefinition.md">OwnerUsersDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Cloudtamerio::ComplianceCheck
Properties:
    <a href="#azurepolicyid" title="AzurePolicyId">AzurePolicyId</a>: <i>Double</i>
    <a href="#body" title="Body">Body</a>: <i>String</i>
    <a href="#cloudproviderid" title="CloudProviderId">CloudProviderId</a>: <i>Double</i>
    <a href="#compliancechecktypeid" title="ComplianceCheckTypeId">ComplianceCheckTypeId</a>: <i>Double</i>
    <a href="#createdbyuserid" title="CreatedByUserId">CreatedByUserId</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#frequencyminutes" title="FrequencyMinutes">FrequencyMinutes</a>: <i>Double</i>
    <a href="#frequencytypeid" title="FrequencyTypeId">FrequencyTypeId</a>: <i>Double</i>
    <a href="#isallregions" title="IsAllRegions">IsAllRegions</a>: <i>Boolean</i>
    <a href="#isautoarchived" title="IsAutoArchived">IsAutoArchived</a>: <i>Boolean</i>
    <a href="#lastupdated" title="LastUpdated">LastUpdated</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#regions" title="Regions">Regions</a>: <i>
      - String</i>
    <a href="#severitytypeid" title="SeverityTypeId">SeverityTypeId</a>: <i>Double</i>
    <a href="#ownerusergroups" title="OwnerUserGroups">OwnerUserGroups</a>: <i>
      - <a href="ownerusergroupsdefinition.md">OwnerUserGroupsDefinition</a></i>
    <a href="#ownerusers" title="OwnerUsers">OwnerUsers</a>: <i>
      - <a href="ownerusersdefinition.md">OwnerUsersDefinition</a></i>
</pre>

## Properties

#### AzurePolicyId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Body

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudProviderId

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComplianceCheckTypeId

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreatedByUserId

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrequencyMinutes

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrequencyTypeId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsAllRegions

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsAutoArchived

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LastUpdated

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Regions

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeverityTypeId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OwnerUserGroups

_Required_: No

_Type_: List of <a href="ownerusergroupsdefinition.md">OwnerUserGroupsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OwnerUsers

_Required_: No

_Type_: List of <a href="ownerusersdefinition.md">OwnerUsersDefinition</a>

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

#### CtManaged

Returns the <code>CtManaged</code> value.

#### Id

Returns the <code>Id</code> value.

#### LastScanId

Returns the <code>LastScanId</code> value.

