# TF::AWS::Apigatewayv2Stage DefaultRouteSettingsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#datatraceenabled" title="DataTraceEnabled">DataTraceEnabled</a>" : <i>Boolean</i>,
    "<a href="#detailedmetricsenabled" title="DetailedMetricsEnabled">DetailedMetricsEnabled</a>" : <i>Boolean</i>,
    "<a href="#logginglevel" title="LoggingLevel">LoggingLevel</a>" : <i>String</i>,
    "<a href="#throttlingburstlimit" title="ThrottlingBurstLimit">ThrottlingBurstLimit</a>" : <i>Double</i>,
    "<a href="#throttlingratelimit" title="ThrottlingRateLimit">ThrottlingRateLimit</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#datatraceenabled" title="DataTraceEnabled">DataTraceEnabled</a>: <i>Boolean</i>
<a href="#detailedmetricsenabled" title="DetailedMetricsEnabled">DetailedMetricsEnabled</a>: <i>Boolean</i>
<a href="#logginglevel" title="LoggingLevel">LoggingLevel</a>: <i>String</i>
<a href="#throttlingburstlimit" title="ThrottlingBurstLimit">ThrottlingBurstLimit</a>: <i>Double</i>
<a href="#throttlingratelimit" title="ThrottlingRateLimit">ThrottlingRateLimit</a>: <i>Double</i>
</pre>

## Properties

#### DataTraceEnabled

Whether data trace logging is enabled for the default route. Affects the log entries pushed to Amazon CloudWatch Logs.
Defaults to `false`. Supported only for WebSocket APIs.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DetailedMetricsEnabled

Whether detailed metrics are enabled for the default route. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingLevel

The logging level for the default route. Affects the log entries pushed to Amazon CloudWatch Logs.
Valid values: `ERROR`, `INFO`, `OFF`. Defaults to `OFF`. Supported only for WebSocket APIs. Terraform will only perform drift detection of its value when present in a configuration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThrottlingBurstLimit

The throttling burst limit for the default route.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThrottlingRateLimit

The throttling rate limit for the default route.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

