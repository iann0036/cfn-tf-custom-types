# TF::Dynatrace::Dashboard DynamicFiltersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#filters" title="Filters">Filters</a>" : <i>[ String, ... ]</i>,
    "<a href="#tagsuggestiontypes" title="TagSuggestionTypes">TagSuggestionTypes</a>" : <i>[ String, ... ]</i>,
    "<a href="#unknowns" title="Unknowns">Unknowns</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#filters" title="Filters">Filters</a>: <i>
      - String</i>
<a href="#tagsuggestiontypes" title="TagSuggestionTypes">TagSuggestionTypes</a>: <i>
      - String</i>
<a href="#unknowns" title="Unknowns">Unknowns</a>: <i>String</i>
</pre>

## Properties

#### Filters

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagSuggestionTypes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unknowns

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

