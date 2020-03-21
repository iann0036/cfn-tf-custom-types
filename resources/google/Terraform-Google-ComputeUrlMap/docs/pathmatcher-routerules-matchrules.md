# Terraform::Google::ComputeUrlMap PathMatcher RouteRules MatchRules

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#fullpathmatch" title="FullPathMatch">FullPathMatch</a>" : <i>String</i>,
    "<a href="#ignorecase" title="IgnoreCase">IgnoreCase</a>" : <i>Boolean</i>,
    "<a href="#prefixmatch" title="PrefixMatch">PrefixMatch</a>" : <i>String</i>,
    "<a href="#regexmatch" title="RegexMatch">RegexMatch</a>" : <i>String</i>,
    "<a href="#headermatches" title="HeaderMatches">HeaderMatches</a>" : <i>[ &lt;a href=&#34;pathmatcher-routerules-matchrules-headermatches.md&#34;&gt;HeaderMatches&lt;/a&gt;, ... ]</i>,
    "<a href="#metadatafilters" title="MetadataFilters">MetadataFilters</a>" : <i>[ &lt;a href=&#34;pathmatcher-routerules-matchrules-metadatafilters.md&#34;&gt;MetadataFilters&lt;/a&gt;, ... ]</i>,
    "<a href="#queryparametermatches" title="QueryParameterMatches">QueryParameterMatches</a>" : <i>[ &lt;a href=&#34;pathmatcher-routerules-matchrules-queryparametermatches.md&#34;&gt;QueryParameterMatches&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#fullpathmatch" title="FullPathMatch">FullPathMatch</a>: <i>String</i>
<a href="#ignorecase" title="IgnoreCase">IgnoreCase</a>: <i>Boolean</i>
<a href="#prefixmatch" title="PrefixMatch">PrefixMatch</a>: <i>String</i>
<a href="#regexmatch" title="RegexMatch">RegexMatch</a>: <i>String</i>
<a href="#headermatches" title="HeaderMatches">HeaderMatches</a>: <i>
      - &lt;a href=&#34;pathmatcher-routerules-matchrules-headermatches.md&#34;&gt;HeaderMatches&lt;/a&gt;</i>
<a href="#metadatafilters" title="MetadataFilters">MetadataFilters</a>: <i>
      - &lt;a href=&#34;pathmatcher-routerules-matchrules-metadatafilters.md&#34;&gt;MetadataFilters&lt;/a&gt;</i>
<a href="#queryparametermatches" title="QueryParameterMatches">QueryParameterMatches</a>: <i>
      - &lt;a href=&#34;pathmatcher-routerules-matchrules-queryparametermatches.md&#34;&gt;QueryParameterMatches&lt;/a&gt;</i>
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
_Type_: List of &lt;a href=&#34;pathmatcher-routerules-matchrules-headermatches.md&#34;&gt;HeaderMatches&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetadataFilters

_Required_: No
_Type_: List of &lt;a href=&#34;pathmatcher-routerules-matchrules-metadatafilters.md&#34;&gt;MetadataFilters&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryParameterMatches

_Required_: No
_Type_: List of &lt;a href=&#34;pathmatcher-routerules-matchrules-queryparametermatches.md&#34;&gt;QueryParameterMatches&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

