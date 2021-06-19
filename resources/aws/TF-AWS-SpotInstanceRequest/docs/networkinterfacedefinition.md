# TF::AWS::SpotInstanceRequest NetworkInterfaceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#deleteontermination" title="DeleteOnTermination">DeleteOnTermination</a>" : <i>Boolean</i>,
    "<a href="#deviceindex" title="DeviceIndex">DeviceIndex</a>" : <i>Double</i>,
    "<a href="#networkinterfaceid" title="NetworkInterfaceId">NetworkInterfaceId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#deleteontermination" title="DeleteOnTermination">DeleteOnTermination</a>: <i>Boolean</i>
<a href="#deviceindex" title="DeviceIndex">DeviceIndex</a>: <i>Double</i>
<a href="#networkinterfaceid" title="NetworkInterfaceId">NetworkInterfaceId</a>: <i>String</i>
</pre>

## Properties

#### DeleteOnTermination

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceIndex

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInterfaceId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

