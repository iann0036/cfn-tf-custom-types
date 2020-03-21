# Terraform::Netlify::Site Repo

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#command" title="Command">Command</a>" : <i>String</i>,
    "<a href="#deploykeyid" title="DeployKeyId">DeployKeyId</a>" : <i>String</i>,
    "<a href="#dir" title="Dir">Dir</a>" : <i>String</i>,
    "<a href="#provider" title="Provider">Provider</a>" : <i>String</i>,
    "<a href="#repobranch" title="RepoBranch">RepoBranch</a>" : <i>String</i>,
    "<a href="#repopath" title="RepoPath">RepoPath</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#command" title="Command">Command</a>: <i>String</i>
<a href="#deploykeyid" title="DeployKeyId">DeployKeyId</a>: <i>String</i>
<a href="#dir" title="Dir">Dir</a>: <i>String</i>
<a href="#provider" title="Provider">Provider</a>: <i>String</i>
<a href="#repobranch" title="RepoBranch">RepoBranch</a>: <i>String</i>
<a href="#repopath" title="RepoPath">RepoPath</a>: <i>String</i>
</pre>

## Properties

#### Command

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeployKeyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dir

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Provider

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RepoBranch

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RepoPath

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

