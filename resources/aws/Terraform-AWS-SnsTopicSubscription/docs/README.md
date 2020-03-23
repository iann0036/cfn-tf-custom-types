# Terraform::AWS::SnsTopicSubscription

Provides a resource for subscribing to SNS topics. Requires that an SNS topic exist for the subscription to attach to.
This resource allows you to automatically place messages sent to SNS topics in SQS queues, send them as HTTP(S) POST requests
to a given endpoint, send SMS messages, or notify devices / applications. The most likely use case for Terraform users will
probably be SQS queues.

~> **NOTE:** If the SNS topic and SQS queue are in different AWS regions, it is important for the "aws_sns_topic_subscription" to use an AWS provider that is in the same region of the SNS topic. If the "aws_sns_topic_subscription" is using a provider with a different region than the SNS topic, terraform will fail to create the subscription.

~> **NOTE:** Setup of cross-account subscriptions from SNS topics to SQS queues requires Terraform to have access to BOTH accounts.

~> **NOTE:** If SNS topic and SQS queue are in different AWS accounts but the same region it is important for the "aws_sns_topic_subscription" to use the AWS provider of the account with the SQS queue. If "aws_sns_topic_subscription" is using a Provider with a different account than the SQS queue, terraform creates the subscriptions but does not keep state and tries to re-create the subscription at every apply.

~> **NOTE:** If SNS topic and SQS queue are in different AWS accounts and different AWS regions it is important to recognize that the subscription needs to be initiated from the account with the SQS queue but in the region of the SNS topic.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::SnsTopicSubscription",
    "Properties" : {
        "<a href="#confirmationtimeoutinminutes" title="ConfirmationTimeoutInMinutes">ConfirmationTimeoutInMinutes</a>" : <i>Double</i>,
        "<a href="#deliverypolicy" title="DeliveryPolicy">DeliveryPolicy</a>" : <i>String</i>,
        "<a href="#endpoint" title="Endpoint">Endpoint</a>" : <i>String</i>,
        "<a href="#endpointautoconfirms" title="EndpointAutoConfirms">EndpointAutoConfirms</a>" : <i>Boolean</i>,
        "<a href="#filterpolicy" title="FilterPolicy">FilterPolicy</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#rawmessagedelivery" title="RawMessageDelivery">RawMessageDelivery</a>" : <i>Boolean</i>,
        "<a href="#topicarn" title="TopicArn">TopicArn</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::SnsTopicSubscription
Properties:
    <a href="#confirmationtimeoutinminutes" title="ConfirmationTimeoutInMinutes">ConfirmationTimeoutInMinutes</a>: <i>Double</i>
    <a href="#deliverypolicy" title="DeliveryPolicy">DeliveryPolicy</a>: <i>String</i>
    <a href="#endpoint" title="Endpoint">Endpoint</a>: <i>String</i>
    <a href="#endpointautoconfirms" title="EndpointAutoConfirms">EndpointAutoConfirms</a>: <i>Boolean</i>
    <a href="#filterpolicy" title="FilterPolicy">FilterPolicy</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#rawmessagedelivery" title="RawMessageDelivery">RawMessageDelivery</a>: <i>Boolean</i>
    <a href="#topicarn" title="TopicArn">TopicArn</a>: <i>String</i>
</pre>

## Properties

#### ConfirmationTimeoutInMinutes

Integer indicating number of minutes to wait in retying mode for fetching subscription arn before marking it as failure. Only applicable for http and https protocols (default is 1 minute).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeliveryPolicy

JSON String with the delivery policy (retries, backoff, etc.) that will be used in the subscription - this only applies to HTTP/S subscriptions. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html) for more details.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Endpoint

The endpoint to send data to, the contents will vary with the protocol. (see below for more information).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndpointAutoConfirms

Boolean indicating whether the end point is capable of [auto confirming subscription](http://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.html#SendMessageToHttp.prepare) e.g., PagerDuty (default is false).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterPolicy

JSON String with the filter policy that will be used in the subscription to filter messages seen by the target resource. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/message-filtering.html) for more details.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

The protocol to use. The possible values for this are: `sqs`, `sms`, `lambda`, `application`. (`http` or `https` are partially supported, see below) (`email` is an option but is unsupported, see below).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RawMessageDelivery

Boolean indicating whether or not to enable raw message delivery (the original message is directly passed, not wrapped in JSON with the original message in the message property) (default is false).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopicArn

The ARN of the SNS topic to subscribe to.

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

#### Id

Returns the <code>Id</code> value.

