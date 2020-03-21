# Terraform::PagerDuty::EscalationPolicy Rule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#escalationdelayinminutes" title="EscalationDelayInMinutes">EscalationDelayInMinutes</a>" : <i>Double</i>,
    "<a href="#target" title="Target">Target</a>" : <i>[ &lt;a href=&#34;rule-target.md&#34;&gt;Target&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#escalationdelayinminutes" title="EscalationDelayInMinutes">EscalationDelayInMinutes</a>: <i>Double</i>
<a href="#target" title="Target">Target</a>: <i>
      - &lt;a href=&#34;rule-target.md&#34;&gt;Target&lt;/a&gt;</i>
</pre>

## Properties

#### EscalationDelayInMinutes

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Target

_Required_: No
_Type_: List of &lt;a href=&#34;rule-target.md&#34;&gt;Target&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

