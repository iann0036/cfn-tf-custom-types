# TF::Kubernetes::NetworkPolicy EgressDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ports" title="Ports">Ports</a>" : <i>[ <a href="portsdefinition.md">PortsDefinition</a>, ... ]</i>,
    "<a href="#to" title="To">To</a>" : <i>[ <a href="todefinition.md">ToDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ports" title="Ports">Ports</a>: <i>
      - <a href="portsdefinition.md">PortsDefinition</a></i>
<a href="#to" title="To">To</a>: <i>
      - <a href="todefinition.md">ToDefinition</a></i>
</pre>

## Properties

#### Ports

_Required_: No

_Type_: List of <a href="portsdefinition.md">PortsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### To

_Required_: No

_Type_: List of <a href="todefinition.md">ToDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

