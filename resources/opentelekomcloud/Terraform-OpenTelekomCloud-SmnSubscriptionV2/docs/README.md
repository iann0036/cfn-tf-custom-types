# Terraform::OpenTelekomCloud::SmnSubscriptionV2

Manages a V2 subscription resource within OpenTelekomCloud.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenTelekomCloud::SmnSubscriptionV2",
    "Properties" : {
        "<a href="#endpoint" title="Endpoint">Endpoint</a>" : <i>String</i>,
        "<a href="#owner" title="Owner">Owner</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#remark" title="Remark">Remark</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>Double</i>,
        "<a href="#subscriptionurn" title="SubscriptionUrn">SubscriptionUrn</a>" : <i>String</i>,
        "<a href="#topicurn" title="TopicUrn">TopicUrn</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenTelekomCloud::SmnSubscriptionV2
Properties:
    <a href="#endpoint" title="Endpoint">Endpoint</a>: <i>String</i>
    <a href="#owner" title="Owner">Owner</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#remark" title="Remark">Remark</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>Double</i>
    <a href="#subscriptionurn" title="SubscriptionUrn">SubscriptionUrn</a>: <i>String</i>
    <a href="#topicurn" title="TopicUrn">TopicUrn</a>: <i>String</i>
</pre>

## Properties

#### Endpoint

Message endpoint.
For an HTTP subscription, the endpoint starts with http\://.
For an HTTPS subscription, the endpoint starts with https\://.
For an email subscription, the endpoint is a mail address.
For an SMS message subscription, the endpoint is a phone number.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Owner

Project ID of the topic creator.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Protocol of the message endpoint. Currently, email,
sms, http, and https are supported.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Remark

Remark information. The remarks must be a UTF-8-coded
character string containing 128 bytes.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Subscription status.
0 indicates that the subscription is not confirmed.
1 indicates that the subscription is confirmed.
3 indicates that the subscription is canceled.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubscriptionUrn

Resource identifier of a subscription, which
is unique.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopicUrn

Resource identifier of a topic, which is unique.

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

