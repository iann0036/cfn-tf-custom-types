# TF::CheckPoint::ManagementThreatProfile OverridesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#capturepackets" title="CapturePackets">CapturePackets</a>" : <i>Boolean</i>,
    "<a href="#protection" title="Protection">Protection</a>" : <i>String</i>,
    "<a href="#track" title="Track">Track</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#capturepackets" title="CapturePackets">CapturePackets</a>: <i>Boolean</i>
<a href="#protection" title="Protection">Protection</a>: <i>String</i>
<a href="#track" title="Track">Track</a>: <i>String</i>
</pre>

## Properties

#### Action

Protection action.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CapturePackets

Capture packets.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protection

IPS protection identified by name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Track

Tracking method for protection.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

