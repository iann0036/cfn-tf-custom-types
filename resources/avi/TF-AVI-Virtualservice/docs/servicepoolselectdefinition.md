# TF::AVI::Virtualservice ServicePoolSelectDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#servicepoolgroupref" title="ServicePoolGroupRef">ServicePoolGroupRef</a>" : <i>String</i>,
    "<a href="#servicepoolref" title="ServicePoolRef">ServicePoolRef</a>" : <i>String</i>,
    "<a href="#serviceport" title="ServicePort">ServicePort</a>" : <i>Double</i>,
    "<a href="#serviceportrangeend" title="ServicePortRangeEnd">ServicePortRangeEnd</a>" : <i>Double</i>,
    "<a href="#serviceprotocol" title="ServiceProtocol">ServiceProtocol</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#servicepoolgroupref" title="ServicePoolGroupRef">ServicePoolGroupRef</a>: <i>String</i>
<a href="#servicepoolref" title="ServicePoolRef">ServicePoolRef</a>: <i>String</i>
<a href="#serviceport" title="ServicePort">ServicePort</a>: <i>Double</i>
<a href="#serviceportrangeend" title="ServicePortRangeEnd">ServicePortRangeEnd</a>: <i>Double</i>
<a href="#serviceprotocol" title="ServiceProtocol">ServiceProtocol</a>: <i>String</i>
</pre>

## Properties

#### ServicePoolGroupRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServicePoolRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServicePort

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServicePortRangeEnd

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceProtocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

