# TF::SumoLogic::Dashboard MetricsQueryDataDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#aggregationtype" title="AggregationType">AggregationType</a>" : <i>String</i>,
    "<a href="#groupby" title="GroupBy">GroupBy</a>" : <i>String</i>,
    "<a href="#metric" title="Metric">Metric</a>" : <i>String</i>,
    "<a href="#filter" title="Filter">Filter</a>" : <i>[ <a href="filterdefinition.md">FilterDefinition</a>, ... ]</i>,
    "<a href="#operator" title="Operator">Operator</a>" : <i>[ <a href="operatordefinition.md">OperatorDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#aggregationtype" title="AggregationType">AggregationType</a>: <i>String</i>
<a href="#groupby" title="GroupBy">GroupBy</a>: <i>String</i>
<a href="#metric" title="Metric">Metric</a>: <i>String</i>
<a href="#filter" title="Filter">Filter</a>: <i>
      - <a href="filterdefinition.md">FilterDefinition</a></i>
<a href="#operator" title="Operator">Operator</a>: <i>
      - <a href="operatordefinition.md">OperatorDefinition</a></i>
</pre>

## Properties

#### AggregationType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupBy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metric

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

_Required_: No

_Type_: List of <a href="filterdefinition.md">FilterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Operator

_Required_: No

_Type_: List of <a href="operatordefinition.md">OperatorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

