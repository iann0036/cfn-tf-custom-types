# Terraform::PagerDuty::Service

CloudFormation equivalent of pagerduty_service

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::PagerDuty::Service",
    "Properties" : {
        "<a href="#acknowledgementtimeout" title="AcknowledgementTimeout">AcknowledgementTimeout</a>" : <i>String</i>,
        "<a href="#alertcreation" title="AlertCreation">AlertCreation</a>" : <i>String</i>,
        "<a href="#alertgrouping" title="AlertGrouping">AlertGrouping</a>" : <i>String</i>,
        "<a href="#alertgroupingtimeout" title="AlertGroupingTimeout">AlertGroupingTimeout</a>" : <i>Double</i>,
        "<a href="#autoresolvetimeout" title="AutoResolveTimeout">AutoResolveTimeout</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#escalationpolicy" title="EscalationPolicy">EscalationPolicy</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#incidenturgencyrule" title="IncidentUrgencyRule">IncidentUrgencyRule</a>" : <i>[ &lt;a href=&#34;incidenturgencyrule.md&#34;&gt;IncidentUrgencyRule&lt;/a&gt;, ... ]</i>,
        "<a href="#scheduledactions" title="ScheduledActions">ScheduledActions</a>" : <i>[ &lt;a href=&#34;scheduledactions.md&#34;&gt;ScheduledActions&lt;/a&gt;, ... ]</i>,
        "<a href="#supporthours" title="SupportHours">SupportHours</a>" : <i>[ &lt;a href=&#34;supporthours.md&#34;&gt;SupportHours&lt;/a&gt;, ... ]</i>,
        "<a href="#duringsupporthours" title="DuringSupportHours">DuringSupportHours</a>" : <i>[ &lt;a href=&#34;duringsupporthours.md&#34;&gt;DuringSupportHours&lt;/a&gt;, ... ]</i>,
        "<a href="#outsidesupporthours" title="OutsideSupportHours">OutsideSupportHours</a>" : <i>[ &lt;a href=&#34;outsidesupporthours.md&#34;&gt;OutsideSupportHours&lt;/a&gt;, ... ]</i>,
        "<a href="#at" title="At">At</a>" : <i>[ &lt;a href=&#34;at.md&#34;&gt;At&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::PagerDuty::Service
Properties:
    <a href="#acknowledgementtimeout" title="AcknowledgementTimeout">AcknowledgementTimeout</a>: <i>String</i>
    <a href="#alertcreation" title="AlertCreation">AlertCreation</a>: <i>String</i>
    <a href="#alertgrouping" title="AlertGrouping">AlertGrouping</a>: <i>String</i>
    <a href="#alertgroupingtimeout" title="AlertGroupingTimeout">AlertGroupingTimeout</a>: <i>Double</i>
    <a href="#autoresolvetimeout" title="AutoResolveTimeout">AutoResolveTimeout</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#escalationpolicy" title="EscalationPolicy">EscalationPolicy</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#incidenturgencyrule" title="IncidentUrgencyRule">IncidentUrgencyRule</a>: <i>
      - &lt;a href=&#34;incidenturgencyrule.md&#34;&gt;IncidentUrgencyRule&lt;/a&gt;</i>
    <a href="#scheduledactions" title="ScheduledActions">ScheduledActions</a>: <i>
      - &lt;a href=&#34;scheduledactions.md&#34;&gt;ScheduledActions&lt;/a&gt;</i>
    <a href="#supporthours" title="SupportHours">SupportHours</a>: <i>
      - &lt;a href=&#34;supporthours.md&#34;&gt;SupportHours&lt;/a&gt;</i>
    <a href="#duringsupporthours" title="DuringSupportHours">DuringSupportHours</a>: <i>
      - &lt;a href=&#34;duringsupporthours.md&#34;&gt;DuringSupportHours&lt;/a&gt;</i>
    <a href="#outsidesupporthours" title="OutsideSupportHours">OutsideSupportHours</a>: <i>
      - &lt;a href=&#34;outsidesupporthours.md&#34;&gt;OutsideSupportHours&lt;/a&gt;</i>
    <a href="#at" title="At">At</a>: <i>
      - &lt;a href=&#34;at.md&#34;&gt;At&lt;/a&gt;</i>
</pre>

## Properties

#### AcknowledgementTimeout

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertCreation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertGrouping

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertGroupingTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoResolveTimeout

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EscalationPolicy

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncidentUrgencyRule

_Required_: No

_Type_: List of &lt;a href=&#34;incidenturgencyrule.md&#34;&gt;IncidentUrgencyRule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduledActions

_Required_: No

_Type_: List of &lt;a href=&#34;scheduledactions.md&#34;&gt;ScheduledActions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SupportHours

_Required_: No

_Type_: List of &lt;a href=&#34;supporthours.md&#34;&gt;SupportHours&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DuringSupportHours

_Required_: No

_Type_: List of &lt;a href=&#34;duringsupporthours.md&#34;&gt;DuringSupportHours&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutsideSupportHours

_Required_: No

_Type_: List of &lt;a href=&#34;outsidesupporthours.md&#34;&gt;OutsideSupportHours&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### At

_Required_: No

_Type_: List of &lt;a href=&#34;at.md&#34;&gt;At&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreatedAt

Returns the &lt;code&gt;CreatedAt&lt;/code&gt; value.

#### HtmlUrl

Returns the &lt;code&gt;HtmlUrl&lt;/code&gt; value.

#### LastIncidentTimestamp

Returns the &lt;code&gt;LastIncidentTimestamp&lt;/code&gt; value.

#### Status

Returns the &lt;code&gt;Status&lt;/code&gt; value.

