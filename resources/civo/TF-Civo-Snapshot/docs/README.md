# TF::Civo::Snapshot

Provides a resource which can be used to create a snapshot from an existing Civo Instance.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Civo::Snapshot",
    "Properties" : {
        "<a href="#crontiming" title="CronTiming">CronTiming</a>" : <i>String</i>,
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#safe" title="Safe">Safe</a>" : <i>Boolean</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Civo::Snapshot
Properties:
    <a href="#crontiming" title="CronTiming">CronTiming</a>: <i>String</i>
    <a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#safe" title="Safe">Safe</a>: <i>Boolean</i>
</pre>

## Properties

#### CronTiming

If a valid cron string is passed, the snapshot will be saved as an automated snapshot
continuing to automatically update based on the schedule of the cron sequence provided
The default is nil meaning the snapshot will be saved as a one-off snapshot.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceId

The ID of the Instance from which the snapshot will be taken.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A name for the instance snapshot.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Safe

If `true` the instance will be shut down during the snapshot to ensure all files
are in a consistent state (e.g. database tables aren't in the middle of being optimised
and hence risking corruption). The default is `false` so you experience no interruption
of service, but a small risk of corruption.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CompletedAt

Returns the <code>CompletedAt</code> value.

#### Hostname

Returns the <code>Hostname</code> value.

#### Id

Returns the <code>Id</code> value.

#### NextExecution

Returns the <code>NextExecution</code> value.

#### Region

Returns the <code>Region</code> value.

#### RequestedAt

Returns the <code>RequestedAt</code> value.

#### SizeGb

Returns the <code>SizeGb</code> value.

#### State

Returns the <code>State</code> value.

#### TemplateId

Returns the <code>TemplateId</code> value.

