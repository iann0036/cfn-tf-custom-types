# TF::AzureDevOps::GitRepository

Manages a git repository within Azure DevOps.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureDevOps::GitRepository",
    "Properties" : {
        "<a href="#defaultbranch" title="DefaultBranch">DefaultBranch</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#parentrepositoryid" title="ParentRepositoryId">ParentRepositoryId</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#initialization" title="Initialization">Initialization</a>" : <i>[ <a href="initializationdefinition.md">InitializationDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureDevOps::GitRepository
Properties:
    <a href="#defaultbranch" title="DefaultBranch">DefaultBranch</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#parentrepositoryid" title="ParentRepositoryId">ParentRepositoryId</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#initialization" title="Initialization">Initialization</a>: <i>
      - <a href="initializationdefinition.md">InitializationDefinition</a></i>
</pre>

## Properties

#### DefaultBranch

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the git repository.
- `parent_repository_id` - (Optional) The ID of a Git project from which a fork is to be created.
- `initialization` - (Required) An `initialization` block as documented below.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParentRepositoryId

The ID of a Git project from which a fork is to be created.
- `initialization` - (Required) An `initialization` block as documented below.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The project ID or project name.
- `name` - (Required) The name of the git repository.
- `parent_repository_id` - (Optional) The ID of a Git project from which a fork is to be created.
- `initialization` - (Required) An `initialization` block as documented below.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Initialization

_Required_: No

_Type_: List of <a href="initializationdefinition.md">InitializationDefinition</a>

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

#### IsFork

Returns the <code>IsFork</code> value.

#### RemoteUrl

Returns the <code>RemoteUrl</code> value.

#### Size

Returns the <code>Size</code> value.

#### SshUrl

Returns the <code>SshUrl</code> value.

#### Url

Returns the <code>Url</code> value.

#### WebUrl

Returns the <code>WebUrl</code> value.

