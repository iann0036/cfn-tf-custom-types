# Terraform::TencentCloud::CosBucket LifecycleRules

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#filterprefix" title="FilterPrefix">FilterPrefix</a>" : <i>String</i>,
    "<a href="#expiration" title="Expiration">Expiration</a>" : <i>[ &lt;a href=&#34;lifecyclerules-expiration.md&#34;&gt;Expiration&lt;/a&gt;, ... ]</i>,
    "<a href="#transition" title="Transition">Transition</a>" : <i>[ &lt;a href=&#34;lifecyclerules-transition.md&#34;&gt;Transition&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#filterprefix" title="FilterPrefix">FilterPrefix</a>: <i>String</i>
<a href="#expiration" title="Expiration">Expiration</a>: <i>
      - &lt;a href=&#34;lifecyclerules-expiration.md&#34;&gt;Expiration&lt;/a&gt;</i>
<a href="#transition" title="Transition">Transition</a>: <i>
      - &lt;a href=&#34;lifecyclerules-transition.md&#34;&gt;Transition&lt;/a&gt;</i>
</pre>

## Properties

#### FilterPrefix

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expiration

_Required_: No
_Type_: List of &lt;a href=&#34;lifecyclerules-expiration.md&#34;&gt;Expiration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Transition

_Required_: No
_Type_: List of &lt;a href=&#34;lifecyclerules-transition.md&#34;&gt;Transition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

