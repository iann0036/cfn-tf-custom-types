# Terraform::AWS::EcsCapacityProvider AutoScalingGroupProvider

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autoscalinggrouparn" title="AutoScalingGroupArn">AutoScalingGroupArn</a>" : <i>String</i>,
    "<a href="#managedterminationprotection" title="ManagedTerminationProtection">ManagedTerminationProtection</a>" : <i>String</i>,
    "<a href="#managedscaling" title="ManagedScaling">ManagedScaling</a>" : <i>[ &lt;a href=&#34;autoscalinggroupprovider-managedscaling.md&#34;&gt;ManagedScaling&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#autoscalinggrouparn" title="AutoScalingGroupArn">AutoScalingGroupArn</a>: <i>String</i>
<a href="#managedterminationprotection" title="ManagedTerminationProtection">ManagedTerminationProtection</a>: <i>String</i>
<a href="#managedscaling" title="ManagedScaling">ManagedScaling</a>: <i>
      - &lt;a href=&#34;autoscalinggroupprovider-managedscaling.md&#34;&gt;ManagedScaling&lt;/a&gt;</i>
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
_Type_: List of &lt;a href=&#34;autoscalinggroupprovider-managedscaling.md&#34;&gt;ManagedScaling&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

