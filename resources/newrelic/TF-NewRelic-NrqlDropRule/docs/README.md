# TF::NewRelic::NrqlDropRule

Use this resource to create, and delete New Relic NRQL Drop Rules.

-> **IMPORTANT!** Version 2.0.0 of the New Relic Terraform Provider introduces some [additional requirements](/docs/providers/newrelic/index.html) for configuring the provider.
<br><br>
Before upgrading to version 2.0.0 or later, it is recommended to upgrade to the most recent 1.x version of the provider and ensure that your environment successfully runs `terraform plan` without unexpected changes.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NewRelic::NrqlDropRule",
    "Properties" : {
        "<a href="#accountid" title="AccountId">AccountId</a>" : <i>Double</i>,
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#nrql" title="Nrql">Nrql</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::NewRelic::NrqlDropRule
Properties:
    <a href="#accountid" title="AccountId">AccountId</a>: <i>Double</i>
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#nrql" title="Nrql">Nrql</a>: <i>String</i>
</pre>

## Properties

#### AccountId

Account where the drop rule will be put. Defaults to the account associated with the API key used.
* `description` - (Optional) The description of the drop rule.
* `nrql` - (Required) A NRQL string that specifies what data types to drop.
* `action` - (Required) An action type specifying how to apply the NRQL string (either `drop_data` or `drop_attributes`).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Action

An action type specifying how to apply the NRQL string (either `drop_data` or `drop_attributes`).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description of the drop rule.
* `nrql` - (Required) A NRQL string that specifies what data types to drop.
* `action` - (Required) An action type specifying how to apply the NRQL string (either `drop_data` or `drop_attributes`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nrql

A NRQL string that specifies what data types to drop.
* `action` - (Required) An action type specifying how to apply the NRQL string (either `drop_data` or `drop_attributes`).

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

