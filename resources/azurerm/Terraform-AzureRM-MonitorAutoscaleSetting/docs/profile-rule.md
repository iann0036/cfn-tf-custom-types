# Terraform::AzureRM::MonitorAutoscaleSetting Profile Rule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#metrictrigger" title="MetricTrigger">MetricTrigger</a>" : <i>[ &lt;a href=&#34;profile-rule-metrictrigger.md&#34;&gt;MetricTrigger&lt;/a&gt;, ... ]</i>,
    "<a href="#scaleaction" title="ScaleAction">ScaleAction</a>" : <i>[ &lt;a href=&#34;profile-rule-scaleaction.md&#34;&gt;ScaleAction&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#metrictrigger" title="MetricTrigger">MetricTrigger</a>: <i>
      - &lt;a href=&#34;profile-rule-metrictrigger.md&#34;&gt;MetricTrigger&lt;/a&gt;</i>
<a href="#scaleaction" title="ScaleAction">ScaleAction</a>: <i>
      - &lt;a href=&#34;profile-rule-scaleaction.md&#34;&gt;ScaleAction&lt;/a&gt;</i>
</pre>

## Properties

#### MetricTrigger

_Required_: No
_Type_: List of &lt;a href=&#34;profile-rule-metrictrigger.md&#34;&gt;MetricTrigger&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleAction

_Required_: No
_Type_: List of &lt;a href=&#34;profile-rule-scaleaction.md&#34;&gt;ScaleAction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

