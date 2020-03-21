# Terraform::AWS::CodedeployDeploymentConfig TrafficRoutingConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#timebasedcanary" title="TimeBasedCanary">TimeBasedCanary</a>" : <i>[ <a href="trafficroutingconfig-timebasedcanary.md">TimeBasedCanary</a>, ... ]</i>,
    "<a href="#timebasedlinear" title="TimeBasedLinear">TimeBasedLinear</a>" : <i>[ <a href="trafficroutingconfig-timebasedlinear.md">TimeBasedLinear</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#timebasedcanary" title="TimeBasedCanary">TimeBasedCanary</a>: <i>
      - <a href="trafficroutingconfig-timebasedcanary.md">TimeBasedCanary</a></i>
<a href="#timebasedlinear" title="TimeBasedLinear">TimeBasedLinear</a>: <i>
      - <a href="trafficroutingconfig-timebasedlinear.md">TimeBasedLinear</a></i>
</pre>

## Properties

#### Type

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeBasedCanary

_Required_: No
_Type_: List of <a href="trafficroutingconfig-timebasedcanary.md">TimeBasedCanary</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeBasedLinear

_Required_: No
_Type_: List of <a href="trafficroutingconfig-timebasedlinear.md">TimeBasedLinear</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

