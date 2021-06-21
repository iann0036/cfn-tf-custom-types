# TF::AzureRM::SpringCloudService ConfigServerGitSettingDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#label" title="Label">Label</a>" : <i>String</i>,
    "<a href="#searchpaths" title="SearchPaths">SearchPaths</a>" : <i>[ String, ... ]</i>,
    "<a href="#uri" title="Uri">Uri</a>" : <i>String</i>,
    "<a href="#httpbasicauth" title="HttpBasicAuth">HttpBasicAuth</a>" : <i>[ <a href="httpbasicauthdefinition.md">HttpBasicAuthDefinition</a>, ... ]</i>,
    "<a href="#repository" title="Repository">Repository</a>" : <i>[ <a href="repositorydefinition.md">RepositoryDefinition</a>, ... ]</i>,
    "<a href="#sshauth" title="SshAuth">SshAuth</a>" : <i>[ <a href="sshauthdefinition.md">SshAuthDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#label" title="Label">Label</a>: <i>String</i>
<a href="#searchpaths" title="SearchPaths">SearchPaths</a>: <i>
      - String</i>
<a href="#uri" title="Uri">Uri</a>: <i>String</i>
<a href="#httpbasicauth" title="HttpBasicAuth">HttpBasicAuth</a>: <i>
      - <a href="httpbasicauthdefinition.md">HttpBasicAuthDefinition</a></i>
<a href="#repository" title="Repository">Repository</a>: <i>
      - <a href="repositorydefinition.md">RepositoryDefinition</a></i>
<a href="#sshauth" title="SshAuth">SshAuth</a>: <i>
      - <a href="sshauthdefinition.md">SshAuthDefinition</a></i>
</pre>

## Properties

#### Label

The default label of the Git repository, should be the branch name, tag name, or commit-id of the repository.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SearchPaths

An array of strings used to search subdirectories of the Git repository.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uri

The URI of the default Git repository used as the Config Server back end, should be started with `http://`, `https://`, `git@`, or `ssh://`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpBasicAuth

_Required_: No

_Type_: List of <a href="httpbasicauthdefinition.md">HttpBasicAuthDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Repository

_Required_: No

_Type_: List of <a href="repositorydefinition.md">RepositoryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshAuth

_Required_: No

_Type_: List of <a href="sshauthdefinition.md">SshAuthDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
