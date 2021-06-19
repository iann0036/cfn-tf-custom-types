# TF::Volterra::Fleet ArraysDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#flasharray" title="FlashArray">FlashArray</a>" : <i>[ <a href="flasharraydefinition.md">FlashArrayDefinition</a>, ... ]</i>,
    "<a href="#flashblade" title="FlashBlade">FlashBlade</a>" : <i>[ <a href="flashbladedefinition.md">FlashBladeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#flasharray" title="FlashArray">FlashArray</a>: <i>
      - <a href="flasharraydefinition.md">FlashArrayDefinition</a></i>
<a href="#flashblade" title="FlashBlade">FlashBlade</a>: <i>
      - <a href="flashbladedefinition.md">FlashBladeDefinition</a></i>
</pre>

## Properties

#### FlashArray

_Required_: No

_Type_: List of <a href="flasharraydefinition.md">FlashArrayDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlashBlade

_Required_: No

_Type_: List of <a href="flashbladedefinition.md">FlashBladeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

