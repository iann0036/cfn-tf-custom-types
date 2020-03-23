# Terraform::AWS::CodedeployDeploymentConfig TrafficRoutingConfig TimeBasedLinear

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#interval" title="Interval">Interval</a>" : <i>Double</i>,
    "<a href="#percentage" title="Percentage">Percentage</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#interval" title="Interval">Interval</a>: <i>Double</i>
<a href="#percentage" title="Percentage">Percentage</a>: <i>Double</i>
</pre>

## Properties

#### Interval

The number of minutes between each incremental traffic shift of a `TimeBasedLinear` deployment.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Percentage

The percentage of traffic that is shifted at the start of each increment of a `TimeBasedLinear` deployment.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

