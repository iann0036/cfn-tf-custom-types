# TF::AWS::SnsTopicSubscription

Provides a resource for subscribing to SNS topics. Requires that an SNS topic exist for the subscription to attach to. This resource allows you to automatically place messages sent to SNS topics in SQS queues, send them as HTTP(S) POST requests to a given endpoint, send SMS messages, or notify devices / applications. The most likely use case for Terraform users will probably be SQS queues.

~> **NOTE:** If the SNS topic and SQS queue are in different AWS regions, the `aws_sns_topic_subscription` must use an AWS provider that is in the same region as the SNS topic. If the `aws_sns_topic_subscription` uses a provider with a different region than the SNS topic, Terraform will fail to create the subscription.

~> **NOTE:** Setup of cross-account subscriptions from SNS topics to SQS queues requires Terraform to have access to BOTH accounts.

~> **NOTE:** If an SNS topic and SQS queue are in different AWS accounts but the same region, the `aws_sns_topic_subscription` must use the AWS provider for the account wi...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::SnsTopicSubscription",
    "Properties" : {
        "<a href="#confirmationtimeoutinminutes" title="ConfirmationTimeoutInMinutes">ConfirmationTimeoutInMinutes</a>" : <i>Double</i>,
        "<a href="#deliverypolicy" title="DeliveryPolicy">DeliveryPolicy</a>" : <i>String</i>,
        "<a href="#endpoint" title="Endpoint">Endpoint</a>" : <i>String</i>,
        "<a href="#endpointautoconfirms" title="EndpointAutoConfirms">EndpointAutoConfirms</a>" : <i>Boolean</i>,
        "<a href="#filterpolicy" title="FilterPolicy">FilterPolicy</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#rawmessagedelivery" title="RawMessageDelivery">RawMessageDelivery</a>" : <i>Boolean</i>,
        "<a href="#redrivepolicy" title="RedrivePolicy">RedrivePolicy</a>" : <i>String</i>,
        "<a href="#subscriptionrolearn" title="SubscriptionRoleArn">SubscriptionRoleArn</a>" : <i>String</i>,
        "<a href="#topicarn" title="TopicArn">TopicArn</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::SnsTopicSubscription
Properties:
    <a href="#confirmationtimeoutinminutes" title="ConfirmationTimeoutInMinutes">ConfirmationTimeoutInMinutes</a>: <i>Double</i>
    <a href="#deliverypolicy" title="DeliveryPolicy">DeliveryPolicy</a>: <i>String</i>
    <a href="#endpoint" title="Endpoint">Endpoint</a>: <i>String</i>
    <a href="#endpointautoconfirms" title="EndpointAutoConfirms">EndpointAutoConfirms</a>: <i>Boolean</i>
    <a href="#filterpolicy" title="FilterPolicy">FilterPolicy</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#rawmessagedelivery" title="RawMessageDelivery">RawMessageDelivery</a>: <i>Boolean</i>
    <a href="#redrivepolicy" title="RedrivePolicy">RedrivePolicy</a>: <i>String</i>
    <a href="#subscriptionrolearn" title="SubscriptionRoleArn">SubscriptionRoleArn</a>: <i>String</i>
    <a href="#topicarn" title="TopicArn">TopicArn</a>: <i>String</i>
</pre>

## Properties

#### ConfirmationTimeoutInMinutes

Integer indicating number of minutes to wait in retrying mode for fetching subscription arn before marking it as failure. Only applicable for http and https protocols. Default is `1`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeliveryPolicy

JSON String with the delivery policy (retries, backoff, etc.) that will be used in the subscription - this only applies to HTTP/S subscriptions. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html) for more details.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Endpoint

Endpoint to send data to. The contents vary with the protocol. See details below.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndpointAutoConfirms

Whether the endpoint is capable of [auto confirming subscription](http://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.html#SendMessageToHttp.prepare) (e.g., PagerDuty). Default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterPolicy

JSON String with the filter policy that will be used in the subscription to filter messages seen by the target resource. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/message-filtering.html) for more details.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Protocol to use. Valid values are: `sqs`, `sms`, `lambda`, `firehose`, and `application`. Protocols `email`, `email-json`, `http` and `https` are also valid but partially supported. See details below.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RawMessageDelivery

Whether to enable raw message delivery (the original message is directly passed, not wrapped in JSON with the original message in the message property). Default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedrivePolicy

JSON String with the redrive policy that will be used in the subscription. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/sns-dead-letter-queues.html#how-messages-moved-into-dead-letter-queue) for more details.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubscriptionRoleArn

ARN of the IAM role to publish to Kinesis Data Firehose delivery stream. Refer to [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/sns-firehose-as-subscriber.html).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopicArn

ARN of the SNS topic to subscribe to.

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

#### Arn

Returns the <code>Arn</code> value.

#### ConfirmationWasAuthenticated

Returns the <code>ConfirmationWasAuthenticated</code> value.

#### Id

Returns the <code>Id</code> value.

#### OwnerId

Returns the <code>OwnerId</code> value.

#### PendingConfirmation

Returns the <code>PendingConfirmation</code> value.

