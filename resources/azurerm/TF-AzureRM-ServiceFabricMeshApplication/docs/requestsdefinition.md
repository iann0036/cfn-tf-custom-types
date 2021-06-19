# TF::AzureRM::ServiceFabricMeshApplication RequestsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cpu" title="Cpu">Cpu</a>" : <i>Double</i>,
    "<a href="#memory" title="Memory">Memory</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#cpu" title="Cpu">Cpu</a>: <i>Double</i>
<a href="#memory" title="Memory">Memory</a>: <i>Double</i>
</pre>

## Properties

#### Cpu

The minimum number of CPU cores the container requires.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Memory

The minimum memory request in GB the container requires.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

