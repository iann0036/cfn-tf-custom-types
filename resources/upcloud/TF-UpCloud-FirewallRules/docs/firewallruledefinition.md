# TF::UpCloud::FirewallRules FirewallRuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
    "<a href="#destinationaddressend" title="DestinationAddressEnd">DestinationAddressEnd</a>" : <i>String</i>,
    "<a href="#destinationaddressstart" title="DestinationAddressStart">DestinationAddressStart</a>" : <i>String</i>,
    "<a href="#destinationportend" title="DestinationPortEnd">DestinationPortEnd</a>" : <i>Double</i>,
    "<a href="#destinationportstart" title="DestinationPortStart">DestinationPortStart</a>" : <i>Double</i>,
    "<a href="#direction" title="Direction">Direction</a>" : <i>String</i>,
    "<a href="#family" title="Family">Family</a>" : <i>String</i>,
    "<a href="#icmptype" title="IcmpType">IcmpType</a>" : <i>String</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#sourceaddressend" title="SourceAddressEnd">SourceAddressEnd</a>" : <i>String</i>,
    "<a href="#sourceaddressstart" title="SourceAddressStart">SourceAddressStart</a>" : <i>String</i>,
    "<a href="#sourceportend" title="SourcePortEnd">SourcePortEnd</a>" : <i>Double</i>,
    "<a href="#sourceportstart" title="SourcePortStart">SourcePortStart</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#comment" title="Comment">Comment</a>: <i>String</i>
<a href="#destinationaddressend" title="DestinationAddressEnd">DestinationAddressEnd</a>: <i>String</i>
<a href="#destinationaddressstart" title="DestinationAddressStart">DestinationAddressStart</a>: <i>String</i>
<a href="#destinationportend" title="DestinationPortEnd">DestinationPortEnd</a>: <i>Double</i>
<a href="#destinationportstart" title="DestinationPortStart">DestinationPortStart</a>: <i>Double</i>
<a href="#direction" title="Direction">Direction</a>: <i>String</i>
<a href="#family" title="Family">Family</a>: <i>String</i>
<a href="#icmptype" title="IcmpType">IcmpType</a>: <i>String</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#sourceaddressend" title="SourceAddressEnd">SourceAddressEnd</a>: <i>String</i>
<a href="#sourceaddressstart" title="SourceAddressStart">SourceAddressStart</a>: <i>String</i>
<a href="#sourceportend" title="SourcePortEnd">SourcePortEnd</a>: <i>Double</i>
<a href="#sourceportstart" title="SourcePortStart">SourcePortStart</a>: <i>Double</i>
</pre>

## Properties

#### Action

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationAddressEnd

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationAddressStart

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationPortEnd

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationPortStart

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Direction

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Family

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcmpType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceAddressEnd

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceAddressStart

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourcePortEnd

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourcePortStart

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

