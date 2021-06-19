# TF::Gitlab::ProjectMirror

This resource allows you to add a mirror target for the repository, all changes will be synced to the remote target.

-> This is for *pushing* changes to a remote repository. *Pull Mirroring* can be configured using a combination of the 
`import_url`, `mirror`, and `mirror_trigger_builds` properties on the `gitlab_project` resource.

For further information on mirroring, consult the 
[gitlab documentation](https://docs.gitlab.com/ee/user/project/repository/repository_mirroring.html#repository-mirroring).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Gitlab::ProjectMirror",
    "Properties" : {
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#keepdivergentrefs" title="KeepDivergentRefs">KeepDivergentRefs</a>" : <i>Boolean</i>,
        "<a href="#onlyprotectedbranches" title="OnlyProtectedBranches">OnlyProtectedBranches</a>" : <i>Boolean</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#url" title="Url">Url</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Gitlab::ProjectMirror
Properties:
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#keepdivergentrefs" title="KeepDivergentRefs">KeepDivergentRefs</a>: <i>Boolean</i>
    <a href="#onlyprotectedbranches" title="OnlyProtectedBranches">OnlyProtectedBranches</a>: <i>Boolean</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#url" title="Url">Url</a>: <i>String</i>
</pre>

## Properties

#### Enabled

Determines if the mirror is enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepDivergentRefs

Determines if divergent refs are skipped.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnlyProtectedBranches

Determines if only protected branches are mirrored.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The id of the project.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

The URL of the remote repository to be mirrored.

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

#### MirrorId

Returns the <code>MirrorId</code> value.

