# Terraform::AzureRM::MonitorScheduledQueryRulesLog Criteria

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#metricname" title="MetricName">MetricName</a>" : <i>String</i>,
    "<a href="#dimension" title="Dimension">Dimension</a>" : <i>[ &lt;a href=&#34;criteria-dimension.md&#34;&gt;Dimension&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#metricname" title="MetricName">MetricName</a>: <i>String</i>
<a href="#dimension" title="Dimension">Dimension</a>: <i>
      - &lt;a href=&#34;criteria-dimension.md&#34;&gt;Dimension&lt;/a&gt;</i>
</pre>

## Properties

#### MetricName

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dimension

_Required_: No
_Type_: List of &lt;a href=&#34;criteria-dimension.md&#34;&gt;Dimension&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

