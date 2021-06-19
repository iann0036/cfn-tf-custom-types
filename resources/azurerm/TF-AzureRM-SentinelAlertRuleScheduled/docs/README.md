# TF::AzureRM::SentinelAlertRuleScheduled

Manages a Sentinel Scheduled Alert Rule.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::SentinelAlertRuleScheduled",
    "Properties" : {
        "<a href="#alertruletemplateguid" title="AlertRuleTemplateGuid">AlertRuleTemplateGuid</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#loganalyticsworkspaceid" title="LogAnalyticsWorkspaceId">LogAnalyticsWorkspaceId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#query" title="Query">Query</a>" : <i>String</i>,
        "<a href="#queryfrequency" title="QueryFrequency">QueryFrequency</a>" : <i>String</i>,
        "<a href="#queryperiod" title="QueryPeriod">QueryPeriod</a>" : <i>String</i>,
        "<a href="#severity" title="Severity">Severity</a>" : <i>String</i>,
        "<a href="#suppressionduration" title="SuppressionDuration">SuppressionDuration</a>" : <i>String</i>,
        "<a href="#suppressionenabled" title="SuppressionEnabled">SuppressionEnabled</a>" : <i>Boolean</i>,
        "<a href="#tactics" title="Tactics">Tactics</a>" : <i>[ String, ... ]</i>,
        "<a href="#triggeroperator" title="TriggerOperator">TriggerOperator</a>" : <i>String</i>,
        "<a href="#triggerthreshold" title="TriggerThreshold">TriggerThreshold</a>" : <i>Double</i>,
        "<a href="#eventgrouping" title="EventGrouping">EventGrouping</a>" : <i>[ <a href="eventgroupingdefinition.md">EventGroupingDefinition</a>, ... ]</i>,
        "<a href="#incidentconfiguration" title="IncidentConfiguration">IncidentConfiguration</a>" : <i>[ <a href="incidentconfigurationdefinition.md">IncidentConfigurationDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::SentinelAlertRuleScheduled
Properties:
    <a href="#alertruletemplateguid" title="AlertRuleTemplateGuid">AlertRuleTemplateGuid</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#loganalyticsworkspaceid" title="LogAnalyticsWorkspaceId">LogAnalyticsWorkspaceId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#query" title="Query">Query</a>: <i>String</i>
    <a href="#queryfrequency" title="QueryFrequency">QueryFrequency</a>: <i>String</i>
    <a href="#queryperiod" title="QueryPeriod">QueryPeriod</a>: <i>String</i>
    <a href="#severity" title="Severity">Severity</a>: <i>String</i>
    <a href="#suppressionduration" title="SuppressionDuration">SuppressionDuration</a>: <i>String</i>
    <a href="#suppressionenabled" title="SuppressionEnabled">SuppressionEnabled</a>: <i>Boolean</i>
    <a href="#tactics" title="Tactics">Tactics</a>: <i>
      - String</i>
    <a href="#triggeroperator" title="TriggerOperator">TriggerOperator</a>: <i>String</i>
    <a href="#triggerthreshold" title="TriggerThreshold">TriggerThreshold</a>: <i>Double</i>
    <a href="#eventgrouping" title="EventGrouping">EventGrouping</a>: <i>
      - <a href="eventgroupingdefinition.md">EventGroupingDefinition</a></i>
    <a href="#incidentconfiguration" title="IncidentConfiguration">IncidentConfiguration</a>: <i>
      - <a href="incidentconfigurationdefinition.md">IncidentConfigurationDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AlertRuleTemplateGuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogAnalyticsWorkspaceId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Query

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryFrequency

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryPeriod

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Severity

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SuppressionDuration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SuppressionEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tactics

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TriggerOperator

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TriggerThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventGrouping

_Required_: No

_Type_: List of <a href="eventgroupingdefinition.md">EventGroupingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncidentConfiguration

_Required_: No

_Type_: List of <a href="incidentconfigurationdefinition.md">IncidentConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

