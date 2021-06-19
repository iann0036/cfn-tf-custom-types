# TF::ILert::UptimeMonitor

An [uptime monitor](https://api.ilert.com/api-docs/#tag/Uptime-Monitors) allows you to quickly setup monitoring for any kind of exposed service e.g. HTTP (e.g. websites), ICMP (ping) or TCP and UDP servers.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ILert::UptimeMonitor",
    "Properties" : {
        "<a href="#checktype" title="CheckType">CheckType</a>" : <i>String</i>,
        "<a href="#createincidentafterfailedchecks" title="CreateIncidentAfterFailedChecks">CreateIncidentAfterFailedChecks</a>" : <i>Double</i>,
        "<a href="#escalationpolicy" title="EscalationPolicy">EscalationPolicy</a>" : <i>String</i>,
        "<a href="#intervalsec" title="IntervalSec">IntervalSec</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#paused" title="Paused">Paused</a>" : <i>Boolean</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#timeoutms" title="TimeoutMs">TimeoutMs</a>" : <i>Double</i>,
        "<a href="#checkparams" title="CheckParams">CheckParams</a>" : <i>[ <a href="checkparamsdefinition.md">CheckParamsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ILert::UptimeMonitor
Properties:
    <a href="#checktype" title="CheckType">CheckType</a>: <i>String</i>
    <a href="#createincidentafterfailedchecks" title="CreateIncidentAfterFailedChecks">CreateIncidentAfterFailedChecks</a>: <i>Double</i>
    <a href="#escalationpolicy" title="EscalationPolicy">EscalationPolicy</a>: <i>String</i>
    <a href="#intervalsec" title="IntervalSec">IntervalSec</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#paused" title="Paused">Paused</a>: <i>Boolean</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#timeoutms" title="TimeoutMs">TimeoutMs</a>: <i>Double</i>
    <a href="#checkparams" title="CheckParams">CheckParams</a>: <i>
      - <a href="checkparamsdefinition.md">CheckParamsDefinition</a></i>
</pre>

## Properties

#### CheckType

The check type of the uptime monitor. Allowed values are `http`, `ping`, `tcp` and `udp`.
- `check_params` - (Required) A [check params](#check-params-arguments) block.
- `interval_sec` - (Optional) The check interval in seconds of the uptime monitor. Allowed values are `60`, `300`, `600`, `900`, `1800` and `3600`. Default: `300`.
- `timeout_ms` - (Optional) The check timeout in milliseconds of the uptime monitor. Allowed values are between `1000` to `60000`. Default: `30000`.
- `create_incident_after_failed_checks` - (Optional) The incident creation ratio after failed checks of the uptime monitor. Allowed values are between `1` to `12`. Default: `1`.
- `escalation_policy` - (Required) The escalation policy id used by this uptime monitor.
- `paused` - (Optional) The paused state of the uptime monitor. Default: `false`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateIncidentAfterFailedChecks

The incident creation ratio after failed checks of the uptime monitor. Allowed values are between `1` to `12`. Default: `1`.
- `escalation_policy` - (Required) The escalation policy id used by this uptime monitor.
- `paused` - (Optional) The paused state of the uptime monitor. Default: `false`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EscalationPolicy

The escalation policy id used by this uptime monitor.
- `paused` - (Optional) The paused state of the uptime monitor. Default: `false`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntervalSec

The check interval in seconds of the uptime monitor. Allowed values are `60`, `300`, `600`, `900`, `1800` and `3600`. Default: `300`.
- `timeout_ms` - (Optional) The check timeout in milliseconds of the uptime monitor. Allowed values are between `1000` to `60000`. Default: `30000`.
- `create_incident_after_failed_checks` - (Optional) The incident creation ratio after failed checks of the uptime monitor. Allowed values are between `1` to `12`. Default: `1`.
- `escalation_policy` - (Required) The escalation policy id used by this uptime monitor.
- `paused` - (Optional) The paused state of the uptime monitor. Default: `false`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the uptime monitor.
- `region` - (Optional) The region of the uptime monitor. Allowed values are `EU` and `US`. Default: `EU`.
- `check_type` - (Required) The check type of the uptime monitor. Allowed values are `http`, `ping`, `tcp` and `udp`.
- `check_params` - (Required) A [check params](#check-params-arguments) block.
- `interval_sec` - (Optional) The check interval in seconds of the uptime monitor. Allowed values are `60`, `300`, `600`, `900`, `1800` and `3600`. Default: `300`.
- `timeout_ms` - (Optional) The check timeout in milliseconds of the uptime monitor. Allowed values are between `1000` to `60000`. Default: `30000`.
- `create_incident_after_failed_checks` - (Optional) The incident creation ratio after failed checks of the uptime monitor. Allowed values are between `1` to `12`. Default: `1`.
- `escalation_policy` - (Required) The escalation policy id used by this uptime monitor.
- `paused` - (Optional) The paused state of the uptime monitor. Default: `false`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Paused

The paused state of the uptime monitor. Default: `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region of the uptime monitor. Allowed values are `EU` and `US`. Default: `EU`.
- `check_type` - (Required) The check type of the uptime monitor. Allowed values are `http`, `ping`, `tcp` and `udp`.
- `check_params` - (Required) A [check params](#check-params-arguments) block.
- `interval_sec` - (Optional) The check interval in seconds of the uptime monitor. Allowed values are `60`, `300`, `600`, `900`, `1800` and `3600`. Default: `300`.
- `timeout_ms` - (Optional) The check timeout in milliseconds of the uptime monitor. Allowed values are between `1000` to `60000`. Default: `30000`.
- `create_incident_after_failed_checks` - (Optional) The incident creation ratio after failed checks of the uptime monitor. Allowed values are between `1` to `12`. Default: `1`.
- `escalation_policy` - (Required) The escalation policy id used by this uptime monitor.
- `paused` - (Optional) The paused state of the uptime monitor. Default: `false`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutMs

The check timeout in milliseconds of the uptime monitor. Allowed values are between `1000` to `60000`. Default: `30000`.
- `create_incident_after_failed_checks` - (Optional) The incident creation ratio after failed checks of the uptime monitor. Allowed values are between `1` to `12`. Default: `1`.
- `escalation_policy` - (Required) The escalation policy id used by this uptime monitor.
- `paused` - (Optional) The paused state of the uptime monitor. Default: `false`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckParams

_Required_: No

_Type_: List of <a href="checkparamsdefinition.md">CheckParamsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### EmbedUrl

Returns the <code>EmbedUrl</code> value.

#### Id

Returns the <code>Id</code> value.

#### ShareUrl

Returns the <code>ShareUrl</code> value.

#### Status

Returns the <code>Status</code> value.

