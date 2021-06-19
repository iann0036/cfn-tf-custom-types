# TF::Rancher2::ClusterTemplate ScheduledClusterScanDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#scanconfig" title="ScanConfig">ScanConfig</a>" : <i>[ <a href="scanconfigdefinition.md">ScanConfigDefinition</a>, ... ]</i>,
    "<a href="#scheduleconfig" title="ScheduleConfig">ScheduleConfig</a>" : <i>[ <a href="scheduleconfigdefinition.md">ScheduleConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#scanconfig" title="ScanConfig">ScanConfig</a>: <i>
      - <a href="scanconfigdefinition.md">ScanConfigDefinition</a></i>
<a href="#scheduleconfig" title="ScheduleConfig">ScheduleConfig</a>: <i>
      - <a href="scheduleconfigdefinition.md">ScheduleConfigDefinition</a></i>
</pre>

## Properties

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScanConfig

_Required_: No

_Type_: List of <a href="scanconfigdefinition.md">ScanConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduleConfig

_Required_: No

_Type_: List of <a href="scheduleconfigdefinition.md">ScheduleConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

