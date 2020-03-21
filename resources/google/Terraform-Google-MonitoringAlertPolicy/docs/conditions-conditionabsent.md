# Terraform::Google::MonitoringAlertPolicy Conditions ConditionAbsent

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#duration" title="Duration">Duration</a>" : <i>String</i>,
    "<a href="#filter" title="Filter">Filter</a>" : <i>String</i>,
    "<a href="#aggregations" title="Aggregations">Aggregations</a>" : <i>[ &lt;a href=&#34;conditions-conditionabsent-aggregations.md&#34;&gt;Aggregations&lt;/a&gt;, ... ]</i>,
    "<a href="#trigger" title="Trigger">Trigger</a>" : <i>[ &lt;a href=&#34;conditions-conditionabsent-trigger.md&#34;&gt;Trigger&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#duration" title="Duration">Duration</a>: <i>String</i>
<a href="#filter" title="Filter">Filter</a>: <i>String</i>
<a href="#aggregations" title="Aggregations">Aggregations</a>: <i>
      - &lt;a href=&#34;conditions-conditionabsent-aggregations.md&#34;&gt;Aggregations&lt;/a&gt;</i>
<a href="#trigger" title="Trigger">Trigger</a>: <i>
      - &lt;a href=&#34;conditions-conditionabsent-trigger.md&#34;&gt;Trigger&lt;/a&gt;</i>
</pre>

## Properties

#### Duration

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Aggregations

_Required_: No
_Type_: List of &lt;a href=&#34;conditions-conditionabsent-aggregations.md&#34;&gt;Aggregations&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trigger

_Required_: No
_Type_: List of &lt;a href=&#34;conditions-conditionabsent-trigger.md&#34;&gt;Trigger&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

