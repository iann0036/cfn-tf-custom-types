# Terraform::AWS::EcsCapacityProvider AutoScalingGroupProvider

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autoscalinggrouparn" title="AutoScalingGroupArn">AutoScalingGroupArn</a>" : <i>String</i>,
    "<a href="#managedterminationprotection" title="ManagedTerminationProtection">ManagedTerminationProtection</a>" : <i>String</i>,
    "<a href="#managedscaling" title="ManagedScaling">ManagedScaling</a>" : <i>[ <a href="autoscalinggroupprovider-managedscaling.md">ManagedScaling</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#autoscalinggrouparn" title="AutoScalingGroupArn">AutoScalingGroupArn</a>: <i>String</i>
<a href="#managedterminationprotection" title="ManagedTerminationProtection">ManagedTerminationProtection</a>: <i>String</i>
<a href="#managedscaling" title="ManagedScaling">ManagedScaling</a>: <i>
      - <a href="autoscalinggroupprovider-managedscaling.md">ManagedScaling</a></i>
</pre>

## Properties

#### AutoScalingGroupArn

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedTerminationProtection

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedScaling

_Required_: No
_Type_: List of <a href="autoscalinggroupprovider-managedscaling.md">ManagedScaling</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

