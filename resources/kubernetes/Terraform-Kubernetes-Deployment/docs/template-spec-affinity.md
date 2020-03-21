# Terraform::Kubernetes::Deployment Template Spec Affinity

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#nodeaffinity" title="NodeAffinity">NodeAffinity</a>" : <i>[ &lt;a href=&#34;template-spec-affinity-nodeaffinity.md&#34;&gt;NodeAffinity&lt;/a&gt;, ... ]</i>,
    "<a href="#podaffinity" title="PodAffinity">PodAffinity</a>" : <i>[ &lt;a href=&#34;template-spec-affinity-podaffinity.md&#34;&gt;PodAffinity&lt;/a&gt;, ... ]</i>,
    "<a href="#podantiaffinity" title="PodAntiAffinity">PodAntiAffinity</a>" : <i>[ &lt;a href=&#34;template-spec-affinity-podantiaffinity.md&#34;&gt;PodAntiAffinity&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#nodeaffinity" title="NodeAffinity">NodeAffinity</a>: <i>
      - &lt;a href=&#34;template-spec-affinity-nodeaffinity.md&#34;&gt;NodeAffinity&lt;/a&gt;</i>
<a href="#podaffinity" title="PodAffinity">PodAffinity</a>: <i>
      - &lt;a href=&#34;template-spec-affinity-podaffinity.md&#34;&gt;PodAffinity&lt;/a&gt;</i>
<a href="#podantiaffinity" title="PodAntiAffinity">PodAntiAffinity</a>: <i>
      - &lt;a href=&#34;template-spec-affinity-podantiaffinity.md&#34;&gt;PodAntiAffinity&lt;/a&gt;</i>
</pre>

## Properties

#### NodeAffinity

_Required_: No
_Type_: List of &lt;a href=&#34;template-spec-affinity-nodeaffinity.md&#34;&gt;NodeAffinity&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PodAffinity

_Required_: No
_Type_: List of &lt;a href=&#34;template-spec-affinity-podaffinity.md&#34;&gt;PodAffinity&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PodAntiAffinity

_Required_: No
_Type_: List of &lt;a href=&#34;template-spec-affinity-podantiaffinity.md&#34;&gt;PodAntiAffinity&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

