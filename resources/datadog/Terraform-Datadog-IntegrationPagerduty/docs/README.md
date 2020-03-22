# Terraform::Datadog::IntegrationPagerduty

Provides a Datadog - PagerDuty resource. This can be used to create and manage Datadog - PagerDuty integration.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Datadog::IntegrationPagerduty",
    "Properties" : {
        "<a href="#apitoken" title="ApiToken">ApiToken</a>" : <i>String</i>,
        "<a href="#individualservices" title="IndividualServices">IndividualServices</a>" : <i>Boolean</i>,
        "<a href="#schedules" title="Schedules">Schedules</a>" : <i>[ String, ... ]</i>,
        "<a href="#subdomain" title="Subdomain">Subdomain</a>" : <i>String</i>,
        "<a href="#services" title="Services">Services</a>" : <i>[ <a href="services.md">Services</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Datadog::IntegrationPagerduty
Properties:
    <a href="#apitoken" title="ApiToken">ApiToken</a>: <i>String</i>
    <a href="#individualservices" title="IndividualServices">IndividualServices</a>: <i>Boolean</i>
    <a href="#schedules" title="Schedules">Schedules</a>: <i>
      - String</i>
    <a href="#subdomain" title="Subdomain">Subdomain</a>: <i>String</i>
    <a href="#services" title="Services">Services</a>: <i>
      - <a href="services.md">Services</a></i>
</pre>

## Properties

#### ApiToken

Your PagerDuty API token.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IndividualServices

Boolean to specify whether or not individual service objects specified by [datadog_integration_pagerduty_service_object](/docs/providers/datadog/r/integration_pagerduty_service_object.html) resource are to be used. Mutually exclusive with `services` key.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedules

Array of your schedule URLs.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subdomain

Your PagerDuty account’s personalized subdomain name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Services

_Required_: No

_Type_: List of <a href="services.md">Services</a>

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

