# TF::AWS::Apigatewayv2Stage RouteSettingsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#datatraceenabled" title="DataTraceEnabled">DataTraceEnabled</a>" : <i>Boolean</i>,
    "<a href="#detailedmetricsenabled" title="DetailedMetricsEnabled">DetailedMetricsEnabled</a>" : <i>Boolean</i>,
    "<a href="#logginglevel" title="LoggingLevel">LoggingLevel</a>" : <i>String</i>,
    "<a href="#routekey" title="RouteKey">RouteKey</a>" : <i>String</i>,
    "<a href="#throttlingburstlimit" title="ThrottlingBurstLimit">ThrottlingBurstLimit</a>" : <i>Double</i>,
    "<a href="#throttlingratelimit" title="ThrottlingRateLimit">ThrottlingRateLimit</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#datatraceenabled" title="DataTraceEnabled">DataTraceEnabled</a>: <i>Boolean</i>
<a href="#detailedmetricsenabled" title="DetailedMetricsEnabled">DetailedMetricsEnabled</a>: <i>Boolean</i>
<a href="#logginglevel" title="LoggingLevel">LoggingLevel</a>: <i>String</i>
<a href="#routekey" title="RouteKey">RouteKey</a>: <i>String</i>
<a href="#throttlingburstlimit" title="ThrottlingBurstLimit">ThrottlingBurstLimit</a>: <i>Double</i>
<a href="#throttlingratelimit" title="ThrottlingRateLimit">ThrottlingRateLimit</a>: <i>Double</i>
</pre>

## Properties

#### DataTraceEnabled

Whether data trace logging is enabled for the route. Affects the log entries pushed to Amazon CloudWatch Logs.
Defaults to `false`. Supported only for WebSocket APIs.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DetailedMetricsEnabled

Whether detailed metrics are enabled for the route. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingLevel

The logging level for the route. Affects the log entries pushed to Amazon CloudWatch Logs.
Valid values: `ERROR`, `INFO`, `OFF`. Defaults to `OFF`. Supported only for WebSocket APIs. Terraform will only perform drift detection of its value when present in a configuration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteKey

Route key.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThrottlingBurstLimit

The throttling burst limit for the route.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThrottlingRateLimit

The throttling rate limit for the route.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

