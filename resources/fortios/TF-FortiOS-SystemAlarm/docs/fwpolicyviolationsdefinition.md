# TF::FortiOS::SystemAlarm FwPolicyViolationsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dstip" title="DstIp">DstIp</a>" : <i>String</i>,
    "<a href="#dstport" title="DstPort">DstPort</a>" : <i>Double</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#srcip" title="SrcIp">SrcIp</a>" : <i>String</i>,
    "<a href="#srcport" title="SrcPort">SrcPort</a>" : <i>Double</i>,
    "<a href="#threshold" title="Threshold">Threshold</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#dstip" title="DstIp">DstIp</a>: <i>String</i>
<a href="#dstport" title="DstPort">DstPort</a>: <i>Double</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#srcip" title="SrcIp">SrcIp</a>: <i>String</i>
<a href="#srcport" title="SrcPort">SrcPort</a>: <i>Double</i>
<a href="#threshold" title="Threshold">Threshold</a>: <i>Double</i>
</pre>

## Properties

#### DstIp

Destination IP (0=all).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DstPort

Destination port (0=all).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

Firewall policy violations ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcIp

Source IP (0=all).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcPort

Source port (0=all).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Threshold

Firewall policy violation threshold.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

