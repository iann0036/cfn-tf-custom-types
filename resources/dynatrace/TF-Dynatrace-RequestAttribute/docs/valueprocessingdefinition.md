# TF::Dynatrace::RequestAttribute ValueProcessingDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#splitat" title="SplitAt">SplitAt</a>" : <i>String</i>,
    "<a href="#trim" title="Trim">Trim</a>" : <i>Boolean</i>,
    "<a href="#unknowns" title="Unknowns">Unknowns</a>" : <i>String</i>,
    "<a href="#valueextractorregex" title="ValueExtractorRegex">ValueExtractorRegex</a>" : <i>String</i>,
    "<a href="#extractsubstring" title="ExtractSubstring">ExtractSubstring</a>" : <i>[ <a href="extractsubstringdefinition.md">ExtractSubstringDefinition</a>, ... ]</i>,
    "<a href="#valuecondition" title="ValueCondition">ValueCondition</a>" : <i>[ <a href="valueconditiondefinition.md">ValueConditionDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#splitat" title="SplitAt">SplitAt</a>: <i>String</i>
<a href="#trim" title="Trim">Trim</a>: <i>Boolean</i>
<a href="#unknowns" title="Unknowns">Unknowns</a>: <i>String</i>
<a href="#valueextractorregex" title="ValueExtractorRegex">ValueExtractorRegex</a>: <i>String</i>
<a href="#extractsubstring" title="ExtractSubstring">ExtractSubstring</a>: <i>
      - <a href="extractsubstringdefinition.md">ExtractSubstringDefinition</a></i>
<a href="#valuecondition" title="ValueCondition">ValueCondition</a>: <i>
      - <a href="valueconditiondefinition.md">ValueConditionDefinition</a></i>
</pre>

## Properties

#### SplitAt

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trim

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unknowns

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValueExtractorRegex

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtractSubstring

_Required_: No

_Type_: List of <a href="extractsubstringdefinition.md">ExtractSubstringDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValueCondition

_Required_: No

_Type_: List of <a href="valueconditiondefinition.md">ValueConditionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

