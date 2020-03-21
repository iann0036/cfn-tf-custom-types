# Terraform::Kubernetes::NetworkPolicy Spec

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#policytypes" title="PolicyTypes">PolicyTypes</a>" : <i>[ String, ... ]</i>,
    "<a href="#egress" title="Egress">Egress</a>" : <i>[ &lt;a href=&#34;spec-egress.md&#34;&gt;Egress&lt;/a&gt;, ... ]</i>,
    "<a href="#ingress" title="Ingress">Ingress</a>" : <i>[ &lt;a href=&#34;spec-ingress.md&#34;&gt;Ingress&lt;/a&gt;, ... ]</i>,
    "<a href="#podselector" title="PodSelector">PodSelector</a>" : <i>[ &lt;a href=&#34;spec-podselector.md&#34;&gt;PodSelector&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#policytypes" title="PolicyTypes">PolicyTypes</a>: <i>
      - String</i>
<a href="#egress" title="Egress">Egress</a>: <i>
      - &lt;a href=&#34;spec-egress.md&#34;&gt;Egress&lt;/a&gt;</i>
<a href="#ingress" title="Ingress">Ingress</a>: <i>
      - &lt;a href=&#34;spec-ingress.md&#34;&gt;Ingress&lt;/a&gt;</i>
<a href="#podselector" title="PodSelector">PodSelector</a>: <i>
      - &lt;a href=&#34;spec-podselector.md&#34;&gt;PodSelector&lt;/a&gt;</i>
</pre>

## Properties

#### PolicyTypes

_Required_: Yes
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Egress

_Required_: No
_Type_: List of &lt;a href=&#34;spec-egress.md&#34;&gt;Egress&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ingress

_Required_: No
_Type_: List of &lt;a href=&#34;spec-ingress.md&#34;&gt;Ingress&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PodSelector

_Required_: No
_Type_: List of &lt;a href=&#34;spec-podselector.md&#34;&gt;PodSelector&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

