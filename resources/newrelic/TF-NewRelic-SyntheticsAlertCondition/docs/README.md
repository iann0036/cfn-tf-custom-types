# TF::NewRelic::SyntheticsAlertCondition

Use this resource to create and manage synthetics alert conditions in New Relic.

-> **NOTE:** The [newrelic_nrql_alert_condition](nrql_alert_condition.html) resource is preferred for configuring alerts conditions. In most cases feature parity can be achieved with a NRQL query. Other condition types may be deprecated in the future and receive fewer product updates.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NewRelic::SyntheticsAlertCondition",
    "Properties" : {
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#monitorid" title="MonitorId">MonitorId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#policyid" title="PolicyId">PolicyId</a>" : <i>Double</i>,
        "<a href="#runbookurl" title="RunbookUrl">RunbookUrl</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NewRelic::SyntheticsAlertCondition
Properties:
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#monitorid" title="MonitorId">MonitorId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#policyid" title="PolicyId">PolicyId</a>: <i>Double</i>
    <a href="#runbookurl" title="RunbookUrl">RunbookUrl</a>: <i>String</i>
</pre>

## Properties

#### Enabled

Set whether to enable the alert condition. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitorId

The ID of the Synthetics monitor to be referenced in the alert condition.
* `runbook_url` - (Optional) Runbook URL to display in notifications.
* `enabled` - (Optional) Set whether to enable the alert condition. Defaults to `true`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The title of this condition.
* `monitor_id` - (Required) The ID of the Synthetics monitor to be referenced in the alert condition.
* `runbook_url` - (Optional) Runbook URL to display in notifications.
* `enabled` - (Optional) Set whether to enable the alert condition. Defaults to `true`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyId

The ID of the policy where this condition should be used.
* `name` - (Required) The title of this condition.
* `monitor_id` - (Required) The ID of the Synthetics monitor to be referenced in the alert condition.
* `runbook_url` - (Optional) Runbook URL to display in notifications.
* `enabled` - (Optional) Set whether to enable the alert condition. Defaults to `true`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunbookUrl

Runbook URL to display in notifications.
* `enabled` - (Optional) Set whether to enable the alert condition. Defaults to `true`.

_Required_: No

_Type_: String

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

