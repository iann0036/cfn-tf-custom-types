# TF::AzureRM::HdinsightSparkCluster ScheduleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#days" title="Days">Days</a>" : <i>[ String, ... ]</i>,
    "<a href="#targetinstancecount" title="TargetInstanceCount">TargetInstanceCount</a>" : <i>Double</i>,
    "<a href="#time" title="Time">Time</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#days" title="Days">Days</a>: <i>
      - String</i>
<a href="#targetinstancecount" title="TargetInstanceCount">TargetInstanceCount</a>: <i>Double</i>
<a href="#time" title="Time">Time</a>: <i>String</i>
</pre>

## Properties

#### Days

The days of the week to perform autoscale.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetInstanceCount

The number of worker nodes to autoscale at the specified time.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Time

The time of day to perform the autoscale in 24hour format.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

