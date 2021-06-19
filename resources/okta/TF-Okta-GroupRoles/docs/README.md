# TF::Okta::GroupRoles

Creates Group level Admin Role Assignments.

This resource allows you to create and configure Group level Admin Role Assignments.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Okta::GroupRoles",
    "Properties" : {
        "<a href="#adminroles" title="AdminRoles">AdminRoles</a>" : <i>[ String, ... ]</i>,
        "<a href="#groupid" title="GroupId">GroupId</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Okta::GroupRoles
Properties:
    <a href="#adminroles" title="AdminRoles">AdminRoles</a>: <i>
      - String</i>
    <a href="#groupid" title="GroupId">GroupId</a>: <i>String</i>
</pre>

## Properties

#### AdminRoles

Admin roles associated with the group. It can be any of the following values `"SUPER_ADMIN"`, `"ORG_ADMIN"`, `"APP_ADMIN"`, `"USER_ADMIN"`, `"HELP_DESK_ADMIN"`, `"READ_ONLY_ADMIN"`, `"MOBILE_ADMIN"`, `"API_ACCESS_MANAGEMENT_ADMIN"`, `"REPORT_ADMIN"`, `"GROUP_MEMBERSHIP_ADMIN"`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupId

The ID of group to attach admin roles to.

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

