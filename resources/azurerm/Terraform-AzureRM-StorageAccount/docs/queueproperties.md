# Terraform::AzureRM::StorageAccount QueueProperties

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#corsrule" title="CorsRule">CorsRule</a>" : <i>[ &lt;a href=&#34;queueproperties-corsrule.md&#34;&gt;CorsRule&lt;/a&gt;, ... ]</i>,
    "<a href="#hourmetrics" title="HourMetrics">HourMetrics</a>" : <i>[ &lt;a href=&#34;queueproperties-hourmetrics.md&#34;&gt;HourMetrics&lt;/a&gt;, ... ]</i>,
    "<a href="#logging" title="Logging">Logging</a>" : <i>[ &lt;a href=&#34;queueproperties-logging.md&#34;&gt;Logging&lt;/a&gt;, ... ]</i>,
    "<a href="#minutemetrics" title="MinuteMetrics">MinuteMetrics</a>" : <i>[ &lt;a href=&#34;queueproperties-minutemetrics.md&#34;&gt;MinuteMetrics&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#corsrule" title="CorsRule">CorsRule</a>: <i>
      - &lt;a href=&#34;queueproperties-corsrule.md&#34;&gt;CorsRule&lt;/a&gt;</i>
<a href="#hourmetrics" title="HourMetrics">HourMetrics</a>: <i>
      - &lt;a href=&#34;queueproperties-hourmetrics.md&#34;&gt;HourMetrics&lt;/a&gt;</i>
<a href="#logging" title="Logging">Logging</a>: <i>
      - &lt;a href=&#34;queueproperties-logging.md&#34;&gt;Logging&lt;/a&gt;</i>
<a href="#minutemetrics" title="MinuteMetrics">MinuteMetrics</a>: <i>
      - &lt;a href=&#34;queueproperties-minutemetrics.md&#34;&gt;MinuteMetrics&lt;/a&gt;</i>
</pre>

## Properties

#### CorsRule

_Required_: No
_Type_: List of &lt;a href=&#34;queueproperties-corsrule.md&#34;&gt;CorsRule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HourMetrics

_Required_: No
_Type_: List of &lt;a href=&#34;queueproperties-hourmetrics.md&#34;&gt;HourMetrics&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logging

_Required_: No
_Type_: List of &lt;a href=&#34;queueproperties-logging.md&#34;&gt;Logging&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinuteMetrics

_Required_: No
_Type_: List of &lt;a href=&#34;queueproperties-minutemetrics.md&#34;&gt;MinuteMetrics&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

