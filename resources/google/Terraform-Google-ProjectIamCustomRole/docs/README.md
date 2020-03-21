# Terraform::Google::ProjectIamCustomRole

Allows management of a customized Cloud IAM project role. For more information see
[the official documentation](https://cloud.google.com/iam/docs/understanding-custom-roles)
and
[API](https://cloud.google.com/iam/reference/rest/v1/projects.roles).

~> **Warning:** Note that custom roles in GCP have the concept of a soft-delete. There are two issues that may arise
 from this and how roles are propagated. 1) creating a role may involve undeleting and then updating a role with the
 same name, possibly causing confusing behavior between undelete and update. 2) A deleted role is permanently deleted
 after 7 days, but it can take up to 30 more days (i.e. between 7 and 37 days after deletion) before the role name is
 made available again. This means a deleted role that has been deleted for more than 7 days cannot be changed at all
 by Terraform, and new roles cannot share that name.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::ProjectIamCustomRole",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#permissions" title="Permissions">Permissions</a>" : <i>[ String, ... ]</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#roleid" title="RoleId">RoleId</a>" : <i>String</i>,
        "<a href="#stage" title="Stage">Stage</a>" : <i>String</i>,
        "<a href="#title" title="Title">Title</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::ProjectIamCustomRole
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#permissions" title="Permissions">Permissions</a>: <i>
      - String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#roleid" title="RoleId">RoleId</a>: <i>String</i>
    <a href="#stage" title="Stage">Stage</a>: <i>String</i>
    <a href="#title" title="Title">Title</a>: <i>String</i>
</pre>

## Properties

#### Description

A human-readable description for the role.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Permissions

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The project that the service account will be created in.
Defaults to the provider project configuration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleId

The camel case role id to use for this role. Cannot contain `-` characters.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Stage

The current launch stage of the role.
Defaults to `GA`.
List of possible stages is [here](https://cloud.google.com/iam/reference/rest/v1/organizations.roles#Role.RoleLaunchStage).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

A human-readable title for the role.

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

#### Deleted

Returns the <code>Deleted</code> value.

