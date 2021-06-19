# TF::GoogleBeta::GoogleDataLossPreventionInspectTemplate ExclusionRuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#matchingtype" title="MatchingType">MatchingType</a>" : <i>String</i>,
    "<a href="#dictionary" title="Dictionary">Dictionary</a>" : <i>[ <a href="dictionarydefinition.md">DictionaryDefinition</a>, ... ]</i>,
    "<a href="#excludeinfotypes" title="ExcludeInfoTypes">ExcludeInfoTypes</a>" : <i>[ <a href="excludeinfotypesdefinition.md">ExcludeInfoTypesDefinition</a>, ... ]</i>,
    "<a href="#regex" title="Regex">Regex</a>" : <i>[ <a href="regexdefinition.md">RegexDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#matchingtype" title="MatchingType">MatchingType</a>: <i>String</i>
<a href="#dictionary" title="Dictionary">Dictionary</a>: <i>
      - <a href="dictionarydefinition.md">DictionaryDefinition</a></i>
<a href="#excludeinfotypes" title="ExcludeInfoTypes">ExcludeInfoTypes</a>: <i>
      - <a href="excludeinfotypesdefinition.md">ExcludeInfoTypesDefinition</a></i>
<a href="#regex" title="Regex">Regex</a>: <i>
      - <a href="regexdefinition.md">RegexDefinition</a></i>
</pre>

## Properties

#### MatchingType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dictionary

_Required_: No

_Type_: List of <a href="dictionarydefinition.md">DictionaryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeInfoTypes

_Required_: No

_Type_: List of <a href="excludeinfotypesdefinition.md">ExcludeInfoTypesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Regex

_Required_: No

_Type_: List of <a href="regexdefinition.md">RegexDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

