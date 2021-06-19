# TF::Google::DataprocAutoscalingPolicy YarnConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#gracefuldecommissiontimeout" title="GracefulDecommissionTimeout">GracefulDecommissionTimeout</a>" : <i>String</i>,
    "<a href="#scaledownfactor" title="ScaleDownFactor">ScaleDownFactor</a>" : <i>Double</i>,
    "<a href="#scaledownminworkerfraction" title="ScaleDownMinWorkerFraction">ScaleDownMinWorkerFraction</a>" : <i>Double</i>,
    "<a href="#scaleupfactor" title="ScaleUpFactor">ScaleUpFactor</a>" : <i>Double</i>,
    "<a href="#scaleupminworkerfraction" title="ScaleUpMinWorkerFraction">ScaleUpMinWorkerFraction</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#gracefuldecommissiontimeout" title="GracefulDecommissionTimeout">GracefulDecommissionTimeout</a>: <i>String</i>
<a href="#scaledownfactor" title="ScaleDownFactor">ScaleDownFactor</a>: <i>Double</i>
<a href="#scaledownminworkerfraction" title="ScaleDownMinWorkerFraction">ScaleDownMinWorkerFraction</a>: <i>Double</i>
<a href="#scaleupfactor" title="ScaleUpFactor">ScaleUpFactor</a>: <i>Double</i>
<a href="#scaleupminworkerfraction" title="ScaleUpMinWorkerFraction">ScaleUpMinWorkerFraction</a>: <i>Double</i>
</pre>

## Properties

#### GracefulDecommissionTimeout

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleDownFactor

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleDownMinWorkerFraction

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleUpFactor

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleUpMinWorkerFraction

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

