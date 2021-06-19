# TF::PagerDuty::TeamMembership

A [team membership](https://v2.developer.pagerduty.com/v2/page/api-reference#!/Teams/put_teams_id_users_user_id) manages memberships within a team.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::PagerDuty::TeamMembership",
    "Properties" : {
        "<a href="#role" title="Role">Role</a>" : <i>String</i>,
        "<a href="#teamid" title="TeamId">TeamId</a>" : <i>String</i>,
        "<a href="#userid" title="UserId">UserId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::PagerDuty::TeamMembership
Properties:
    <a href="#role" title="Role">Role</a>: <i>String</i>
    <a href="#teamid" title="TeamId">TeamId</a>: <i>String</i>
    <a href="#userid" title="UserId">UserId</a>: <i>String</i>
</pre>

## Properties

#### Role

The role of the user in the team. One of `observer`, `responder`, or `manager`. Defaults to `manager`.
These roles match up to user roles in the following ways:
* User role of `user` is a Team role of `manager`
* User role of `limited_user` is a Team role of `responder`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TeamId

The ID of the team in which the user will belong.
* `role`    - (Optional) The role of the user in the team. One of `observer`, `responder`, or `manager`. Defaults to `manager`.
These roles match up to user roles in the following ways:
* User role of `user` is a Team role of `manager`
* User role of `limited_user` is a Team role of `responder`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserId

The ID of the user to add to the team.
* `team_id` - (Required) The ID of the team in which the user will belong.
* `role`    - (Optional) The role of the user in the team. One of `observer`, `responder`, or `manager`. Defaults to `manager`.
These roles match up to user roles in the following ways:
* User role of `user` is a Team role of `manager`
* User role of `limited_user` is a Team role of `responder`.

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

