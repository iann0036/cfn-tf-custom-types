# Terraform::AzureRM::EventgridEventSubscription

CloudFormation equivalent of azurerm_eventgrid_event_subscription

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::EventgridEventSubscription",
    "Properties" : {
        "<a href="#eventdeliveryschema" title="EventDeliverySchema">EventDeliverySchema</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#includedeventtypes" title="IncludedEventTypes">IncludedEventTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#scope" title="Scope">Scope</a>" : <i>String</i>,
        "<a href="#topicname" title="TopicName">TopicName</a>" : <i>String</i>,
        "<a href="#eventhubendpoint" title="EventhubEndpoint">EventhubEndpoint</a>" : <i>[ <a href="eventhubendpoint.md">EventhubEndpoint</a>, ... ]</i>,
        "<a href="#hybridconnectionendpoint" title="HybridConnectionEndpoint">HybridConnectionEndpoint</a>" : <i>[ <a href="hybridconnectionendpoint.md">HybridConnectionEndpoint</a>, ... ]</i>,
        "<a href="#retrypolicy" title="RetryPolicy">RetryPolicy</a>" : <i>[ <a href="retrypolicy.md">RetryPolicy</a>, ... ]</i>,
        "<a href="#storageblobdeadletterdestination" title="StorageBlobDeadLetterDestination">StorageBlobDeadLetterDestination</a>" : <i>[ <a href="storageblobdeadletterdestination.md">StorageBlobDeadLetterDestination</a>, ... ]</i>,
        "<a href="#storagequeueendpoint" title="StorageQueueEndpoint">StorageQueueEndpoint</a>" : <i>[ <a href="storagequeueendpoint.md">StorageQueueEndpoint</a>, ... ]</i>,
        "<a href="#subjectfilter" title="SubjectFilter">SubjectFilter</a>" : <i>[ <a href="subjectfilter.md">SubjectFilter</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#webhookendpoint" title="WebhookEndpoint">WebhookEndpoint</a>" : <i>[ <a href="webhookendpoint.md">WebhookEndpoint</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::EventgridEventSubscription
Properties:
    <a href="#eventdeliveryschema" title="EventDeliverySchema">EventDeliverySchema</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#includedeventtypes" title="IncludedEventTypes">IncludedEventTypes</a>: <i>
      - String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#scope" title="Scope">Scope</a>: <i>String</i>
    <a href="#topicname" title="TopicName">TopicName</a>: <i>String</i>
    <a href="#eventhubendpoint" title="EventhubEndpoint">EventhubEndpoint</a>: <i>
      - <a href="eventhubendpoint.md">EventhubEndpoint</a></i>
    <a href="#hybridconnectionendpoint" title="HybridConnectionEndpoint">HybridConnectionEndpoint</a>: <i>
      - <a href="hybridconnectionendpoint.md">HybridConnectionEndpoint</a></i>
    <a href="#retrypolicy" title="RetryPolicy">RetryPolicy</a>: <i>
      - <a href="retrypolicy.md">RetryPolicy</a></i>
    <a href="#storageblobdeadletterdestination" title="StorageBlobDeadLetterDestination">StorageBlobDeadLetterDestination</a>: <i>
      - <a href="storageblobdeadletterdestination.md">StorageBlobDeadLetterDestination</a></i>
    <a href="#storagequeueendpoint" title="StorageQueueEndpoint">StorageQueueEndpoint</a>: <i>
      - <a href="storagequeueendpoint.md">StorageQueueEndpoint</a></i>
    <a href="#subjectfilter" title="SubjectFilter">SubjectFilter</a>: <i>
      - <a href="subjectfilter.md">SubjectFilter</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#webhookendpoint" title="WebhookEndpoint">WebhookEndpoint</a>: <i>
      - <a href="webhookendpoint.md">WebhookEndpoint</a></i>
</pre>

## Properties

#### EventDeliverySchema

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludedEventTypes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopicName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventhubEndpoint

_Required_: No

_Type_: List of <a href="eventhubendpoint.md">EventhubEndpoint</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HybridConnectionEndpoint

_Required_: No

_Type_: List of <a href="hybridconnectionendpoint.md">HybridConnectionEndpoint</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryPolicy

_Required_: No

_Type_: List of <a href="retrypolicy.md">RetryPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageBlobDeadLetterDestination

_Required_: No

_Type_: List of <a href="storageblobdeadletterdestination.md">StorageBlobDeadLetterDestination</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageQueueEndpoint

_Required_: No

_Type_: List of <a href="storagequeueendpoint.md">StorageQueueEndpoint</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubjectFilter

_Required_: No

_Type_: List of <a href="subjectfilter.md">SubjectFilter</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebhookEndpoint

_Required_: No

_Type_: List of <a href="webhookendpoint.md">WebhookEndpoint</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

