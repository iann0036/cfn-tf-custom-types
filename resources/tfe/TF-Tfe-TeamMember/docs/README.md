# TF::Tfe::TeamMember

Add or remove a user from a team.

~> **NOTE** on managing team memberships: Terraform currently provides three
resources for managing team memberships.
The [tfe_team_organization_member](team_organization_member.html) resource is
the preferred way. The [tfe_team_member](team_member.html)
resource can be used multiple times as it manages the team membership for a
single user.  The [tfe_team_members](team_members.html) resource, on the other
hand, is used to manage all team memberships for a specific team and can only be
used once. All three resources cannot be used for the same team simultaneously.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Tfe::TeamMember",
    "Properties" : {
        "<a href="#teamid" title="TeamId">TeamId</a>" : <i>String</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Tfe::TeamMember
Properties:
    <a href="#teamid" title="TeamId">TeamId</a>: <i>String</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
</pre>

## Properties

#### TeamId

ID of the team.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

Name of the user to add.

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

