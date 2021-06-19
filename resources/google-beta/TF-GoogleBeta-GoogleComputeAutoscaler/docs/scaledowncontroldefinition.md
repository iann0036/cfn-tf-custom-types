# TF::GoogleBeta::GoogleComputeAutoscaler ScaleDownControlDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#timewindowsec" title="TimeWindowSec">TimeWindowSec</a>" : <i>Double</i>,
    "<a href="#maxscaleddownreplicas" title="MaxScaledDownReplicas">MaxScaledDownReplicas</a>" : <i>[ <a href="maxscaleddownreplicasdefinition.md">MaxScaledDownReplicasDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#timewindowsec" title="TimeWindowSec">TimeWindowSec</a>: <i>Double</i>
<a href="#maxscaleddownreplicas" title="MaxScaledDownReplicas">MaxScaledDownReplicas</a>: <i>
      - <a href="maxscaleddownreplicasdefinition.md">MaxScaledDownReplicasDefinition</a></i>
</pre>

## Properties

#### TimeWindowSec

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxScaledDownReplicas

_Required_: No

_Type_: List of <a href="maxscaleddownreplicasdefinition.md">MaxScaledDownReplicasDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

