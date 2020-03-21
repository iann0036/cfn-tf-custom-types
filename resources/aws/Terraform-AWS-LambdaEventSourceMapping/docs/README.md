# Terraform::AWS::LambdaEventSourceMapping

CloudFormation equivalent of aws_lambda_event_source_mapping

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::LambdaEventSourceMapping",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#batchsize" title="BatchSize">BatchSize</a>" : <i>Double</i>,
        "<a href="#bisectbatchonfunctionerror" title="BisectBatchOnFunctionError">BisectBatchOnFunctionError</a>" : <i>Boolean</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#eventsourcearn" title="EventSourceArn">EventSourceArn</a>" : <i>String</i>,
        "<a href="#functionarn" title="FunctionArn">FunctionArn</a>" : <i>String</i>,
        "<a href="#functionname" title="FunctionName">FunctionName</a>" : <i>String</i>,
        "<a href="#lastmodified" title="LastModified">LastModified</a>" : <i>String</i>,
        "<a href="#lastprocessingresult" title="LastProcessingResult">LastProcessingResult</a>" : <i>String</i>,
        "<a href="#maximumbatchingwindowinseconds" title="MaximumBatchingWindowInSeconds">MaximumBatchingWindowInSeconds</a>" : <i>Double</i>,
        "<a href="#maximumrecordageinseconds" title="MaximumRecordAgeInSeconds">MaximumRecordAgeInSeconds</a>" : <i>Double</i>,
        "<a href="#maximumretryattempts" title="MaximumRetryAttempts">MaximumRetryAttempts</a>" : <i>Double</i>,
        "<a href="#parallelizationfactor" title="ParallelizationFactor">ParallelizationFactor</a>" : <i>Double</i>,
        "<a href="#startingposition" title="StartingPosition">StartingPosition</a>" : <i>String</i>,
        "<a href="#startingpositiontimestamp" title="StartingPositionTimestamp">StartingPositionTimestamp</a>" : <i>String</i>,
        "<a href="#state" title="State">State</a>" : <i>String</i>,
        "<a href="#statetransitionreason" title="StateTransitionReason">StateTransitionReason</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#destinationconfig" title="DestinationConfig">DestinationConfig</a>" : <i>[ &lt;a href=&#34;destinationconfig.md&#34;&gt;DestinationConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#onfailure" title="OnFailure">OnFailure</a>" : <i>[ &lt;a href=&#34;onfailure.md&#34;&gt;OnFailure&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::LambdaEventSourceMapping
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#batchsize" title="BatchSize">BatchSize</a>: <i>Double</i>
    <a href="#bisectbatchonfunctionerror" title="BisectBatchOnFunctionError">BisectBatchOnFunctionError</a>: <i>Boolean</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#eventsourcearn" title="EventSourceArn">EventSourceArn</a>: <i>String</i>
    <a href="#functionarn" title="FunctionArn">FunctionArn</a>: <i>String</i>
    <a href="#functionname" title="FunctionName">FunctionName</a>: <i>String</i>
    <a href="#lastmodified" title="LastModified">LastModified</a>: <i>String</i>
    <a href="#lastprocessingresult" title="LastProcessingResult">LastProcessingResult</a>: <i>String</i>
    <a href="#maximumbatchingwindowinseconds" title="MaximumBatchingWindowInSeconds">MaximumBatchingWindowInSeconds</a>: <i>Double</i>
    <a href="#maximumrecordageinseconds" title="MaximumRecordAgeInSeconds">MaximumRecordAgeInSeconds</a>: <i>Double</i>
    <a href="#maximumretryattempts" title="MaximumRetryAttempts">MaximumRetryAttempts</a>: <i>Double</i>
    <a href="#parallelizationfactor" title="ParallelizationFactor">ParallelizationFactor</a>: <i>Double</i>
    <a href="#startingposition" title="StartingPosition">StartingPosition</a>: <i>String</i>
    <a href="#startingpositiontimestamp" title="StartingPositionTimestamp">StartingPositionTimestamp</a>: <i>String</i>
    <a href="#state" title="State">State</a>: <i>String</i>
    <a href="#statetransitionreason" title="StateTransitionReason">StateTransitionReason</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#destinationconfig" title="DestinationConfig">DestinationConfig</a>: <i>
      - &lt;a href=&#34;destinationconfig.md&#34;&gt;DestinationConfig&lt;/a&gt;</i>
    <a href="#onfailure" title="OnFailure">OnFailure</a>: <i>
      - &lt;a href=&#34;onfailure.md&#34;&gt;OnFailure&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

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

#### FunctionArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FunctionName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LastModified

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LastProcessingResult

_Required_: No

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

#### State

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StateTransitionReason

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationConfig

_Required_: No

_Type_: List of &lt;a href=&#34;destinationconfig.md&#34;&gt;DestinationConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnFailure

_Required_: No

_Type_: List of &lt;a href=&#34;onfailure.md&#34;&gt;OnFailure&lt;/a&gt;

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

Returns the &lt;code&gt;FunctionArn&lt;/code&gt; value.

#### LastModified

Returns the &lt;code&gt;LastModified&lt;/code&gt; value.

#### LastProcessingResult

Returns the &lt;code&gt;LastProcessingResult&lt;/code&gt; value.

#### State

Returns the &lt;code&gt;State&lt;/code&gt; value.

#### StateTransitionReason

Returns the &lt;code&gt;StateTransitionReason&lt;/code&gt; value.

#### Uuid

Returns the &lt;code&gt;Uuid&lt;/code&gt; value.

