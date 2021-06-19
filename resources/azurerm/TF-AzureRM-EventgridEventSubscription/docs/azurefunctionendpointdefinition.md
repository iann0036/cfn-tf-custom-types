# TF::AzureRM::EventgridEventSubscription AzureFunctionEndpointDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#functionid" title="FunctionId">FunctionId</a>" : <i>String</i>,
    "<a href="#maxeventsperbatch" title="MaxEventsPerBatch">MaxEventsPerBatch</a>" : <i>Double</i>,
    "<a href="#preferredbatchsizeinkilobytes" title="PreferredBatchSizeInKilobytes">PreferredBatchSizeInKilobytes</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#functionid" title="FunctionId">FunctionId</a>: <i>String</i>
<a href="#maxeventsperbatch" title="MaxEventsPerBatch">MaxEventsPerBatch</a>: <i>Double</i>
<a href="#preferredbatchsizeinkilobytes" title="PreferredBatchSizeInKilobytes">PreferredBatchSizeInKilobytes</a>: <i>Double</i>
</pre>

## Properties

#### FunctionId

Specifies the ID of the Function where the Event Subscription will receive events. This must be the functions ID in format {function_app.id}/functions/{name}.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxEventsPerBatch

Maximum number of events per batch.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreferredBatchSizeInKilobytes

Preferred batch size in Kilobytes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

