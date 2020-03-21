# Terraform::AWS::AutoscalingGroup MixedInstancesPolicy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#instancesdistribution" title="InstancesDistribution">InstancesDistribution</a>" : <i>[ <a href="mixedinstancespolicy-instancesdistribution.md">InstancesDistribution</a>, ... ]</i>,
    "<a href="#launchtemplate" title="LaunchTemplate">LaunchTemplate</a>" : <i>[ <a href="mixedinstancespolicy-launchtemplate.md">LaunchTemplate</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#instancesdistribution" title="InstancesDistribution">InstancesDistribution</a>: <i>
      - <a href="mixedinstancespolicy-instancesdistribution.md">InstancesDistribution</a></i>
<a href="#launchtemplate" title="LaunchTemplate">LaunchTemplate</a>: <i>
      - <a href="mixedinstancespolicy-launchtemplate.md">LaunchTemplate</a></i>
</pre>

## Properties

#### InstancesDistribution

_Required_: No
_Type_: List of <a href="mixedinstancespolicy-instancesdistribution.md">InstancesDistribution</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchTemplate

_Required_: No
_Type_: List of <a href="mixedinstancespolicy-launchtemplate.md">LaunchTemplate</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

