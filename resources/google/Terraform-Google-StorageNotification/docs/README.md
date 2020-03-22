# Terraform::Google::StorageNotification

Creates a new notification configuration on a specified bucket, establishing a flow of event notifications from GCS to a Cloud Pub/Sub topic.
 For more information see 
[the official documentation](https://cloud.google.com/storage/docs/pubsub-notifications) 
and 
[API](https://cloud.google.com/storage/docs/json_api/v1/notifications).

In order to enable notifications, a special Google Cloud Storage service account unique to the project
must have the IAM permission "projects.topics.publish" for a Cloud Pub/Sub topic in the project. To get the service
account's email address, use the `google_storage_project_service_account` datasource's `email_address` value, and see below
for an example of enabling notifications by granting the correct IAM permission. See
[the notifications documentation](https://cloud.google.com/storage/docs/gsutil/commands/notification) for more details.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::StorageNotification",
    "Properties" : {
        "<a href="#bucket" title="Bucket">Bucket</a>" : <i>String</i>,
        "<a href="#customattributes" title="CustomAttributes">CustomAttributes</a>" : <i>[ <a href="customattributes.md">CustomAttributes</a>, ... ]</i>,
        "<a href="#eventtypes" title="EventTypes">EventTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#objectnameprefix" title="ObjectNamePrefix">ObjectNamePrefix</a>" : <i>String</i>,
        "<a href="#payloadformat" title="PayloadFormat">PayloadFormat</a>" : <i>String</i>,
        "<a href="#topic" title="Topic">Topic</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::StorageNotification
Properties:
    <a href="#bucket" title="Bucket">Bucket</a>: <i>String</i>
    <a href="#customattributes" title="CustomAttributes">CustomAttributes</a>: <i>
      - <a href="customattributes.md">CustomAttributes</a></i>
    <a href="#eventtypes" title="EventTypes">EventTypes</a>: <i>
      - String</i>
    <a href="#objectnameprefix" title="ObjectNamePrefix">ObjectNamePrefix</a>: <i>String</i>
    <a href="#payloadformat" title="PayloadFormat">PayloadFormat</a>: <i>String</i>
    <a href="#topic" title="Topic">Topic</a>: <i>String</i>
</pre>

## Properties

#### Bucket

The name of the bucket.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomAttributes

A set of key/value attribute pairs to attach to each Cloud PubSub message published for this notification subscription.

_Required_: No

_Type_: List of <a href="customattributes.md">CustomAttributes</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventTypes

List of event type filters for this notification config. If not specified, Cloud Storage will send notifications for all event types. The valid types are: `"OBJECT_FINALIZE"`, `"OBJECT_METADATA_UPDATE"`, `"OBJECT_DELETE"`, `"OBJECT_ARCHIVE"`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectNamePrefix

Specifies a prefix path filter for this notification config. Cloud Storage will only send notifications for objects in this bucket whose names begin with the specified prefix.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PayloadFormat

The desired content of the Payload. One of `"JSON_API_V1"` or `"NONE"`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Topic

The Cloud PubSub topic to which this subscription publishes. Expects either the
topic name, assumed to belong to the default GCP provider project, or the project-level name,
i.e. `projects/my-gcp-project/topics/my-topic` or `my-topic`. If the project is not set in the provider,
you will need to use the project-level name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### NotificationId

Returns the <code>NotificationId</code> value.

#### SelfLink

Returns the <code>SelfLink</code> value.

