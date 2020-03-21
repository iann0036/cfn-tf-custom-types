# Terraform::Panos::PanoramaNatRuleGroup Destination

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dynamic" title="Dynamic">Dynamic</a>" : <i>[ <a href="destination-dynamic.md">Dynamic</a>, ... ]</i>,
    "<a href="#dynamictranslation" title="DynamicTranslation">DynamicTranslation</a>" : <i>[ <a href="destination-dynamictranslation.md">DynamicTranslation</a>, ... ]</i>,
    "<a href="#static" title="Static">Static</a>" : <i>[ <a href="destination-static.md">Static</a>, ... ]</i>,
    "<a href="#statictranslation" title="StaticTranslation">StaticTranslation</a>" : <i>[ <a href="destination-statictranslation.md">StaticTranslation</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dynamic" title="Dynamic">Dynamic</a>: <i>
      - <a href="destination-dynamic.md">Dynamic</a></i>
<a href="#dynamictranslation" title="DynamicTranslation">DynamicTranslation</a>: <i>
      - <a href="destination-dynamictranslation.md">DynamicTranslation</a></i>
<a href="#static" title="Static">Static</a>: <i>
      - <a href="destination-static.md">Static</a></i>
<a href="#statictranslation" title="StaticTranslation">StaticTranslation</a>: <i>
      - <a href="destination-statictranslation.md">StaticTranslation</a></i>
</pre>

## Properties

#### Dynamic

_Required_: No
_Type_: List of <a href="destination-dynamic.md">Dynamic</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicTranslation

_Required_: No
_Type_: List of <a href="destination-dynamictranslation.md">DynamicTranslation</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Static

_Required_: No
_Type_: List of <a href="destination-static.md">Static</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticTranslation

_Required_: No
_Type_: List of <a href="destination-statictranslation.md">StaticTranslation</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

