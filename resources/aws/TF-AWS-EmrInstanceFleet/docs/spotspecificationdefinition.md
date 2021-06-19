# TF::AWS::EmrInstanceFleet SpotSpecificationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allocationstrategy" title="AllocationStrategy">AllocationStrategy</a>" : <i>String</i>,
    "<a href="#blockdurationminutes" title="BlockDurationMinutes">BlockDurationMinutes</a>" : <i>Double</i>,
    "<a href="#timeoutaction" title="TimeoutAction">TimeoutAction</a>" : <i>String</i>,
    "<a href="#timeoutdurationminutes" title="TimeoutDurationMinutes">TimeoutDurationMinutes</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#allocationstrategy" title="AllocationStrategy">AllocationStrategy</a>: <i>String</i>
<a href="#blockdurationminutes" title="BlockDurationMinutes">BlockDurationMinutes</a>: <i>Double</i>
<a href="#timeoutaction" title="TimeoutAction">TimeoutAction</a>: <i>String</i>
<a href="#timeoutdurationminutes" title="TimeoutDurationMinutes">TimeoutDurationMinutes</a>: <i>Double</i>
</pre>

## Properties

#### AllocationStrategy

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockDurationMinutes

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutAction

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutDurationMinutes

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

