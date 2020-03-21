# Terraform::AzureRM::BatchPool ContainerConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#containerregistries" title="ContainerRegistries">ContainerRegistries</a>" : <i>[ <a href="containerconfiguration-containerregistries.md">ContainerRegistries</a>, ... ]</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#containerregistries" title="ContainerRegistries">ContainerRegistries</a>: <i>
      - <a href="containerconfiguration-containerregistries.md">ContainerRegistries</a></i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### ContainerRegistries

Additional container registries from which container images can be pulled by the pool's VMs.

_Required_: No

_Type_: List of <a href="containerconfiguration-containerregistries.md">ContainerRegistries</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of container configuration. Possible value is `DockerCompatible`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

