# TF::SignalFx::DataLink TargetSplunkDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#propertykeymapping" title="PropertyKeyMapping">PropertyKeyMapping</a>" : <i>[ <a href="propertykeymappingdefinition.md">PropertyKeyMappingDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#propertykeymapping" title="PropertyKeyMapping">PropertyKeyMapping</a>: <i>
      - <a href="propertykeymappingdefinition.md">PropertyKeyMappingDefinition</a></i>
</pre>

## Properties

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PropertyKeyMapping

_Required_: No

_Type_: List of <a href="propertykeymappingdefinition.md">PropertyKeyMappingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

