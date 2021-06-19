# TF::GoogleBeta::GoogleDataLossPreventionDeidentifyTemplate PrimitiveTransformationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#charactermaskconfig" title="CharacterMaskConfig">CharacterMaskConfig</a>" : <i>[ <a href="charactermaskconfigdefinition.md">CharacterMaskConfigDefinition</a>, ... ]</i>,
    "<a href="#replaceconfig" title="ReplaceConfig">ReplaceConfig</a>" : <i>[ <a href="replaceconfigdefinition.md">ReplaceConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#charactermaskconfig" title="CharacterMaskConfig">CharacterMaskConfig</a>: <i>
      - <a href="charactermaskconfigdefinition.md">CharacterMaskConfigDefinition</a></i>
<a href="#replaceconfig" title="ReplaceConfig">ReplaceConfig</a>: <i>
      - <a href="replaceconfigdefinition.md">ReplaceConfigDefinition</a></i>
</pre>

## Properties

#### CharacterMaskConfig

_Required_: No

_Type_: List of <a href="charactermaskconfigdefinition.md">CharacterMaskConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplaceConfig

_Required_: No

_Type_: List of <a href="replaceconfigdefinition.md">ReplaceConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

