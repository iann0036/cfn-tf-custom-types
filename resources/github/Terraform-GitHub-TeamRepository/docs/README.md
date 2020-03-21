# Terraform::GitHub::TeamRepository

This resource manages relationships between teams and repositories
in your GitHub organization.

Creating this resource grants a particular team permissions on a
particular repository.

The repository and the team must both belong to the same organization
on GitHub. This resource does not actually *create* any repositories;
to do that, see [`github_repository`](repository.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::GitHub::TeamRepository",
    "Properties" : {
        "<a href="#permission" title="Permission">Permission</a>" : <i>String</i>,
        "<a href="#repository" title="Repository">Repository</a>" : <i>String</i>,
        "<a href="#teamid" title="TeamId">TeamId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::GitHub::TeamRepository
Properties:
    <a href="#permission" title="Permission">Permission</a>: <i>String</i>
    <a href="#repository" title="Repository">Repository</a>: <i>String</i>
    <a href="#teamid" title="TeamId">TeamId</a>: <i>String</i>
</pre>

## Properties

#### Permission

The permissions of team members regarding the repository.
Must be one of `pull`, `triage`, `push`, `maintain`, or `admin`. Defaults to `pull`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Repository

The repository to add to the team.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TeamId

The GitHub team id.

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

#### Etag

Returns the <code>Etag</code> value.

