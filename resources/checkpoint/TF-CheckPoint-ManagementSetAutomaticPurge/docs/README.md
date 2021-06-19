# TF::CheckPoint::ManagementSetAutomaticPurge

This command resource allows you to execute Check Point Set Automatic Purge.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CheckPoint::ManagementSetAutomaticPurge",
    "Properties" : {
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#keepsessionsbycount" title="KeepSessionsByCount">KeepSessionsByCount</a>" : <i>Boolean</i>,
        "<a href="#keepsessionsbydays" title="KeepSessionsByDays">KeepSessionsByDays</a>" : <i>Boolean</i>,
        "<a href="#numberofdaystokeep" title="NumberOfDaysToKeep">NumberOfDaysToKeep</a>" : <i>Double</i>,
        "<a href="#numberofsessionstokeep" title="NumberOfSessionsToKeep">NumberOfSessionsToKeep</a>" : <i>Double</i>,
        "<a href="#scheduling" title="Scheduling">Scheduling</a>" : <i>[ <a href="schedulingdefinition.md">SchedulingDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::CheckPoint::ManagementSetAutomaticPurge
Properties:
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#keepsessionsbycount" title="KeepSessionsByCount">KeepSessionsByCount</a>: <i>Boolean</i>
    <a href="#keepsessionsbydays" title="KeepSessionsByDays">KeepSessionsByDays</a>: <i>Boolean</i>
    <a href="#numberofdaystokeep" title="NumberOfDaysToKeep">NumberOfDaysToKeep</a>: <i>Double</i>
    <a href="#numberofsessionstokeep" title="NumberOfSessionsToKeep">NumberOfSessionsToKeep</a>: <i>Double</i>
    <a href="#scheduling" title="Scheduling">Scheduling</a>: <i>
      - <a href="schedulingdefinition.md">SchedulingDefinition</a></i>
</pre>

## Properties

#### Enabled

Turn on/off the automatic-purge feature.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepSessionsByCount

Whether or not to keep the latest N sessions.
Note: when the automatic purge feature is enabled, this field and/or the "keep-sessions-by-date" field must be set to 'true'.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepSessionsByDays

Whether or not to keep the sessions for D days.
Note: when the automatic purge feature is enabled, this field and/or the "keep-sessions-by-count" field must be set to 'true'.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumberOfDaysToKeep

When "keep-sessions-by-days = true" this sets the number of days to keep the sessions.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumberOfSessionsToKeep

When "keep-sessions-by-count = true" this sets the number of newest sessions to preserve, by the sessions's publish date.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scheduling

When to purge sessions that do not meet the "keep" criteria. Note: when the automatic purge feature is enabled, this field must be set.scheduling blocks are documented below.

_Required_: No

_Type_: List of <a href="schedulingdefinition.md">SchedulingDefinition</a>

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

