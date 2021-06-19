# TF::AWS::CloudwatchEventTarget RetryPolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#maximumeventageinseconds" title="MaximumEventAgeInSeconds">MaximumEventAgeInSeconds</a>" : <i>Double</i>,
    "<a href="#maximumretryattempts" title="MaximumRetryAttempts">MaximumRetryAttempts</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#maximumeventageinseconds" title="MaximumEventAgeInSeconds">MaximumEventAgeInSeconds</a>: <i>Double</i>
<a href="#maximumretryattempts" title="MaximumRetryAttempts">MaximumRetryAttempts</a>: <i>Double</i>
</pre>

## Properties

#### MaximumEventAgeInSeconds

The age in seconds to continue to make retry attempts.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumRetryAttempts

maximum number of retry attempts to make before the request fails.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

