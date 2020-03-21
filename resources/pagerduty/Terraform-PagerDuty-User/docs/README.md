# Terraform::PagerDuty::User

A [user](https://v2.developer.pagerduty.com/v2/page/api-reference#!/Users/get_users) is a member of a PagerDuty account that have the ability to interact with incidents and other data on the account.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::PagerDuty::User",
    "Properties" : {
        "<a href="#color" title="Color">Color</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#email" title="Email">Email</a>" : <i>String</i>,
        "<a href="#jobtitle" title="JobTitle">JobTitle</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#role" title="Role">Role</a>" : <i>String</i>,
        "<a href="#teams" title="Teams">Teams</a>" : <i>[ String, ... ]</i>,
        "<a href="#timezone" title="TimeZone">TimeZone</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::PagerDuty::User
Properties:
    <a href="#color" title="Color">Color</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#email" title="Email">Email</a>: <i>String</i>
    <a href="#jobtitle" title="JobTitle">JobTitle</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#role" title="Role">Role</a>: <i>String</i>
    <a href="#teams" title="Teams">Teams</a>: <i>
      - String</i>
    <a href="#timezone" title="TimeZone">TimeZone</a>: <i>String</i>
</pre>

## Properties

#### Color

The schedule color for the user. Valid options are purple, red, green, blue, teal, orange, brown, turquoise, dark-slate-blue, cayenne, orange-red, dark-orchid, dark-slate-grey, lime, dark-magenta, lime-green, midnight-blue, deep-pink, dark-green, dark-orange, dark-cyan, darkolive-green, dark-slate-gray, grey20, firebrick, maroon, crimson, dark-red, dark-goldenrod, chocolate, medium-violet-red, sea-green, olivedrab, forest-green, dark-olive-green, blue-violet, royal-blue, indigo, slate-blue, saddle-brown, or steel-blue.
* `role` - (Optional) The user role. Account must have the `read_only_users` ability to set a user as a `read_only_user`. Can be `admin`, `limited_user`, `observer`, `owner`, `read_only_user` or `user`
* `job_title` - (Optional) The user's title.
* `teams` - (Optional, **DEPRECATED**) A list of teams the user should belong to. Please use `pagerduty_team_membership` instead.
* `description` - (Optional) A human-friendly description of the user.
If not set, a placeholder of "Managed by Terraform" will be set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A human-friendly description of the user.
If not set, a placeholder of "Managed by Terraform" will be set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

The user's email address.
* `color` - (Optional) The schedule color for the user. Valid options are purple, red, green, blue, teal, orange, brown, turquoise, dark-slate-blue, cayenne, orange-red, dark-orchid, dark-slate-grey, lime, dark-magenta, lime-green, midnight-blue, deep-pink, dark-green, dark-orange, dark-cyan, darkolive-green, dark-slate-gray, grey20, firebrick, maroon, crimson, dark-red, dark-goldenrod, chocolate, medium-violet-red, sea-green, olivedrab, forest-green, dark-olive-green, blue-violet, royal-blue, indigo, slate-blue, saddle-brown, or steel-blue.
* `role` - (Optional) The user role. Account must have the `read_only_users` ability to set a user as a `read_only_user`. Can be `admin`, `limited_user`, `observer`, `owner`, `read_only_user` or `user`
* `job_title` - (Optional) The user's title.
* `teams` - (Optional, **DEPRECATED**) A list of teams the user should belong to. Please use `pagerduty_team_membership` instead.
* `description` - (Optional) A human-friendly description of the user.
If not set, a placeholder of "Managed by Terraform" will be set.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JobTitle

The user's title.
* `teams` - (Optional, **DEPRECATED**) A list of teams the user should belong to. Please use `pagerduty_team_membership` instead.
* `description` - (Optional) A human-friendly description of the user.
If not set, a placeholder of "Managed by Terraform" will be set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the user.
* `email` - (Required) The user's email address.
* `color` - (Optional) The schedule color for the user. Valid options are purple, red, green, blue, teal, orange, brown, turquoise, dark-slate-blue, cayenne, orange-red, dark-orchid, dark-slate-grey, lime, dark-magenta, lime-green, midnight-blue, deep-pink, dark-green, dark-orange, dark-cyan, darkolive-green, dark-slate-gray, grey20, firebrick, maroon, crimson, dark-red, dark-goldenrod, chocolate, medium-violet-red, sea-green, olivedrab, forest-green, dark-olive-green, blue-violet, royal-blue, indigo, slate-blue, saddle-brown, or steel-blue.
* `role` - (Optional) The user role. Account must have the `read_only_users` ability to set a user as a `read_only_user`. Can be `admin`, `limited_user`, `observer`, `owner`, `read_only_user` or `user`
* `job_title` - (Optional) The user's title.
* `teams` - (Optional, **DEPRECATED**) A list of teams the user should belong to. Please use `pagerduty_team_membership` instead.
* `description` - (Optional) A human-friendly description of the user.
If not set, a placeholder of "Managed by Terraform" will be set.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

The user role. Account must have the `read_only_users` ability to set a user as a `read_only_user`. Can be `admin`, `limited_user`, `observer`, `owner`, `read_only_user` or `user`
* `job_title` - (Optional) The user's title.
* `teams` - (Optional, **DEPRECATED**) A list of teams the user should belong to. Please use `pagerduty_team_membership` instead.
* `description` - (Optional) A human-friendly description of the user.
If not set, a placeholder of "Managed by Terraform" will be set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Teams

A list of teams the user should belong to. Please use `pagerduty_team_membership` instead.
* `description` - (Optional) A human-friendly description of the user.
If not set, a placeholder of "Managed by Terraform" will be set.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeZone

_Required_: No

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

#### AvatarUrl

Returns the <code>AvatarUrl</code> value.

#### HtmlUrl

Returns the <code>HtmlUrl</code> value.

#### InvitationSent

Returns the <code>InvitationSent</code> value.

