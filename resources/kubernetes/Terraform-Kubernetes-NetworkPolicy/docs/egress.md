# Terraform::Kubernetes::NetworkPolicy Egress

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ports" title="Ports">Ports</a>" : <i>[ &lt;a href=&#34;egress-ports.md&#34;&gt;Ports&lt;/a&gt;, ... ]</i>,
    "<a href="#to" title="To">To</a>" : <i>[ &lt;a href=&#34;egress-to.md&#34;&gt;To&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ports" title="Ports">Ports</a>: <i>
      - &lt;a href=&#34;egress-ports.md&#34;&gt;Ports&lt;/a&gt;</i>
<a href="#to" title="To">To</a>: <i>
      - &lt;a href=&#34;egress-to.md&#34;&gt;To&lt;/a&gt;</i>
</pre>

## Properties

#### Ports

_Required_: No
_Type_: List of &lt;a href=&#34;egress-ports.md&#34;&gt;Ports&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### To

_Required_: No
_Type_: List of &lt;a href=&#34;egress-to.md&#34;&gt;To&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

