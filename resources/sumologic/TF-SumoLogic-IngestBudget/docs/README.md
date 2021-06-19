# TF::SumoLogic::IngestBudget

Provides a [Sumologic Ingest Budget][1]. To assign an Ingest Budget to the Collector use the field `_budget` with the Field Value of the Ingest Budget to assign.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::SumoLogic::IngestBudget",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#capacitybytes" title="CapacityBytes">CapacityBytes</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#fieldvalue" title="FieldValue">FieldValue</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resettime" title="ResetTime">ResetTime</a>" : <i>String</i>,
        "<a href="#timezone" title="Timezone">Timezone</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::SumoLogic::IngestBudget
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#capacitybytes" title="CapacityBytes">CapacityBytes</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#fieldvalue" title="FieldValue">FieldValue</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resettime" title="ResetTime">ResetTime</a>: <i>String</i>
    <a href="#timezone" title="Timezone">Timezone</a>: <i>String</i>
</pre>

## Properties

#### Action

Action to take when ingest budget's capacity is reached. All actions are audited. Supported values are `stopCollecting` and `keepCollecting`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CapacityBytes

Capacity of the ingest budget, in bytes.
* `description` - (Optional) The description of the collector.
* `timezone` - (Optional) The time zone to use for this collector. The value follows the [tzdata][2] naming convention. Defaults to `Etc/UTC`
* `reset_time` - (Optional) Reset time of the ingest budget in HH:MM format. Defaults to `00:00`
* `reset_time` - (Optional) Reset time of the ingest budget in HH:MM format. Defaults to `00:00`
* `description` - (Optional) Description of the ingest budget.
* `action` - (Optional) Action to take when ingest budget's capacity is reached. All actions are audited. Supported values are `stopCollecting` and `keepCollecting`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of the ingest budget.
* `action` - (Optional) Action to take when ingest budget's capacity is reached. All actions are audited. Supported values are `stopCollecting` and `keepCollecting`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FieldValue

Custom field value that is used to assign Collectors to the ingest budget.
* `capacity_bytes` - (Required) Capacity of the ingest budget, in bytes.
* `description` - (Optional) The description of the collector.
* `timezone` - (Optional) The time zone to use for this collector. The value follows the [tzdata][2] naming convention. Defaults to `Etc/UTC`
* `reset_time` - (Optional) Reset time of the ingest budget in HH:MM format. Defaults to `00:00`
* `reset_time` - (Optional) Reset time of the ingest budget in HH:MM format. Defaults to `00:00`
* `description` - (Optional) Description of the ingest budget.
* `action` - (Optional) Action to take when ingest budget's capacity is reached. All actions are audited. Supported values are `stopCollecting` and `keepCollecting`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Display name of the ingest budget. This must be unique across all of the ingest budgets
* `field_value` - (Required) Custom field value that is used to assign Collectors to the ingest budget.
* `capacity_bytes` - (Required) Capacity of the ingest budget, in bytes.
* `description` - (Optional) The description of the collector.
* `timezone` - (Optional) The time zone to use for this collector. The value follows the [tzdata][2] naming convention. Defaults to `Etc/UTC`
* `reset_time` - (Optional) Reset time of the ingest budget in HH:MM format. Defaults to `00:00`
* `reset_time` - (Optional) Reset time of the ingest budget in HH:MM format. Defaults to `00:00`
* `description` - (Optional) Description of the ingest budget.
* `action` - (Optional) Action to take when ingest budget's capacity is reached. All actions are audited. Supported values are `stopCollecting` and `keepCollecting`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResetTime

Reset time of the ingest budget in HH:MM format. Defaults to `00:00`
* `description` - (Optional) Description of the ingest budget.
* `action` - (Optional) Action to take when ingest budget's capacity is reached. All actions are audited. Supported values are `stopCollecting` and `keepCollecting`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timezone

The time zone to use for this collector. The value follows the [tzdata][2] naming convention. Defaults to `Etc/UTC`
* `reset_time` - (Optional) Reset time of the ingest budget in HH:MM format. Defaults to `00:00`
* `reset_time` - (Optional) Reset time of the ingest budget in HH:MM format. Defaults to `00:00`
* `description` - (Optional) Description of the ingest budget.
* `action` - (Optional) Action to take when ingest budget's capacity is reached. All actions are audited. Supported values are `stopCollecting` and `keepCollecting`.

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

The internal ID of the ingest budget. This can be used to assign collectors to the ingest budget.

