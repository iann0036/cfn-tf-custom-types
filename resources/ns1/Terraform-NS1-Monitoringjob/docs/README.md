# Terraform::NS1::Monitoringjob

Provides a NS1 Monitoring Job resource. This can be used to create, modify, and delete monitoring jobs.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::NS1::Monitoringjob",
    "Properties" : {
        "<a href="#active" title="Active">Active</a>" : <i>Boolean</i>,
        "<a href="#config" title="Config">Config</a>" : <i>[ <a href="config.md">Config</a>, ... ]</i>,
        "<a href="#frequency" title="Frequency">Frequency</a>" : <i>Double</i>,
        "<a href="#jobtype" title="JobType">JobType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#notes" title="Notes">Notes</a>" : <i>String</i>,
        "<a href="#notifydelay" title="NotifyDelay">NotifyDelay</a>" : <i>Double</i>,
        "<a href="#notifyfailback" title="NotifyFailback">NotifyFailback</a>" : <i>Boolean</i>,
        "<a href="#notifylist" title="NotifyList">NotifyList</a>" : <i>String</i>,
        "<a href="#notifyregional" title="NotifyRegional">NotifyRegional</a>" : <i>Boolean</i>,
        "<a href="#notifyrepeat" title="NotifyRepeat">NotifyRepeat</a>" : <i>Double</i>,
        "<a href="#policy" title="Policy">Policy</a>" : <i>String</i>,
        "<a href="#rapidrecheck" title="RapidRecheck">RapidRecheck</a>" : <i>Boolean</i>,
        "<a href="#regions" title="Regions">Regions</a>" : <i>[ String, ... ]</i>,
        "<a href="#rules" title="Rules">Rules</a>" : <i>[ <a href="rules.md">Rules</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::NS1::Monitoringjob
Properties:
    <a href="#active" title="Active">Active</a>: <i>Boolean</i>
    <a href="#config" title="Config">Config</a>: <i>
      - <a href="config.md">Config</a></i>
    <a href="#frequency" title="Frequency">Frequency</a>: <i>Double</i>
    <a href="#jobtype" title="JobType">JobType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#notes" title="Notes">Notes</a>: <i>String</i>
    <a href="#notifydelay" title="NotifyDelay">NotifyDelay</a>: <i>Double</i>
    <a href="#notifyfailback" title="NotifyFailback">NotifyFailback</a>: <i>Boolean</i>
    <a href="#notifylist" title="NotifyList">NotifyList</a>: <i>String</i>
    <a href="#notifyregional" title="NotifyRegional">NotifyRegional</a>: <i>Boolean</i>
    <a href="#notifyrepeat" title="NotifyRepeat">NotifyRepeat</a>: <i>Double</i>
    <a href="#policy" title="Policy">Policy</a>: <i>String</i>
    <a href="#rapidrecheck" title="RapidRecheck">RapidRecheck</a>: <i>Boolean</i>
    <a href="#regions" title="Regions">Regions</a>: <i>
      - String</i>
    <a href="#rules" title="Rules">Rules</a>: <i>
      - <a href="rules.md">Rules</a></i>
</pre>

## Properties

#### Active

Indicates if the job is active or temporarily disabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Config

A configuration dictionary with keys and values depending on the jobs' type.

_Required_: Yes

_Type_: List of <a href="config.md">Config</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Frequency

The frequency, in seconds, at which to run the monitoring job in each region.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JobType

The type of monitoring job to be run. See NS1 API
docs for supported values.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The free-form display name for the monitoring job.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notes

Freeform notes to be included in any notifications about this job.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyDelay

The time in seconds after a failure to wait before sending a notification.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyFailback

If true, a notification is sent when a job returns to an "up" state.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyList

The id of the notification list to send notifications to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyRegional

If true, notifications are sent for any regional failure (and failback if desired), in addition to global state notifications.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyRepeat

The time in seconds between repeat notifications of a failed job.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policy

The policy for determining the monitor's global status
based on the status of the job in all regions. See NS1 API docs for supported values.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RapidRecheck

If true, on any apparent state change, the job is quickly re-run after one second to confirm the state change before notification.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Regions

The list of region codes in which to run the monitoring
job. See NS1 API docs for supported values.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rules

_Required_: No

_Type_: List of <a href="rules.md">Rules</a>

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

