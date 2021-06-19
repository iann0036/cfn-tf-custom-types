# TF::Datadog::Dashboard ApmQueryDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#index" title="Index">Index</a>" : <i>String</i>,
    "<a href="#searchquery" title="SearchQuery">SearchQuery</a>" : <i>String</i>,
    "<a href="#computequery" title="ComputeQuery">ComputeQuery</a>" : <i>[ <a href="computequerydefinition.md">ComputeQueryDefinition</a>, ... ]</i>,
    "<a href="#groupby" title="GroupBy">GroupBy</a>" : <i>[ <a href="groupbydefinition.md">GroupByDefinition</a>, ... ]</i>,
    "<a href="#multicompute" title="MultiCompute">MultiCompute</a>" : <i>[ <a href="multicomputedefinition.md">MultiComputeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#index" title="Index">Index</a>: <i>String</i>
<a href="#searchquery" title="SearchQuery">SearchQuery</a>: <i>String</i>
<a href="#computequery" title="ComputeQuery">ComputeQuery</a>: <i>
      - <a href="computequerydefinition.md">ComputeQueryDefinition</a></i>
<a href="#groupby" title="GroupBy">GroupBy</a>: <i>
      - <a href="groupbydefinition.md">GroupByDefinition</a></i>
<a href="#multicompute" title="MultiCompute">MultiCompute</a>: <i>
      - <a href="multicomputedefinition.md">MultiComputeDefinition</a></i>
</pre>

## Properties

#### Index

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SearchQuery

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComputeQuery

_Required_: No

_Type_: List of <a href="computequerydefinition.md">ComputeQueryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupBy

_Required_: No

_Type_: List of <a href="groupbydefinition.md">GroupByDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MultiCompute

_Required_: No

_Type_: List of <a href="multicomputedefinition.md">MultiComputeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

