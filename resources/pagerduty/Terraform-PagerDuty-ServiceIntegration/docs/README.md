# Terraform::PagerDuty::ServiceIntegration

A [service integration](https://v2.developer.pagerduty.com/v2/page/api-reference#!/Services/post_services_id_integrations) is an integration that belongs to a service.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::PagerDuty::ServiceIntegration",
    "Properties" : {
        "<a href="#integrationemail" title="IntegrationEmail">IntegrationEmail</a>" : <i>String</i>,
        "<a href="#integrationkey" title="IntegrationKey">IntegrationKey</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#service" title="Service">Service</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#vendor" title="Vendor">Vendor</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::PagerDuty::ServiceIntegration
Properties:
    <a href="#integrationemail" title="IntegrationEmail">IntegrationEmail</a>: <i>String</i>
    <a href="#integrationkey" title="IntegrationKey">IntegrationKey</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#service" title="Service">Service</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#vendor" title="Vendor">Vendor</a>: <i>String</i>
</pre>

## Properties

#### IntegrationEmail

This is the unique fully-qualified email address used for routing emails to this integration for processing.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationKey

This is the unique key used to route events to this integration when received via the PagerDuty Events API.
* `integration_email` - (Optional) This is the unique fully-qualified email address used for routing emails to this integration for processing.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the service integration.
* `type` - (Optional) The service type. Can be:
`aws_cloudwatch_inbound_integration`,
`cloudkick_inbound_integration`,
`event_transformer_api_inbound_integration`,
`events_api_v2_inbound_integration` (requires service `alert_creation` to be `create_alerts_and_incidents`),
`generic_email_inbound_integration`,
`generic_events_api_inbound_integration`,
`keynote_inbound_integration`,
`nagios_inbound_integration`,
`pingdom_inbound_integration`or `sql_monitor_inbound_integration`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

The ID of the service the integration should belong to.
* `name` - (Optional) The name of the service integration.
* `type` - (Optional) The service type. Can be:
`aws_cloudwatch_inbound_integration`,
`cloudkick_inbound_integration`,
`event_transformer_api_inbound_integration`,
`events_api_v2_inbound_integration` (requires service `alert_creation` to be `create_alerts_and_incidents`),
`generic_email_inbound_integration`,
`generic_events_api_inbound_integration`,
`keynote_inbound_integration`,
`nagios_inbound_integration`,
`pingdom_inbound_integration`or `sql_monitor_inbound_integration`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The service type. Can be:
`aws_cloudwatch_inbound_integration`,
`cloudkick_inbound_integration`,
`event_transformer_api_inbound_integration`,
`events_api_v2_inbound_integration` (requires service `alert_creation` to be `create_alerts_and_incidents`),
`generic_email_inbound_integration`,
`generic_events_api_inbound_integration`,
`keynote_inbound_integration`,
`nagios_inbound_integration`,
`pingdom_inbound_integration`or `sql_monitor_inbound_integration`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vendor

The ID of the vendor the integration should integrate with (e.g Datadog or Amazon Cloudwatch).
* `integration_key` - (Optional) This is the unique key used to route events to this integration when received via the PagerDuty Events API.
* `integration_email` - (Optional) This is the unique fully-qualified email address used for routing emails to this integration for processing.

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

#### HtmlUrl

Returns the <code>HtmlUrl</code> value.

#### Id

Returns the <code>Id</code> value.

