# TF::NewRelic::EventsToMetricsRule

Use this resource to create, update, and delete New Relic Events to Metrics rules.

-> **IMPORTANT!** Version 2.0.0 of the New Relic Terraform Provider introduces some [additional requirements](/docs/providers/newrelic/index.html) for configuring the provider.
<br><br>
Before upgrading to version 2.0.0 or later, it is recommended to upgrade to the most recent 1.x version of the provider and ensure that your environment successfully runs `terraform plan` without unexpected changes.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NewRelic::EventsToMetricsRule",
    "Properties" : {
        "<a href="#accountid" title="AccountId">AccountId</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nrql" title="Nrql">Nrql</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::NewRelic::EventsToMetricsRule
Properties:
    <a href="#accountid" title="AccountId">AccountId</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nrql" title="Nrql">Nrql</a>: <i>String</i>
</pre>

## Properties

#### AccountId

Account with the event and where the metrics will be put.
* `name` - (Required) The name of the rule. This must be unique within an account.
* `nrql` - (Required) Explains how to create metrics from events.
* `description` - (Optional) Provides additional information about the rule.
* `enabled` - (Optional) True means this rule is enabled. False means the rule is currently not creating metrics.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Provides additional information about the rule.
* `enabled` - (Optional) True means this rule is enabled. False means the rule is currently not creating metrics.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

True means this rule is enabled. False means the rule is currently not creating metrics.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the rule. This must be unique within an account.
* `nrql` - (Required) Explains how to create metrics from events.
* `description` - (Optional) Provides additional information about the rule.
* `enabled` - (Optional) True means this rule is enabled. False means the rule is currently not creating metrics.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nrql

Explains how to create metrics from events.
* `description` - (Optional) Provides additional information about the rule.
* `enabled` - (Optional) True means this rule is enabled. False means the rule is currently not creating metrics.

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

#### RuleId

Returns the <code>RuleId</code> value.

