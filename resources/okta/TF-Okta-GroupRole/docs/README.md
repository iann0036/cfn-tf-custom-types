# TF::Okta::GroupRole

Assigns Admin roles to Okta Groups.

This resource allows you to assign Okta administrator roles to Okta Groups. This resource provides a one-to-one
interface between the Okta group and the admin role.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Okta::GroupRole",
    "Properties" : {
        "<a href="#groupid" title="GroupId">GroupId</a>" : <i>String</i>,
        "<a href="#roletype" title="RoleType">RoleType</a>" : <i>String</i>,
        "<a href="#targetapplist" title="TargetAppList">TargetAppList</a>" : <i>[ String, ... ]</i>,
        "<a href="#targetgrouplist" title="TargetGroupList">TargetGroupList</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Okta::GroupRole
Properties:
    <a href="#groupid" title="GroupId">GroupId</a>: <i>String</i>
    <a href="#roletype" title="RoleType">RoleType</a>: <i>String</i>
    <a href="#targetapplist" title="TargetAppList">TargetAppList</a>: <i>
      - String</i>
    <a href="#targetgrouplist" title="TargetGroupList">TargetGroupList</a>: <i>
      - String</i>
</pre>

## Properties

#### GroupId

The ID of group to attach admin roles to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleType

Admin role assigned to the group. It can be any one of the following values `"SUPER_ADMIN"`
, `"ORG_ADMIN"`, `"APP_ADMIN"`, `"USER_ADMIN"`, `"HELP_DESK_ADMIN"`, `"READ_ONLY_ADMIN"`
, `"MOBILE_ADMIN"`, `"API_ACCESS_MANAGEMENT_ADMIN"`, `"REPORT_ADMIN"`, `"GROUP_MEMBERSHIP_ADMIN"`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetAppList

A list of app names (name represents set of app instances, like 'salesforce' or '
facebook'), or a combination of app name and app instance ID (like 'facebook.0oapsqQ6dv19pqyEo0g3') you would like as
the targets of the admin role.
- Only supported when used with the role type `"APP_ADMIN"`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetGroupList

A list of group IDs you would like as the targets of the admin role.
- Only supported when used with the role types: `GROUP_MEMBERSHIP_ADMIN`, `HELP_DESK_ADMIN`, or `USER_ADMIN`.

_Required_: No

_Type_: List of String

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

