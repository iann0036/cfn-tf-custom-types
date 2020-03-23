# Terraform::AWS::S3BucketNotification Queue

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#events" title="Events">Events</a>" : <i>[ String, ... ]</i>,
    "<a href="#filterprefix" title="FilterPrefix">FilterPrefix</a>" : <i>String</i>,
    "<a href="#filtersuffix" title="FilterSuffix">FilterSuffix</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#queuearn" title="QueueArn">QueueArn</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#events" title="Events">Events</a>: <i>
      - String</i>
<a href="#filterprefix" title="FilterPrefix">FilterPrefix</a>: <i>String</i>
<a href="#filtersuffix" title="FilterSuffix">FilterSuffix</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#queuearn" title="QueueArn">QueueArn</a>: <i>String</i>
</pre>

## Properties

#### Events

Specifies [event](http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html#notification-how-to-event-types-and-destinations) for which to send notifications.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterPrefix

Specifies object key name prefix.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterSuffix

Specifies object key name suffix.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

Specifies unique identifier for each of the notification configurations.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueueArn

Specifies Amazon SQS queue ARN.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

