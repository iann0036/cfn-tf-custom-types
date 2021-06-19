# TF::AWS::Kinesisanalyticsv2Application FlinkApplicationConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#checkpointconfiguration" title="CheckpointConfiguration">CheckpointConfiguration</a>" : <i>[ <a href="checkpointconfigurationdefinition.md">CheckpointConfigurationDefinition</a>, ... ]</i>,
    "<a href="#monitoringconfiguration" title="MonitoringConfiguration">MonitoringConfiguration</a>" : <i>[ <a href="monitoringconfigurationdefinition.md">MonitoringConfigurationDefinition</a>, ... ]</i>,
    "<a href="#parallelismconfiguration" title="ParallelismConfiguration">ParallelismConfiguration</a>" : <i>[ <a href="parallelismconfigurationdefinition.md">ParallelismConfigurationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#checkpointconfiguration" title="CheckpointConfiguration">CheckpointConfiguration</a>: <i>
      - <a href="checkpointconfigurationdefinition.md">CheckpointConfigurationDefinition</a></i>
<a href="#monitoringconfiguration" title="MonitoringConfiguration">MonitoringConfiguration</a>: <i>
      - <a href="monitoringconfigurationdefinition.md">MonitoringConfigurationDefinition</a></i>
<a href="#parallelismconfiguration" title="ParallelismConfiguration">ParallelismConfiguration</a>: <i>
      - <a href="parallelismconfigurationdefinition.md">ParallelismConfigurationDefinition</a></i>
</pre>

## Properties

#### CheckpointConfiguration

_Required_: No

_Type_: List of <a href="checkpointconfigurationdefinition.md">CheckpointConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitoringConfiguration

_Required_: No

_Type_: List of <a href="monitoringconfigurationdefinition.md">MonitoringConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParallelismConfiguration

_Required_: No

_Type_: List of <a href="parallelismconfigurationdefinition.md">ParallelismConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

