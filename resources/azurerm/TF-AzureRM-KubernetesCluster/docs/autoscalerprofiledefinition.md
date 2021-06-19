# TF::AzureRM::KubernetesCluster AutoScalerProfileDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#balancesimilarnodegroups" title="BalanceSimilarNodeGroups">BalanceSimilarNodeGroups</a>" : <i>Boolean</i>,
    "<a href="#emptybulkdeletemax" title="EmptyBulkDeleteMax">EmptyBulkDeleteMax</a>" : <i>String</i>,
    "<a href="#expander" title="Expander">Expander</a>" : <i>String</i>,
    "<a href="#maxgracefulterminationsec" title="MaxGracefulTerminationSec">MaxGracefulTerminationSec</a>" : <i>String</i>,
    "<a href="#maxnodeprovisioningtime" title="MaxNodeProvisioningTime">MaxNodeProvisioningTime</a>" : <i>String</i>,
    "<a href="#maxunreadynodes" title="MaxUnreadyNodes">MaxUnreadyNodes</a>" : <i>Double</i>,
    "<a href="#maxunreadypercentage" title="MaxUnreadyPercentage">MaxUnreadyPercentage</a>" : <i>Double</i>,
    "<a href="#newpodscaleupdelay" title="NewPodScaleUpDelay">NewPodScaleUpDelay</a>" : <i>String</i>,
    "<a href="#scaledowndelayafteradd" title="ScaleDownDelayAfterAdd">ScaleDownDelayAfterAdd</a>" : <i>String</i>,
    "<a href="#scaledowndelayafterdelete" title="ScaleDownDelayAfterDelete">ScaleDownDelayAfterDelete</a>" : <i>String</i>,
    "<a href="#scaledowndelayafterfailure" title="ScaleDownDelayAfterFailure">ScaleDownDelayAfterFailure</a>" : <i>String</i>,
    "<a href="#scaledownunneeded" title="ScaleDownUnneeded">ScaleDownUnneeded</a>" : <i>String</i>,
    "<a href="#scaledownunready" title="ScaleDownUnready">ScaleDownUnready</a>" : <i>String</i>,
    "<a href="#scaledownutilizationthreshold" title="ScaleDownUtilizationThreshold">ScaleDownUtilizationThreshold</a>" : <i>String</i>,
    "<a href="#scaninterval" title="ScanInterval">ScanInterval</a>" : <i>String</i>,
    "<a href="#skipnodeswithlocalstorage" title="SkipNodesWithLocalStorage">SkipNodesWithLocalStorage</a>" : <i>Boolean</i>,
    "<a href="#skipnodeswithsystempods" title="SkipNodesWithSystemPods">SkipNodesWithSystemPods</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#balancesimilarnodegroups" title="BalanceSimilarNodeGroups">BalanceSimilarNodeGroups</a>: <i>Boolean</i>
<a href="#emptybulkdeletemax" title="EmptyBulkDeleteMax">EmptyBulkDeleteMax</a>: <i>String</i>
<a href="#expander" title="Expander">Expander</a>: <i>String</i>
<a href="#maxgracefulterminationsec" title="MaxGracefulTerminationSec">MaxGracefulTerminationSec</a>: <i>String</i>
<a href="#maxnodeprovisioningtime" title="MaxNodeProvisioningTime">MaxNodeProvisioningTime</a>: <i>String</i>
<a href="#maxunreadynodes" title="MaxUnreadyNodes">MaxUnreadyNodes</a>: <i>Double</i>
<a href="#maxunreadypercentage" title="MaxUnreadyPercentage">MaxUnreadyPercentage</a>: <i>Double</i>
<a href="#newpodscaleupdelay" title="NewPodScaleUpDelay">NewPodScaleUpDelay</a>: <i>String</i>
<a href="#scaledowndelayafteradd" title="ScaleDownDelayAfterAdd">ScaleDownDelayAfterAdd</a>: <i>String</i>
<a href="#scaledowndelayafterdelete" title="ScaleDownDelayAfterDelete">ScaleDownDelayAfterDelete</a>: <i>String</i>
<a href="#scaledowndelayafterfailure" title="ScaleDownDelayAfterFailure">ScaleDownDelayAfterFailure</a>: <i>String</i>
<a href="#scaledownunneeded" title="ScaleDownUnneeded">ScaleDownUnneeded</a>: <i>String</i>
<a href="#scaledownunready" title="ScaleDownUnready">ScaleDownUnready</a>: <i>String</i>
<a href="#scaledownutilizationthreshold" title="ScaleDownUtilizationThreshold">ScaleDownUtilizationThreshold</a>: <i>String</i>
<a href="#scaninterval" title="ScanInterval">ScanInterval</a>: <i>String</i>
<a href="#skipnodeswithlocalstorage" title="SkipNodesWithLocalStorage">SkipNodesWithLocalStorage</a>: <i>Boolean</i>
<a href="#skipnodeswithsystempods" title="SkipNodesWithSystemPods">SkipNodesWithSystemPods</a>: <i>Boolean</i>
</pre>

## Properties

#### BalanceSimilarNodeGroups

Detect similar node groups and balance the number of nodes between them. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmptyBulkDeleteMax

Maximum number of empty nodes that can be deleted at the same time. Defaults to `10`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expander

Expander to use. Possible values are `least-waste`, `priority`, `most-pods` and `random`. Defaults to `random`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxGracefulTerminationSec

Maximum number of seconds the cluster autoscaler waits for pod termination when trying to scale down a node. Defaults to `600`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxNodeProvisioningTime

Maximum time the autoscaler waits for a node to be provisioned. Defaults to `15m`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxUnreadyNodes

Maximum Number of allowed unready nodes. Defaults to `3`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxUnreadyPercentage

Maximum percentage of unready nodes the cluster autoscaler will stop if the percentage is exceeded. Defaults to `45`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NewPodScaleUpDelay

For scenarios like burst/batch scale where you don't want CA to act before the kubernetes scheduler could schedule all the pods, you can tell CA to ignore unscheduled pods before they're a certain age. Defaults to `10s`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleDownDelayAfterAdd

How long after the scale up of AKS nodes the scale down evaluation resumes. Defaults to `10m`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleDownDelayAfterDelete

How long after node deletion that scale down evaluation resumes. Defaults to the value used for `scan_interval`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleDownDelayAfterFailure

How long after scale down failure that scale down evaluation resumes. Defaults to `3m`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleDownUnneeded

How long a node should be unneeded before it is eligible for scale down. Defaults to `10m`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleDownUnready

How long an unready node should be unneeded before it is eligible for scale down. Defaults to `20m`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleDownUtilizationThreshold

Node utilization level, defined as sum of requested resources divided by capacity, below which a node can be considered for scale down. Defaults to `0.5`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScanInterval

How often the AKS Cluster should be re-evaluated for scale up/down. Defaults to `10s`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipNodesWithLocalStorage

If `true` cluster autoscaler will never delete nodes with pods with local storage, for example, EmptyDir or HostPath. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipNodesWithSystemPods

If `true` cluster autoscaler will never delete nodes with pods from kube-system (except for DaemonSet or mirror pods). Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

