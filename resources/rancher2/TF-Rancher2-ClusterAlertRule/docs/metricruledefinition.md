# TF::Rancher2::ClusterAlertRule MetricRuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#comparison" title="Comparison">Comparison</a>" : <i>String</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#duration" title="Duration">Duration</a>" : <i>String</i>,
    "<a href="#expression" title="Expression">Expression</a>" : <i>String</i>,
    "<a href="#thresholdvalue" title="ThresholdValue">ThresholdValue</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#comparison" title="Comparison">Comparison</a>: <i>String</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#duration" title="Duration">Duration</a>: <i>String</i>
<a href="#expression" title="Expression">Expression</a>: <i>String</i>
<a href="#thresholdvalue" title="ThresholdValue">ThresholdValue</a>: <i>Double</i>
</pre>

## Properties

#### Comparison

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Duration

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expression

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThresholdValue

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
