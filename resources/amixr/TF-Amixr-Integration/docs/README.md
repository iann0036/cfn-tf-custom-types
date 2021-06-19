# TF::Amixr::Integration

[Integrations](https://api-docs.amixr.io/#integrations) are sources of alerts and incidents for Amixr.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Amixr::Integration",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#templates" title="Templates">Templates</a>" : <i>[ <a href="templatesdefinition.md">TemplatesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Amixr::Integration
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#templates" title="Templates">Templates</a>: <i>
      - <a href="templatesdefinition.md">TemplatesDefinition</a></i>
</pre>

## Properties

#### Name

The name of the service integration.
* `type` - (Required) The type of integration. Can be:
`grafana`, `webhook`, `alertmanager`, `kapacitor` , `fabric`,
`newrelic`, `datadog`, `pagerduty`, `pingdom`,
`elastalert`, `amazon_sns`, `curler`, `sentry`,
`formatted_webhook`, `heartbeat`, `demo`, `stackdriver`,
`uptimerobot`, `sentry_platform`, `zabbix`, `prtg`
or `inbound_email`.
* `templates` - (Optional) Jinja2 templates for Alert payload. Includes:
- `grouping_key`- (Optional) Template for the key by which alerts are grouped.
- `resolve_signal`- (Optional) Template for sending a signal to resolve the Incident. This template should output one of the following values: ok, true, 1 (case insensitive)
- `slack`- (Optional) Templates for Slack:
- `title`- (Optional) Template for Alert title.
- `message`- (Optional) Template for Alert message.
- `image_url`- (Optional) Template for Alert image url.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of integration. Can be:
`grafana`, `webhook`, `alertmanager`, `kapacitor` , `fabric`,
`newrelic`, `datadog`, `pagerduty`, `pingdom`,
`elastalert`, `amazon_sns`, `curler`, `sentry`,
`formatted_webhook`, `heartbeat`, `demo`, `stackdriver`,
`uptimerobot`, `sentry_platform`, `zabbix`, `prtg`
or `inbound_email`.
* `templates` - (Optional) Jinja2 templates for Alert payload. Includes:
- `grouping_key`- (Optional) Template for the key by which alerts are grouped.
- `resolve_signal`- (Optional) Template for sending a signal to resolve the Incident. This template should output one of the following values: ok, true, 1 (case insensitive)
- `slack`- (Optional) Templates for Slack:
- `title`- (Optional) Template for Alert title.
- `message`- (Optional) Template for Alert message.
- `image_url`- (Optional) Template for Alert image url.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Templates

_Required_: No

_Type_: List of <a href="templatesdefinition.md">TemplatesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### DefaultRouteId

Returns the <code>DefaultRouteId</code> value.

#### Id

Returns the <code>Id</code> value.

#### Link

Returns the <code>Link</code> value.

