# Terraform::AzureRM::StreamAnalyticsStreamInputIothub

Manages a Stream Analytics Stream Input IoTHub.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::StreamAnalyticsStreamInputIothub",
    "Properties" : {
        "<a href="#endpoint" title="Endpoint">Endpoint</a>" : <i>String</i>,
        "<a href="#eventhubconsumergroupname" title="EventhubConsumerGroupName">EventhubConsumerGroupName</a>" : <i>String</i>,
        "<a href="#iothubnamespace" title="IothubNamespace">IothubNamespace</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#sharedaccesspolicykey" title="SharedAccessPolicyKey">SharedAccessPolicyKey</a>" : <i>String</i>,
        "<a href="#sharedaccesspolicyname" title="SharedAccessPolicyName">SharedAccessPolicyName</a>" : <i>String</i>,
        "<a href="#streamanalyticsjobname" title="StreamAnalyticsJobName">StreamAnalyticsJobName</a>" : <i>String</i>,
        "<a href="#serialization" title="Serialization">Serialization</a>" : <i>[ <a href="serialization.md">Serialization</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::StreamAnalyticsStreamInputIothub
Properties:
    <a href="#endpoint" title="Endpoint">Endpoint</a>: <i>String</i>
    <a href="#eventhubconsumergroupname" title="EventhubConsumerGroupName">EventhubConsumerGroupName</a>: <i>String</i>
    <a href="#iothubnamespace" title="IothubNamespace">IothubNamespace</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#sharedaccesspolicykey" title="SharedAccessPolicyKey">SharedAccessPolicyKey</a>: <i>String</i>
    <a href="#sharedaccesspolicyname" title="SharedAccessPolicyName">SharedAccessPolicyName</a>: <i>String</i>
    <a href="#streamanalyticsjobname" title="StreamAnalyticsJobName">StreamAnalyticsJobName</a>: <i>String</i>
    <a href="#serialization" title="Serialization">Serialization</a>: <i>
      - <a href="serialization.md">Serialization</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Endpoint

The IoT Hub endpoint to connect to (ie. messages/events, messages/operationsMonitoringEvents, etc.).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventhubConsumerGroupName

The name of an Event Hub Consumer Group that should be used to read events from the Event Hub. Specifying distinct consumer group names for multiple inputs allows each of those inputs to receive the same events from the Event Hub.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IothubNamespace

The name or the URI of the IoT Hub.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Stream Input IoTHub. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedAccessPolicyKey

The shared access policy key for the specified shared access policy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedAccessPolicyName

The shared access policy name for the Event Hub, Service Bus Queue, Service Bus Topic, etc.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StreamAnalyticsJobName

The name of the Stream Analytics Job. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Serialization

_Required_: No

_Type_: List of <a href="serialization.md">Serialization</a>

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

