# TF::Google::LoggingBillingAccountBucketConfig

Manages a billing account level logging bucket config. For more information see
[the official logging documentation](https://cloud.google.com/logging/docs/) and
[Storing Logs](https://cloud.google.com/logging/docs/storage).

~> **Note:** Logging buckets are automatically created for a given folder, project, organization, billingAccount and cannot be deleted. Creating a resource of this type will acquire and update the resource that already exists at the desired location. These buckets cannot be removed so deleting this resource will remove the bucket config from your terraform state but will leave the logging bucket unchanged. The buckets that are currently automatically created are "_Default" and "_Required".

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Google::LoggingBillingAccountBucketConfig",
    "Properties" : {
        "<a href="#billingaccount" title="BillingAccount">BillingAccount</a>" : <i>String</i>,
        "<a href="#bucketid" title="BucketId">BucketId</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#retentiondays" title="RetentionDays">RetentionDays</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Google::LoggingBillingAccountBucketConfig
Properties:
    <a href="#billingaccount" title="BillingAccount">BillingAccount</a>: <i>String</i>
    <a href="#bucketid" title="BucketId">BucketId</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#retentiondays" title="RetentionDays">RetentionDays</a>: <i>Double</i>
</pre>

## Properties

#### BillingAccount

The parent resource that contains the logging bucket.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BucketId

The name of the logging bucket. Logging automatically creates two log buckets: `_Required` and `_Default`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Describes this bucket.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

The location of the bucket.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionDays

Logs will be retained by default for this amount of time, after which they will automatically be deleted. The minimum retention period is 1 day. If this value is set to zero at bucket creation time, the default time of 30 days will be used. Bucket retention can not be increased on buckets outside of projects.

_Required_: No

_Type_: Double

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

#### LifecycleState

Returns the <code>LifecycleState</code> value.

#### Name

Returns the <code>Name</code> value.

