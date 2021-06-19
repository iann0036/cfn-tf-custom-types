# TF::Datadog::Dashboard QueryDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#eventquery" title="EventQuery">EventQuery</a>" : <i>[ <a href="eventquerydefinition.md">EventQueryDefinition</a>, ... ]</i>,
    "<a href="#metricquery" title="MetricQuery">MetricQuery</a>" : <i>[ <a href="metricquerydefinition.md">MetricQueryDefinition</a>, ... ]</i>,
    "<a href="#processquery" title="ProcessQuery">ProcessQuery</a>" : <i>[ <a href="processquerydefinition.md">ProcessQueryDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#eventquery" title="EventQuery">EventQuery</a>: <i>
      - <a href="eventquerydefinition.md">EventQueryDefinition</a></i>
<a href="#metricquery" title="MetricQuery">MetricQuery</a>: <i>
      - <a href="metricquerydefinition.md">MetricQueryDefinition</a></i>
<a href="#processquery" title="ProcessQuery">ProcessQuery</a>: <i>
      - <a href="processquerydefinition.md">ProcessQueryDefinition</a></i>
</pre>

## Properties

#### EventQuery

_Required_: No

_Type_: List of <a href="eventquerydefinition.md">EventQueryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricQuery

_Required_: No

_Type_: List of <a href="metricquerydefinition.md">MetricQueryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessQuery

_Required_: No

_Type_: List of <a href="processquerydefinition.md">ProcessQueryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

