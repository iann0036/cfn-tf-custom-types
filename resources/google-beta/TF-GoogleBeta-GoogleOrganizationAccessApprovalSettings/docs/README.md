# TF::GoogleBeta::GoogleOrganizationAccessApprovalSettings

CloudFormation equivalent of google_organization_access_approval_settings

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GoogleBeta::GoogleOrganizationAccessApprovalSettings",
    "Properties" : {
        "<a href="#notificationemails" title="NotificationEmails">NotificationEmails</a>" : <i>[ String, ... ]</i>,
        "<a href="#organizationid" title="OrganizationId">OrganizationId</a>" : <i>String</i>,
        "<a href="#enrolledservices" title="EnrolledServices">EnrolledServices</a>" : <i>[ <a href="enrolledservicesdefinition.md">EnrolledServicesDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GoogleBeta::GoogleOrganizationAccessApprovalSettings
Properties:
    <a href="#notificationemails" title="NotificationEmails">NotificationEmails</a>: <i>
      - String</i>
    <a href="#organizationid" title="OrganizationId">OrganizationId</a>: <i>String</i>
    <a href="#enrolledservices" title="EnrolledServices">EnrolledServices</a>: <i>
      - <a href="enrolledservicesdefinition.md">EnrolledServicesDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### NotificationEmails

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrganizationId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnrolledServices

_Required_: No

_Type_: List of <a href="enrolledservicesdefinition.md">EnrolledServicesDefinition</a>

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

#### EnrolledAncestor

Returns the <code>EnrolledAncestor</code> value.

#### Id

Returns the <code>Id</code> value.

#### Name

Returns the <code>Name</code> value.

