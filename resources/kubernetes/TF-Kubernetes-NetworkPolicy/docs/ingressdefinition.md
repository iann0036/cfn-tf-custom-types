# TF::Kubernetes::NetworkPolicy IngressDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#from" title="From">From</a>" : <i>[ <a href="fromdefinition.md">FromDefinition</a>, ... ]</i>,
    "<a href="#ports" title="Ports">Ports</a>" : <i>[ <a href="portsdefinition.md">PortsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#from" title="From">From</a>: <i>
      - <a href="fromdefinition.md">FromDefinition</a></i>
<a href="#ports" title="Ports">Ports</a>: <i>
      - <a href="portsdefinition.md">PortsDefinition</a></i>
</pre>

## Properties

#### From

_Required_: No

_Type_: List of <a href="fromdefinition.md">FromDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ports

_Required_: No

_Type_: List of <a href="portsdefinition.md">PortsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

