# Terraform::Kubernetes::ReplicationController Template Container Lifecycle

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#poststart" title="PostStart">PostStart</a>" : <i>[ &lt;a href=&#34;template-container-lifecycle-poststart.md&#34;&gt;PostStart&lt;/a&gt;, ... ]</i>,
    "<a href="#prestop" title="PreStop">PreStop</a>" : <i>[ &lt;a href=&#34;template-container-lifecycle-prestop.md&#34;&gt;PreStop&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#poststart" title="PostStart">PostStart</a>: <i>
      - &lt;a href=&#34;template-container-lifecycle-poststart.md&#34;&gt;PostStart&lt;/a&gt;</i>
<a href="#prestop" title="PreStop">PreStop</a>: <i>
      - &lt;a href=&#34;template-container-lifecycle-prestop.md&#34;&gt;PreStop&lt;/a&gt;</i>
</pre>

## Properties

#### PostStart

_Required_: No
_Type_: List of &lt;a href=&#34;template-container-lifecycle-poststart.md&#34;&gt;PostStart&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreStop

_Required_: No
_Type_: List of &lt;a href=&#34;template-container-lifecycle-prestop.md&#34;&gt;PreStop&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

