# TF::AWS::EmrCluster CoreInstanceFleetDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#targetondemandcapacity" title="TargetOnDemandCapacity">TargetOnDemandCapacity</a>" : <i>Double</i>,
    "<a href="#targetspotcapacity" title="TargetSpotCapacity">TargetSpotCapacity</a>" : <i>Double</i>,
    "<a href="#instancetypeconfigs" title="InstanceTypeConfigs">InstanceTypeConfigs</a>" : <i>[ <a href="instancetypeconfigsdefinition.md">InstanceTypeConfigsDefinition</a>, ... ]</i>,
    "<a href="#launchspecifications" title="LaunchSpecifications">LaunchSpecifications</a>" : <i>[ <a href="launchspecificationsdefinition.md">LaunchSpecificationsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#targetondemandcapacity" title="TargetOnDemandCapacity">TargetOnDemandCapacity</a>: <i>Double</i>
<a href="#targetspotcapacity" title="TargetSpotCapacity">TargetSpotCapacity</a>: <i>Double</i>
<a href="#instancetypeconfigs" title="InstanceTypeConfigs">InstanceTypeConfigs</a>: <i>
      - <a href="instancetypeconfigsdefinition.md">InstanceTypeConfigsDefinition</a></i>
<a href="#launchspecifications" title="LaunchSpecifications">LaunchSpecifications</a>: <i>
      - <a href="launchspecificationsdefinition.md">LaunchSpecificationsDefinition</a></i>
</pre>

## Properties

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetOnDemandCapacity

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetSpotCapacity

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceTypeConfigs

_Required_: No

_Type_: List of <a href="instancetypeconfigsdefinition.md">InstanceTypeConfigsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchSpecifications

_Required_: No

_Type_: List of <a href="launchspecificationsdefinition.md">LaunchSpecificationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

