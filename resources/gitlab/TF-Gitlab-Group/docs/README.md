# TF::Gitlab::Group

This resource allows you to create and manage GitLab groups.
Note your provider will need to be configured with admin-level access for this resource to work.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Gitlab::Group",
    "Properties" : {
        "<a href="#autodevopsenabled" title="AutoDevopsEnabled">AutoDevopsEnabled</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#emailsdisabled" title="EmailsDisabled">EmailsDisabled</a>" : <i>Boolean</i>,
        "<a href="#lfsenabled" title="LfsEnabled">LfsEnabled</a>" : <i>Boolean</i>,
        "<a href="#mentionsdisabled" title="MentionsDisabled">MentionsDisabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#parentid" title="ParentId">ParentId</a>" : <i>Double</i>,
        "<a href="#path" title="Path">Path</a>" : <i>String</i>,
        "<a href="#projectcreationlevel" title="ProjectCreationLevel">ProjectCreationLevel</a>" : <i>String</i>,
        "<a href="#requestaccessenabled" title="RequestAccessEnabled">RequestAccessEnabled</a>" : <i>Boolean</i>,
        "<a href="#requiretwofactorauthentication" title="RequireTwoFactorAuthentication">RequireTwoFactorAuthentication</a>" : <i>Boolean</i>,
        "<a href="#sharewithgrouplock" title="ShareWithGroupLock">ShareWithGroupLock</a>" : <i>Boolean</i>,
        "<a href="#subgroupcreationlevel" title="SubgroupCreationLevel">SubgroupCreationLevel</a>" : <i>String</i>,
        "<a href="#twofactorgraceperiod" title="TwoFactorGracePeriod">TwoFactorGracePeriod</a>" : <i>Double</i>,
        "<a href="#visibilitylevel" title="VisibilityLevel">VisibilityLevel</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Gitlab::Group
Properties:
    <a href="#autodevopsenabled" title="AutoDevopsEnabled">AutoDevopsEnabled</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#emailsdisabled" title="EmailsDisabled">EmailsDisabled</a>: <i>Boolean</i>
    <a href="#lfsenabled" title="LfsEnabled">LfsEnabled</a>: <i>Boolean</i>
    <a href="#mentionsdisabled" title="MentionsDisabled">MentionsDisabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#parentid" title="ParentId">ParentId</a>: <i>Double</i>
    <a href="#path" title="Path">Path</a>: <i>String</i>
    <a href="#projectcreationlevel" title="ProjectCreationLevel">ProjectCreationLevel</a>: <i>String</i>
    <a href="#requestaccessenabled" title="RequestAccessEnabled">RequestAccessEnabled</a>: <i>Boolean</i>
    <a href="#requiretwofactorauthentication" title="RequireTwoFactorAuthentication">RequireTwoFactorAuthentication</a>: <i>Boolean</i>
    <a href="#sharewithgrouplock" title="ShareWithGroupLock">ShareWithGroupLock</a>: <i>Boolean</i>
    <a href="#subgroupcreationlevel" title="SubgroupCreationLevel">SubgroupCreationLevel</a>: <i>String</i>
    <a href="#twofactorgraceperiod" title="TwoFactorGracePeriod">TwoFactorGracePeriod</a>: <i>Double</i>
    <a href="#visibilitylevel" title="VisibilityLevel">VisibilityLevel</a>: <i>String</i>
</pre>

## Properties

#### AutoDevopsEnabled

Boolean, defaults to false.  Default to Auto
DevOps pipeline for all projects within this group.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description of the group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailsDisabled

Boolean, defaults to false.  Disable email notifications.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LfsEnabled

Boolean, defaults to true.  Whether to enable LFS
support for projects in this group.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MentionsDisabled

Boolean, defaults to false.  Disable the capability
of a group from getting mentioned.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of this group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParentId

Integer, id of the parent group (creates a nested group).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

The path of the group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectCreationLevel

, defaults to Maintainer.
Determine if developers can create projects
in the group. Can be noone (No one), maintainer (Maintainers),
or developer (Developers + Maintainers).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestAccessEnabled

Boolean, defaults to false.  Whether to
enable users to request access to the group.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireTwoFactorAuthentication

Boolean, defaults to false.
equire all users in this group to setup Two-factor authentication.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShareWithGroupLock

Boolean, defaults to false.  Prevent sharing
a project with another group within this group.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubgroupCreationLevel

, defaults to Owner.
Allowed to create subgroups.
Can be owner (Owners), or maintainer (Maintainers).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TwoFactorGracePeriod

Int, defaults to 48.
Time before Two-factor authentication is enforced (in hours).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VisibilityLevel

The group's visibility. Can be `private`, `internal`, or `public`.

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

#### FullName

Returns the <code>FullName</code> value.

#### FullPath

Returns the <code>FullPath</code> value.

#### Id

Returns the <code>Id</code> value.

#### RunnersToken

Returns the <code>RunnersToken</code> value.

#### WebUrl

Returns the <code>WebUrl</code> value.

