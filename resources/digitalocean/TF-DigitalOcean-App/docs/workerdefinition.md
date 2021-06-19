# TF::DigitalOcean::App WorkerDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#buildcommand" title="BuildCommand">BuildCommand</a>" : <i>String</i>,
    "<a href="#dockerfilepath" title="DockerfilePath">DockerfilePath</a>" : <i>String</i>,
    "<a href="#environmentslug" title="EnvironmentSlug">EnvironmentSlug</a>" : <i>String</i>,
    "<a href="#instancecount" title="InstanceCount">InstanceCount</a>" : <i>Double</i>,
    "<a href="#instancesizeslug" title="InstanceSizeSlug">InstanceSizeSlug</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#runcommand" title="RunCommand">RunCommand</a>" : <i>String</i>,
    "<a href="#sourcedir" title="SourceDir">SourceDir</a>" : <i>String</i>,
    "<a href="#env" title="Env">Env</a>" : <i>[ <a href="envdefinition.md">EnvDefinition</a>, ... ]</i>,
    "<a href="#git" title="Git">Git</a>" : <i>[ <a href="gitdefinition.md">GitDefinition</a>, ... ]</i>,
    "<a href="#github" title="Github">Github</a>" : <i>[ <a href="githubdefinition.md">GithubDefinition</a>, ... ]</i>,
    "<a href="#gitlab" title="Gitlab">Gitlab</a>" : <i>[ <a href="gitlabdefinition.md">GitlabDefinition</a>, ... ]</i>,
    "<a href="#image" title="Image">Image</a>" : <i>[ <a href="imagedefinition.md">ImageDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#buildcommand" title="BuildCommand">BuildCommand</a>: <i>String</i>
<a href="#dockerfilepath" title="DockerfilePath">DockerfilePath</a>: <i>String</i>
<a href="#environmentslug" title="EnvironmentSlug">EnvironmentSlug</a>: <i>String</i>
<a href="#instancecount" title="InstanceCount">InstanceCount</a>: <i>Double</i>
<a href="#instancesizeslug" title="InstanceSizeSlug">InstanceSizeSlug</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#runcommand" title="RunCommand">RunCommand</a>: <i>String</i>
<a href="#sourcedir" title="SourceDir">SourceDir</a>: <i>String</i>
<a href="#env" title="Env">Env</a>: <i>
      - <a href="envdefinition.md">EnvDefinition</a></i>
<a href="#git" title="Git">Git</a>: <i>
      - <a href="gitdefinition.md">GitDefinition</a></i>
<a href="#github" title="Github">Github</a>: <i>
      - <a href="githubdefinition.md">GithubDefinition</a></i>
<a href="#gitlab" title="Gitlab">Gitlab</a>: <i>
      - <a href="gitlabdefinition.md">GitlabDefinition</a></i>
<a href="#image" title="Image">Image</a>: <i>
      - <a href="imagedefinition.md">ImageDefinition</a></i>
</pre>

## Properties

#### BuildCommand

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DockerfilePath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvironmentSlug

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceSizeSlug

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunCommand

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceDir

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Env

_Required_: No

_Type_: List of <a href="envdefinition.md">EnvDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Git

_Required_: No

_Type_: List of <a href="gitdefinition.md">GitDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Github

_Required_: No

_Type_: List of <a href="githubdefinition.md">GithubDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gitlab

_Required_: No

_Type_: List of <a href="gitlabdefinition.md">GitlabDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

_Required_: No

_Type_: List of <a href="imagedefinition.md">ImageDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

