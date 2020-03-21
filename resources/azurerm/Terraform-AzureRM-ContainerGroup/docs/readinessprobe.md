# Terraform::AzureRM::ContainerGroup ReadinessProbe

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#exec" title="Exec">Exec</a>" : <i>[ String, ... ]</i>,
    "<a href="#failurethreshold" title="FailureThreshold">FailureThreshold</a>" : <i>Double</i>,
    "<a href="#initialdelayseconds" title="InitialDelaySeconds">InitialDelaySeconds</a>" : <i>Double</i>,
    "<a href="#periodseconds" title="PeriodSeconds">PeriodSeconds</a>" : <i>Double</i>,
    "<a href="#successthreshold" title="SuccessThreshold">SuccessThreshold</a>" : <i>Double</i>,
    "<a href="#timeoutseconds" title="TimeoutSeconds">TimeoutSeconds</a>" : <i>Double</i>,
    "<a href="#httpget" title="HttpGet">HttpGet</a>" : <i>[ <a href="readinessprobe-httpget.md">HttpGet</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#exec" title="Exec">Exec</a>: <i>
      - String</i>
<a href="#failurethreshold" title="FailureThreshold">FailureThreshold</a>: <i>Double</i>
<a href="#initialdelayseconds" title="InitialDelaySeconds">InitialDelaySeconds</a>: <i>Double</i>
<a href="#periodseconds" title="PeriodSeconds">PeriodSeconds</a>: <i>Double</i>
<a href="#successthreshold" title="SuccessThreshold">SuccessThreshold</a>: <i>Double</i>
<a href="#timeoutseconds" title="TimeoutSeconds">TimeoutSeconds</a>: <i>Double</i>
<a href="#httpget" title="HttpGet">HttpGet</a>: <i>
      - <a href="readinessprobe-httpget.md">HttpGet</a></i>
</pre>

## Properties

#### Exec

Commands to be run to validate container readiness. Changing this forces a new resource to be created.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailureThreshold

How many times to try the probe before restarting the container (liveness probe) or marking the container as unhealthy (readiness probe). The default value is `3` and the minimum value is `1`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitialDelaySeconds

Number of seconds after the container has started before liveness or readiness probes are initiated. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeriodSeconds

How often (in seconds) to perform the probe. The default value is `10` and the minimum value is `1`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SuccessThreshold

Minimum consecutive successes for the probe to be considered successful after having failed. The default value is `1` and the minimum value is `1`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutSeconds

Number of seconds after which the probe times out. The default value is `1` and the minimum value is `1`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpGet

_Required_: No

_Type_: List of <a href="readinessprobe-httpget.md">HttpGet</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

