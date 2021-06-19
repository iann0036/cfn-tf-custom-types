# TF::Volterra::Route RetryPolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#numretries" title="NumRetries">NumRetries</a>" : <i>Double</i>,
    "<a href="#pertrytimeout" title="PerTryTimeout">PerTryTimeout</a>" : <i>Double</i>,
    "<a href="#retriablestatuscodes" title="RetriableStatusCodes">RetriableStatusCodes</a>" : <i>[ Double, ... ]</i>,
    "<a href="#retryon" title="RetryOn">RetryOn</a>" : <i>String</i>,
    "<a href="#backoff" title="BackOff">BackOff</a>" : <i>[ <a href="backoffdefinition.md">BackOffDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#numretries" title="NumRetries">NumRetries</a>: <i>Double</i>
<a href="#pertrytimeout" title="PerTryTimeout">PerTryTimeout</a>: <i>Double</i>
<a href="#retriablestatuscodes" title="RetriableStatusCodes">RetriableStatusCodes</a>: <i>
      - Double</i>
<a href="#retryon" title="RetryOn">RetryOn</a>: <i>String</i>
<a href="#backoff" title="BackOff">BackOff</a>: <i>
      - <a href="backoffdefinition.md">BackOffDefinition</a></i>
</pre>

## Properties

#### NumRetries

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PerTryTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetriableStatusCodes

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryOn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackOff

_Required_: No

_Type_: List of <a href="backoffdefinition.md">BackOffDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

