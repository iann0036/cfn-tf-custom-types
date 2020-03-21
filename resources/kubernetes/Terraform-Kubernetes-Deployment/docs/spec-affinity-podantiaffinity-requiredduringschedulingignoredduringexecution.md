# Terraform::Kubernetes::Deployment Spec Affinity PodAntiAffinity RequiredDuringSchedulingIgnoredDuringExecution

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#namespaces" title="Namespaces">Namespaces</a>" : <i>[ String, ... ]</i>,
    "<a href="#topologykey" title="TopologyKey">TopologyKey</a>" : <i>String</i>,
    "<a href="#labelselector" title="LabelSelector">LabelSelector</a>" : <i>[ &lt;a href=&#34;spec-affinity-podantiaffinity-requiredduringschedulingignoredduringexecution-labelselector.md&#34;&gt;LabelSelector&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#namespaces" title="Namespaces">Namespaces</a>: <i>
      - String</i>
<a href="#topologykey" title="TopologyKey">TopologyKey</a>: <i>String</i>
<a href="#labelselector" title="LabelSelector">LabelSelector</a>: <i>
      - &lt;a href=&#34;spec-affinity-podantiaffinity-requiredduringschedulingignoredduringexecution-labelselector.md&#34;&gt;LabelSelector&lt;/a&gt;</i>
</pre>

## Properties

#### Namespaces

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopologyKey

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LabelSelector

_Required_: No
_Type_: List of &lt;a href=&#34;spec-affinity-podantiaffinity-requiredduringschedulingignoredduringexecution-labelselector.md&#34;&gt;LabelSelector&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

