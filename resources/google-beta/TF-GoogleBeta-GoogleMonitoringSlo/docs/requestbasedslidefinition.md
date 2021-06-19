# TF::GoogleBeta::GoogleMonitoringSlo RequestBasedSliDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#distributioncut" title="DistributionCut">DistributionCut</a>" : <i>[ <a href="distributioncutdefinition.md">DistributionCutDefinition</a>, ... ]</i>,
    "<a href="#goodtotalratio" title="GoodTotalRatio">GoodTotalRatio</a>" : <i>[ <a href="goodtotalratiodefinition.md">GoodTotalRatioDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#distributioncut" title="DistributionCut">DistributionCut</a>: <i>
      - <a href="distributioncutdefinition.md">DistributionCutDefinition</a></i>
<a href="#goodtotalratio" title="GoodTotalRatio">GoodTotalRatio</a>: <i>
      - <a href="goodtotalratiodefinition.md">GoodTotalRatioDefinition</a></i>
</pre>

## Properties

#### DistributionCut

_Required_: No

_Type_: List of <a href="distributioncutdefinition.md">DistributionCutDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GoodTotalRatio

_Required_: No

_Type_: List of <a href="goodtotalratiodefinition.md">GoodTotalRatioDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

