# TF::LaunchDarkly::FeatureFlagEnvironment RulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bucketby" title="BucketBy">BucketBy</a>" : <i>String</i>,
    "<a href="#rolloutweights" title="RolloutWeights">RolloutWeights</a>" : <i>[ Double, ... ]</i>,
    "<a href="#variation" title="Variation">Variation</a>" : <i>Double</i>,
    "<a href="#clauses" title="Clauses">Clauses</a>" : <i>[ <a href="clausesdefinition.md">ClausesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#bucketby" title="BucketBy">BucketBy</a>: <i>String</i>
<a href="#rolloutweights" title="RolloutWeights">RolloutWeights</a>: <i>
      - Double</i>
<a href="#variation" title="Variation">Variation</a>: <i>Double</i>
<a href="#clauses" title="Clauses">Clauses</a>: <i>
      - <a href="clausesdefinition.md">ClausesDefinition</a></i>
</pre>

## Properties

#### BucketBy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RolloutWeights

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Variation

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Clauses

_Required_: No

_Type_: List of <a href="clausesdefinition.md">ClausesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

