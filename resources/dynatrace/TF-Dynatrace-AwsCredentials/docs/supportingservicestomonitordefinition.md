# TF::Dynatrace::AwsCredentials SupportingServicesToMonitorDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#unknowns" title="Unknowns">Unknowns</a>" : <i>String</i>,
    "<a href="#monitoredmetrics" title="MonitoredMetrics">MonitoredMetrics</a>" : <i>[ <a href="monitoredmetricsdefinition.md">MonitoredMetricsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#unknowns" title="Unknowns">Unknowns</a>: <i>String</i>
<a href="#monitoredmetrics" title="MonitoredMetrics">MonitoredMetrics</a>: <i>
      - <a href="monitoredmetricsdefinition.md">MonitoredMetricsDefinition</a></i>
</pre>

## Properties

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unknowns

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitoredMetrics

_Required_: No

_Type_: List of <a href="monitoredmetricsdefinition.md">MonitoredMetricsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

