# TF::HCloud::LoadBalancerService HealthCheckDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#interval" title="Interval">Interval</a>" : <i>Double</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#retries" title="Retries">Retries</a>" : <i>Double</i>,
    "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
    "<a href="#http" title="Http">Http</a>" : <i>[ <a href="httpdefinition.md">HttpDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#interval" title="Interval">Interval</a>: <i>Double</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#retries" title="Retries">Retries</a>: <i>Double</i>
<a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
<a href="#http" title="Http">Http</a>: <i>
      - <a href="httpdefinition.md">HttpDefinition</a></i>
</pre>

## Properties

#### Interval

Interval how often the health check will be performed, in seconds.
- `timeout` - (Required, int) Timeout when a health check try will be canceled if there is no response, in seconds.
- `retries` - (Optional, int) Number of tries a health check will be performed until a target will be listed as `unhealthy`.
- `http` - (Optional, list) List of http configurations. Required if `protocol` is `http`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

Port the health check tries to connect to, required if protocol is `tcp`. Can be everything between `1` and `65535`. Must be unique per Load Balancer.
- `interval` - (Required, int) Interval how often the health check will be performed, in seconds.
- `timeout` - (Required, int) Timeout when a health check try will be canceled if there is no response, in seconds.
- `retries` - (Optional, int) Number of tries a health check will be performed until a target will be listed as `unhealthy`.
- `http` - (Optional, list) List of http configurations. Required if `protocol` is `http`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Protocol the health check uses. `http` or `tcp`
- `port` - (Required, int) Port the health check tries to connect to, required if protocol is `tcp`. Can be everything between `1` and `65535`. Must be unique per Load Balancer.
- `interval` - (Required, int) Interval how often the health check will be performed, in seconds.
- `timeout` - (Required, int) Timeout when a health check try will be canceled if there is no response, in seconds.
- `retries` - (Optional, int) Number of tries a health check will be performed until a target will be listed as `unhealthy`.
- `http` - (Optional, list) List of http configurations. Required if `protocol` is `http`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Retries

Number of tries a health check will be performed until a target will be listed as `unhealthy`.
- `http` - (Optional, list) List of http configurations. Required if `protocol` is `http`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

Timeout when a health check try will be canceled if there is no response, in seconds.
- `retries` - (Optional, int) Number of tries a health check will be performed until a target will be listed as `unhealthy`.
- `http` - (Optional, list) List of http configurations. Required if `protocol` is `http`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Http

_Required_: No

_Type_: List of <a href="httpdefinition.md">HttpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

