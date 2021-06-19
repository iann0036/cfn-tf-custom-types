# TF::AWS::LambdaEventSourceMapping

Provides a Lambda event source mapping. This allows Lambda functions to get events from Kinesis, DynamoDB, SQS and Managed Streaming for Apache Kafka (MSK).

For information about Lambda and how to use it, see [What is AWS Lambda?][1].
For information about event source mappings, see [CreateEventSourceMapping][2] in the API docs.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::LambdaEventSourceMapping",
    "Properties" : {
        "<a href="#batchsize" title="BatchSize">BatchSize</a>" : <i>Double</i>,
        "<a href="#bisectbatchonfunctionerror" title="BisectBatchOnFunctionError">BisectBatchOnFunctionError</a>" : <i>Boolean</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#eventsourcearn" title="EventSourceArn">EventSourceArn</a>" : <i>String</i>,
        "<a href="#functionname" title="FunctionName">FunctionName</a>" : <i>String</i>,
        "<a href="#functionresponsetypes" title="FunctionResponseTypes">FunctionResponseTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#maximumbatchingwindowinseconds" title="MaximumBatchingWindowInSeconds">MaximumBatchingWindowInSeconds</a>" : <i>Double</i>,
        "<a href="#maximumrecordageinseconds" title="MaximumRecordAgeInSeconds">MaximumRecordAgeInSeconds</a>" : <i>Double</i>,
        "<a href="#maximumretryattempts" title="MaximumRetryAttempts">MaximumRetryAttempts</a>" : <i>Double</i>,
        "<a href="#parallelizationfactor" title="ParallelizationFactor">ParallelizationFactor</a>" : <i>Double</i>,
        "<a href="#queues" title="Queues">Queues</a>" : <i>[ String, ... ]</i>,
        "<a href="#startingposition" title="StartingPosition">StartingPosition</a>" : <i>String</i>,
        "<a href="#startingpositiontimestamp" title="StartingPositionTimestamp">StartingPositionTimestamp</a>" : <i>String</i>,
        "<a href="#topics" title="Topics">Topics</a>" : <i>[ String, ... ]</i>,
        "<a href="#tumblingwindowinseconds" title="TumblingWindowInSeconds">TumblingWindowInSeconds</a>" : <i>Double</i>,
        "<a href="#destinationconfig" title="DestinationConfig">DestinationConfig</a>" : <i>[ <a href="destinationconfigdefinition.md">DestinationConfigDefinition</a>, ... ]</i>,
        "<a href="#selfmanagedeventsource" title="SelfManagedEventSource">SelfManagedEventSource</a>" : <i>[ <a href="selfmanagedeventsourcedefinition.md">SelfManagedEventSourceDefinition</a>, ... ]</i>,
        "<a href="#sourceaccessconfiguration" title="SourceAccessConfiguration">SourceAccessConfiguration</a>" : <i>[ <a href="sourceaccessconfigurationdefinition.md">SourceAccessConfigurationDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::LambdaEventSourceMapping
Properties:
    <a href="#batchsize" title="BatchSize">BatchSize</a>: <i>Double</i>
    <a href="#bisectbatchonfunctionerror" title="BisectBatchOnFunctionError">BisectBatchOnFunctionError</a>: <i>Boolean</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#eventsourcearn" title="EventSourceArn">EventSourceArn</a>: <i>String</i>
    <a href="#functionname" title="FunctionName">FunctionName</a>: <i>String</i>
    <a href="#functionresponsetypes" title="FunctionResponseTypes">FunctionResponseTypes</a>: <i>
      - String</i>
    <a href="#maximumbatchingwindowinseconds" title="MaximumBatchingWindowInSeconds">MaximumBatchingWindowInSeconds</a>: <i>Double</i>
    <a href="#maximumrecordageinseconds" title="MaximumRecordAgeInSeconds">MaximumRecordAgeInSeconds</a>: <i>Double</i>
    <a href="#maximumretryattempts" title="MaximumRetryAttempts">MaximumRetryAttempts</a>: <i>Double</i>
    <a href="#parallelizationfactor" title="ParallelizationFactor">ParallelizationFactor</a>: <i>Double</i>
    <a href="#queues" title="Queues">Queues</a>: <i>
      - String</i>
    <a href="#startingposition" title="StartingPosition">StartingPosition</a>: <i>String</i>
    <a href="#startingpositiontimestamp" title="StartingPositionTimestamp">StartingPositionTimestamp</a>: <i>String</i>
    <a href="#topics" title="Topics">Topics</a>: <i>
      - String</i>
    <a href="#tumblingwindowinseconds" title="TumblingWindowInSeconds">TumblingWindowInSeconds</a>: <i>Double</i>
    <a href="#destinationconfig" title="DestinationConfig">DestinationConfig</a>: <i>
      - <a href="destinationconfigdefinition.md">DestinationConfigDefinition</a></i>
    <a href="#selfmanagedeventsource" title="SelfManagedEventSource">SelfManagedEventSource</a>: <i>
      - <a href="selfmanagedeventsourcedefinition.md">SelfManagedEventSourceDefinition</a></i>
    <a href="#sourceaccessconfiguration" title="SourceAccessConfiguration">SourceAccessConfiguration</a>: <i>
      - <a href="sourceaccessconfigurationdefinition.md">SourceAccessConfigurationDefinition</a></i>
</pre>

## Properties

#### BatchSize

The largest number of records that Lambda will retrieve from your event source at the time of invocation. Defaults to `100` for DynamoDB, Kinesis, MQ and MSK, `10` for SQS.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BisectBatchOnFunctionError

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Determines if the mapping will be enabled on creation. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventSourceArn

The event source ARN - this is required for Kinesis stream, DynamoDB stream, SQS queue, MQ broker or MSK cluster.  It is incompatible with a Self Managed Kafka source.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FunctionName

The name or the ARN of the Lambda function that will be subscribing to events.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FunctionResponseTypes

A list of current response type enums applied to the event source mapping for [AWS Lambda checkpointing](https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html#services-ddb-batchfailurereporting). Only available for stream sources (DynamoDB and Kinesis). Valid values: `ReportBatchItemFailures`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumBatchingWindowInSeconds

The maximum amount of time to gather records before invoking the function, in seconds (between 0 and 300). Records will continue to buffer (or accumulate in the case of an SQS queue event source) until either `maximum_batching_window_in_seconds` expires or `batch_size` has been met. For streaming event sources, defaults to as soon as records are available in the stream. If the batch it reads from the stream/queue only has one record in it, Lambda only sends one record to the function. Only available for stream sources (DynamoDB and Kinesis) and SQS standard queues.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumRecordAgeInSeconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumRetryAttempts

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParallelizationFactor

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Queues

The name of the Amazon MQ broker destination queue to consume. Only available for MQ sources. A single queue name must be specified.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartingPosition

The position in the stream where AWS Lambda should start reading. Must be one of `AT_TIMESTAMP` (Kinesis only), `LATEST` or `TRIM_HORIZON` if getting events from Kinesis, DynamoDB or MSK. Must not be provided if getting events from SQS. More information about these positions can be found in the [AWS DynamoDB Streams API Reference](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_GetShardIterator.html) and [AWS Kinesis API Reference](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetShardIterator.html#Kinesis-GetShardIterator-request-ShardIteratorType).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartingPositionTimestamp

A timestamp in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) of the data record which to start reading when using `starting_position` set to `AT_TIMESTAMP`. If a record with this exact timestamp does not exist, the next later record is chosen. If the timestamp is older than the current trim horizon, the oldest available record is chosen.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Topics

The name of the Kafka topics. Only available for MSK sources. A single topic name must be specified.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TumblingWindowInSeconds

The duration in seconds of a processing window for [AWS Lambda streaming analytics](https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html#services-kinesis-windows). The range is between 1 second up to 900 seconds. Only available for stream sources (DynamoDB and Kinesis).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationConfig

_Required_: No

_Type_: List of <a href="destinationconfigdefinition.md">DestinationConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SelfManagedEventSource

_Required_: No

_Type_: List of <a href="selfmanagedeventsourcedefinition.md">SelfManagedEventSourceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceAccessConfiguration

_Required_: No

_Type_: List of <a href="sourceaccessconfigurationdefinition.md">SourceAccessConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### FunctionArn

Returns the <code>FunctionArn</code> value.

#### Id

Returns the <code>Id</code> value.

#### LastModified

Returns the <code>LastModified</code> value.

#### LastProcessingResult

Returns the <code>LastProcessingResult</code> value.

#### State

Returns the <code>State</code> value.

#### StateTransitionReason

Returns the <code>StateTransitionReason</code> value.

#### Uuid

Returns the <code>Uuid</code> value.

