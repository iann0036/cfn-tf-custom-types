# TF::ILert::AlertSource

An [alert source](https://api.ilert.com/api-docs/#tag/Alert-Sources) represents the connection between your tools (usually a monitoring system, a ticketing tool, or an application) and iLert. We often refer to alert sources as inbound integrations.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ILert::AlertSource",
    "Properties" : {
        "<a href="#active" title="Active">Active</a>" : <i>Boolean</i>,
        "<a href="#autoresolutiontimeout" title="AutoResolutionTimeout">AutoResolutionTimeout</a>" : <i>String</i>,
        "<a href="#email" title="Email">Email</a>" : <i>String</i>,
        "<a href="#emailfiltered" title="EmailFiltered">EmailFiltered</a>" : <i>Boolean</i>,
        "<a href="#emailresolvefiltered" title="EmailResolveFiltered">EmailResolveFiltered</a>" : <i>Boolean</i>,
        "<a href="#escalationpolicy" title="EscalationPolicy">EscalationPolicy</a>" : <i>String</i>,
        "<a href="#filteroperator" title="FilterOperator">FilterOperator</a>" : <i>String</i>,
        "<a href="#incidentcreation" title="IncidentCreation">IncidentCreation</a>" : <i>String</i>,
        "<a href="#incidentpriorityrule" title="IncidentPriorityRule">IncidentPriorityRule</a>" : <i>String</i>,
        "<a href="#integrationtype" title="IntegrationType">IntegrationType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resolvefilteroperator" title="ResolveFilterOperator">ResolveFilterOperator</a>" : <i>String</i>,
        "<a href="#teams" title="Teams">Teams</a>" : <i>[ Double, ... ]</i>,
        "<a href="#autotaskmetadata" title="AutotaskMetadata">AutotaskMetadata</a>" : <i>[ <a href="autotaskmetadatadefinition.md">AutotaskMetadataDefinition</a>, ... ]</i>,
        "<a href="#emailpredicate" title="EmailPredicate">EmailPredicate</a>" : <i>[ <a href="emailpredicatedefinition.md">EmailPredicateDefinition</a>, ... ]</i>,
        "<a href="#emailresolvepredicate" title="EmailResolvePredicate">EmailResolvePredicate</a>" : <i>[ <a href="emailresolvepredicatedefinition.md">EmailResolvePredicateDefinition</a>, ... ]</i>,
        "<a href="#heartbeat" title="Heartbeat">Heartbeat</a>" : <i>[ <a href="heartbeatdefinition.md">HeartbeatDefinition</a>, ... ]</i>,
        "<a href="#resolvekeyextractor" title="ResolveKeyExtractor">ResolveKeyExtractor</a>" : <i>[ <a href="resolvekeyextractordefinition.md">ResolveKeyExtractorDefinition</a>, ... ]</i>,
        "<a href="#supporthours" title="SupportHours">SupportHours</a>" : <i>[ <a href="supporthoursdefinition.md">SupportHoursDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ILert::AlertSource
Properties:
    <a href="#active" title="Active">Active</a>: <i>Boolean</i>
    <a href="#autoresolutiontimeout" title="AutoResolutionTimeout">AutoResolutionTimeout</a>: <i>String</i>
    <a href="#email" title="Email">Email</a>: <i>String</i>
    <a href="#emailfiltered" title="EmailFiltered">EmailFiltered</a>: <i>Boolean</i>
    <a href="#emailresolvefiltered" title="EmailResolveFiltered">EmailResolveFiltered</a>: <i>Boolean</i>
    <a href="#escalationpolicy" title="EscalationPolicy">EscalationPolicy</a>: <i>String</i>
    <a href="#filteroperator" title="FilterOperator">FilterOperator</a>: <i>String</i>
    <a href="#incidentcreation" title="IncidentCreation">IncidentCreation</a>: <i>String</i>
    <a href="#incidentpriorityrule" title="IncidentPriorityRule">IncidentPriorityRule</a>: <i>String</i>
    <a href="#integrationtype" title="IntegrationType">IntegrationType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resolvefilteroperator" title="ResolveFilterOperator">ResolveFilterOperator</a>: <i>String</i>
    <a href="#teams" title="Teams">Teams</a>: <i>
      - Double</i>
    <a href="#autotaskmetadata" title="AutotaskMetadata">AutotaskMetadata</a>: <i>
      - <a href="autotaskmetadatadefinition.md">AutotaskMetadataDefinition</a></i>
    <a href="#emailpredicate" title="EmailPredicate">EmailPredicate</a>: <i>
      - <a href="emailpredicatedefinition.md">EmailPredicateDefinition</a></i>
    <a href="#emailresolvepredicate" title="EmailResolvePredicate">EmailResolvePredicate</a>: <i>
      - <a href="emailresolvepredicatedefinition.md">EmailResolvePredicateDefinition</a></i>
    <a href="#heartbeat" title="Heartbeat">Heartbeat</a>: <i>
      - <a href="heartbeatdefinition.md">HeartbeatDefinition</a></i>
    <a href="#resolvekeyextractor" title="ResolveKeyExtractor">ResolveKeyExtractor</a>: <i>
      - <a href="resolvekeyextractordefinition.md">ResolveKeyExtractorDefinition</a></i>
    <a href="#supporthours" title="SupportHours">SupportHours</a>: <i>
      - <a href="supporthoursdefinition.md">SupportHoursDefinition</a></i>
</pre>

## Properties

#### Active

The state of the alert source. Default: `true`.
- `incident_priority_rule` - (Optional) The incident priority rule. This option is recommended. Allowed values are `HIGH`, `LOW`, `HIGH_DURING_SUPPORT_HOURS`, `LOW_DURING_SUPPORT_HOURS`.
- `auto_resolution_timeout` - (Optional) The auto resolution timeout. Allowed values are `PT10M`, `PT20M`, `PT30M`, `PT40M`, `PT50M`, `PT60M`, `PT90M`, `PT2H`, `PT3H`, `PT4H`, `PT5H`, `PT6H`, `PT12H`, `PT24H` (`H` means hour and `M` means minute).
- `email` - (Optional) The email address. This option is required if `integration_type` is `EMAIL`.
- `email_filtered` - (Optional) The email filtered. This option is required if `integration_type` is `EMAIL`.
- `email_resolve_filtered` - (Optional) The email resolve filtered. This option is required if `integration_type` is `EMAIL`.
- `filter_operator` - (Optional) The filter operator. This option is required if `integration_type` is `EMAIL`. Allowed values are `AND` and `OR`.
- `resolve_filter_operator` - (Optional) The resolve filter operator. This option is required if `integration_type` is `EMAIL`. Allowed values are `AND` and `OR`.
- `resolve_key_extractor` - (Optional) A [resolve key extractor](#resolve-key-extractor-arguments) block. This option is required if `integration_type` is `EMAIL`.
- `email_predicate` - (Optional) One or more [email predicate](#email-predicate-arguments) blocks. This option is required if `integration_type` is `EMAIL`.
- `email_resolve_predicate` - (Optional) One or more [email resolve predicate](#email-resolve-predicate-arguments) blocks. This option is required if `integration_type` is `EMAIL`.
- `heartbeat` - (Optional) A [heartbeat](#heartbeat-arguments) block. This option is required if `integration_type` is `HEARTBEAT`.
- `support_hours` - (Optional) A [support_hours](#support-hours-arguments) block. This option is allowed if `incident_priority_rule` is `HIGH_DURING_SUPPORT_HOURS` or `LOW_DURING_SUPPORT_HOURS`.
- `autotask_metadata` - (Optional) An [autotask metadata](#autotask-metadata-arguments) block. This option is required if `integration_type` is `AUTOTASK`.
- `teams` - (Optional) A list of related team ids.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoResolutionTimeout

The auto resolution timeout. Allowed values are `PT10M`, `PT20M`, `PT30M`, `PT40M`, `PT50M`, `PT60M`, `PT90M`, `PT2H`, `PT3H`, `PT4H`, `PT5H`, `PT6H`, `PT12H`, `PT24H` (`H` means hour and `M` means minute).
- `email` - (Optional) The email address. This option is required if `integration_type` is `EMAIL`.
- `email_filtered` - (Optional) The email filtered. This option is required if `integration_type` is `EMAIL`.
- `email_resolve_filtered` - (Optional) The email resolve filtered. This option is required if `integration_type` is `EMAIL`.
- `filter_operator` - (Optional) The filter operator. This option is required if `integration_type` is `EMAIL`. Allowed values are `AND` and `OR`.
- `resolve_filter_operator` - (Optional) The resolve filter operator. This option is required if `integration_type` is `EMAIL`. Allowed values are `AND` and `OR`.
- `resolve_key_extractor` - (Optional) A [resolve key extractor](#resolve-key-extractor-arguments) block. This option is required if `integration_type` is `EMAIL`.
- `email_predicate` - (Optional) One or more [email predicate](#email-predicate-arguments) blocks. This option is required if `integration_type` is `EMAIL`.
- `email_resolve_predicate` - (Optional) One or more [email resolve predicate](#email-resolve-predicate-arguments) blocks. This option is required if `integration_type` is `EMAIL`.
- `heartbeat` - (Optional) A [heartbeat](#heartbeat-arguments) block. This option is required if `integration_type` is `HEARTBEAT`.
- `support_hours` - (Optional) A [support_hours](#support-hours-arguments) block. This option is allowed if `incident_priority_rule` is `HIGH_DURING_SUPPORT_HOURS` or `LOW_DURING_SUPPORT_HOURS`.
- `autotask_metadata` - (Optional) An [autotask metadata](#autotask-metadata-arguments) block. This option is required if `integration_type` is `AUTOTASK`.
- `teams` - (Optional) A list of related team ids.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

The email address. This option is required if `integration_type` is `EMAIL`.
- `email_filtered` - (Optional) The email filtered. This option is required if `integration_type` is `EMAIL`.
- `email_resolve_filtered` - (Optional) The email resolve filtered. This option is required if `integration_type` is `EMAIL`.
- `filter_operator` - (Optional) The filter operator. This option is required if `integration_type` is `EMAIL`. Allowed values are `AND` and `OR`.
- `resolve_filter_operator` - (Optional) The resolve filter operator. This option is required if `integration_type` is `EMAIL`. Allowed values are `AND` and `OR`.
- `resolve_key_extractor` - (Optional) A [resolve key extractor](#resolve-key-extractor-arguments) block. This option is required if `integration_type` is `EMAIL`.
- `email_predicate` - (Optional) One or more [email predicate](#email-predicate-arguments) blocks. This option is required if `integration_type` is `EMAIL`.
- `email_resolve_predicate` - (Optional) One or more [email resolve predicate](#email-resolve-predicate-arguments) blocks. This option is required if `integration_type` is `EMAIL`.
- `heartbeat` - (Optional) A [heartbeat](#heartbeat-arguments) block. This option is required if `integration_type` is `HEARTBEAT`.
- `support_hours` - (Optional) A [support_hours](#support-hours-arguments) block. This option is allowed if `incident_priority_rule` is `HIGH_DURING_SUPPORT_HOURS` or `LOW_DURING_SUPPORT_HOURS`.
- `autotask_metadata` - (Optional) An [autotask metadata](#autotask-metadata-arguments) block. This option is required if `integration_type` is `AUTOTASK`.
- `teams` - (Optional) A list of related team ids.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailFiltered

The email filtered. This option is required if `integration_type` is `EMAIL`.
- `email_resolve_filtered` - (Optional) The email resolve filtered. This option is required if `integration_type` is `EMAIL`.
- `filter_operator` - (Optional) The filter operator. This option is required if `integration_type` is `EMAIL`. Allowed values are `AND` and `OR`.
- `resolve_filter_operator` - (Optional) The resolve filter operator. This option is required if `integration_type` is `EMAIL`. Allowed values are `AND` and `OR`.
- `resolve_key_extractor` - (Optional) A [resolve key extractor](#resolve-key-extractor-arguments) block. This option is required if `integration_type` is `EMAIL`.
- `email_predicate` - (Optional) One or more [email predicate](#email-predicate-arguments) blocks. This option is required if `integration_type` is `EMAIL`.
- `email_resolve_predicate` - (Optional) One or more [email resolve predicate](#email-resolve-predicate-arguments) blocks. This option is required if `integration_type` is `EMAIL`.
- `heartbeat` - (Optional) A [heartbeat](#heartbeat-arguments) block. This option is required if `integration_type` is `HEARTBEAT`.
- `support_hours` - (Optional) A [support_hours](#support-hours-arguments) block. This option is allowed if `incident_priority_rule` is `HIGH_DURING_SUPPORT_HOURS` or `LOW_DURING_SUPPORT_HOURS`.
- `autotask_metadata` - (Optional) An [autotask metadata](#autotask-metadata-arguments) block. This option is required if `integration_type` is `AUTOTASK`.
- `teams` - (Optional) A list of related team ids.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailResolveFiltered

The email resolve filtered. This option is required if `integration_type` is `EMAIL`.
- `filter_operator` - (Optional) The filter operator. This option is required if `integration_type` is `EMAIL`. Allowed values are `AND` and `OR`.
- `resolve_filter_operator` - (Optional) The resolve filter operator. This option is required if `integration_type` is `EMAIL`. Allowed values are `AND` and `OR`.
- `resolve_key_extractor` - (Optional) A [resolve key extractor](#resolve-key-extractor-arguments) block. This option is required if `integration_type` is `EMAIL`.
- `email_predicate` - (Optional) One or more [email predicate](#email-predicate-arguments) blocks. This option is required if `integration_type` is `EMAIL`.
- `email_resolve_predicate` - (Optional) One or more [email resolve predicate](#email-resolve-predicate-arguments) blocks. This option is required if `integration_type` is `EMAIL`.
- `heartbeat` - (Optional) A [heartbeat](#heartbeat-arguments) block. This option is required if `integration_type` is `HEARTBEAT`.
- `support_hours` - (Optional) A [support_hours](#support-hours-arguments) block. This option is allowed if `incident_priority_rule` is `HIGH_DURING_SUPPORT_HOURS` or `LOW_DURING_SUPPORT_HOURS`.
- `autotask_metadata` - (Optional) An [autotask metadata](#autotask-metadata-arguments) block. This option is required if `integration_type` is `AUTOTASK`.
- `teams` - (Optional) A list of related team ids.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EscalationPolicy

The escalation policy id used by this alert source.
- `incident_creation` - (Optional) iLert receives events from your monitoring systems and can then create incidents in different ways. This option is recommended. Allowed values are `ONE_INCIDENT_PER_EMAIL`, `ONE_INCIDENT_PER_EMAIL_SUBJECT`, `ONE_PENDING_INCIDENT_ALLOWED`, `ONE_OPEN_INCIDENT_ALLOWED`, `OPEN_RESOLVE_ON_EXTRACTION`.
- `active` - (Optional) The state of the alert source. Default: `true`.
- `incident_priority_rule` - (Optional) The incident priority rule. This option is recommended. Allowed values are `HIGH`, `LOW`, `HIGH_DURING_SUPPORT_HOURS`, `LOW_DURING_SUPPORT_HOURS`.
- `auto_resolution_timeout` - (Optional) The auto resolution timeout. Allowed values are `PT10M`, `PT20M`, `PT30M`, `PT40M`, `PT50M`, `PT60M`, `PT90M`, `PT2H`, `PT3H`, `PT4H`, `PT5H`, `PT6H`, `PT12H`, `PT24H` (`H` means hour and `M` means minute).
- `email` - (Optional) The email address. This option is required if `integration_type` is `EMAIL`.
- `email_filtered` - (Optional) The email filtered. This option is required if `integration_type` is `EMAIL`.
- `email_resolve_filtered` - (Optional) The email resolve filtered. This option is required if `integration_type` is `EMAIL`.
- `filter_operator` - (Optional) The filter operator. This option is required if `integration_type` is `EMAIL`. Allowed values are `AND` and `OR`.
- `resolve_filter_operator` - (Optional) The resolve filter operator. This option is required if `integration_type` is `EMAIL`. Allowed values are `AND` and `OR`.
- `resolve_key_extractor` - (Optional) A [resolve key extractor](#resolve-key-extractor-arguments) block. This option is required if `integration_type` is `EMAIL`.
- `email_predicate` - (Optional) One or more [email predicate](#email-predicate-arguments) blocks. This option is required if `integration_type` is `EMAIL`.
- `email_resolve_predicate` - (Optional) One or more [email resolve predicate](#email-resolve-predicate-arguments) blocks. This option is required if `integration_type` is `EMAIL`.
- `heartbeat` - (Optional) A [heartbeat](#heartbeat-arguments) block. This option is required if `integration_type` is `HEARTBEAT`.
- `support_hours` - (Optional) A [support_hours](#support-hours-arguments) block. This option is allowed if `incident_priority_rule` is `HIGH_DURING_SUPPORT_HOURS` or `LOW_DURING_SUPPORT_HOURS`.
- `autotask_metadata` - (Optional) An [autotask metadata](#autotask-metadata-arguments) block. This option is required if `integration_type` is `AUTOTASK`.
- `teams` - (Optional) A list of related team ids.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterOperator

The filter operator. This option is required if `integration_type` is `EMAIL`. Allowed values are `AND` and `OR`.
- `resolve_filter_operator` - (Optional) The resolve filter operator. This option is required if `integration_type` is `EMAIL`. Allowed values are `AND` and `OR`.
- `resolve_key_extractor` - (Optional) A [resolve key extractor](#resolve-key-extractor-arguments) block. This option is required if `integration_type` is `EMAIL`.
- `email_predicate` - (Optional) One or more [email predicate](#email-predicate-arguments) blocks. This option is required if `integration_type` is `EMAIL`.
- `email_resolve_predicate` - (Optional) One or more [email resolve predicate](#email-resolve-predicate-arguments) blocks. This option is required if `integration_type` is `EMAIL`.
- `heartbeat` - (Optional) A [heartbeat](#heartbeat-arguments) block. This option is required if `integration_type` is `HEARTBEAT`.
- `support_hours` - (Optional) A [support_hours](#support-hours-arguments) block. This option is allowed if `incident_priority_rule` is `HIGH_DURING_SUPPORT_HOURS` or `LOW_DURING_SUPPORT_HOURS`.
- `autotask_metadata` - (Optional) An [autotask metadata](#autotask-metadata-arguments) block. This option is required if `integration_type` is `AUTOTASK`.
- `teams` - (Optional) A list of related team ids.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncidentCreation

iLert receives events from your monitoring systems and can then create incidents in different ways. This option is recommended. Allowed values are `ONE_INCIDENT_PER_EMAIL`, `ONE_INCIDENT_PER_EMAIL_SUBJECT`, `ONE_PENDING_INCIDENT_ALLOWED`, `ONE_OPEN_INCIDENT_ALLOWED`, `OPEN_RESOLVE_ON_EXTRACTION`.
- `active` - (Optional) The state of the alert source. Default: `true`.
- `incident_priority_rule` - (Optional) The incident priority rule. This option is recommended. Allowed values are `HIGH`, `LOW`, `HIGH_DURING_SUPPORT_HOURS`, `LOW_DURING_SUPPORT_HOURS`.
- `auto_resolution_timeout` - (Optional) The auto resolution timeout. Allowed values are `PT10M`, `PT20M`, `PT30M`, `PT40M`, `PT50M`, `PT60M`, `PT90M`, `PT2H`, `PT3H`, `PT4H`, `PT5H`, `PT6H`, `PT12H`, `PT24H` (`H` means hour and `M` means minute).
- `email` - (Optional) The email address. This option is required if `integration_type` is `EMAIL`.
- `email_filtered` - (Optional) The email filtered. This option is required if `integration_type` is `EMAIL`.
- `email_resolve_filtered` - (Optional) The email resolve filtered. This option is required if `integration_type` is `EMAIL`.
- `filter_operator` - (Optional) The filter operator. This option is required if `integration_type` is `EMAIL`. Allowed values are `AND` and `OR`.
- `resolve_filter_operator` - (Optional) The resolve filter operator. This option is required if `integration_type` is `EMAIL`. Allowed values are `AND` and `OR`.
- `resolve_key_extractor` - (Optional) A [resolve key extractor](#resolve-key-extractor-arguments) block. This option is required if `integration_type` is `EMAIL`.
- `email_predicate` - (Optional) One or more [email predicate](#email-predicate-arguments) blocks. This option is required if `integration_type` is `EMAIL`.
- `email_resolve_predicate` - (Optional) One or more [email resolve predicate](#email-resolve-predicate-arguments) blocks. This option is required if `integration_type` is `EMAIL`.
- `heartbeat` - (Optional) A [heartbeat](#heartbeat-arguments) block. This option is required if `integration_type` is `HEARTBEAT`.
- `support_hours` - (Optional) A [support_hours](#support-hours-arguments) block. This option is allowed if `incident_priority_rule` is `HIGH_DURING_SUPPORT_HOURS` or `LOW_DURING_SUPPORT_HOURS`.
- `autotask_metadata` - (Optional) An [autotask metadata](#autotask-metadata-arguments) block. This option is required if `integration_type` is `AUTOTASK`.
- `teams` - (Optional) A list of related team ids.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncidentPriorityRule

The incident priority rule. This option is recommended. Allowed values are `HIGH`, `LOW`, `HIGH_DURING_SUPPORT_HOURS`, `LOW_DURING_SUPPORT_HOURS`.
- `auto_resolution_timeout` - (Optional) The auto resolution timeout. Allowed values are `PT10M`, `PT20M`, `PT30M`, `PT40M`, `PT50M`, `PT60M`, `PT90M`, `PT2H`, `PT3H`, `PT4H`, `PT5H`, `PT6H`, `PT12H`, `PT24H` (`H` means hour and `M` means minute).
- `email` - (Optional) The email address. This option is required if `integration_type` is `EMAIL`.
- `email_filtered` - (Optional) The email filtered. This option is required if `integration_type` is `EMAIL`.
- `email_resolve_filtered` - (Optional) The email resolve filtered. This option is required if `integration_type` is `EMAIL`.
- `filter_operator` - (Optional) The filter operator. This option is required if `integration_type` is `EMAIL`. Allowed values are `AND` and `OR`.
- `resolve_filter_operator` - (Optional) The resolve filter operator. This option is required if `integration_type` is `EMAIL`. Allowed values are `AND` and `OR`.
- `resolve_key_extractor` - (Optional) A [resolve key extractor](#resolve-key-extractor-arguments) block. This option is required if `integration_type` is `EMAIL`.
- `email_predicate` - (Optional) One or more [email predicate](#email-predicate-arguments) blocks. This option is required if `integration_type` is `EMAIL`.
- `email_resolve_predicate` - (Optional) One or more [email resolve predicate](#email-resolve-predicate-arguments) blocks. This option is required if `integration_type` is `EMAIL`.
- `heartbeat` - (Optional) A [heartbeat](#heartbeat-arguments) block. This option is required if `integration_type` is `HEARTBEAT`.
- `support_hours` - (Optional) A [support_hours](#support-hours-arguments) block. This option is allowed if `incident_priority_rule` is `HIGH_DURING_SUPPORT_HOURS` or `LOW_DURING_SUPPORT_HOURS`.
- `autotask_metadata` - (Optional) An [autotask metadata](#autotask-metadata-arguments) block. This option is required if `integration_type` is `AUTOTASK`.
- `teams` - (Optional) A list of related team ids.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationType

The integration type of the alert source. Allowed values are `NAGIOS`, `ICINGA`, `EMAIL`, `SMS`, `API`, `CRN`, `HEARTBEAT`, `PRTG`, `PINGDOM`, `CLOUDWATCH`, `AWSPHD`, `STACKDRIVER`, `INSTANA`, `ZABBIX`, `SOLARWINDS`, `PROMETHEUS`, `NEWRELIC`, `GRAFANA`, `GITHUB`, `DATADOG`, `UPTIMEROBOT`, `APPDYNAMICS`, `DYNATRACE`, `TOPDESK`, `STATUSCAKE`, `MONITOR`, `TOOL`, `CHECKMK`, `AUTOTASK`, `AWSBUDGET`, `KENTIXAM`, `JIRA`, `CONSUL`, `ZAMMAD`, `SIGNALFX`, `SPLUNK`, `KUBERNETES`, `SEMATEXT`, `SENTRY`, `SUMOLOGIC`, `RAYGUN`, `MXTOOLBOX`, `ESWATCHER`, `AMAZONSNS`, `KAPACITOR`, `CORTEXXSOAR`.
- `escalation_policy` - (Required) The escalation policy id used by this alert source.
- `incident_creation` - (Optional) iLert receives events from your monitoring systems and can then create incidents in different ways. This option is recommended. Allowed values are `ONE_INCIDENT_PER_EMAIL`, `ONE_INCIDENT_PER_EMAIL_SUBJECT`, `ONE_PENDING_INCIDENT_ALLOWED`, `ONE_OPEN_INCIDENT_ALLOWED`, `OPEN_RESOLVE_ON_EXTRACTION`.
- `active` - (Optional) The state of the alert source. Default: `true`.
- `incident_priority_rule` - (Optional) The incident priority rule. This option is recommended. Allowed values are `HIGH`, `LOW`, `HIGH_DURING_SUPPORT_HOURS`, `LOW_DURING_SUPPORT_HOURS`.
- `auto_resolution_timeout` - (Optional) The auto resolution timeout. Allowed values are `PT10M`, `PT20M`, `PT30M`, `PT40M`, `PT50M`, `PT60M`, `PT90M`, `PT2H`, `PT3H`, `PT4H`, `PT5H`, `PT6H`, `PT12H`, `PT24H` (`H` means hour and `M` means minute).
- `email` - (Optional) The email address. This option is required if `integration_type` is `EMAIL`.
- `email_filtered` - (Optional) The email filtered. This option is required if `integration_type` is `EMAIL`.
- `email_resolve_filtered` - (Optional) The email resolve filtered. This option is required if `integration_type` is `EMAIL`.
- `filter_operator` - (Optional) The filter operator. This option is required if `integration_type` is `EMAIL`. Allowed values are `AND` and `OR`.
- `resolve_filter_operator` - (Optional) The resolve filter operator. This option is required if `integration_type` is `EMAIL`. Allowed values are `AND` and `OR`.
- `resolve_key_extractor` - (Optional) A [resolve key extractor](#resolve-key-extractor-arguments) block. This option is required if `integration_type` is `EMAIL`.
- `email_predicate` - (Optional) One or more [email predicate](#email-predicate-arguments) blocks. This option is required if `integration_type` is `EMAIL`.
- `email_resolve_predicate` - (Optional) One or more [email resolve predicate](#email-resolve-predicate-arguments) blocks. This option is required if `integration_type` is `EMAIL`.
- `heartbeat` - (Optional) A [heartbeat](#heartbeat-arguments) block. This option is required if `integration_type` is `HEARTBEAT`.
- `support_hours` - (Optional) A [support_hours](#support-hours-arguments) block. This option is allowed if `incident_priority_rule` is `HIGH_DURING_SUPPORT_HOURS` or `LOW_DURING_SUPPORT_HOURS`.
- `autotask_metadata` - (Optional) An [autotask metadata](#autotask-metadata-arguments) block. This option is required if `integration_type` is `AUTOTASK`.
- `teams` - (Optional) A list of related team ids.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the alert source.
- `integration_type` - (Required) The integration type of the alert source. Allowed values are `NAGIOS`, `ICINGA`, `EMAIL`, `SMS`, `API`, `CRN`, `HEARTBEAT`, `PRTG`, `PINGDOM`, `CLOUDWATCH`, `AWSPHD`, `STACKDRIVER`, `INSTANA`, `ZABBIX`, `SOLARWINDS`, `PROMETHEUS`, `NEWRELIC`, `GRAFANA`, `GITHUB`, `DATADOG`, `UPTIMEROBOT`, `APPDYNAMICS`, `DYNATRACE`, `TOPDESK`, `STATUSCAKE`, `MONITOR`, `TOOL`, `CHECKMK`, `AUTOTASK`, `AWSBUDGET`, `KENTIXAM`, `JIRA`, `CONSUL`, `ZAMMAD`, `SIGNALFX`, `SPLUNK`, `KUBERNETES`, `SEMATEXT`, `SENTRY`, `SUMOLOGIC`, `RAYGUN`, `MXTOOLBOX`, `ESWATCHER`, `AMAZONSNS`, `KAPACITOR`, `CORTEXXSOAR`.
- `escalation_policy` - (Required) The escalation policy id used by this alert source.
- `incident_creation` - (Optional) iLert receives events from your monitoring systems and can then create incidents in different ways. This option is recommended. Allowed values are `ONE_INCIDENT_PER_EMAIL`, `ONE_INCIDENT_PER_EMAIL_SUBJECT`, `ONE_PENDING_INCIDENT_ALLOWED`, `ONE_OPEN_INCIDENT_ALLOWED`, `OPEN_RESOLVE_ON_EXTRACTION`.
- `active` - (Optional) The state of the alert source. Default: `true`.
- `incident_priority_rule` - (Optional) The incident priority rule. This option is recommended. Allowed values are `HIGH`, `LOW`, `HIGH_DURING_SUPPORT_HOURS`, `LOW_DURING_SUPPORT_HOURS`.
- `auto_resolution_timeout` - (Optional) The auto resolution timeout. Allowed values are `PT10M`, `PT20M`, `PT30M`, `PT40M`, `PT50M`, `PT60M`, `PT90M`, `PT2H`, `PT3H`, `PT4H`, `PT5H`, `PT6H`, `PT12H`, `PT24H` (`H` means hour and `M` means minute).
- `email` - (Optional) The email address. This option is required if `integration_type` is `EMAIL`.
- `email_filtered` - (Optional) The email filtered. This option is required if `integration_type` is `EMAIL`.
- `email_resolve_filtered` - (Optional) The email resolve filtered. This option is required if `integration_type` is `EMAIL`.
- `filter_operator` - (Optional) The filter operator. This option is required if `integration_type` is `EMAIL`. Allowed values are `AND` and `OR`.
- `resolve_filter_operator` - (Optional) The resolve filter operator. This option is required if `integration_type` is `EMAIL`. Allowed values are `AND` and `OR`.
- `resolve_key_extractor` - (Optional) A [resolve key extractor](#resolve-key-extractor-arguments) block. This option is required if `integration_type` is `EMAIL`.
- `email_predicate` - (Optional) One or more [email predicate](#email-predicate-arguments) blocks. This option is required if `integration_type` is `EMAIL`.
- `email_resolve_predicate` - (Optional) One or more [email resolve predicate](#email-resolve-predicate-arguments) blocks. This option is required if `integration_type` is `EMAIL`.
- `heartbeat` - (Optional) A [heartbeat](#heartbeat-arguments) block. This option is required if `integration_type` is `HEARTBEAT`.
- `support_hours` - (Optional) A [support_hours](#support-hours-arguments) block. This option is allowed if `incident_priority_rule` is `HIGH_DURING_SUPPORT_HOURS` or `LOW_DURING_SUPPORT_HOURS`.
- `autotask_metadata` - (Optional) An [autotask metadata](#autotask-metadata-arguments) block. This option is required if `integration_type` is `AUTOTASK`.
- `teams` - (Optional) A list of related team ids.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResolveFilterOperator

The resolve filter operator. This option is required if `integration_type` is `EMAIL`. Allowed values are `AND` and `OR`.
- `resolve_key_extractor` - (Optional) A [resolve key extractor](#resolve-key-extractor-arguments) block. This option is required if `integration_type` is `EMAIL`.
- `email_predicate` - (Optional) One or more [email predicate](#email-predicate-arguments) blocks. This option is required if `integration_type` is `EMAIL`.
- `email_resolve_predicate` - (Optional) One or more [email resolve predicate](#email-resolve-predicate-arguments) blocks. This option is required if `integration_type` is `EMAIL`.
- `heartbeat` - (Optional) A [heartbeat](#heartbeat-arguments) block. This option is required if `integration_type` is `HEARTBEAT`.
- `support_hours` - (Optional) A [support_hours](#support-hours-arguments) block. This option is allowed if `incident_priority_rule` is `HIGH_DURING_SUPPORT_HOURS` or `LOW_DURING_SUPPORT_HOURS`.
- `autotask_metadata` - (Optional) An [autotask metadata](#autotask-metadata-arguments) block. This option is required if `integration_type` is `AUTOTASK`.
- `teams` - (Optional) A list of related team ids.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Teams

A list of related team ids.

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutotaskMetadata

_Required_: No

_Type_: List of <a href="autotaskmetadatadefinition.md">AutotaskMetadataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailPredicate

_Required_: No

_Type_: List of <a href="emailpredicatedefinition.md">EmailPredicateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailResolvePredicate

_Required_: No

_Type_: List of <a href="emailresolvepredicatedefinition.md">EmailResolvePredicateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Heartbeat

_Required_: No

_Type_: List of <a href="heartbeatdefinition.md">HeartbeatDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResolveKeyExtractor

_Required_: No

_Type_: List of <a href="resolvekeyextractordefinition.md">ResolveKeyExtractorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SupportHours

_Required_: No

_Type_: List of <a href="supporthoursdefinition.md">SupportHoursDefinition</a>

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

#### IntegrationKey

Returns the <code>IntegrationKey</code> value.

#### IntegrationUrl

Returns the <code>IntegrationUrl</code> value.

#### Status

Returns the <code>Status</code> value.

