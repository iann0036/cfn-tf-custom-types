# TF::NewRelic::SyntheticsMultilocationAlertCondition

Use this resource to create, update, and delete a New Relic Synthetics Location Alerts.

-> **NOTE:** The [newrelic_nrql_alert_condition](nrql_alert_condition.html) resource is preferred for configuring alerts conditions. In most cases feature parity can be achieved with a NRQL query. Other condition types may be deprecated in the future and receive fewer product updates.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NewRelic::SyntheticsMultilocationAlertCondition",
    "Properties" : {
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#entities" title="Entities">Entities</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#policyid" title="PolicyId">PolicyId</a>" : <i>Double</i>,
        "<a href="#runbookurl" title="RunbookUrl">RunbookUrl</a>" : <i>String</i>,
        "<a href="#violationtimelimitseconds" title="ViolationTimeLimitSeconds">ViolationTimeLimitSeconds</a>" : <i>Double</i>,
        "<a href="#critical" title="Critical">Critical</a>" : <i>[ <a href="criticaldefinition.md">CriticalDefinition</a>, ... ]</i>,
        "<a href="#warning" title="Warning">Warning</a>" : <i>[ <a href="warningdefinition.md">WarningDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NewRelic::SyntheticsMultilocationAlertCondition
Properties:
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#entities" title="Entities">Entities</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#policyid" title="PolicyId">PolicyId</a>: <i>Double</i>
    <a href="#runbookurl" title="RunbookUrl">RunbookUrl</a>: <i>String</i>
    <a href="#violationtimelimitseconds" title="ViolationTimeLimitSeconds">ViolationTimeLimitSeconds</a>: <i>Double</i>
    <a href="#critical" title="Critical">Critical</a>: <i>
      - <a href="criticaldefinition.md">CriticalDefinition</a></i>
    <a href="#warning" title="Warning">Warning</a>: <i>
      - <a href="warningdefinition.md">WarningDefinition</a></i>
</pre>

## Properties

#### Enabled

Set whether to enable the alert condition.  Defaults to true.
* `entities` - (Required) The GUIDs of the Synthetics monitors to alert on.
* `critical` - (Required) A condition term with the priority set to critical.
* `warning` - (Optional) A condition term with the priority set to warning.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Entities

The GUIDs of the Synthetics monitors to alert on.
* `critical` - (Required) A condition term with the priority set to critical.
* `warning` - (Optional) A condition term with the priority set to warning.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The title of the condition.
* `policy_id` - (Required) The ID of the policy where this condition will be used.
* `runbook_url` - (Optional) Runbook URL to display in notifications.
* `enabled` - (Optional) Set whether to enable the alert condition.  Defaults to true.
* `entities` - (Required) The GUIDs of the Synthetics monitors to alert on.
* `critical` - (Required) A condition term with the priority set to critical.
* `warning` - (Optional) A condition term with the priority set to warning.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyId

The ID of the policy where this condition will be used.
* `runbook_url` - (Optional) Runbook URL to display in notifications.
* `enabled` - (Optional) Set whether to enable the alert condition.  Defaults to true.
* `entities` - (Required) The GUIDs of the Synthetics monitors to alert on.
* `critical` - (Required) A condition term with the priority set to critical.
* `warning` - (Optional) A condition term with the priority set to warning.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunbookUrl

Runbook URL to display in notifications.
* `enabled` - (Optional) Set whether to enable the alert condition.  Defaults to true.
* `entities` - (Required) The GUIDs of the Synthetics monitors to alert on.
* `critical` - (Required) A condition term with the priority set to critical.
* `warning` - (Optional) A condition term with the priority set to warning.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ViolationTimeLimitSeconds

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Critical

_Required_: No

_Type_: List of <a href="criticaldefinition.md">CriticalDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Warning

_Required_: No

_Type_: List of <a href="warningdefinition.md">WarningDefinition</a>

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

