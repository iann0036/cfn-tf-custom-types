# Terraform::AzureRM::BatchPool FixedScale

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#resizetimeout" title="ResizeTimeout">ResizeTimeout</a>" : <i>String</i>,
    "<a href="#targetdedicatednodes" title="TargetDedicatedNodes">TargetDedicatedNodes</a>" : <i>Double</i>,
    "<a href="#targetlowprioritynodes" title="TargetLowPriorityNodes">TargetLowPriorityNodes</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#resizetimeout" title="ResizeTimeout">ResizeTimeout</a>: <i>String</i>
<a href="#targetdedicatednodes" title="TargetDedicatedNodes">TargetDedicatedNodes</a>: <i>Double</i>
<a href="#targetlowprioritynodes" title="TargetLowPriorityNodes">TargetLowPriorityNodes</a>: <i>Double</i>
</pre>

## Properties

#### ResizeTimeout

The timeout for resize operations. Defaults to `PT15M`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetDedicatedNodes

The number of nodes in the Batch pool. Defaults to `1`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetLowPriorityNodes

The number of low priority nodes in the Batch pool. Defaults to `0`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

