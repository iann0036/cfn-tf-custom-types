# TF::Google::ContainerCluster NodePoolDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#initialnodecount" title="InitialNodeCount">InitialNodeCount</a>" : <i>Double</i>,
    "<a href="#maxpodspernode" title="MaxPodsPerNode">MaxPodsPerNode</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#nameprefix" title="NamePrefix">NamePrefix</a>" : <i>String</i>,
    "<a href="#nodecount" title="NodeCount">NodeCount</a>" : <i>Double</i>,
    "<a href="#nodelocations" title="NodeLocations">NodeLocations</a>" : <i>[ String, ... ]</i>,
    "<a href="#version" title="Version">Version</a>" : <i>String</i>,
    "<a href="#autoscaling" title="Autoscaling">Autoscaling</a>" : <i>[ <a href="autoscalingdefinition.md">AutoscalingDefinition</a>, ... ]</i>,
    "<a href="#management" title="Management">Management</a>" : <i>[ <a href="managementdefinition.md">ManagementDefinition</a>, ... ]</i>,
    "<a href="#nodeconfig" title="NodeConfig">NodeConfig</a>" : <i>[ <a href="nodeconfigdefinition.md">NodeConfigDefinition</a>, ... ]</i>,
    "<a href="#upgradesettings" title="UpgradeSettings">UpgradeSettings</a>" : <i>[ <a href="upgradesettingsdefinition.md">UpgradeSettingsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#initialnodecount" title="InitialNodeCount">InitialNodeCount</a>: <i>Double</i>
<a href="#maxpodspernode" title="MaxPodsPerNode">MaxPodsPerNode</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#nameprefix" title="NamePrefix">NamePrefix</a>: <i>String</i>
<a href="#nodecount" title="NodeCount">NodeCount</a>: <i>Double</i>
<a href="#nodelocations" title="NodeLocations">NodeLocations</a>: <i>
      - String</i>
<a href="#version" title="Version">Version</a>: <i>String</i>
<a href="#autoscaling" title="Autoscaling">Autoscaling</a>: <i>
      - <a href="autoscalingdefinition.md">AutoscalingDefinition</a></i>
<a href="#management" title="Management">Management</a>: <i>
      - <a href="managementdefinition.md">ManagementDefinition</a></i>
<a href="#nodeconfig" title="NodeConfig">NodeConfig</a>: <i>
      - <a href="nodeconfigdefinition.md">NodeConfigDefinition</a></i>
<a href="#upgradesettings" title="UpgradeSettings">UpgradeSettings</a>: <i>
      - <a href="upgradesettingsdefinition.md">UpgradeSettingsDefinition</a></i>
</pre>

## Properties

#### InitialNodeCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPodsPerNode

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamePrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeLocations

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Autoscaling

_Required_: No

_Type_: List of <a href="autoscalingdefinition.md">AutoscalingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Management

_Required_: No

_Type_: List of <a href="managementdefinition.md">ManagementDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeConfig

_Required_: No

_Type_: List of <a href="nodeconfigdefinition.md">NodeConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpgradeSettings

_Required_: No

_Type_: List of <a href="upgradesettingsdefinition.md">UpgradeSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

