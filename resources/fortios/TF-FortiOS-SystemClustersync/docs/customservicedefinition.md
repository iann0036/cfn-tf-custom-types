# TF::FortiOS::SystemClustersync CustomServiceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dstportrange" title="DstPortRange">DstPortRange</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#srcportrange" title="SrcPortRange">SrcPortRange</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#dstportrange" title="DstPortRange">DstPortRange</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#srcportrange" title="SrcPortRange">SrcPortRange</a>: <i>String</i>
</pre>

## Properties

#### DstPortRange

Custom service destination port range.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

Custom service ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcPortRange

Custom service source port range.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

