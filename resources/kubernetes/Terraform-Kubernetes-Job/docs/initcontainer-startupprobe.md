# Terraform::Kubernetes::Job InitContainer StartupProbe

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
    "<a href="#exec" title="Exec">Exec</a>" : <i>[ &lt;a href=&#34;initcontainer-startupprobe-exec.md&#34;&gt;Exec&lt;/a&gt;, ... ]</i>,
    "<a href="#httpget" title="HttpGet">HttpGet</a>" : <i>[ &lt;a href=&#34;initcontainer-startupprobe-httpget.md&#34;&gt;HttpGet&lt;/a&gt;, ... ]</i>,
    "<a href="#tcpsocket" title="TcpSocket">TcpSocket</a>" : <i>[ &lt;a href=&#34;initcontainer-startupprobe-tcpsocket.md&#34;&gt;TcpSocket&lt;/a&gt;, ... ]</i>
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
      - &lt;a href=&#34;initcontainer-startupprobe-exec.md&#34;&gt;Exec&lt;/a&gt;</i>
<a href="#httpget" title="HttpGet">HttpGet</a>: <i>
      - &lt;a href=&#34;initcontainer-startupprobe-httpget.md&#34;&gt;HttpGet&lt;/a&gt;</i>
<a href="#tcpsocket" title="TcpSocket">TcpSocket</a>: <i>
      - &lt;a href=&#34;initcontainer-startupprobe-tcpsocket.md&#34;&gt;TcpSocket&lt;/a&gt;</i>
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
_Type_: List of &lt;a href=&#34;initcontainer-startupprobe-exec.md&#34;&gt;Exec&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpGet

_Required_: No
_Type_: List of &lt;a href=&#34;initcontainer-startupprobe-httpget.md&#34;&gt;HttpGet&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpSocket

_Required_: No
_Type_: List of &lt;a href=&#34;initcontainer-startupprobe-tcpsocket.md&#34;&gt;TcpSocket&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

