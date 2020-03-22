# Terraform::AzureRM::ServicebusQueue

Manages a ServiceBus Queue.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::ServicebusQueue",
    "Properties" : {
        "<a href="#autodeleteonidle" title="AutoDeleteOnIdle">AutoDeleteOnIdle</a>" : <i>String</i>,
        "<a href="#deadletteringonmessageexpiration" title="DeadLetteringOnMessageExpiration">DeadLetteringOnMessageExpiration</a>" : <i>Boolean</i>,
        "<a href="#defaultmessagettl" title="DefaultMessageTtl">DefaultMessageTtl</a>" : <i>String</i>,
        "<a href="#duplicatedetectionhistorytimewindow" title="DuplicateDetectionHistoryTimeWindow">DuplicateDetectionHistoryTimeWindow</a>" : <i>String</i>,
        "<a href="#enableexpress" title="EnableExpress">EnableExpress</a>" : <i>Boolean</i>,
        "<a href="#enablepartitioning" title="EnablePartitioning">EnablePartitioning</a>" : <i>Boolean</i>,
        "<a href="#lockduration" title="LockDuration">LockDuration</a>" : <i>String</i>,
        "<a href="#maxdeliverycount" title="MaxDeliveryCount">MaxDeliveryCount</a>" : <i>Double</i>,
        "<a href="#maxsizeinmegabytes" title="MaxSizeInMegabytes">MaxSizeInMegabytes</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namespacename" title="NamespaceName">NamespaceName</a>" : <i>String</i>,
        "<a href="#requiresduplicatedetection" title="RequiresDuplicateDetection">RequiresDuplicateDetection</a>" : <i>Boolean</i>,
        "<a href="#requiressession" title="RequiresSession">RequiresSession</a>" : <i>Boolean</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::ServicebusQueue
Properties:
    <a href="#autodeleteonidle" title="AutoDeleteOnIdle">AutoDeleteOnIdle</a>: <i>String</i>
    <a href="#deadletteringonmessageexpiration" title="DeadLetteringOnMessageExpiration">DeadLetteringOnMessageExpiration</a>: <i>Boolean</i>
    <a href="#defaultmessagettl" title="DefaultMessageTtl">DefaultMessageTtl</a>: <i>String</i>
    <a href="#duplicatedetectionhistorytimewindow" title="DuplicateDetectionHistoryTimeWindow">DuplicateDetectionHistoryTimeWindow</a>: <i>String</i>
    <a href="#enableexpress" title="EnableExpress">EnableExpress</a>: <i>Boolean</i>
    <a href="#enablepartitioning" title="EnablePartitioning">EnablePartitioning</a>: <i>Boolean</i>
    <a href="#lockduration" title="LockDuration">LockDuration</a>: <i>String</i>
    <a href="#maxdeliverycount" title="MaxDeliveryCount">MaxDeliveryCount</a>: <i>Double</i>
    <a href="#maxsizeinmegabytes" title="MaxSizeInMegabytes">MaxSizeInMegabytes</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namespacename" title="NamespaceName">NamespaceName</a>: <i>String</i>
    <a href="#requiresduplicatedetection" title="RequiresDuplicateDetection">RequiresDuplicateDetection</a>: <i>Boolean</i>
    <a href="#requiressession" title="RequiresSession">RequiresSession</a>: <i>Boolean</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AutoDeleteOnIdle

The ISO 8601 timespan duration of the idle interval after which the
Queue is automatically deleted, minimum of 5 minutes.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeadLetteringOnMessageExpiration

Boolean flag which controls whether the Queue has dead letter support when a message expires. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultMessageTtl

The ISO 8601 timespan duration of the TTL of messages sent to this
queue. This is the default value used when TTL is not set on message itself.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DuplicateDetectionHistoryTimeWindow

The ISO 8601 timespan duration during which
duplicates can be detected. Default value is 10 minutes. (`PT10M`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableExpress

Boolean flag which controls whether Express Entities
are enabled. An express queue holds a message in memory temporarily before writing
it to persistent storage. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnablePartitioning

Boolean flag which controls whether to enable
the queue to be partitioned across multiple message brokers. Changing this forces
a new resource to be created. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LockDuration

The ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. Maximum value is 5 minutes. Defaults to 1 minute. (`PT1M`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxDeliveryCount

Integer value which controls when a message is automatically deadlettered. Defaults to `10`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSizeInMegabytes

Integer value which controls the size of
memory allocated for the queue. For supported values see the "Queue/topic size"
section of [this document](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the ServiceBus Queue resource. Changing this forces a
new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamespaceName

The name of the ServiceBus Namespace to create
this queue in. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequiresDuplicateDetection

Boolean flag which controls whether
the Queue requires duplicate detection. Changing this forces
a new resource to be created. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequiresSession

Boolean flag which controls whether the Queue requires sessions.
This will allow ordered handling of unbounded sequences of related messages. With sessions enabled
a queue can guarantee first-in-first-out delivery of messages.
Changing this forces a new resource to be created. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

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

