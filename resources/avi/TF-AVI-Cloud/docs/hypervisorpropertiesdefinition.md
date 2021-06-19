# TF::AVI::Cloud HypervisorPropertiesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#hypervisor" title="Hypervisor">Hypervisor</a>" : <i>String</i>,
    "<a href="#imageproperties" title="ImageProperties">ImageProperties</a>" : <i>[ <a href="imagepropertiesdefinition.md">ImagePropertiesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#hypervisor" title="Hypervisor">Hypervisor</a>: <i>String</i>
<a href="#imageproperties" title="ImageProperties">ImageProperties</a>: <i>
      - <a href="imagepropertiesdefinition.md">ImagePropertiesDefinition</a></i>
</pre>

## Properties

#### Hypervisor

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageProperties

_Required_: No

_Type_: List of <a href="imagepropertiesdefinition.md">ImagePropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

