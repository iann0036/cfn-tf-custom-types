# TF::AzureRM::EventgridEventSubscription RetryPolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#eventtimetolive" title="EventTimeToLive">EventTimeToLive</a>" : <i>Double</i>,
    "<a href="#maxdeliveryattempts" title="MaxDeliveryAttempts">MaxDeliveryAttempts</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#eventtimetolive" title="EventTimeToLive">EventTimeToLive</a>: <i>Double</i>
<a href="#maxdeliveryattempts" title="MaxDeliveryAttempts">MaxDeliveryAttempts</a>: <i>Double</i>
</pre>

## Properties

#### EventTimeToLive

Specifies the time to live (in minutes) for events. Supported range is `1` to `1440`. Defaults to `1440`. See [official documentation](https://docs.microsoft.com/en-us/azure/event-grid/manage-event-delivery#set-retry-policy) for more details.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxDeliveryAttempts

Specifies the maximum number of delivery retry attempts for events.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

