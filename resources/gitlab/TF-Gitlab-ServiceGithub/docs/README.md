# TF::Gitlab::ServiceGithub

**NOTE**: requires either EE (self-hosted) or Silver and above (GitLab.com).

This resource manages a [GitHub integration](https://docs.gitlab.com/ee/user/project/integrations/github.html) that updates pipeline statuses on a GitHub repo's pull requests.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Gitlab::ServiceGithub",
    "Properties" : {
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#repositoryurl" title="RepositoryUrl">RepositoryUrl</a>" : <i>String</i>,
        "<a href="#staticcontext" title="StaticContext">StaticContext</a>" : <i>Boolean</i>,
        "<a href="#token" title="Token">Token</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Gitlab::ServiceGithub
Properties:
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#repositoryurl" title="RepositoryUrl">RepositoryUrl</a>: <i>String</i>
    <a href="#staticcontext" title="StaticContext">StaticContext</a>: <i>Boolean</i>
    <a href="#token" title="Token">Token</a>: <i>String</i>
</pre>

## Properties

#### Project

ID of the project you want to activate integration on.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RepositoryUrl

The URL of the GitHub repo to integrate with, e,g, https://github.com/gitlabhq/terraform-provider-gitlab.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticContext

Append instance name instead of branch to the status. Must enable to set a GitLab status check as _required_ in GitHub. See [Static / dynamic status check names] to learn more.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Token

A GitHub personal access token with at least `repo:status` scope.

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

#### Active

Returns the <code>Active</code> value.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### Id

Returns the <code>Id</code> value.

#### Title

Returns the <code>Title</code> value.

#### UpdatedAt

Returns the <code>UpdatedAt</code> value.

