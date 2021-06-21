# TF::GoogleBeta::GoogleComputeRegionUrlMap RetryPolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#numretries" title="NumRetries">NumRetries</a>" : <i>Double</i>,
    "<a href="#retryconditions" title="RetryConditions">RetryConditions</a>" : <i>[ String, ... ]</i>,
    "<a href="#pertrytimeout" title="PerTryTimeout">PerTryTimeout</a>" : <i>[ <a href="pertrytimeoutdefinition.md">PerTryTimeoutDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#numretries" title="NumRetries">NumRetries</a>: <i>Double</i>
<a href="#retryconditions" title="RetryConditions">RetryConditions</a>: <i>
      - String</i>
<a href="#pertrytimeout" title="PerTryTimeout">PerTryTimeout</a>: <i>
      - <a href="pertrytimeoutdefinition.md">PerTryTimeoutDefinition</a></i>
</pre>

## Properties

#### NumRetries

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryConditions

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PerTryTimeout

_Required_: No

_Type_: List of <a href="pertrytimeoutdefinition.md">PerTryTimeoutDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
