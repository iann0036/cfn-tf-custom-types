# TF::DigitalOcean::Loadbalancer HealthcheckDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#checkintervalseconds" title="CheckIntervalSeconds">CheckIntervalSeconds</a>" : <i>Double</i>,
    "<a href="#healthythreshold" title="HealthyThreshold">HealthyThreshold</a>" : <i>Double</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#responsetimeoutseconds" title="ResponseTimeoutSeconds">ResponseTimeoutSeconds</a>" : <i>Double</i>,
    "<a href="#unhealthythreshold" title="UnhealthyThreshold">UnhealthyThreshold</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#checkintervalseconds" title="CheckIntervalSeconds">CheckIntervalSeconds</a>: <i>Double</i>
<a href="#healthythreshold" title="HealthyThreshold">HealthyThreshold</a>: <i>Double</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#responsetimeoutseconds" title="ResponseTimeoutSeconds">ResponseTimeoutSeconds</a>: <i>Double</i>
<a href="#unhealthythreshold" title="UnhealthyThreshold">UnhealthyThreshold</a>: <i>Double</i>
</pre>

## Properties

#### CheckIntervalSeconds

The number of seconds between between two consecutive health checks. If not specified, the default value is `10`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthyThreshold

The number of times a health check must pass for a backend Droplet to be marked "healthy" and be re-added to the pool. If not specified, the default value is `5`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

The path on the backend Droplets to which the Load Balancer instance will send a request.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

An integer representing the port on the backend Droplets on which the health check will attempt a connection.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

The protocol used for health checks sent to the backend Droplets. The possible values are `http`, `https` or `tcp`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseTimeoutSeconds

The number of seconds the Load Balancer instance will wait for a response until marking a health check as failed. If not specified, the default value is `5`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnhealthyThreshold

The number of times a health check must fail for a backend Droplet to be marked "unhealthy" and be removed from the pool. If not specified, the default value is `3`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

