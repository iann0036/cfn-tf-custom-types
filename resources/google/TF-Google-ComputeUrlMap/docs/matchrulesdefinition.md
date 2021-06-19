# TF::Google::ComputeUrlMap MatchRulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#fullpathmatch" title="FullPathMatch">FullPathMatch</a>" : <i>String</i>,
    "<a href="#ignorecase" title="IgnoreCase">IgnoreCase</a>" : <i>Boolean</i>,
    "<a href="#prefixmatch" title="PrefixMatch">PrefixMatch</a>" : <i>String</i>,
    "<a href="#regexmatch" title="RegexMatch">RegexMatch</a>" : <i>String</i>,
    "<a href="#headermatches" title="HeaderMatches">HeaderMatches</a>" : <i>[ <a href="headermatchesdefinition.md">HeaderMatchesDefinition</a>, ... ]</i>,
    "<a href="#metadatafilters" title="MetadataFilters">MetadataFilters</a>" : <i>[ <a href="metadatafiltersdefinition.md">MetadataFiltersDefinition</a>, ... ]</i>,
    "<a href="#queryparametermatches" title="QueryParameterMatches">QueryParameterMatches</a>" : <i>[ <a href="queryparametermatchesdefinition.md">QueryParameterMatchesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#fullpathmatch" title="FullPathMatch">FullPathMatch</a>: <i>String</i>
<a href="#ignorecase" title="IgnoreCase">IgnoreCase</a>: <i>Boolean</i>
<a href="#prefixmatch" title="PrefixMatch">PrefixMatch</a>: <i>String</i>
<a href="#regexmatch" title="RegexMatch">RegexMatch</a>: <i>String</i>
<a href="#headermatches" title="HeaderMatches">HeaderMatches</a>: <i>
      - <a href="headermatchesdefinition.md">HeaderMatchesDefinition</a></i>
<a href="#metadatafilters" title="MetadataFilters">MetadataFilters</a>: <i>
      - <a href="metadatafiltersdefinition.md">MetadataFiltersDefinition</a></i>
<a href="#queryparametermatches" title="QueryParameterMatches">QueryParameterMatches</a>: <i>
      - <a href="queryparametermatchesdefinition.md">QueryParameterMatchesDefinition</a></i>
</pre>

## Properties

#### FullPathMatch

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreCase

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefixMatch

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegexMatch

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderMatches

_Required_: No

_Type_: List of <a href="headermatchesdefinition.md">HeaderMatchesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetadataFilters

_Required_: No

_Type_: List of <a href="metadatafiltersdefinition.md">MetadataFiltersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryParameterMatches

_Required_: No

_Type_: List of <a href="queryparametermatchesdefinition.md">QueryParameterMatchesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

