# TF::AWS::Kinesisanalyticsv2Application RunConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#applicationrestoreconfiguration" title="ApplicationRestoreConfiguration">ApplicationRestoreConfiguration</a>" : <i>[ <a href="applicationrestoreconfigurationdefinition.md">ApplicationRestoreConfigurationDefinition</a>, ... ]</i>,
    "<a href="#flinkrunconfiguration" title="FlinkRunConfiguration">FlinkRunConfiguration</a>" : <i>[ <a href="flinkrunconfigurationdefinition.md">FlinkRunConfigurationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#applicationrestoreconfiguration" title="ApplicationRestoreConfiguration">ApplicationRestoreConfiguration</a>: <i>
      - <a href="applicationrestoreconfigurationdefinition.md">ApplicationRestoreConfigurationDefinition</a></i>
<a href="#flinkrunconfiguration" title="FlinkRunConfiguration">FlinkRunConfiguration</a>: <i>
      - <a href="flinkrunconfigurationdefinition.md">FlinkRunConfigurationDefinition</a></i>
</pre>

## Properties

#### ApplicationRestoreConfiguration

_Required_: No

_Type_: List of <a href="applicationrestoreconfigurationdefinition.md">ApplicationRestoreConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlinkRunConfiguration

_Required_: No

_Type_: List of <a href="flinkrunconfigurationdefinition.md">FlinkRunConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

