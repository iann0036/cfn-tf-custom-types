# Terraform::OCI::AutoscalingAutoScalingConfiguration Rules

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
    "<a href="#action" title="Action">Action</a>" : <i>[ &lt;a href=&#34;rules-action.md&#34;&gt;Action&lt;/a&gt;, ... ]</i>,
    "<a href="#metric" title="Metric">Metric</a>" : <i>[ &lt;a href=&#34;rules-metric.md&#34;&gt;Metric&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
<a href="#action" title="Action">Action</a>: <i>
      - &lt;a href=&#34;rules-action.md&#34;&gt;Action&lt;/a&gt;</i>
<a href="#metric" title="Metric">Metric</a>: <i>
      - &lt;a href=&#34;rules-metric.md&#34;&gt;Metric&lt;/a&gt;</i>
</pre>

## Properties

#### DisplayName

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Action

_Required_: No
_Type_: List of &lt;a href=&#34;rules-action.md&#34;&gt;Action&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metric

_Required_: No
_Type_: List of &lt;a href=&#34;rules-metric.md&#34;&gt;Metric&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

