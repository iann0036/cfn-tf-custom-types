# TF::GoogleBeta::GoogleDataLossPreventionInspectTemplate InspectConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#contentoptions" title="ContentOptions">ContentOptions</a>" : <i>[ String, ... ]</i>,
    "<a href="#excludeinfotypes" title="ExcludeInfoTypes">ExcludeInfoTypes</a>" : <i>Boolean</i>,
    "<a href="#includequote" title="IncludeQuote">IncludeQuote</a>" : <i>Boolean</i>,
    "<a href="#minlikelihood" title="MinLikelihood">MinLikelihood</a>" : <i>String</i>,
    "<a href="#custominfotypes" title="CustomInfoTypes">CustomInfoTypes</a>" : <i>[ <a href="custominfotypesdefinition.md">CustomInfoTypesDefinition</a>, ... ]</i>,
    "<a href="#infotypes" title="InfoTypes">InfoTypes</a>" : <i>[ <a href="infotypesdefinition.md">InfoTypesDefinition</a>, ... ]</i>,
    "<a href="#limits" title="Limits">Limits</a>" : <i>[ <a href="limitsdefinition.md">LimitsDefinition</a>, ... ]</i>,
    "<a href="#ruleset" title="RuleSet">RuleSet</a>" : <i>[ <a href="rulesetdefinition.md">RuleSetDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#contentoptions" title="ContentOptions">ContentOptions</a>: <i>
      - String</i>
<a href="#excludeinfotypes" title="ExcludeInfoTypes">ExcludeInfoTypes</a>: <i>Boolean</i>
<a href="#includequote" title="IncludeQuote">IncludeQuote</a>: <i>Boolean</i>
<a href="#minlikelihood" title="MinLikelihood">MinLikelihood</a>: <i>String</i>
<a href="#custominfotypes" title="CustomInfoTypes">CustomInfoTypes</a>: <i>
      - <a href="custominfotypesdefinition.md">CustomInfoTypesDefinition</a></i>
<a href="#infotypes" title="InfoTypes">InfoTypes</a>: <i>
      - <a href="infotypesdefinition.md">InfoTypesDefinition</a></i>
<a href="#limits" title="Limits">Limits</a>: <i>
      - <a href="limitsdefinition.md">LimitsDefinition</a></i>
<a href="#ruleset" title="RuleSet">RuleSet</a>: <i>
      - <a href="rulesetdefinition.md">RuleSetDefinition</a></i>
</pre>

## Properties

#### ContentOptions

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeInfoTypes

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeQuote

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinLikelihood

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomInfoTypes

_Required_: No

_Type_: List of <a href="custominfotypesdefinition.md">CustomInfoTypesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InfoTypes

_Required_: No

_Type_: List of <a href="infotypesdefinition.md">InfoTypesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Limits

_Required_: No

_Type_: List of <a href="limitsdefinition.md">LimitsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleSet

_Required_: No

_Type_: List of <a href="rulesetdefinition.md">RuleSetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

