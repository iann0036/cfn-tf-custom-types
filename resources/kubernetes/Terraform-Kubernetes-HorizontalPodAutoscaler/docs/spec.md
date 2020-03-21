# Terraform::Kubernetes::HorizontalPodAutoscaler Spec

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#maxreplicas" title="MaxReplicas">MaxReplicas</a>" : <i>Double</i>,
    "<a href="#minreplicas" title="MinReplicas">MinReplicas</a>" : <i>Double</i>,
    "<a href="#targetcpuutilizationpercentage" title="TargetCpuUtilizationPercentage">TargetCpuUtilizationPercentage</a>" : <i>Double</i>,
    "<a href="#scaletargetref" title="ScaleTargetRef">ScaleTargetRef</a>" : <i>[ &lt;a href=&#34;spec-scaletargetref.md&#34;&gt;ScaleTargetRef&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#maxreplicas" title="MaxReplicas">MaxReplicas</a>: <i>Double</i>
<a href="#minreplicas" title="MinReplicas">MinReplicas</a>: <i>Double</i>
<a href="#targetcpuutilizationpercentage" title="TargetCpuUtilizationPercentage">TargetCpuUtilizationPercentage</a>: <i>Double</i>
<a href="#scaletargetref" title="ScaleTargetRef">ScaleTargetRef</a>: <i>
      - &lt;a href=&#34;spec-scaletargetref.md&#34;&gt;ScaleTargetRef&lt;/a&gt;</i>
</pre>

## Properties

#### MaxReplicas

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinReplicas

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetCpuUtilizationPercentage

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleTargetRef

_Required_: No
_Type_: List of &lt;a href=&#34;spec-scaletargetref.md&#34;&gt;ScaleTargetRef&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

