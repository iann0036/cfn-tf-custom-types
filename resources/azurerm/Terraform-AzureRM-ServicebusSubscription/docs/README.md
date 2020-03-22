# Terraform::AzureRM::ServicebusSubscription

Manages a ServiceBus Subscription.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::ServicebusSubscription",
    "Properties" : {
        "<a href="#autodeleteonidle" title="AutoDeleteOnIdle">AutoDeleteOnIdle</a>" : <i>String</i>,
        "<a href="#deadletteringonmessageexpiration" title="DeadLetteringOnMessageExpiration">DeadLetteringOnMessageExpiration</a>" : <i>Boolean</i>,
        "<a href="#defaultmessagettl" title="DefaultMessageTtl">DefaultMessageTtl</a>" : <i>String</i>,
        "<a href="#enablebatchedoperations" title="EnableBatchedOperations">EnableBatchedOperations</a>" : <i>Boolean</i>,
        "<a href="#forwarddeadletteredmessagesto" title="ForwardDeadLetteredMessagesTo">ForwardDeadLetteredMessagesTo</a>" : <i>String</i>,
        "<a href="#forwardto" title="ForwardTo">ForwardTo</a>" : <i>String</i>,
        "<a href="#lockduration" title="LockDuration">LockDuration</a>" : <i>String</i>,
        "<a href="#maxdeliverycount" title="MaxDeliveryCount">MaxDeliveryCount</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namespacename" title="NamespaceName">NamespaceName</a>" : <i>String</i>,
        "<a href="#requiressession" title="RequiresSession">RequiresSession</a>" : <i>Boolean</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#topicname" title="TopicName">TopicName</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::ServicebusSubscription
Properties:
    <a href="#autodeleteonidle" title="AutoDeleteOnIdle">AutoDeleteOnIdle</a>: <i>String</i>
    <a href="#deadletteringonmessageexpiration" title="DeadLetteringOnMessageExpiration">DeadLetteringOnMessageExpiration</a>: <i>Boolean</i>
    <a href="#defaultmessagettl" title="DefaultMessageTtl">DefaultMessageTtl</a>: <i>String</i>
    <a href="#enablebatchedoperations" title="EnableBatchedOperations">EnableBatchedOperations</a>: <i>Boolean</i>
    <a href="#forwarddeadletteredmessagesto" title="ForwardDeadLetteredMessagesTo">ForwardDeadLetteredMessagesTo</a>: <i>String</i>
    <a href="#forwardto" title="ForwardTo">ForwardTo</a>: <i>String</i>
    <a href="#lockduration" title="LockDuration">LockDuration</a>: <i>String</i>
    <a href="#maxdeliverycount" title="MaxDeliveryCount">MaxDeliveryCount</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namespacename" title="NamespaceName">NamespaceName</a>: <i>String</i>
    <a href="#requiressession" title="RequiresSession">RequiresSession</a>: <i>Boolean</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#topicname" title="TopicName">TopicName</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AutoDeleteOnIdle

The idle interval after which the topic is automatically deleted as an [ISO 8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations). The minimum duration is `5` minutes or `P5M`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeadLetteringOnMessageExpiration

Boolean flag which controls whether the Subscription has dead letter support when a message expires. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultMessageTtl

The Default message timespan to live as an [ISO 8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations). This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableBatchedOperations

Boolean flag which controls whether the Subscription supports batched operations. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardDeadLetteredMessagesTo

The name of a Queue or Topic to automatically forward Dead Letter messages to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardTo

The name of a Queue or Topic to automatically forward messages to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LockDuration

The lock duration for the subscription as an [ISO 8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations). The default value is `1` minute or `P1M`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxDeliveryCount

The maximum number of deliveries.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the ServiceBus Subscription resource. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamespaceName

The name of the ServiceBus Namespace to create this Subscription in. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequiresSession

Boolean flag which controls whether this Subscription supports the concept of a session. Defaults to `false`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to create the namespace. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopicName

The name of the ServiceBus Topic to create this Subscription in. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

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

