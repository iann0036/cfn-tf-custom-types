# TF::AWS::CodedeployDeploymentConfig MinimumHealthyHostsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#value" title="Value">Value</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#value" title="Value">Value</a>: <i>Double</i>
</pre>

## Properties

#### Type

The type can either be `FLEET_PERCENT` or `HOST_COUNT`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

The value when the type is `FLEET_PERCENT` represents the minimum number of healthy instances as
a percentage of the total number of instances in the deployment. If you specify FLEET_PERCENT, at the start of the
deployment, AWS CodeDeploy converts the percentage to the equivalent number of instance and rounds up fractional instances.
When the type is `HOST_COUNT`, the value represents the minimum number of healthy instances as an absolute value.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

