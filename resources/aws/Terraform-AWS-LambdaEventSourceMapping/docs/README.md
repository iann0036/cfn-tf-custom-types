# Terraform::AWS::LambdaEventSourceMapping

CloudFormation equivalent of aws_lambda_event_source_mapping

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::LambdaEventSourceMapping",
    "Properties" : {
        "<a href="#batchsize" title="BatchSize">BatchSize</a>" : <i>Double</i>,
        "<a href="#bisectbatchonfunctionerror" title="BisectBatchOnFunctionError">BisectBatchOnFunctionError</a>" : <i>Boolean</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#eventsourcearn" title="EventSourceArn">EventSourceArn</a>" : <i>String</i>,
        "<a href="#functionname" title="FunctionName">FunctionName</a>" : <i>String</i>,
        "<a href="#maximumbatchingwindowinseconds" title="MaximumBatchingWindowInSeconds">MaximumBatchingWindowInSeconds</a>" : <i>Double</i>,
        "<a href="#maximumrecordageinseconds" title="MaximumRecordAgeInSeconds">MaximumRecordAgeInSeconds</a>" : <i>Double</i>,
        "<a href="#maximumretryattempts" title="MaximumRetryAttempts">MaximumRetryAttempts</a>" : <i>Double</i>,
        "<a href="#parallelizationfactor" title="ParallelizationFactor">ParallelizationFactor</a>" : <i>Double</i>,
        "<a href="#startingposition" title="StartingPosition">StartingPosition</a>" : <i>String</i>,
        "<a href="#startingpositiontimestamp" title="StartingPositionTimestamp">StartingPositionTimestamp</a>" : <i>String</i>,
        "<a href="#destinationconfig" title="DestinationConfig">DestinationConfig</a>" : <i>[ <a href="destinationconfig.md">DestinationConfig</a>, ... ]</i>,
        "<a href="#onfailure" title="OnFailure">OnFailure</a>" : <i>[ <a href="onfailure.md">OnFailure</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::LambdaEventSourceMapping
Properties:
    <a href="#batchsize" title="BatchSize">BatchSize</a>: <i>Double</i>
    <a href="#bisectbatchonfunctionerror" title="BisectBatchOnFunctionError">BisectBatchOnFunctionError</a>: <i>Boolean</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#eventsourcearn" title="EventSourceArn">EventSourceArn</a>: <i>String</i>
    <a href="#functionname" title="FunctionName">FunctionName</a>: <i>String</i>
    <a href="#maximumbatchingwindowinseconds" title="MaximumBatchingWindowInSeconds">MaximumBatchingWindowInSeconds</a>: <i>Double</i>
    <a href="#maximumrecordageinseconds" title="MaximumRecordAgeInSeconds">MaximumRecordAgeInSeconds</a>: <i>Double</i>
    <a href="#maximumretryattempts" title="MaximumRetryAttempts">MaximumRetryAttempts</a>: <i>Double</i>
    <a href="#parallelizationfactor" title="ParallelizationFactor">ParallelizationFactor</a>: <i>Double</i>
    <a href="#startingposition" title="StartingPosition">StartingPosition</a>: <i>String</i>
    <a href="#startingpositiontimestamp" title="StartingPositionTimestamp">StartingPositionTimestamp</a>: <i>String</i>
    <a href="#destinationconfig" title="DestinationConfig">DestinationConfig</a>: <i>
      - <a href="destinationconfig.md">DestinationConfig</a></i>
    <a href="#onfailure" title="OnFailure">OnFailure</a>: <i>
      - <a href="onfailure.md">OnFailure</a></i>
</pre>

## Properties

#### BatchSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BisectBatchOnFunctionError

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventSourceArn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FunctionName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumBatchingWindowInSeconds

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

#### StartingPosition

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartingPositionTimestamp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationConfig

_Required_: No

_Type_: List of <a href="destinationconfig.md">DestinationConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnFailure

_Required_: No

_Type_: List of <a href="onfailure.md">OnFailure</a>

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

