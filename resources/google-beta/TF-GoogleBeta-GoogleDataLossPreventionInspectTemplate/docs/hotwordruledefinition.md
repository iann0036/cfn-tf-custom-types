# TF::GoogleBeta::GoogleDataLossPreventionInspectTemplate HotwordRuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#hotwordregex" title="HotwordRegex">HotwordRegex</a>" : <i>[ <a href="hotwordregexdefinition.md">HotwordRegexDefinition</a>, ... ]</i>,
    "<a href="#likelihoodadjustment" title="LikelihoodAdjustment">LikelihoodAdjustment</a>" : <i>[ <a href="likelihoodadjustmentdefinition.md">LikelihoodAdjustmentDefinition</a>, ... ]</i>,
    "<a href="#proximity" title="Proximity">Proximity</a>" : <i>[ <a href="proximitydefinition.md">ProximityDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#hotwordregex" title="HotwordRegex">HotwordRegex</a>: <i>
      - <a href="hotwordregexdefinition.md">HotwordRegexDefinition</a></i>
<a href="#likelihoodadjustment" title="LikelihoodAdjustment">LikelihoodAdjustment</a>: <i>
      - <a href="likelihoodadjustmentdefinition.md">LikelihoodAdjustmentDefinition</a></i>
<a href="#proximity" title="Proximity">Proximity</a>: <i>
      - <a href="proximitydefinition.md">ProximityDefinition</a></i>
</pre>

## Properties

#### HotwordRegex

_Required_: No

_Type_: List of <a href="hotwordregexdefinition.md">HotwordRegexDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LikelihoodAdjustment

_Required_: No

_Type_: List of <a href="likelihoodadjustmentdefinition.md">LikelihoodAdjustmentDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Proximity

_Required_: No

_Type_: List of <a href="proximitydefinition.md">ProximityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

