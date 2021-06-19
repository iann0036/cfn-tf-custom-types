# TF::SignalFx::DataLink TargetExternalUrlDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#minimumtimewindow" title="MinimumTimeWindow">MinimumTimeWindow</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#propertykeymapping" title="PropertyKeyMapping">PropertyKeyMapping</a>" : <i>[ <a href="propertykeymappingdefinition.md">PropertyKeyMappingDefinition</a>, ... ]</i>,
    "<a href="#timeformat" title="TimeFormat">TimeFormat</a>" : <i>String</i>,
    "<a href="#url" title="Url">Url</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#minimumtimewindow" title="MinimumTimeWindow">MinimumTimeWindow</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#propertykeymapping" title="PropertyKeyMapping">PropertyKeyMapping</a>: <i>
      - <a href="propertykeymappingdefinition.md">PropertyKeyMappingDefinition</a></i>
<a href="#timeformat" title="TimeFormat">TimeFormat</a>: <i>String</i>
<a href="#url" title="Url">Url</a>: <i>String</i>
</pre>

## Properties

#### MinimumTimeWindow

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PropertyKeyMapping

_Required_: No

_Type_: List of <a href="propertykeymappingdefinition.md">PropertyKeyMappingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

