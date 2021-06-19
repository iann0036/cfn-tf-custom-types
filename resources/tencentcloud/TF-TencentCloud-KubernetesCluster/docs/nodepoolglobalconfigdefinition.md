# TF::TencentCloud::KubernetesCluster NodePoolGlobalConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#expander" title="Expander">Expander</a>" : <i>String</i>,
    "<a href="#ignoredaemonsetsutilization" title="IgnoreDaemonSetsUtilization">IgnoreDaemonSetsUtilization</a>" : <i>Boolean</i>,
    "<a href="#isscaleinenabled" title="IsScaleInEnabled">IsScaleInEnabled</a>" : <i>Boolean</i>,
    "<a href="#maxconcurrentscalein" title="MaxConcurrentScaleIn">MaxConcurrentScaleIn</a>" : <i>Double</i>,
    "<a href="#scaleindelay" title="ScaleInDelay">ScaleInDelay</a>" : <i>Double</i>,
    "<a href="#scaleinunneededtime" title="ScaleInUnneededTime">ScaleInUnneededTime</a>" : <i>Double</i>,
    "<a href="#scaleinutilizationthreshold" title="ScaleInUtilizationThreshold">ScaleInUtilizationThreshold</a>" : <i>Double</i>,
    "<a href="#skipnodeswithlocalstorage" title="SkipNodesWithLocalStorage">SkipNodesWithLocalStorage</a>" : <i>Boolean</i>,
    "<a href="#skipnodeswithsystempods" title="SkipNodesWithSystemPods">SkipNodesWithSystemPods</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#expander" title="Expander">Expander</a>: <i>String</i>
<a href="#ignoredaemonsetsutilization" title="IgnoreDaemonSetsUtilization">IgnoreDaemonSetsUtilization</a>: <i>Boolean</i>
<a href="#isscaleinenabled" title="IsScaleInEnabled">IsScaleInEnabled</a>: <i>Boolean</i>
<a href="#maxconcurrentscalein" title="MaxConcurrentScaleIn">MaxConcurrentScaleIn</a>: <i>Double</i>
<a href="#scaleindelay" title="ScaleInDelay">ScaleInDelay</a>: <i>Double</i>
<a href="#scaleinunneededtime" title="ScaleInUnneededTime">ScaleInUnneededTime</a>: <i>Double</i>
<a href="#scaleinutilizationthreshold" title="ScaleInUtilizationThreshold">ScaleInUtilizationThreshold</a>: <i>Double</i>
<a href="#skipnodeswithlocalstorage" title="SkipNodesWithLocalStorage">SkipNodesWithLocalStorage</a>: <i>Boolean</i>
<a href="#skipnodeswithsystempods" title="SkipNodesWithSystemPods">SkipNodesWithSystemPods</a>: <i>Boolean</i>
</pre>

## Properties

#### Expander

Indicates which scale-out method will be used when there are multiple scaling groups. Valid values: `random` - select a random scaling group, `most-pods` - select the scaling group that can schedule the most pods, `least-waste` - select the scaling group that can ensure the fewest remaining resources after Pod scheduling.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreDaemonSetsUtilization

Whether to ignore DaemonSet pods by default when calculating resource usage.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsScaleInEnabled

Indicates whether to enable scale-in.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxConcurrentScaleIn

Max concurrent scale-in volume.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleInDelay

Number of minutes after cluster scale-out when the system starts judging whether to perform scale-in.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleInUnneededTime

Number of consecutive minutes of idleness after which the node is subject to scale-in.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleInUtilizationThreshold

Percentage of node resource usage below which the node is considered to be idle.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipNodesWithLocalStorage

During scale-in, ignore nodes with local storage pods.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipNodesWithSystemPods

During scale-in, ignore nodes with pods in the kube-system namespace that are not managed by DaemonSet.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

