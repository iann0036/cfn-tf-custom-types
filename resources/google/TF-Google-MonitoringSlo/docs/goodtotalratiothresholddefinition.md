# TF::Google::MonitoringSlo GoodTotalRatioThresholdDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#threshold" title="Threshold">Threshold</a>" : <i>Double</i>,
    "<a href="#basicsliperformance" title="BasicSliPerformance">BasicSliPerformance</a>" : <i>[ <a href="basicsliperformancedefinition.md">BasicSliPerformanceDefinition</a>, ... ]</i>,
    "<a href="#performance" title="Performance">Performance</a>" : <i>[ <a href="performancedefinition.md">PerformanceDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#threshold" title="Threshold">Threshold</a>: <i>Double</i>
<a href="#basicsliperformance" title="BasicSliPerformance">BasicSliPerformance</a>: <i>
      - <a href="basicsliperformancedefinition.md">BasicSliPerformanceDefinition</a></i>
<a href="#performance" title="Performance">Performance</a>: <i>
      - <a href="performancedefinition.md">PerformanceDefinition</a></i>
</pre>

## Properties

#### Threshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BasicSliPerformance

_Required_: No

_Type_: List of <a href="basicsliperformancedefinition.md">BasicSliPerformanceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Performance

_Required_: No

_Type_: List of <a href="performancedefinition.md">PerformanceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

