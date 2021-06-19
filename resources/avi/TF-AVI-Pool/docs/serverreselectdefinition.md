# TF::AVI::Pool ServerReselectDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#numretries" title="NumRetries">NumRetries</a>" : <i>Double</i>,
    "<a href="#retrynonidempotent" title="RetryNonidempotent">RetryNonidempotent</a>" : <i>Boolean</i>,
    "<a href="#retrytimeout" title="RetryTimeout">RetryTimeout</a>" : <i>Double</i>,
    "<a href="#svrrespcode" title="SvrRespCode">SvrRespCode</a>" : <i>[ <a href="svrrespcodedefinition.md">SvrRespCodeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#numretries" title="NumRetries">NumRetries</a>: <i>Double</i>
<a href="#retrynonidempotent" title="RetryNonidempotent">RetryNonidempotent</a>: <i>Boolean</i>
<a href="#retrytimeout" title="RetryTimeout">RetryTimeout</a>: <i>Double</i>
<a href="#svrrespcode" title="SvrRespCode">SvrRespCode</a>: <i>
      - <a href="svrrespcodedefinition.md">SvrRespCodeDefinition</a></i>
</pre>

## Properties

#### Enabled

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumRetries

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryNonidempotent

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SvrRespCode

_Required_: No

_Type_: List of <a href="svrrespcodedefinition.md">SvrRespCodeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

