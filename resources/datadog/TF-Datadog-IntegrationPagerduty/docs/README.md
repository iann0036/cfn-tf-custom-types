# TF::Datadog::IntegrationPagerduty

CloudFormation equivalent of datadog_integration_pagerduty

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Datadog::IntegrationPagerduty",
    "Properties" : {
        "<a href="#apitoken" title="ApiToken">ApiToken</a>" : <i>String</i>,
        "<a href="#schedules" title="Schedules">Schedules</a>" : <i>[ String, ... ]</i>,
        "<a href="#subdomain" title="Subdomain">Subdomain</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Datadog::IntegrationPagerduty
Properties:
    <a href="#apitoken" title="ApiToken">ApiToken</a>: <i>String</i>
    <a href="#schedules" title="Schedules">Schedules</a>: <i>
      - String</i>
    <a href="#subdomain" title="Subdomain">Subdomain</a>: <i>String</i>
</pre>

## Properties

#### ApiToken

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedules

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subdomain

_Required_: Yes

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

