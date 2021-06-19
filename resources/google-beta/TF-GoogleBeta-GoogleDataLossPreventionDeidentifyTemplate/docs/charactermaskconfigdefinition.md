# TF::GoogleBeta::GoogleDataLossPreventionDeidentifyTemplate CharacterMaskConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#maskingcharacter" title="MaskingCharacter">MaskingCharacter</a>" : <i>String</i>,
    "<a href="#numbertomask" title="NumberToMask">NumberToMask</a>" : <i>Double</i>,
    "<a href="#reverseorder" title="ReverseOrder">ReverseOrder</a>" : <i>Boolean</i>,
    "<a href="#characterstoignore" title="CharactersToIgnore">CharactersToIgnore</a>" : <i>[ <a href="characterstoignoredefinition.md">CharactersToIgnoreDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#maskingcharacter" title="MaskingCharacter">MaskingCharacter</a>: <i>String</i>
<a href="#numbertomask" title="NumberToMask">NumberToMask</a>: <i>Double</i>
<a href="#reverseorder" title="ReverseOrder">ReverseOrder</a>: <i>Boolean</i>
<a href="#characterstoignore" title="CharactersToIgnore">CharactersToIgnore</a>: <i>
      - <a href="characterstoignoredefinition.md">CharactersToIgnoreDefinition</a></i>
</pre>

## Properties

#### MaskingCharacter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumberToMask

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReverseOrder

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CharactersToIgnore

_Required_: No

_Type_: List of <a href="characterstoignoredefinition.md">CharactersToIgnoreDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

