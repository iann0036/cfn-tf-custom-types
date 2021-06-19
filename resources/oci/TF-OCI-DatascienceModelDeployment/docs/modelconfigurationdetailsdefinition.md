# TF::OCI::DatascienceModelDeployment ModelConfigurationDetailsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bandwidthmbps" title="BandwidthMbps">BandwidthMbps</a>" : <i>Double</i>,
    "<a href="#modelid" title="ModelId">ModelId</a>" : <i>String</i>,
    "<a href="#instanceconfiguration" title="InstanceConfiguration">InstanceConfiguration</a>" : <i>[ <a href="instanceconfigurationdefinition.md">InstanceConfigurationDefinition</a>, ... ]</i>,
    "<a href="#scalingpolicy" title="ScalingPolicy">ScalingPolicy</a>" : <i>[ <a href="scalingpolicydefinition.md">ScalingPolicyDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#bandwidthmbps" title="BandwidthMbps">BandwidthMbps</a>: <i>Double</i>
<a href="#modelid" title="ModelId">ModelId</a>: <i>String</i>
<a href="#instanceconfiguration" title="InstanceConfiguration">InstanceConfiguration</a>: <i>
      - <a href="instanceconfigurationdefinition.md">InstanceConfigurationDefinition</a></i>
<a href="#scalingpolicy" title="ScalingPolicy">ScalingPolicy</a>: <i>
      - <a href="scalingpolicydefinition.md">ScalingPolicyDefinition</a></i>
</pre>

## Properties

#### BandwidthMbps

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ModelId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceConfiguration

_Required_: No

_Type_: List of <a href="instanceconfigurationdefinition.md">InstanceConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingPolicy

_Required_: No

_Type_: List of <a href="scalingpolicydefinition.md">ScalingPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

