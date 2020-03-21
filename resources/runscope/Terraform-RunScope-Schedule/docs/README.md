# Terraform::RunScope::Schedule

A [schedule](https://www.runscope.com/docs/api/schedules) resource.
Tests can be scheduled to run on frequencies up to every minute.
One ore more schedules can be configured per test with each schedule
using a unique Test-specific or Shared [Environment](environment.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::RunScope::Schedule",
    "Properties" : {
        "<a href="#bucketid" title="BucketId">BucketId</a>" : <i>String</i>,
        "<a href="#environmentid" title="EnvironmentId">EnvironmentId</a>" : <i>String</i>,
        "<a href="#interval" title="Interval">Interval</a>" : <i>String</i>,
        "<a href="#note" title="Note">Note</a>" : <i>String</i>,
        "<a href="#testid" title="TestId">TestId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::RunScope::Schedule
Properties:
    <a href="#bucketid" title="BucketId">BucketId</a>: <i>String</i>
    <a href="#environmentid" title="EnvironmentId">EnvironmentId</a>: <i>String</i>
    <a href="#interval" title="Interval">Interval</a>: <i>String</i>
    <a href="#note" title="Note">Note</a>: <i>String</i>
    <a href="#testid" title="TestId">TestId</a>: <i>String</i>
</pre>

## Properties

#### BucketId

The id of the bucket to associate this schedule with.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvironmentId

The id of the environment to use when running the test.
If given, creates a test specific schedule, otherwise creates a shared schedule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interval

The schedule's interval, must be one of:
* 1m — every minute
* 5m — every 5 minutes
* 15m — every 15 minutes
* 30m — every 30 minutes
* 1h — every hour
* 6h — every 6 hours
* 1d — every day.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Note

A human-friendly description for the schedule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TestId

The id of the test to associate this schedule with.

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

