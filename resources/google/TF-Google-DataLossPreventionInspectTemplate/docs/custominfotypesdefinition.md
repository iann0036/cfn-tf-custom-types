# TF::Google::DataLossPreventionInspectTemplate CustomInfoTypesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#exclusiontype" title="ExclusionType">ExclusionType</a>" : <i>String</i>,
    "<a href="#likelihood" title="Likelihood">Likelihood</a>" : <i>String</i>,
    "<a href="#dictionary" title="Dictionary">Dictionary</a>" : <i>[ <a href="dictionarydefinition.md">DictionaryDefinition</a>, ... ]</i>,
    "<a href="#infotype" title="InfoType">InfoType</a>" : <i>[ <a href="infotypedefinition.md">InfoTypeDefinition</a>, ... ]</i>,
    "<a href="#regex" title="Regex">Regex</a>" : <i>[ <a href="regexdefinition.md">RegexDefinition</a>, ... ]</i>,
    "<a href="#storedtype" title="StoredType">StoredType</a>" : <i>[ <a href="storedtypedefinition.md">StoredTypeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#exclusiontype" title="ExclusionType">ExclusionType</a>: <i>String</i>
<a href="#likelihood" title="Likelihood">Likelihood</a>: <i>String</i>
<a href="#dictionary" title="Dictionary">Dictionary</a>: <i>
      - <a href="dictionarydefinition.md">DictionaryDefinition</a></i>
<a href="#infotype" title="InfoType">InfoType</a>: <i>
      - <a href="infotypedefinition.md">InfoTypeDefinition</a></i>
<a href="#regex" title="Regex">Regex</a>: <i>
      - <a href="regexdefinition.md">RegexDefinition</a></i>
<a href="#storedtype" title="StoredType">StoredType</a>: <i>
      - <a href="storedtypedefinition.md">StoredTypeDefinition</a></i>
</pre>

## Properties

#### ExclusionType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Likelihood

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dictionary

_Required_: No

_Type_: List of <a href="dictionarydefinition.md">DictionaryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InfoType

_Required_: No

_Type_: List of <a href="infotypedefinition.md">InfoTypeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Regex

_Required_: No

_Type_: List of <a href="regexdefinition.md">RegexDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StoredType

_Required_: No

_Type_: List of <a href="storedtypedefinition.md">StoredTypeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

