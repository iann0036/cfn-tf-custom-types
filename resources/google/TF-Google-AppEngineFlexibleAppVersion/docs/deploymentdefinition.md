# TF::Google::AppEngineFlexibleAppVersion DeploymentDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cloudbuildoptions" title="CloudBuildOptions">CloudBuildOptions</a>" : <i>[ <a href="cloudbuildoptionsdefinition.md">CloudBuildOptionsDefinition</a>, ... ]</i>,
    "<a href="#container" title="Container">Container</a>" : <i>[ <a href="containerdefinition.md">ContainerDefinition</a>, ... ]</i>,
    "<a href="#files" title="Files">Files</a>" : <i>[ <a href="filesdefinition.md">FilesDefinition</a>, ... ]</i>,
    "<a href="#zip" title="Zip">Zip</a>" : <i>[ <a href="zipdefinition.md">ZipDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cloudbuildoptions" title="CloudBuildOptions">CloudBuildOptions</a>: <i>
      - <a href="cloudbuildoptionsdefinition.md">CloudBuildOptionsDefinition</a></i>
<a href="#container" title="Container">Container</a>: <i>
      - <a href="containerdefinition.md">ContainerDefinition</a></i>
<a href="#files" title="Files">Files</a>: <i>
      - <a href="filesdefinition.md">FilesDefinition</a></i>
<a href="#zip" title="Zip">Zip</a>: <i>
      - <a href="zipdefinition.md">ZipDefinition</a></i>
</pre>

## Properties

#### CloudBuildOptions

_Required_: No

_Type_: List of <a href="cloudbuildoptionsdefinition.md">CloudBuildOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Container

_Required_: No

_Type_: List of <a href="containerdefinition.md">ContainerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Files

_Required_: No

_Type_: List of <a href="filesdefinition.md">FilesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zip

_Required_: No

_Type_: List of <a href="zipdefinition.md">ZipDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

