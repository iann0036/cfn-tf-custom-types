# TF::AWS::NetworkInterface AttachmentDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#deviceindex" title="DeviceIndex">DeviceIndex</a>" : <i>Double</i>,
    "<a href="#instance" title="Instance">Instance</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#deviceindex" title="DeviceIndex">DeviceIndex</a>: <i>Double</i>
<a href="#instance" title="Instance">Instance</a>: <i>String</i>
</pre>

## Properties

#### DeviceIndex

Integer to define the devices index.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Instance

ID of the instance to attach to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

