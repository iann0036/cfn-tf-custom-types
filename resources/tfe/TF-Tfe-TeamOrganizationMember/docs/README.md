# TF::Tfe::TeamOrganizationMember

Add or remove a team member using a
[tfe_organization_membership](organization_membership.html).

~> **NOTE** on managing team memberships: Terraform currently provides three
resources for managing team memberships. This is the preferred method as it
allows you to add a member to a team by email address.

~> **NOTE:** This resource requires using the provider with Terraform Cloud or
an instance of Terraform Enterprise at least as recent as v202004-1.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Tfe::TeamOrganizationMember",
    "Properties" : {
        "<a href="#organizationmembershipid" title="OrganizationMembershipId">OrganizationMembershipId</a>" : <i>String</i>,
        "<a href="#teamid" title="TeamId">TeamId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Tfe::TeamOrganizationMember
Properties:
    <a href="#organizationmembershipid" title="OrganizationMembershipId">OrganizationMembershipId</a>: <i>String</i>
    <a href="#teamid" title="TeamId">TeamId</a>: <i>String</i>
</pre>

## Properties

#### OrganizationMembershipId

ID of the organization membership.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TeamId

ID of the team.

_Required_: Yes

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

