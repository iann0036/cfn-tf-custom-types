# Terraform::AzureRM::ContainerGroup LivenessProbe

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
    "<a href="#httpget" title="HttpGet">HttpGet</a>" : <i>[ <a href="livenessprobe-httpget.md">HttpGet</a>, ... ]</i>
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
      - <a href="livenessprobe-httpget.md">HttpGet</a></i>
</pre>

## Properties

#### Exec

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailureThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitialDelaySeconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeriodSeconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SuccessThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutSeconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpGet

_Required_: No

_Type_: List of <a href="livenessprobe-httpget.md">HttpGet</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

