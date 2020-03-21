# Terraform::AzureRM::StorageAccount QueueProperties

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#corsrule" title="CorsRule">CorsRule</a>" : <i>[ <a href="queueproperties-corsrule.md">CorsRule</a>, ... ]</i>,
    "<a href="#hourmetrics" title="HourMetrics">HourMetrics</a>" : <i>[ <a href="queueproperties-hourmetrics.md">HourMetrics</a>, ... ]</i>,
    "<a href="#logging" title="Logging">Logging</a>" : <i>[ <a href="queueproperties-logging.md">Logging</a>, ... ]</i>,
    "<a href="#minutemetrics" title="MinuteMetrics">MinuteMetrics</a>" : <i>[ <a href="queueproperties-minutemetrics.md">MinuteMetrics</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#corsrule" title="CorsRule">CorsRule</a>: <i>
      - <a href="queueproperties-corsrule.md">CorsRule</a></i>
<a href="#hourmetrics" title="HourMetrics">HourMetrics</a>: <i>
      - <a href="queueproperties-hourmetrics.md">HourMetrics</a></i>
<a href="#logging" title="Logging">Logging</a>: <i>
      - <a href="queueproperties-logging.md">Logging</a></i>
<a href="#minutemetrics" title="MinuteMetrics">MinuteMetrics</a>: <i>
      - <a href="queueproperties-minutemetrics.md">MinuteMetrics</a></i>
</pre>

## Properties

#### CorsRule

_Required_: No

_Type_: List of <a href="queueproperties-corsrule.md">CorsRule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HourMetrics

_Required_: No

_Type_: List of <a href="queueproperties-hourmetrics.md">HourMetrics</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logging

_Required_: No

_Type_: List of <a href="queueproperties-logging.md">Logging</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinuteMetrics

_Required_: No

_Type_: List of <a href="queueproperties-minutemetrics.md">MinuteMetrics</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

