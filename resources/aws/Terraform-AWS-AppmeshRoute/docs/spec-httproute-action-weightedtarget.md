# Terraform::AWS::AppmeshRoute Spec HttpRoute Action WeightedTarget

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#virtualnode" title="VirtualNode">VirtualNode</a>" : <i>String</i>,
    "<a href="#weight" title="Weight">Weight</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#virtualnode" title="VirtualNode">VirtualNode</a>: <i>String</i>
<a href="#weight" title="Weight">Weight</a>: <i>Double</i>
</pre>

## Properties

#### VirtualNode

The virtual node to associate with the weighted target.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Weight

The relative weight of the weighted target. An integer between 0 and 100.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

