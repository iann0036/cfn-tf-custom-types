# TF::Kubernetes::CronJob PreferredDuringSchedulingIgnoredDuringExecutionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#weight" title="Weight">Weight</a>" : <i>Double</i>,
    "<a href="#podaffinityterm" title="PodAffinityTerm">PodAffinityTerm</a>" : <i>[ <a href="podaffinitytermdefinition.md">PodAffinityTermDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#weight" title="Weight">Weight</a>: <i>Double</i>
<a href="#podaffinityterm" title="PodAffinityTerm">PodAffinityTerm</a>: <i>
      - <a href="podaffinitytermdefinition.md">PodAffinityTermDefinition</a></i>
</pre>

## Properties

#### Weight

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PodAffinityTerm

_Required_: No

_Type_: List of <a href="podaffinitytermdefinition.md">PodAffinityTermDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

