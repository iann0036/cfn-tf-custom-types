# Terraform::AzureRM::DataFactory VstsConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accountname" title="AccountName">AccountName</a>" : <i>String</i>,
    "<a href="#branchname" title="BranchName">BranchName</a>" : <i>String</i>,
    "<a href="#projectname" title="ProjectName">ProjectName</a>" : <i>String</i>,
    "<a href="#repositoryname" title="RepositoryName">RepositoryName</a>" : <i>String</i>,
    "<a href="#rootfolder" title="RootFolder">RootFolder</a>" : <i>String</i>,
    "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#accountname" title="AccountName">AccountName</a>: <i>String</i>
<a href="#branchname" title="BranchName">BranchName</a>: <i>String</i>
<a href="#projectname" title="ProjectName">ProjectName</a>: <i>String</i>
<a href="#repositoryname" title="RepositoryName">RepositoryName</a>: <i>String</i>
<a href="#rootfolder" title="RootFolder">RootFolder</a>: <i>String</i>
<a href="#tenantid" title="TenantId">TenantId</a>: <i>String</i>
</pre>

## Properties

#### AccountName

Specifies the VSTS account name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BranchName

Specifies the branch of the repository to get code from.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectName

Specifies the name of the VSTS project.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RepositoryName

Specifies the name of the git repository.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootFolder

Specifies the root folder within the repository. Set to `/` for the top level.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

Specifies the Tenant ID associated with the VSTS account.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

