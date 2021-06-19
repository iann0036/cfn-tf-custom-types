# TF::AWS::Route53HealthCheck

Provides a Route53 health check.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::Route53HealthCheck",
    "Properties" : {
        "<a href="#childhealththreshold" title="ChildHealthThreshold">ChildHealthThreshold</a>" : <i>Double</i>,
        "<a href="#childhealthchecks" title="ChildHealthchecks">ChildHealthchecks</a>" : <i>[ String, ... ]</i>,
        "<a href="#cloudwatchalarmname" title="CloudwatchAlarmName">CloudwatchAlarmName</a>" : <i>String</i>,
        "<a href="#cloudwatchalarmregion" title="CloudwatchAlarmRegion">CloudwatchAlarmRegion</a>" : <i>String</i>,
        "<a href="#disabled" title="Disabled">Disabled</a>" : <i>Boolean</i>,
        "<a href="#enablesni" title="EnableSni">EnableSni</a>" : <i>Boolean</i>,
        "<a href="#failurethreshold" title="FailureThreshold">FailureThreshold</a>" : <i>Double</i>,
        "<a href="#fqdn" title="Fqdn">Fqdn</a>" : <i>String</i>,
        "<a href="#insufficientdatahealthstatus" title="InsufficientDataHealthStatus">InsufficientDataHealthStatus</a>" : <i>String</i>,
        "<a href="#inverthealthcheck" title="InvertHealthcheck">InvertHealthcheck</a>" : <i>Boolean</i>,
        "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>String</i>,
        "<a href="#measurelatency" title="MeasureLatency">MeasureLatency</a>" : <i>Boolean</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#referencename" title="ReferenceName">ReferenceName</a>" : <i>String</i>,
        "<a href="#regions" title="Regions">Regions</a>" : <i>[ String, ... ]</i>,
        "<a href="#requestinterval" title="RequestInterval">RequestInterval</a>" : <i>Double</i>,
        "<a href="#resourcepath" title="ResourcePath">ResourcePath</a>" : <i>String</i>,
        "<a href="#searchstring" title="SearchString">SearchString</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::Route53HealthCheck
Properties:
    <a href="#childhealththreshold" title="ChildHealthThreshold">ChildHealthThreshold</a>: <i>Double</i>
    <a href="#childhealthchecks" title="ChildHealthchecks">ChildHealthchecks</a>: <i>
      - String</i>
    <a href="#cloudwatchalarmname" title="CloudwatchAlarmName">CloudwatchAlarmName</a>: <i>String</i>
    <a href="#cloudwatchalarmregion" title="CloudwatchAlarmRegion">CloudwatchAlarmRegion</a>: <i>String</i>
    <a href="#disabled" title="Disabled">Disabled</a>: <i>Boolean</i>
    <a href="#enablesni" title="EnableSni">EnableSni</a>: <i>Boolean</i>
    <a href="#failurethreshold" title="FailureThreshold">FailureThreshold</a>: <i>Double</i>
    <a href="#fqdn" title="Fqdn">Fqdn</a>: <i>String</i>
    <a href="#insufficientdatahealthstatus" title="InsufficientDataHealthStatus">InsufficientDataHealthStatus</a>: <i>String</i>
    <a href="#inverthealthcheck" title="InvertHealthcheck">InvertHealthcheck</a>: <i>Boolean</i>
    <a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>String</i>
    <a href="#measurelatency" title="MeasureLatency">MeasureLatency</a>: <i>Boolean</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#referencename" title="ReferenceName">ReferenceName</a>: <i>String</i>
    <a href="#regions" title="Regions">Regions</a>: <i>
      - String</i>
    <a href="#requestinterval" title="RequestInterval">RequestInterval</a>: <i>Double</i>
    <a href="#resourcepath" title="ResourcePath">ResourcePath</a>: <i>String</i>
    <a href="#searchstring" title="SearchString">SearchString</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### ChildHealthThreshold

The minimum number of child health checks that must be healthy for Route 53 to consider the parent health check to be healthy. Valid values are integers between 0 and 256, inclusive.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChildHealthchecks

For a specified parent health check, a list of HealthCheckId values for the associated child health checks.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudwatchAlarmName

The name of the CloudWatch alarm.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudwatchAlarmRegion

The CloudWatchRegion that the CloudWatch alarm was created in.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disabled

A boolean value that stops Route 53 from performing health checks. When set to true, Route 53 will do the following depending on the type of health check:
* For health checks that check the health of endpoints, Route5 53 stops submitting requests to your application, server, or other resource.
* For calculated health checks, Route 53 stops aggregating the status of the referenced health checks.
* For health checks that monitor CloudWatch alarms, Route 53 stops monitoring the corresponding CloudWatch metrics.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableSni

A boolean value that indicates whether Route53 should send the `fqdn` to the endpoint when performing the health check. This defaults to AWS' defaults: when the `type` is "HTTPS" `enable_sni` defaults to `true`, when `type` is anything else `enable_sni` defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailureThreshold

The number of consecutive health checks that an endpoint must pass or fail.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fqdn

The fully qualified domain name of the endpoint to be checked.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsufficientDataHealthStatus

The status of the health check when CloudWatch has insufficient data about the state of associated alarm. Valid values are `Healthy` , `Unhealthy` and `LastKnownStatus`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InvertHealthcheck

A boolean value that indicates whether the status of health check should be inverted. For example, if a health check is healthy but Inverted is True , then Route 53 considers the health check to be unhealthy.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddress

The IP address of the endpoint to be checked.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MeasureLatency

A Boolean value that indicates whether you want Route 53 to measure the latency between health checkers in multiple AWS regions and your endpoint and to display CloudWatch latency graphs in the Route 53 console.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

The port of the endpoint to be checked.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReferenceName

This is a reference name used in Caller Reference
(helpful for identifying single health_check set amongst others).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Regions

A list of AWS regions that you want Amazon Route 53 health checkers to check the specified endpoint from.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestInterval

The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health-check request.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourcePath

The path that you want Amazon Route 53 to request when performing health checks.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SearchString

String searched in the first 5120 bytes of the response body for check to be considered healthy. Only valid with `HTTP_STR_MATCH` and `HTTPS_STR_MATCH`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A map of tags to assign to the health check. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The protocol to use when performing health checks. Valid values are `HTTP`, `HTTPS`, `HTTP_STR_MATCH`, `HTTPS_STR_MATCH`, `TCP`, `CALCULATED` and `CLOUDWATCH_METRIC`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

