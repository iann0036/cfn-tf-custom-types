# Terraform::AWS::CodedeployDeploymentConfig TrafficRoutingConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#timebasedcanary" title="TimeBasedCanary">TimeBasedCanary</a>" : <i>[ &lt;a href=&#34;trafficroutingconfig-timebasedcanary.md&#34;&gt;TimeBasedCanary&lt;/a&gt;, ... ]</i>,
    "<a href="#timebasedlinear" title="TimeBasedLinear">TimeBasedLinear</a>" : <i>[ &lt;a href=&#34;trafficroutingconfig-timebasedlinear.md&#34;&gt;TimeBasedLinear&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#timebasedcanary" title="TimeBasedCanary">TimeBasedCanary</a>: <i>
      - &lt;a href=&#34;trafficroutingconfig-timebasedcanary.md&#34;&gt;TimeBasedCanary&lt;/a&gt;</i>
<a href="#timebasedlinear" title="TimeBasedLinear">TimeBasedLinear</a>: <i>
      - &lt;a href=&#34;trafficroutingconfig-timebasedlinear.md&#34;&gt;TimeBasedLinear&lt;/a&gt;</i>
</pre>

## Properties

#### Type

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeBasedCanary

_Required_: No
_Type_: List of &lt;a href=&#34;trafficroutingconfig-timebasedcanary.md&#34;&gt;TimeBasedCanary&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeBasedLinear

_Required_: No
_Type_: List of &lt;a href=&#34;trafficroutingconfig-timebasedlinear.md&#34;&gt;TimeBasedLinear&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

