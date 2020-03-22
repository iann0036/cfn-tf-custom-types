# Terraform::Tfe::PolicySet

Sentinel Policy as Code is an embedded policy as code framework integrated
with Terraform Enterprise.

Policy sets are groups of policies that are applied together to related workspaces.
By using policy sets, you can group your policies by attributes such as environment
or region. Individual policies that are members of policy sets will only be checked
for workspaces that the policy set is attached to.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Tfe::PolicySet",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#global" title="Global">Global</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#organization" title="Organization">Organization</a>" : <i>String</i>,
        "<a href="#policiespath" title="PoliciesPath">PoliciesPath</a>" : <i>String</i>,
        "<a href="#policyids" title="PolicyIds">PolicyIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#workspaceexternalids" title="WorkspaceExternalIds">WorkspaceExternalIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#vcsrepo" title="VcsRepo">VcsRepo</a>" : <i>[ <a href="vcsrepo.md">VcsRepo</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Tfe::PolicySet
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#global" title="Global">Global</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#organization" title="Organization">Organization</a>: <i>String</i>
    <a href="#policiespath" title="PoliciesPath">PoliciesPath</a>: <i>String</i>
    <a href="#policyids" title="PolicyIds">PolicyIds</a>: <i>
      - String</i>
    <a href="#workspaceexternalids" title="WorkspaceExternalIds">WorkspaceExternalIds</a>: <i>
      - String</i>
    <a href="#vcsrepo" title="VcsRepo">VcsRepo</a>: <i>
      - <a href="vcsrepo.md">VcsRepo</a></i>
</pre>

## Properties

#### Description

A description of the policy set's purpose.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Global

Whether or not policies in this set will apply to
all workspaces. Defaults to `false`. This value _must not_ be provided if
`workspace_external_ids` are provided.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the policy set.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Organization

Name of the organization.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PoliciesPath

The sub-path within the attached VCS repository
to ingress when using `vcs_repo`. All files and directories outside of this
sub-path will be ignored. This option can only be supplied when `vcs_repo` is
present. Forces a new resource if changed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyIds

A list of Sentinel policy IDs. This value _must not_ be provided if `vcs_repo` is provided.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkspaceExternalIds

A list of workspace external IDs. This
value _must not_ be provided if `global` is provided.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VcsRepo

_Required_: No

_Type_: List of <a href="vcsrepo.md">VcsRepo</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

