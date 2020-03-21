# Terraform::AzureRM::MonitorScheduledQueryRulesAlert Trigger

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#operator" title="Operator">Operator</a>" : <i>String</i>,
    "<a href="#threshold" title="Threshold">Threshold</a>" : <i>Double</i>,
    "<a href="#metrictrigger" title="MetricTrigger">MetricTrigger</a>" : <i>[ &lt;a href=&#34;trigger-metrictrigger.md&#34;&gt;MetricTrigger&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#operator" title="Operator">Operator</a>: <i>String</i>
<a href="#threshold" title="Threshold">Threshold</a>: <i>Double</i>
<a href="#metrictrigger" title="MetricTrigger">MetricTrigger</a>: <i>
      - &lt;a href=&#34;trigger-metrictrigger.md&#34;&gt;MetricTrigger&lt;/a&gt;</i>
</pre>

## Properties

#### Operator

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Threshold

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricTrigger

_Required_: No
_Type_: List of &lt;a href=&#34;trigger-metrictrigger.md&#34;&gt;MetricTrigger&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

