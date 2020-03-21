# Terraform::Kubernetes::Job PreferredDuringSchedulingIgnoredDuringExecution

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#weight" title="Weight">Weight</a>" : <i>Double</i>,
    "<a href="#podaffinityterm" title="PodAffinityTerm">PodAffinityTerm</a>" : <i>[ &lt;a href=&#34;preferredduringschedulingignoredduringexecution-podaffinityterm.md&#34;&gt;PodAffinityTerm&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#weight" title="Weight">Weight</a>: <i>Double</i>
<a href="#podaffinityterm" title="PodAffinityTerm">PodAffinityTerm</a>: <i>
      - &lt;a href=&#34;preferredduringschedulingignoredduringexecution-podaffinityterm.md&#34;&gt;PodAffinityTerm&lt;/a&gt;</i>
</pre>

## Properties

#### Weight

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PodAffinityTerm

_Required_: No
_Type_: List of &lt;a href=&#34;preferredduringschedulingignoredduringexecution-podaffinityterm.md&#34;&gt;PodAffinityTerm&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

