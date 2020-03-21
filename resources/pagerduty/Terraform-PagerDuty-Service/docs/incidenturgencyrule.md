# Terraform::PagerDuty::Service IncidentUrgencyRule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#urgency" title="Urgency">Urgency</a>" : <i>String</i>,
    "<a href="#duringsupporthours" title="DuringSupportHours">DuringSupportHours</a>" : <i>[ &lt;a href=&#34;incidenturgencyrule-duringsupporthours.md&#34;&gt;DuringSupportHours&lt;/a&gt;, ... ]</i>,
    "<a href="#outsidesupporthours" title="OutsideSupportHours">OutsideSupportHours</a>" : <i>[ &lt;a href=&#34;incidenturgencyrule-outsidesupporthours.md&#34;&gt;OutsideSupportHours&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#urgency" title="Urgency">Urgency</a>: <i>String</i>
<a href="#duringsupporthours" title="DuringSupportHours">DuringSupportHours</a>: <i>
      - &lt;a href=&#34;incidenturgencyrule-duringsupporthours.md&#34;&gt;DuringSupportHours&lt;/a&gt;</i>
<a href="#outsidesupporthours" title="OutsideSupportHours">OutsideSupportHours</a>: <i>
      - &lt;a href=&#34;incidenturgencyrule-outsidesupporthours.md&#34;&gt;OutsideSupportHours&lt;/a&gt;</i>
</pre>

## Properties

#### Type

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Urgency

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DuringSupportHours

_Required_: No
_Type_: List of &lt;a href=&#34;incidenturgencyrule-duringsupporthours.md&#34;&gt;DuringSupportHours&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutsideSupportHours

_Required_: No
_Type_: List of &lt;a href=&#34;incidenturgencyrule-outsidesupporthours.md&#34;&gt;OutsideSupportHours&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

