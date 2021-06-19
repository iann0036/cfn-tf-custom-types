# TF::AzureRM::AppService SourceControlDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#branch" title="Branch">Branch</a>" : <i>String</i>,
    "<a href="#manualintegration" title="ManualIntegration">ManualIntegration</a>" : <i>Boolean</i>,
    "<a href="#repourl" title="RepoUrl">RepoUrl</a>" : <i>String</i>,
    "<a href="#rollbackenabled" title="RollbackEnabled">RollbackEnabled</a>" : <i>Boolean</i>,
    "<a href="#usemercurial" title="UseMercurial">UseMercurial</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#branch" title="Branch">Branch</a>: <i>String</i>
<a href="#manualintegration" title="ManualIntegration">ManualIntegration</a>: <i>Boolean</i>
<a href="#repourl" title="RepoUrl">RepoUrl</a>: <i>String</i>
<a href="#rollbackenabled" title="RollbackEnabled">RollbackEnabled</a>: <i>Boolean</i>
<a href="#usemercurial" title="UseMercurial">UseMercurial</a>: <i>Boolean</i>
</pre>

## Properties

#### Branch

The branch of the remote repository to use. Defaults to 'master'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManualIntegration

Limits to manual integration. Defaults to `false` if not specified.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RepoUrl

The URL of the source code repository.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RollbackEnabled

Enable roll-back for the repository. Defaults to `false` if not specified.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseMercurial

Use Mercurial if `true`, otherwise uses Git.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

