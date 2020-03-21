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
        "<a href="#incidenturgencyrule" title="IncidentUrgencyRule">IncidentUrgencyRule</a>" : <i>[ <a href="incidenturgencyrule.md">IncidentUrgencyRule</a>, ... ]</i>,
        "<a href="#scheduledactions" title="ScheduledActions">ScheduledActions</a>" : <i>[ <a href="scheduledactions.md">ScheduledActions</a>, ... ]</i>,
        "<a href="#supporthours" title="SupportHours">SupportHours</a>" : <i>[ <a href="supporthours.md">SupportHours</a>, ... ]</i>,
        "<a href="#duringsupporthours" title="DuringSupportHours">DuringSupportHours</a>" : <i>[ <a href="duringsupporthours.md">DuringSupportHours</a>, ... ]</i>,
        "<a href="#outsidesupporthours" title="OutsideSupportHours">OutsideSupportHours</a>" : <i>[ <a href="outsidesupporthours.md">OutsideSupportHours</a>, ... ]</i>,
        "<a href="#at" title="At">At</a>" : <i>[ <a href="at.md">At</a>, ... ]</i>
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
      - <a href="incidenturgencyrule.md">IncidentUrgencyRule</a></i>
    <a href="#scheduledactions" title="ScheduledActions">ScheduledActions</a>: <i>
      - <a href="scheduledactions.md">ScheduledActions</a></i>
    <a href="#supporthours" title="SupportHours">SupportHours</a>: <i>
      - <a href="supporthours.md">SupportHours</a></i>
    <a href="#duringsupporthours" title="DuringSupportHours">DuringSupportHours</a>: <i>
      - <a href="duringsupporthours.md">DuringSupportHours</a></i>
    <a href="#outsidesupporthours" title="OutsideSupportHours">OutsideSupportHours</a>: <i>
      - <a href="outsidesupporthours.md">OutsideSupportHours</a></i>
    <a href="#at" title="At">At</a>: <i>
      - <a href="at.md">At</a></i>
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

_Type_: List of <a href="incidenturgencyrule.md">IncidentUrgencyRule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduledActions

_Required_: No

_Type_: List of <a href="scheduledactions.md">ScheduledActions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SupportHours

_Required_: No

_Type_: List of <a href="supporthours.md">SupportHours</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DuringSupportHours

_Required_: No

_Type_: List of <a href="duringsupporthours.md">DuringSupportHours</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutsideSupportHours

_Required_: No

_Type_: List of <a href="outsidesupporthours.md">OutsideSupportHours</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### At

_Required_: No

_Type_: List of <a href="at.md">At</a>

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

Returns the <code>CreatedAt</code> value.

#### HtmlUrl

Returns the <code>HtmlUrl</code> value.

#### LastIncidentTimestamp

Returns the <code>LastIncidentTimestamp</code> value.

#### Status

Returns the <code>Status</code> value.

