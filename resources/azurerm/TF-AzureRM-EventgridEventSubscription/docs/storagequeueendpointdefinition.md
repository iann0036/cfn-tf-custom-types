# TF::AzureRM::EventgridEventSubscription StorageQueueEndpointDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#queuename" title="QueueName">QueueName</a>" : <i>String</i>,
    "<a href="#storageaccountid" title="StorageAccountId">StorageAccountId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#queuename" title="QueueName">QueueName</a>: <i>String</i>
<a href="#storageaccountid" title="StorageAccountId">StorageAccountId</a>: <i>String</i>
</pre>

## Properties

#### QueueName

Specifies the name of the storage queue where the Event Subscription will receive events.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountId

Specifies the id of the storage account id where the storage queue is located.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

