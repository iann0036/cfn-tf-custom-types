# TF::Artifactory::PermissionTarget RepoDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#excludespattern" title="ExcludesPattern">ExcludesPattern</a>" : <i>[ String, ... ]</i>,
    "<a href="#includespattern" title="IncludesPattern">IncludesPattern</a>" : <i>[ String, ... ]</i>,
    "<a href="#repositories" title="Repositories">Repositories</a>" : <i>[ String, ... ]</i>,
    "<a href="#actions" title="Actions">Actions</a>" : <i>[ <a href="actionsdefinition.md">ActionsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#excludespattern" title="ExcludesPattern">ExcludesPattern</a>: <i>
      - String</i>
<a href="#includespattern" title="IncludesPattern">IncludesPattern</a>: <i>
      - String</i>
<a href="#repositories" title="Repositories">Repositories</a>: <i>
      - String</i>
<a href="#actions" title="Actions">Actions</a>: <i>
      - <a href="actionsdefinition.md">ActionsDefinition</a></i>
</pre>

## Properties

#### ExcludesPattern

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludesPattern

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Repositories

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Actions

_Required_: No

_Type_: List of <a href="actionsdefinition.md">ActionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

