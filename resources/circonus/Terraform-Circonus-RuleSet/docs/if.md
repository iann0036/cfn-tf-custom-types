# Terraform::Circonus::RuleSet If

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#then" title="Then">Then</a>" : <i>[ &lt;a href=&#34;if-then.md&#34;&gt;Then&lt;/a&gt;, ... ]</i>,
    "<a href="#value" title="Value">Value</a>" : <i>[ &lt;a href=&#34;if-value.md&#34;&gt;Value&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#then" title="Then">Then</a>: <i>
      - &lt;a href=&#34;if-then.md&#34;&gt;Then&lt;/a&gt;</i>
<a href="#value" title="Value">Value</a>: <i>
      - &lt;a href=&#34;if-value.md&#34;&gt;Value&lt;/a&gt;</i>
</pre>

## Properties

#### Then

_Required_: No
_Type_: List of &lt;a href=&#34;if-then.md&#34;&gt;Then&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

_Required_: No
_Type_: List of &lt;a href=&#34;if-value.md&#34;&gt;Value&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

