# TF::AWS::SagemakerAppImageConfig KernelGatewayImageConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#filesystemconfig" title="FileSystemConfig">FileSystemConfig</a>" : <i>[ <a href="filesystemconfigdefinition.md">FileSystemConfigDefinition</a>, ... ]</i>,
    "<a href="#kernelspec" title="KernelSpec">KernelSpec</a>" : <i>[ <a href="kernelspecdefinition.md">KernelSpecDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#filesystemconfig" title="FileSystemConfig">FileSystemConfig</a>: <i>
      - <a href="filesystemconfigdefinition.md">FileSystemConfigDefinition</a></i>
<a href="#kernelspec" title="KernelSpec">KernelSpec</a>: <i>
      - <a href="kernelspecdefinition.md">KernelSpecDefinition</a></i>
</pre>

## Properties

#### FileSystemConfig

_Required_: No

_Type_: List of <a href="filesystemconfigdefinition.md">FileSystemConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KernelSpec

_Required_: No

_Type_: List of <a href="kernelspecdefinition.md">KernelSpecDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

