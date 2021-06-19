# TF::SignalFx::AlertMutingRule

Provides a SignalFx resource for managing alert muting rules. See [Mute Notifications](https://docs.signalfx.com/en/latest/detect-alert/mute-notifications.html) for more information.

~> **WARNING** SignalFx does not allow the start time of a **currently active** muting rule to be modified. As such, attempting to modify a currently active rule will destroy the existing rule and create a new rule. This may result in the emission of notifications.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::SignalFx::AlertMutingRule",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#detectors" title="Detectors">Detectors</a>" : <i>[ String, ... ]</i>,
        "<a href="#starttime" title="StartTime">StartTime</a>" : <i>Double</i>,
        "<a href="#stoptime" title="StopTime">StopTime</a>" : <i>Double</i>,
        "<a href="#filter" title="Filter">Filter</a>" : <i>[ <a href="filterdefinition.md">FilterDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::SignalFx::AlertMutingRule
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#detectors" title="Detectors">Detectors</a>: <i>
      - String</i>
    <a href="#starttime" title="StartTime">StartTime</a>: <i>Double</i>
    <a href="#stoptime" title="StopTime">StopTime</a>: <i>Double</i>
    <a href="#filter" title="Filter">Filter</a>: <i>
      - <a href="filterdefinition.md">FilterDefinition</a></i>
</pre>

## Properties

#### Description

The description for this muting rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Detectors

A convenience attribute that associated this muting rule with specific detector ids.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTime

Starting time of an alert muting rule as a Unit time stamp in seconds.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StopTime

Starting time of an alert muting rule as a Unix time stamp in seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

_Required_: No

_Type_: List of <a href="filterdefinition.md">FilterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### EffectiveStartTime

Returns the <code>EffectiveStartTime</code> value.

#### Id

Returns the <code>Id</code> value.

