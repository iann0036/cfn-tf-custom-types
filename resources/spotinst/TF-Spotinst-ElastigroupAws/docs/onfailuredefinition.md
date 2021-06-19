# TF::Spotinst::ElastigroupAws OnFailureDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#actiontype" title="ActionType">ActionType</a>" : <i>String</i>,
    "<a href="#batchnum" title="BatchNum">BatchNum</a>" : <i>Double</i>,
    "<a href="#drainingtimeout" title="DrainingTimeout">DrainingTimeout</a>" : <i>Double</i>,
    "<a href="#shoulddecrementtargetcapacity" title="ShouldDecrementTargetCapacity">ShouldDecrementTargetCapacity</a>" : <i>Boolean</i>,
    "<a href="#shouldhandleallbatches" title="ShouldHandleAllBatches">ShouldHandleAllBatches</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#actiontype" title="ActionType">ActionType</a>: <i>String</i>
<a href="#batchnum" title="BatchNum">BatchNum</a>: <i>Double</i>
<a href="#drainingtimeout" title="DrainingTimeout">DrainingTimeout</a>: <i>Double</i>
<a href="#shoulddecrementtargetcapacity" title="ShouldDecrementTargetCapacity">ShouldDecrementTargetCapacity</a>: <i>Boolean</i>
<a href="#shouldhandleallbatches" title="ShouldHandleAllBatches">ShouldHandleAllBatches</a>: <i>Boolean</i>
</pre>

## Properties

#### ActionType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BatchNum

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DrainingTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShouldDecrementTargetCapacity

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShouldHandleAllBatches

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

