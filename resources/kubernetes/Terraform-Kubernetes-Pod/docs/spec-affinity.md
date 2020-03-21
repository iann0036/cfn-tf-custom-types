# Terraform::Kubernetes::Pod Spec Affinity

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#nodeaffinity" title="NodeAffinity">NodeAffinity</a>" : <i>[ <a href="spec-affinity-nodeaffinity.md">NodeAffinity</a>, ... ]</i>,
    "<a href="#podaffinity" title="PodAffinity">PodAffinity</a>" : <i>[ <a href="spec-affinity-podaffinity.md">PodAffinity</a>, ... ]</i>,
    "<a href="#podantiaffinity" title="PodAntiAffinity">PodAntiAffinity</a>" : <i>[ <a href="spec-affinity-podantiaffinity.md">PodAntiAffinity</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#nodeaffinity" title="NodeAffinity">NodeAffinity</a>: <i>
      - <a href="spec-affinity-nodeaffinity.md">NodeAffinity</a></i>
<a href="#podaffinity" title="PodAffinity">PodAffinity</a>: <i>
      - <a href="spec-affinity-podaffinity.md">PodAffinity</a></i>
<a href="#podantiaffinity" title="PodAntiAffinity">PodAntiAffinity</a>: <i>
      - <a href="spec-affinity-podantiaffinity.md">PodAntiAffinity</a></i>
</pre>

## Properties

#### NodeAffinity

_Required_: No
_Type_: List of <a href="spec-affinity-nodeaffinity.md">NodeAffinity</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PodAffinity

_Required_: No
_Type_: List of <a href="spec-affinity-podaffinity.md">PodAffinity</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PodAntiAffinity

_Required_: No
_Type_: List of <a href="spec-affinity-podantiaffinity.md">PodAntiAffinity</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

