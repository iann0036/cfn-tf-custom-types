# TF::Kubernetes::Daemonset StartupProbeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#failurethreshold" title="FailureThreshold">FailureThreshold</a>" : <i>Double</i>,
    "<a href="#initialdelayseconds" title="InitialDelaySeconds">InitialDelaySeconds</a>" : <i>Double</i>,
    "<a href="#periodseconds" title="PeriodSeconds">PeriodSeconds</a>" : <i>Double</i>,
    "<a href="#successthreshold" title="SuccessThreshold">SuccessThreshold</a>" : <i>Double</i>,
    "<a href="#timeoutseconds" title="TimeoutSeconds">TimeoutSeconds</a>" : <i>Double</i>,
    "<a href="#exec" title="Exec">Exec</a>" : <i>[ <a href="execdefinition.md">ExecDefinition</a>, ... ]</i>,
    "<a href="#httpget" title="HttpGet">HttpGet</a>" : <i>[ <a href="httpgetdefinition.md">HttpGetDefinition</a>, ... ]</i>,
    "<a href="#tcpsocket" title="TcpSocket">TcpSocket</a>" : <i>[ <a href="tcpsocketdefinition.md">TcpSocketDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#failurethreshold" title="FailureThreshold">FailureThreshold</a>: <i>Double</i>
<a href="#initialdelayseconds" title="InitialDelaySeconds">InitialDelaySeconds</a>: <i>Double</i>
<a href="#periodseconds" title="PeriodSeconds">PeriodSeconds</a>: <i>Double</i>
<a href="#successthreshold" title="SuccessThreshold">SuccessThreshold</a>: <i>Double</i>
<a href="#timeoutseconds" title="TimeoutSeconds">TimeoutSeconds</a>: <i>Double</i>
<a href="#exec" title="Exec">Exec</a>: <i>
      - <a href="execdefinition.md">ExecDefinition</a></i>
<a href="#httpget" title="HttpGet">HttpGet</a>: <i>
      - <a href="httpgetdefinition.md">HttpGetDefinition</a></i>
<a href="#tcpsocket" title="TcpSocket">TcpSocket</a>: <i>
      - <a href="tcpsocketdefinition.md">TcpSocketDefinition</a></i>
</pre>

## Properties

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

#### Exec

_Required_: No

_Type_: List of <a href="execdefinition.md">ExecDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpGet

_Required_: No

_Type_: List of <a href="httpgetdefinition.md">HttpGetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpSocket

_Required_: No

_Type_: List of <a href="tcpsocketdefinition.md">TcpSocketDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

