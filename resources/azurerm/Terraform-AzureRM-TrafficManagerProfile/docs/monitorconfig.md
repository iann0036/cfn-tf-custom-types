# Terraform::AzureRM::TrafficManagerProfile MonitorConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#expectedstatuscoderanges" title="ExpectedStatusCodeRanges">ExpectedStatusCodeRanges</a>" : <i>[ String, ... ]</i>,
    "<a href="#intervalinseconds" title="IntervalInSeconds">IntervalInSeconds</a>" : <i>Double</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#timeoutinseconds" title="TimeoutInSeconds">TimeoutInSeconds</a>" : <i>Double</i>,
    "<a href="#toleratednumberoffailures" title="ToleratedNumberOfFailures">ToleratedNumberOfFailures</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#expectedstatuscoderanges" title="ExpectedStatusCodeRanges">ExpectedStatusCodeRanges</a>: <i>
      - String</i>
<a href="#intervalinseconds" title="IntervalInSeconds">IntervalInSeconds</a>: <i>Double</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#timeoutinseconds" title="TimeoutInSeconds">TimeoutInSeconds</a>: <i>Double</i>
<a href="#toleratednumberoffailures" title="ToleratedNumberOfFailures">ToleratedNumberOfFailures</a>: <i>Double</i>
</pre>

## Properties

#### ExpectedStatusCodeRanges

A list of status code ranges in the format of `100-101`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntervalInSeconds

The interval used to check the endpoint health from a Traffic Manager probing agent. You can specify two values here: `30` (normal probing) and `10` (fast probing). The default value is `30`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

The path used by the monitoring checks. Required when `protocol` is set to `HTTP` or `HTTPS` - cannot be set when `protocol` is set to `TCP`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

The port number used by the monitoring checks.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

The protocol used by the monitoring checks, supported values are `HTTP`, `HTTPS` and `TCP`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutInSeconds

The amount of time the Traffic Manager probing agent should wait before considering that check a failure when a health check probe is sent to the endpoint. If `interval_in_seconds` is set to `30`, then `timeout_in_seconds` can be between `5` and `10`. The default value is `10`. If `interval_in_seconds` is set to `10`, then valid values are between `5` and `9` and `timeout_in_seconds` is required.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ToleratedNumberOfFailures

The number of failures a Traffic Manager probing agent tolerates before marking that endpoint as unhealthy. Valid values are between `0` and `9`. The default value is `3`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

