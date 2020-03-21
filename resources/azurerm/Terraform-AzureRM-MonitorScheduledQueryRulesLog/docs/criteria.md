# Terraform::AzureRM::MonitorScheduledQueryRulesLog Criteria

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#metricname" title="MetricName">MetricName</a>" : <i>String</i>,
    "<a href="#dimension" title="Dimension">Dimension</a>" : <i>[ <a href="criteria-dimension.md">Dimension</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#metricname" title="MetricName">MetricName</a>: <i>String</i>
<a href="#dimension" title="Dimension">Dimension</a>: <i>
      - <a href="criteria-dimension.md">Dimension</a></i>
</pre>

## Properties

#### MetricName

Name of the metric.  Supported metrics are listed in the Azure Monitor [Microsoft.OperationalInsights/workspaces](https://docs.microsoft.com/en-us/azure/azure-monitor/platform/metrics-supported#microsoftoperationalinsightsworkspaces) metrics namespace.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dimension

_Required_: No

_Type_: List of <a href="criteria-dimension.md">Dimension</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

