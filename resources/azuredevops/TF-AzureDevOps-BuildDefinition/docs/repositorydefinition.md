# TF::AzureDevOps::BuildDefinition RepositoryDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#branchname" title="BranchName">BranchName</a>" : <i>String</i>,
    "<a href="#githubenterpriseurl" title="GithubEnterpriseUrl">GithubEnterpriseUrl</a>" : <i>String</i>,
    "<a href="#repoid" title="RepoId">RepoId</a>" : <i>String</i>,
    "<a href="#repotype" title="RepoType">RepoType</a>" : <i>String</i>,
    "<a href="#reportbuildstatus" title="ReportBuildStatus">ReportBuildStatus</a>" : <i>Boolean</i>,
    "<a href="#serviceconnectionid" title="ServiceConnectionId">ServiceConnectionId</a>" : <i>String</i>,
    "<a href="#ymlpath" title="YmlPath">YmlPath</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#branchname" title="BranchName">BranchName</a>: <i>String</i>
<a href="#githubenterpriseurl" title="GithubEnterpriseUrl">GithubEnterpriseUrl</a>: <i>String</i>
<a href="#repoid" title="RepoId">RepoId</a>: <i>String</i>
<a href="#repotype" title="RepoType">RepoType</a>: <i>String</i>
<a href="#reportbuildstatus" title="ReportBuildStatus">ReportBuildStatus</a>: <i>Boolean</i>
<a href="#serviceconnectionid" title="ServiceConnectionId">ServiceConnectionId</a>: <i>String</i>
<a href="#ymlpath" title="YmlPath">YmlPath</a>: <i>String</i>
</pre>

## Properties

#### BranchName

The branch name for which builds are triggered. Defaults to `master`.
- `repo_id` - (Required) The id of the repository. For `TfsGit` repos, this is simply the ID of the repository. For `Github` repos, this will take the form of `<GitHub Org>/<Repo Name>`. For `Bitbucket` repos, this will take the form of `<Workspace ID>/<Repo Name>`.
- `repo_type` - (Optional) The repository type. Valid values: `GitHub` or `TfsGit` or `Bitbucket` or `GitHub Enterprise`. Defaults to `GitHub`. If `repo_type` is `GitHubEnterprise`, must use existing project and GitHub Enterprise service connection.
- `service_connection_id` - (Optional) The service connection ID. Used if the `repo_type` is `GitHub` or `GitHubEnterprise`.
- `yml_path` - (Required) The path of the Yaml file describing the build definition.
- `github_enterprise_url` - (Optional) The Github Enterprise URL. Used if `repo_type` is `GithubEnterprise`.
- `report_build_status` - (Optional) Report build status. Default is true.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GithubEnterpriseUrl

The Github Enterprise URL. Used if `repo_type` is `GithubEnterprise`.
- `report_build_status` - (Optional) Report build status. Default is true.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RepoId

The id of the repository. For `TfsGit` repos, this is simply the ID of the repository. For `Github` repos, this will take the form of `<GitHub Org>/<Repo Name>`. For `Bitbucket` repos, this will take the form of `<Workspace ID>/<Repo Name>`.
- `repo_type` - (Optional) The repository type. Valid values: `GitHub` or `TfsGit` or `Bitbucket` or `GitHub Enterprise`. Defaults to `GitHub`. If `repo_type` is `GitHubEnterprise`, must use existing project and GitHub Enterprise service connection.
- `service_connection_id` - (Optional) The service connection ID. Used if the `repo_type` is `GitHub` or `GitHubEnterprise`.
- `yml_path` - (Required) The path of the Yaml file describing the build definition.
- `github_enterprise_url` - (Optional) The Github Enterprise URL. Used if `repo_type` is `GithubEnterprise`.
- `report_build_status` - (Optional) Report build status. Default is true.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RepoType

The repository type. Valid values: `GitHub` or `TfsGit` or `Bitbucket` or `GitHub Enterprise`. Defaults to `GitHub`. If `repo_type` is `GitHubEnterprise`, must use existing project and GitHub Enterprise service connection.
- `service_connection_id` - (Optional) The service connection ID. Used if the `repo_type` is `GitHub` or `GitHubEnterprise`.
- `yml_path` - (Required) The path of the Yaml file describing the build definition.
- `github_enterprise_url` - (Optional) The Github Enterprise URL. Used if `repo_type` is `GithubEnterprise`.
- `report_build_status` - (Optional) Report build status. Default is true.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReportBuildStatus

Report build status. Default is true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceConnectionId

The service connection ID. Used if the `repo_type` is `GitHub` or `GitHubEnterprise`.
- `yml_path` - (Required) The path of the Yaml file describing the build definition.
- `github_enterprise_url` - (Optional) The Github Enterprise URL. Used if `repo_type` is `GithubEnterprise`.
- `report_build_status` - (Optional) Report build status. Default is true.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### YmlPath

The path of the Yaml file describing the build definition.
- `github_enterprise_url` - (Optional) The Github Enterprise URL. Used if `repo_type` is `GithubEnterprise`.
- `report_build_status` - (Optional) Report build status. Default is true.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

