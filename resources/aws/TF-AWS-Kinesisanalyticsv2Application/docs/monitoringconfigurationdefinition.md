# TF::AWS::Kinesisanalyticsv2Application MonitoringConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#configurationtype" title="ConfigurationType">ConfigurationType</a>" : <i>String</i>,
    "<a href="#loglevel" title="LogLevel">LogLevel</a>" : <i>String</i>,
    "<a href="#metricslevel" title="MetricsLevel">MetricsLevel</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#configurationtype" title="ConfigurationType">ConfigurationType</a>: <i>String</i>
<a href="#loglevel" title="LogLevel">LogLevel</a>: <i>String</i>
<a href="#metricslevel" title="MetricsLevel">MetricsLevel</a>: <i>String</i>
</pre>

## Properties

#### ConfigurationType

Describes whether to use the default CloudWatch logging configuration for an application. Valid values: `CUSTOM`, `DEFAULT`. Set this attribute to `CUSTOM` in order for any specified `log_level` or `metrics_level` attribute values to be effective.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogLevel

Describes the verbosity of the CloudWatch Logs for an application. Valid values: `DEBUG`, `ERROR`, `INFO`, `WARN`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricsLevel

Describes the granularity of the CloudWatch Logs for an application. Valid values: `APPLICATION`, `OPERATOR`, `PARALLELISM`, `TASK`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

