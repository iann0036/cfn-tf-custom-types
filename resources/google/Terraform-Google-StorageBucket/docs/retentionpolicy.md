# Terraform::Google::StorageBucket RetentionPolicy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#islocked" title="IsLocked">IsLocked</a>" : <i>Boolean</i>,
    "<a href="#retentionperiod" title="RetentionPeriod">RetentionPeriod</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#islocked" title="IsLocked">IsLocked</a>: <i>Boolean</i>
<a href="#retentionperiod" title="RetentionPeriod">RetentionPeriod</a>: <i>Double</i>
</pre>

## Properties

#### IsLocked

If set to `true`, the bucket will be [locked](https://cloud.google.com/storage/docs/using-bucket-lock#lock-bucket) and permanently restrict edits to the bucket's retention policy.  Caution: Locking a bucket is an irreversible action.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionPeriod

The period of time, in seconds, that objects in the bucket must be retained and cannot be deleted, overwritten, or archived. The value must be less than 3,155,760,000 seconds.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

