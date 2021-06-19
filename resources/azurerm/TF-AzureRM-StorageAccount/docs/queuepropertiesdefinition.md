# TF::AzureRM::StorageAccount QueuePropertiesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#corsrule" title="CorsRule">CorsRule</a>" : <i>[ <a href="corsruledefinition.md">CorsRuleDefinition</a>, ... ]</i>,
    "<a href="#hourmetrics" title="HourMetrics">HourMetrics</a>" : <i>[ <a href="hourmetricsdefinition.md">HourMetricsDefinition</a>, ... ]</i>,
    "<a href="#logging" title="Logging">Logging</a>" : <i>[ <a href="loggingdefinition.md">LoggingDefinition</a>, ... ]</i>,
    "<a href="#minutemetrics" title="MinuteMetrics">MinuteMetrics</a>" : <i>[ <a href="minutemetricsdefinition.md">MinuteMetricsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#corsrule" title="CorsRule">CorsRule</a>: <i>
      - <a href="corsruledefinition.md">CorsRuleDefinition</a></i>
<a href="#hourmetrics" title="HourMetrics">HourMetrics</a>: <i>
      - <a href="hourmetricsdefinition.md">HourMetricsDefinition</a></i>
<a href="#logging" title="Logging">Logging</a>: <i>
      - <a href="loggingdefinition.md">LoggingDefinition</a></i>
<a href="#minutemetrics" title="MinuteMetrics">MinuteMetrics</a>: <i>
      - <a href="minutemetricsdefinition.md">MinuteMetricsDefinition</a></i>
</pre>

## Properties

#### CorsRule

_Required_: No

_Type_: List of <a href="corsruledefinition.md">CorsRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HourMetrics

_Required_: No

_Type_: List of <a href="hourmetricsdefinition.md">HourMetricsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logging

_Required_: No

_Type_: List of <a href="loggingdefinition.md">LoggingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinuteMetrics

_Required_: No

_Type_: List of <a href="minutemetricsdefinition.md">MinuteMetricsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

