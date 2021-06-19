# TF::AWS::CodedeployDeploymentConfig TrafficRoutingConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#timebasedcanary" title="TimeBasedCanary">TimeBasedCanary</a>" : <i>[ <a href="timebasedcanarydefinition.md">TimeBasedCanaryDefinition</a>, ... ]</i>,
    "<a href="#timebasedlinear" title="TimeBasedLinear">TimeBasedLinear</a>" : <i>[ <a href="timebasedlineardefinition.md">TimeBasedLinearDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#timebasedcanary" title="TimeBasedCanary">TimeBasedCanary</a>: <i>
      - <a href="timebasedcanarydefinition.md">TimeBasedCanaryDefinition</a></i>
<a href="#timebasedlinear" title="TimeBasedLinear">TimeBasedLinear</a>: <i>
      - <a href="timebasedlineardefinition.md">TimeBasedLinearDefinition</a></i>
</pre>

## Properties

#### Type

Type of traffic routing config. One of `TimeBasedCanary`, `TimeBasedLinear`, `AllAtOnce`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeBasedCanary

_Required_: No

_Type_: List of <a href="timebasedcanarydefinition.md">TimeBasedCanaryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeBasedLinear

_Required_: No

_Type_: List of <a href="timebasedlineardefinition.md">TimeBasedLinearDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

