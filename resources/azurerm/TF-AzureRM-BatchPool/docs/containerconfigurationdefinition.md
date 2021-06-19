# TF::AzureRM::BatchPool ContainerConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#containerimagenames" title="ContainerImageNames">ContainerImageNames</a>" : <i>[ String, ... ]</i>,
    "<a href="#containerregistries" title="ContainerRegistries">ContainerRegistries</a>" : <i>[ <a href="containerregistriesdefinition.md">ContainerRegistriesDefinition</a>, ... ]</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#containerimagenames" title="ContainerImageNames">ContainerImageNames</a>: <i>
      - String</i>
<a href="#containerregistries" title="ContainerRegistries">ContainerRegistries</a>: <i>
      - <a href="containerregistriesdefinition.md">ContainerRegistriesDefinition</a></i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### ContainerImageNames

A list of container image names to use, as would be specified by `docker pull`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContainerRegistries

Additional container registries from which container images can be pulled by the pool's VMs.

_Required_: No

_Type_: List of <a href="containerregistriesdefinition.md">ContainerRegistriesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of container configuration. Possible value is `DockerCompatible`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

