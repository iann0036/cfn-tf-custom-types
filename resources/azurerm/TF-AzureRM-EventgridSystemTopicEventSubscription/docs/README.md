# TF::AzureRM::EventgridSystemTopicEventSubscription

Manages an EventGrid System Topic Event Subscription.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::EventgridSystemTopicEventSubscription",
    "Properties" : {
        "<a href="#eventdeliveryschema" title="EventDeliverySchema">EventDeliverySchema</a>" : <i>String</i>,
        "<a href="#eventhubendpointid" title="EventhubEndpointId">EventhubEndpointId</a>" : <i>String</i>,
        "<a href="#expirationtimeutc" title="ExpirationTimeUtc">ExpirationTimeUtc</a>" : <i>String</i>,
        "<a href="#hybridconnectionendpointid" title="HybridConnectionEndpointId">HybridConnectionEndpointId</a>" : <i>String</i>,
        "<a href="#includedeventtypes" title="IncludedEventTypes">IncludedEventTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#servicebusqueueendpointid" title="ServiceBusQueueEndpointId">ServiceBusQueueEndpointId</a>" : <i>String</i>,
        "<a href="#servicebustopicendpointid" title="ServiceBusTopicEndpointId">ServiceBusTopicEndpointId</a>" : <i>String</i>,
        "<a href="#systemtopic" title="SystemTopic">SystemTopic</a>" : <i>String</i>,
        "<a href="#advancedfilter" title="AdvancedFilter">AdvancedFilter</a>" : <i>[ <a href="advancedfilterdefinition.md">AdvancedFilterDefinition</a>, ... ]</i>,
        "<a href="#azurefunctionendpoint" title="AzureFunctionEndpoint">AzureFunctionEndpoint</a>" : <i>[ <a href="azurefunctionendpointdefinition.md">AzureFunctionEndpointDefinition</a>, ... ]</i>,
        "<a href="#retrypolicy" title="RetryPolicy">RetryPolicy</a>" : <i>[ <a href="retrypolicydefinition.md">RetryPolicyDefinition</a>, ... ]</i>,
        "<a href="#storageblobdeadletterdestination" title="StorageBlobDeadLetterDestination">StorageBlobDeadLetterDestination</a>" : <i>[ <a href="storageblobdeadletterdestinationdefinition.md">StorageBlobDeadLetterDestinationDefinition</a>, ... ]</i>,
        "<a href="#storagequeueendpoint" title="StorageQueueEndpoint">StorageQueueEndpoint</a>" : <i>[ <a href="storagequeueendpointdefinition.md">StorageQueueEndpointDefinition</a>, ... ]</i>,
        "<a href="#subjectfilter" title="SubjectFilter">SubjectFilter</a>" : <i>[ <a href="subjectfilterdefinition.md">SubjectFilterDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#webhookendpoint" title="WebhookEndpoint">WebhookEndpoint</a>" : <i>[ <a href="webhookendpointdefinition.md">WebhookEndpointDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::EventgridSystemTopicEventSubscription
Properties:
    <a href="#eventdeliveryschema" title="EventDeliverySchema">EventDeliverySchema</a>: <i>String</i>
    <a href="#eventhubendpointid" title="EventhubEndpointId">EventhubEndpointId</a>: <i>String</i>
    <a href="#expirationtimeutc" title="ExpirationTimeUtc">ExpirationTimeUtc</a>: <i>String</i>
    <a href="#hybridconnectionendpointid" title="HybridConnectionEndpointId">HybridConnectionEndpointId</a>: <i>String</i>
    <a href="#includedeventtypes" title="IncludedEventTypes">IncludedEventTypes</a>: <i>
      - String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#servicebusqueueendpointid" title="ServiceBusQueueEndpointId">ServiceBusQueueEndpointId</a>: <i>String</i>
    <a href="#servicebustopicendpointid" title="ServiceBusTopicEndpointId">ServiceBusTopicEndpointId</a>: <i>String</i>
    <a href="#systemtopic" title="SystemTopic">SystemTopic</a>: <i>String</i>
    <a href="#advancedfilter" title="AdvancedFilter">AdvancedFilter</a>: <i>
      - <a href="advancedfilterdefinition.md">AdvancedFilterDefinition</a></i>
    <a href="#azurefunctionendpoint" title="AzureFunctionEndpoint">AzureFunctionEndpoint</a>: <i>
      - <a href="azurefunctionendpointdefinition.md">AzureFunctionEndpointDefinition</a></i>
    <a href="#retrypolicy" title="RetryPolicy">RetryPolicy</a>: <i>
      - <a href="retrypolicydefinition.md">RetryPolicyDefinition</a></i>
    <a href="#storageblobdeadletterdestination" title="StorageBlobDeadLetterDestination">StorageBlobDeadLetterDestination</a>: <i>
      - <a href="storageblobdeadletterdestinationdefinition.md">StorageBlobDeadLetterDestinationDefinition</a></i>
    <a href="#storagequeueendpoint" title="StorageQueueEndpoint">StorageQueueEndpoint</a>: <i>
      - <a href="storagequeueendpointdefinition.md">StorageQueueEndpointDefinition</a></i>
    <a href="#subjectfilter" title="SubjectFilter">SubjectFilter</a>: <i>
      - <a href="subjectfilterdefinition.md">SubjectFilterDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#webhookendpoint" title="WebhookEndpoint">WebhookEndpoint</a>: <i>
      - <a href="webhookendpointdefinition.md">WebhookEndpointDefinition</a></i>
</pre>

## Properties

#### EventDeliverySchema

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventhubEndpointId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpirationTimeUtc

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HybridConnectionEndpointId

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

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceBusQueueEndpointId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceBusTopicEndpointId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemTopic

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvancedFilter

_Required_: No

_Type_: List of <a href="advancedfilterdefinition.md">AdvancedFilterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureFunctionEndpoint

_Required_: No

_Type_: List of <a href="azurefunctionendpointdefinition.md">AzureFunctionEndpointDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryPolicy

_Required_: No

_Type_: List of <a href="retrypolicydefinition.md">RetryPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageBlobDeadLetterDestination

_Required_: No

_Type_: List of <a href="storageblobdeadletterdestinationdefinition.md">StorageBlobDeadLetterDestinationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageQueueEndpoint

_Required_: No

_Type_: List of <a href="storagequeueendpointdefinition.md">StorageQueueEndpointDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubjectFilter

_Required_: No

_Type_: List of <a href="subjectfilterdefinition.md">SubjectFilterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebhookEndpoint

_Required_: No

_Type_: List of <a href="webhookendpointdefinition.md">WebhookEndpointDefinition</a>

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

