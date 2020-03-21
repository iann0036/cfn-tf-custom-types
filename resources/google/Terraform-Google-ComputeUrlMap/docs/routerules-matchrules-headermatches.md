# Terraform::Google::ComputeUrlMap RouteRules MatchRules HeaderMatches

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#exactmatch" title="ExactMatch">ExactMatch</a>" : <i>String</i>,
    "<a href="#headername" title="HeaderName">HeaderName</a>" : <i>String</i>,
    "<a href="#invertmatch" title="InvertMatch">InvertMatch</a>" : <i>Boolean</i>,
    "<a href="#prefixmatch" title="PrefixMatch">PrefixMatch</a>" : <i>String</i>,
    "<a href="#presentmatch" title="PresentMatch">PresentMatch</a>" : <i>Boolean</i>,
    "<a href="#regexmatch" title="RegexMatch">RegexMatch</a>" : <i>String</i>,
    "<a href="#suffixmatch" title="SuffixMatch">SuffixMatch</a>" : <i>String</i>,
    "<a href="#rangematch" title="RangeMatch">RangeMatch</a>" : <i>[ <a href="routerules-matchrules-headermatches-rangematch.md">RangeMatch</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#exactmatch" title="ExactMatch">ExactMatch</a>: <i>String</i>
<a href="#headername" title="HeaderName">HeaderName</a>: <i>String</i>
<a href="#invertmatch" title="InvertMatch">InvertMatch</a>: <i>Boolean</i>
<a href="#prefixmatch" title="PrefixMatch">PrefixMatch</a>: <i>String</i>
<a href="#presentmatch" title="PresentMatch">PresentMatch</a>: <i>Boolean</i>
<a href="#regexmatch" title="RegexMatch">RegexMatch</a>: <i>String</i>
<a href="#suffixmatch" title="SuffixMatch">SuffixMatch</a>: <i>String</i>
<a href="#rangematch" title="RangeMatch">RangeMatch</a>: <i>
      - <a href="routerules-matchrules-headermatches-rangematch.md">RangeMatch</a></i>
</pre>

## Properties

#### ExactMatch

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderName

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InvertMatch

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefixMatch

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PresentMatch

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegexMatch

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SuffixMatch

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RangeMatch

_Required_: No
_Type_: List of <a href="routerules-matchrules-headermatches-rangematch.md">RangeMatch</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

