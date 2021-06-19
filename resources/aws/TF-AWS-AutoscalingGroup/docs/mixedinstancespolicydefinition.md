# TF::AWS::AutoscalingGroup MixedInstancesPolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#instancesdistribution" title="InstancesDistribution">InstancesDistribution</a>" : <i>[ <a href="instancesdistributiondefinition.md">InstancesDistributionDefinition</a>, ... ]</i>,
    "<a href="#launchtemplate" title="LaunchTemplate">LaunchTemplate</a>" : <i>[ <a href="launchtemplatedefinition.md">LaunchTemplateDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#instancesdistribution" title="InstancesDistribution">InstancesDistribution</a>: <i>
      - <a href="instancesdistributiondefinition.md">InstancesDistributionDefinition</a></i>
<a href="#launchtemplate" title="LaunchTemplate">LaunchTemplate</a>: <i>
      - <a href="launchtemplatedefinition.md">LaunchTemplateDefinition</a></i>
</pre>

## Properties

#### InstancesDistribution

_Required_: No

_Type_: List of <a href="instancesdistributiondefinition.md">InstancesDistributionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchTemplate

_Required_: No

_Type_: List of <a href="launchtemplatedefinition.md">LaunchTemplateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

