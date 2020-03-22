# Terraform::OCI::MonitoringAlarm

This resource provides the Alarm resource in Oracle Cloud Infrastructure Monitoring service.

Creates a new alarm in the specified compartment.
For important limits information, see [Limits on Monitoring](https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#Limits).

This call is subject to a Monitoring limit that applies to the total number of requests across all alarm operations. 
Monitoring might throttle this call to reject an otherwise valid request when the total rate of alarm operations exceeds 10 requests, 
or transactions, per second (TPS) for a given tenancy.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::MonitoringAlarm",
    "Properties" : {
        "<a href="#body" title="Body">Body</a>" : <i>String</i>,
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtags.md">DefinedTags</a>, ... ]</i>,
        "<a href="#destinations" title="Destinations">Destinations</a>" : <i>[ String, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtags.md">FreeformTags</a>, ... ]</i>,
        "<a href="#isenabled" title="IsEnabled">IsEnabled</a>" : <i>Boolean</i>,
        "<a href="#metriccompartmentid" title="MetricCompartmentId">MetricCompartmentId</a>" : <i>String</i>,
        "<a href="#metriccompartmentidinsubtree" title="MetricCompartmentIdInSubtree">MetricCompartmentIdInSubtree</a>" : <i>Boolean</i>,
        "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
        "<a href="#pendingduration" title="PendingDuration">PendingDuration</a>" : <i>String</i>,
        "<a href="#query" title="Query">Query</a>" : <i>String</i>,
        "<a href="#repeatnotificationduration" title="RepeatNotificationDuration">RepeatNotificationDuration</a>" : <i>String</i>,
        "<a href="#resolution" title="Resolution">Resolution</a>" : <i>String</i>,
        "<a href="#resourcegroup" title="ResourceGroup">ResourceGroup</a>" : <i>String</i>,
        "<a href="#severity" title="Severity">Severity</a>" : <i>String</i>,
        "<a href="#suppression" title="Suppression">Suppression</a>" : <i>[ <a href="suppression.md">Suppression</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::MonitoringAlarm
Properties:
    <a href="#body" title="Body">Body</a>: <i>String</i>
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtags.md">DefinedTags</a></i>
    <a href="#destinations" title="Destinations">Destinations</a>: <i>
      - String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtags.md">FreeformTags</a></i>
    <a href="#isenabled" title="IsEnabled">IsEnabled</a>: <i>Boolean</i>
    <a href="#metriccompartmentid" title="MetricCompartmentId">MetricCompartmentId</a>: <i>String</i>
    <a href="#metriccompartmentidinsubtree" title="MetricCompartmentIdInSubtree">MetricCompartmentIdInSubtree</a>: <i>Boolean</i>
    <a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
    <a href="#pendingduration" title="PendingDuration">PendingDuration</a>: <i>String</i>
    <a href="#query" title="Query">Query</a>: <i>String</i>
    <a href="#repeatnotificationduration" title="RepeatNotificationDuration">RepeatNotificationDuration</a>: <i>String</i>
    <a href="#resolution" title="Resolution">Resolution</a>: <i>String</i>
    <a href="#resourcegroup" title="ResourceGroup">ResourceGroup</a>: <i>String</i>
    <a href="#severity" title="Severity">Severity</a>: <i>String</i>
    <a href="#suppression" title="Suppression">Suppression</a>: <i>
      - <a href="suppression.md">Suppression</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Body

(Updatable) The human-readable content of the notification delivered. Oracle recommends providing guidance to operators for resolving the alarm condition. Consider adding links to standard runbook practices. Avoid entering confidential information.  Example: `High CPU usage alert. Follow runbook instructions for resolution.`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompartmentId

(Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the alarm.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

(Updatable) Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{"Operations.CostCenter": "42"}`.

_Required_: No

_Type_: List of <a href="definedtags.md">DefinedTags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destinations

(Updatable) A list of destinations to which the notifications for this alarm will be delivered.  Each destination is represented by an [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) related to the supported destination service. For example, a destination using the Notifications service is represented by a topic OCID.  Supported destination services: Notifications Service. Limit: One destination per supported destination service.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

(Updatable) A user-friendly name for the alarm. It does not have to be unique, and it's changeable. Avoid entering confidential information.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

(Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"Department": "Finance"}`.

_Required_: No

_Type_: List of <a href="freeformtags.md">FreeformTags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsEnabled

(Updatable) Whether the alarm is enabled.  Example: `true`.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricCompartmentId

(Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the metric being evaluated by the alarm.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricCompartmentIdInSubtree

(Updatable) When true, the alarm evaluates metrics from all compartments and subcompartments. The parameter can only be set to true when metricCompartmentId is the tenancy OCID (the tenancy is the root compartment). A true value requires the user to have tenancy-level permissions. If this requirement is not met, then the call is rejected. When false, the alarm evaluates metrics from only the compartment specified in metricCompartmentId. Default is false.  Example: `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

(Updatable) The source service or application emitting the metric that is evaluated by the alarm.  Example: `oci_computeagent`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PendingDuration

(Updatable) The period of time that the condition defined in the alarm must persist before the alarm state  changes from "OK" to "FIRING". For example, a value of 5 minutes means that the  alarm must persist in breaching the condition for five minutes before the alarm updates its  state to "FIRING".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Query

(Updatable) The Monitoring Query Language (MQL) expression to evaluate for the alarm. The Alarms feature of  the Monitoring service interprets results for each returned time series as Boolean values,  where zero represents false and a non-zero value represents true. A true value means that the trigger  rule condition has been met. The query must specify a metric, statistic, interval, and trigger  rule (threshold or absence). Supported values for interval: `1m`-`60m` (also `1h`). You can optionally  specify dimensions and grouping functions. Supported grouping functions: `grouping()`, `groupBy()`.  For details about Monitoring Query Language (MQL), see [Monitoring Query Language (MQL) Reference](https://docs.cloud.oracle.com/iaas/Content/Monitoring/Reference/mql.htm). For available dimensions, review the metric definition for the supported service.  See [Supported Services](https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#SupportedServices).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RepeatNotificationDuration

(Updatable) The frequency at which notifications are re-submitted, if the alarm keeps firing without interruption. Format defined by ISO 8601. For example, `PT4H` indicates four hours. Minimum: PT1M. Maximum: P30D.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resolution

(Updatable) The time between calculated aggregation windows for the alarm. Supported value: `1m`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroup

(Updatable) Resource group that you want to use as a filter. The alarm retrieves metric data associated with the specified resource group only. Only one resource group can be applied per metric. A valid resourceGroup value starts with an alphabetical character and includes only alphanumeric characters, periods (.), underscores (_), hyphens (-), and dollar signs ($). Avoid entering confidential information.  Example: `frontend-fleet`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Severity

(Updatable) The perceived type of response required when the alarm is in the "FIRING" state.  Example: `CRITICAL`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Suppression

_Required_: No

_Type_: List of <a href="suppression.md">Suppression</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

#### TimeUpdated

Returns the <code>TimeUpdated</code> value.

