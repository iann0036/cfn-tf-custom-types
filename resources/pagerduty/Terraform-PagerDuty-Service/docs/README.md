# Terraform::PagerDuty::Service

A [service](https://v2.developer.pagerduty.com/v2/page/api-reference#!/Services/get_services) represents something you monitor (like a web service, email service, or database service). It is a container for related incidents that associates them with escalation policies.

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

Time in seconds that an incident changes to the Triggered State after being Acknowledged. Disabled if set to the `"null"` string.
* `escalation_policy` - (Required) The escalation policy used by this service.
* `alert_creation` - (Optional) Must be one of two values. PagerDuty receives events from your monitoring systems and can then create incidents in different ways. Value "create_incidents" is default: events will create an incident that cannot be merged. Value "create_alerts_and_incidents" is the alternative: events will create an alert and then add it to a new incident, these incidents can be merged.
* `alert_grouping` - (Optional) Defines how alerts on this service will be automatically grouped into incidents. Note that the alert grouping features are available only on certain plans. If not set, each alert will create a separate incident; If value is set to `time`: All alerts within a specified duration will be grouped into the same incident. This duration is set in the `alert_grouping_timeout` setting (described below). Available on Standard, Enterprise, and Event Intelligence plans; If value is set to `intelligent` - Alerts will be intelligently grouped based on a machine learning model that looks at the alert summary, timing, and the history of grouped alerts. Available on Enterprise and Event Intelligence plan.
* `alert_grouping_timeout` - (Optional) The duration in minutes within which to automatically group incoming alerts. This setting applies only when `alert_grouping` is set to `time`. To continue grouping alerts until the incident is resolved, set this value to `0`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertCreation

Must be one of two values. PagerDuty receives events from your monitoring systems and can then create incidents in different ways. Value "create_incidents" is default: events will create an incident that cannot be merged. Value "create_alerts_and_incidents" is the alternative: events will create an alert and then add it to a new incident, these incidents can be merged.
* `alert_grouping` - (Optional) Defines how alerts on this service will be automatically grouped into incidents. Note that the alert grouping features are available only on certain plans. If not set, each alert will create a separate incident; If value is set to `time`: All alerts within a specified duration will be grouped into the same incident. This duration is set in the `alert_grouping_timeout` setting (described below). Available on Standard, Enterprise, and Event Intelligence plans; If value is set to `intelligent` - Alerts will be intelligently grouped based on a machine learning model that looks at the alert summary, timing, and the history of grouped alerts. Available on Enterprise and Event Intelligence plan.
* `alert_grouping_timeout` - (Optional) The duration in minutes within which to automatically group incoming alerts. This setting applies only when `alert_grouping` is set to `time`. To continue grouping alerts until the incident is resolved, set this value to `0`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertGrouping

Defines how alerts on this service will be automatically grouped into incidents. Note that the alert grouping features are available only on certain plans. If not set, each alert will create a separate incident; If value is set to `time`: All alerts within a specified duration will be grouped into the same incident. This duration is set in the `alert_grouping_timeout` setting (described below). Available on Standard, Enterprise, and Event Intelligence plans; If value is set to `intelligent` - Alerts will be intelligently grouped based on a machine learning model that looks at the alert summary, timing, and the history of grouped alerts. Available on Enterprise and Event Intelligence plan.
* `alert_grouping_timeout` - (Optional) The duration in minutes within which to automatically group incoming alerts. This setting applies only when `alert_grouping` is set to `time`. To continue grouping alerts until the incident is resolved, set this value to `0`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertGroupingTimeout

The duration in minutes within which to automatically group incoming alerts. This setting applies only when `alert_grouping` is set to `time`. To continue grouping alerts until the incident is resolved, set this value to `0`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoResolveTimeout

Time in seconds that an incident is automatically resolved if left open for that long. Disabled if set to the `"null"` string.
* `acknowledgement_timeout` - (Optional) Time in seconds that an incident changes to the Triggered State after being Acknowledged. Disabled if set to the `"null"` string.
* `escalation_policy` - (Required) The escalation policy used by this service.
* `alert_creation` - (Optional) Must be one of two values. PagerDuty receives events from your monitoring systems and can then create incidents in different ways. Value "create_incidents" is default: events will create an incident that cannot be merged. Value "create_alerts_and_incidents" is the alternative: events will create an alert and then add it to a new incident, these incidents can be merged.
* `alert_grouping` - (Optional) Defines how alerts on this service will be automatically grouped into incidents. Note that the alert grouping features are available only on certain plans. If not set, each alert will create a separate incident; If value is set to `time`: All alerts within a specified duration will be grouped into the same incident. This duration is set in the `alert_grouping_timeout` setting (described below). Available on Standard, Enterprise, and Event Intelligence plans; If value is set to `intelligent` - Alerts will be intelligently grouped based on a machine learning model that looks at the alert summary, timing, and the history of grouped alerts. Available on Enterprise and Event Intelligence plan.
* `alert_grouping_timeout` - (Optional) The duration in minutes within which to automatically group incoming alerts. This setting applies only when `alert_grouping` is set to `time`. To continue grouping alerts until the incident is resolved, set this value to `0`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A human-friendly description of the service.
If not set, a placeholder of "Managed by Terraform" will be set.
* `auto_resolve_timeout` - (Optional) Time in seconds that an incident is automatically resolved if left open for that long. Disabled if set to the `"null"` string.
* `acknowledgement_timeout` - (Optional) Time in seconds that an incident changes to the Triggered State after being Acknowledged. Disabled if set to the `"null"` string.
* `escalation_policy` - (Required) The escalation policy used by this service.
* `alert_creation` - (Optional) Must be one of two values. PagerDuty receives events from your monitoring systems and can then create incidents in different ways. Value "create_incidents" is default: events will create an incident that cannot be merged. Value "create_alerts_and_incidents" is the alternative: events will create an alert and then add it to a new incident, these incidents can be merged.
* `alert_grouping` - (Optional) Defines how alerts on this service will be automatically grouped into incidents. Note that the alert grouping features are available only on certain plans. If not set, each alert will create a separate incident; If value is set to `time`: All alerts within a specified duration will be grouped into the same incident. This duration is set in the `alert_grouping_timeout` setting (described below). Available on Standard, Enterprise, and Event Intelligence plans; If value is set to `intelligent` - Alerts will be intelligently grouped based on a machine learning model that looks at the alert summary, timing, and the history of grouped alerts. Available on Enterprise and Event Intelligence plan.
* `alert_grouping_timeout` - (Optional) The duration in minutes within which to automatically group incoming alerts. This setting applies only when `alert_grouping` is set to `time`. To continue grouping alerts until the incident is resolved, set this value to `0`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EscalationPolicy

The escalation policy used by this service.
* `alert_creation` - (Optional) Must be one of two values. PagerDuty receives events from your monitoring systems and can then create incidents in different ways. Value "create_incidents" is default: events will create an incident that cannot be merged. Value "create_alerts_and_incidents" is the alternative: events will create an alert and then add it to a new incident, these incidents can be merged.
* `alert_grouping` - (Optional) Defines how alerts on this service will be automatically grouped into incidents. Note that the alert grouping features are available only on certain plans. If not set, each alert will create a separate incident; If value is set to `time`: All alerts within a specified duration will be grouped into the same incident. This duration is set in the `alert_grouping_timeout` setting (described below). Available on Standard, Enterprise, and Event Intelligence plans; If value is set to `intelligent` - Alerts will be intelligently grouped based on a machine learning model that looks at the alert summary, timing, and the history of grouped alerts. Available on Enterprise and Event Intelligence plan.
* `alert_grouping_timeout` - (Optional) The duration in minutes within which to automatically group incoming alerts. This setting applies only when `alert_grouping` is set to `time`. To continue grouping alerts until the incident is resolved, set this value to `0`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Designates either the start or the end of the scheduled action. Can be `support_hours_start` or `support_hours_end`.

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

#### Id

Returns the <code>Id</code> value.

#### LastIncidentTimestamp

Returns the <code>LastIncidentTimestamp</code> value.

#### Status

Returns the <code>Status</code> value.

