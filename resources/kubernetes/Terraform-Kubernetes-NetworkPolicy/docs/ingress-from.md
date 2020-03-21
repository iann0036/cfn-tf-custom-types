# Terraform::Kubernetes::NetworkPolicy Ingress From

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ipblock" title="IpBlock">IpBlock</a>" : <i>[ &lt;a href=&#34;ingress-from-ipblock.md&#34;&gt;IpBlock&lt;/a&gt;, ... ]</i>,
    "<a href="#namespaceselector" title="NamespaceSelector">NamespaceSelector</a>" : <i>[ &lt;a href=&#34;ingress-from-namespaceselector.md&#34;&gt;NamespaceSelector&lt;/a&gt;, ... ]</i>,
    "<a href="#podselector" title="PodSelector">PodSelector</a>" : <i>[ &lt;a href=&#34;ingress-from-podselector.md&#34;&gt;PodSelector&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ipblock" title="IpBlock">IpBlock</a>: <i>
      - &lt;a href=&#34;ingress-from-ipblock.md&#34;&gt;IpBlock&lt;/a&gt;</i>
<a href="#namespaceselector" title="NamespaceSelector">NamespaceSelector</a>: <i>
      - &lt;a href=&#34;ingress-from-namespaceselector.md&#34;&gt;NamespaceSelector&lt;/a&gt;</i>
<a href="#podselector" title="PodSelector">PodSelector</a>: <i>
      - &lt;a href=&#34;ingress-from-podselector.md&#34;&gt;PodSelector&lt;/a&gt;</i>
</pre>

## Properties

#### IpBlock

_Required_: No
_Type_: List of &lt;a href=&#34;ingress-from-ipblock.md&#34;&gt;IpBlock&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamespaceSelector

_Required_: No
_Type_: List of &lt;a href=&#34;ingress-from-namespaceselector.md&#34;&gt;NamespaceSelector&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PodSelector

_Required_: No
_Type_: List of &lt;a href=&#34;ingress-from-podselector.md&#34;&gt;PodSelector&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

