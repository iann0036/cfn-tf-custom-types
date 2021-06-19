# TF::Panos::PanoramaNatRuleGroup DestinationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dynamic" title="Dynamic">Dynamic</a>" : <i>[ <a href="dynamicdefinition.md">DynamicDefinition</a>, ... ]</i>,
    "<a href="#dynamictranslation" title="DynamicTranslation">DynamicTranslation</a>" : <i>[ <a href="dynamictranslationdefinition.md">DynamicTranslationDefinition</a>, ... ]</i>,
    "<a href="#static" title="Static">Static</a>" : <i>[ <a href="staticdefinition.md">StaticDefinition</a>, ... ]</i>,
    "<a href="#statictranslation" title="StaticTranslation">StaticTranslation</a>" : <i>[ <a href="statictranslationdefinition.md">StaticTranslationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dynamic" title="Dynamic">Dynamic</a>: <i>
      - <a href="dynamicdefinition.md">DynamicDefinition</a></i>
<a href="#dynamictranslation" title="DynamicTranslation">DynamicTranslation</a>: <i>
      - <a href="dynamictranslationdefinition.md">DynamicTranslationDefinition</a></i>
<a href="#static" title="Static">Static</a>: <i>
      - <a href="staticdefinition.md">StaticDefinition</a></i>
<a href="#statictranslation" title="StaticTranslation">StaticTranslation</a>: <i>
      - <a href="statictranslationdefinition.md">StaticTranslationDefinition</a></i>
</pre>

## Properties

#### Dynamic

_Required_: No

_Type_: List of <a href="dynamicdefinition.md">DynamicDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicTranslation

_Required_: No

_Type_: List of <a href="dynamictranslationdefinition.md">DynamicTranslationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Static

_Required_: No

_Type_: List of <a href="staticdefinition.md">StaticDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticTranslation

_Required_: No

_Type_: List of <a href="statictranslationdefinition.md">StaticTranslationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

