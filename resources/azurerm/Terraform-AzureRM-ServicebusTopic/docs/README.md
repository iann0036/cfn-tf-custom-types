# Terraform::AzureRM::ServicebusTopic

Manages a ServiceBus Topic.

**Note** Topics can only be created in Namespaces with an SKU of `standard` or higher.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::ServicebusTopic",
    "Properties" : {
        "<a href="#autodeleteonidle" title="AutoDeleteOnIdle">AutoDeleteOnIdle</a>" : <i>String</i>,
        "<a href="#defaultmessagettl" title="DefaultMessageTtl">DefaultMessageTtl</a>" : <i>String</i>,
        "<a href="#duplicatedetectionhistorytimewindow" title="DuplicateDetectionHistoryTimeWindow">DuplicateDetectionHistoryTimeWindow</a>" : <i>String</i>,
        "<a href="#enablebatchedoperations" title="EnableBatchedOperations">EnableBatchedOperations</a>" : <i>Boolean</i>,
        "<a href="#enableexpress" title="EnableExpress">EnableExpress</a>" : <i>Boolean</i>,
        "<a href="#enablepartitioning" title="EnablePartitioning">EnablePartitioning</a>" : <i>Boolean</i>,
        "<a href="#maxsizeinmegabytes" title="MaxSizeInMegabytes">MaxSizeInMegabytes</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namespacename" title="NamespaceName">NamespaceName</a>" : <i>String</i>,
        "<a href="#requiresduplicatedetection" title="RequiresDuplicateDetection">RequiresDuplicateDetection</a>" : <i>Boolean</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#supportordering" title="SupportOrdering">SupportOrdering</a>" : <i>Boolean</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::ServicebusTopic
Properties:
    <a href="#autodeleteonidle" title="AutoDeleteOnIdle">AutoDeleteOnIdle</a>: <i>String</i>
    <a href="#defaultmessagettl" title="DefaultMessageTtl">DefaultMessageTtl</a>: <i>String</i>
    <a href="#duplicatedetectionhistorytimewindow" title="DuplicateDetectionHistoryTimeWindow">DuplicateDetectionHistoryTimeWindow</a>: <i>String</i>
    <a href="#enablebatchedoperations" title="EnableBatchedOperations">EnableBatchedOperations</a>: <i>Boolean</i>
    <a href="#enableexpress" title="EnableExpress">EnableExpress</a>: <i>Boolean</i>
    <a href="#enablepartitioning" title="EnablePartitioning">EnablePartitioning</a>: <i>Boolean</i>
    <a href="#maxsizeinmegabytes" title="MaxSizeInMegabytes">MaxSizeInMegabytes</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namespacename" title="NamespaceName">NamespaceName</a>: <i>String</i>
    <a href="#requiresduplicatedetection" title="RequiresDuplicateDetection">RequiresDuplicateDetection</a>: <i>Boolean</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#supportordering" title="SupportOrdering">SupportOrdering</a>: <i>Boolean</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AutoDeleteOnIdle

The ISO 8601 timespan duration of the idle interval after which the
Topic is automatically deleted, minimum of 5 minutes.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultMessageTtl

The ISO 8601 timespan duration of TTL of messages sent to this topic if no
TTL value is set on the message itself.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DuplicateDetectionHistoryTimeWindow

The ISO 8601 timespan duration during which
duplicates can be detected. Defaults to 10 minutes. (`PT10M`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableBatchedOperations

Boolean flag which controls if server-side
batched operations are enabled. Defaults to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableExpress

Boolean flag which controls whether Express Entities
are enabled. An express topic holds a message in memory temporarily before writing
it to persistent storage. Defaults to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnablePartitioning

Boolean flag which controls whether to enable
the topic to be partitioned across multiple message brokers. Defaults to false.
Changing this forces a new resource to be created.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSizeInMegabytes

Integer value which controls the size of
memory allocated for the topic. For supported values see the "Queue/topic size"
section of [this document](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the ServiceBus Topic resource. Changing this forces a
new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamespaceName

The name of the ServiceBus Namespace to create
this topic in. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequiresDuplicateDetection

Boolean flag which controls whether
the Topic requires duplicate detection. Defaults to false. Changing this forces
a new resource to be created.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

The Status of the Service Bus Topic. Acceptable values are `Active` or `Disabled`. Defaults to `Active`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SupportOrdering

Boolean flag which controls whether the Topic
supports ordering. Defaults to false.

_Required_: No

_Type_: Boolean

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

