# TF::NewRelic::AlertMutingRule

Use this resource to create a muting rule for New Relic Alerts violations.

-> **IMPORTANT!** Version 2.0.0 of the New Relic Terraform Provider introduces some [additional requirements](/docs/providers/newrelic/index.html) for configuring the provider.
<br><br>
Before upgrading to version 2.0.0 or later, it is recommended to upgrade to the most recent 1.x version of the provider and ensure that your environment successfully runs `terraform plan` without unexpected changes.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NewRelic::AlertMutingRule",
    "Properties" : {
        "<a href="#accountid" title="AccountId">AccountId</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#condition" title="Condition">Condition</a>" : <i>[ <a href="conditiondefinition.md">ConditionDefinition</a>, ... ]</i>,
        "<a href="#schedule" title="Schedule">Schedule</a>" : <i>[ <a href="scheduledefinition.md">ScheduleDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NewRelic::AlertMutingRule
Properties:
    <a href="#accountid" title="AccountId">AccountId</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#condition" title="Condition">Condition</a>: <i>
      - <a href="conditiondefinition.md">ConditionDefinition</a></i>
    <a href="#schedule" title="Schedule">Schedule</a>: <i>
      - <a href="scheduledefinition.md">ScheduleDefinition</a></i>
</pre>

## Properties

#### AccountId

The account id of the MutingRule.
* `condition`  - (Required) The condition that defines which violations to target. See [Nested condition blocks](#nested-condition-blocks) below for details.
* `enabled` - (Required) Whether the MutingRule is enabled.
* `name` - The name of the MutingRule.
* `description` - The description of the MutingRule.
* `schedule` - (Optional) Specify a schedule for enabling the MutingRule. See [Schedule](#schedule) below for details.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description of the MutingRule.
* `schedule` - (Optional) Specify a schedule for enabling the MutingRule. See [Schedule](#schedule) below for details.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Whether the MutingRule is enabled.
* `name` - The name of the MutingRule.
* `description` - The description of the MutingRule.
* `schedule` - (Optional) Specify a schedule for enabling the MutingRule. See [Schedule](#schedule) below for details.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the MutingRule.
* `description` - The description of the MutingRule.
* `schedule` - (Optional) Specify a schedule for enabling the MutingRule. See [Schedule](#schedule) below for details.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Condition

_Required_: No

_Type_: List of <a href="conditiondefinition.md">ConditionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

_Required_: No

_Type_: List of <a href="scheduledefinition.md">ScheduleDefinition</a>

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

