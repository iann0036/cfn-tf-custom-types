# TF::AWS::Kinesisanalyticsv2Application ApplicationConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#applicationcodeconfiguration" title="ApplicationCodeConfiguration">ApplicationCodeConfiguration</a>" : <i>[ <a href="applicationcodeconfigurationdefinition.md">ApplicationCodeConfigurationDefinition</a>, ... ]</i>,
    "<a href="#applicationsnapshotconfiguration" title="ApplicationSnapshotConfiguration">ApplicationSnapshotConfiguration</a>" : <i>[ <a href="applicationsnapshotconfigurationdefinition.md">ApplicationSnapshotConfigurationDefinition</a>, ... ]</i>,
    "<a href="#environmentproperties" title="EnvironmentProperties">EnvironmentProperties</a>" : <i>[ <a href="environmentpropertiesdefinition.md">EnvironmentPropertiesDefinition</a>, ... ]</i>,
    "<a href="#flinkapplicationconfiguration" title="FlinkApplicationConfiguration">FlinkApplicationConfiguration</a>" : <i>[ <a href="flinkapplicationconfigurationdefinition.md">FlinkApplicationConfigurationDefinition</a>, ... ]</i>,
    "<a href="#runconfiguration" title="RunConfiguration">RunConfiguration</a>" : <i>[ <a href="runconfigurationdefinition.md">RunConfigurationDefinition</a>, ... ]</i>,
    "<a href="#sqlapplicationconfiguration" title="SqlApplicationConfiguration">SqlApplicationConfiguration</a>" : <i>[ <a href="sqlapplicationconfigurationdefinition.md">SqlApplicationConfigurationDefinition</a>, ... ]</i>,
    "<a href="#vpcconfiguration" title="VpcConfiguration">VpcConfiguration</a>" : <i>[ <a href="vpcconfigurationdefinition.md">VpcConfigurationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#applicationcodeconfiguration" title="ApplicationCodeConfiguration">ApplicationCodeConfiguration</a>: <i>
      - <a href="applicationcodeconfigurationdefinition.md">ApplicationCodeConfigurationDefinition</a></i>
<a href="#applicationsnapshotconfiguration" title="ApplicationSnapshotConfiguration">ApplicationSnapshotConfiguration</a>: <i>
      - <a href="applicationsnapshotconfigurationdefinition.md">ApplicationSnapshotConfigurationDefinition</a></i>
<a href="#environmentproperties" title="EnvironmentProperties">EnvironmentProperties</a>: <i>
      - <a href="environmentpropertiesdefinition.md">EnvironmentPropertiesDefinition</a></i>
<a href="#flinkapplicationconfiguration" title="FlinkApplicationConfiguration">FlinkApplicationConfiguration</a>: <i>
      - <a href="flinkapplicationconfigurationdefinition.md">FlinkApplicationConfigurationDefinition</a></i>
<a href="#runconfiguration" title="RunConfiguration">RunConfiguration</a>: <i>
      - <a href="runconfigurationdefinition.md">RunConfigurationDefinition</a></i>
<a href="#sqlapplicationconfiguration" title="SqlApplicationConfiguration">SqlApplicationConfiguration</a>: <i>
      - <a href="sqlapplicationconfigurationdefinition.md">SqlApplicationConfigurationDefinition</a></i>
<a href="#vpcconfiguration" title="VpcConfiguration">VpcConfiguration</a>: <i>
      - <a href="vpcconfigurationdefinition.md">VpcConfigurationDefinition</a></i>
</pre>

## Properties

#### ApplicationCodeConfiguration

_Required_: No

_Type_: List of <a href="applicationcodeconfigurationdefinition.md">ApplicationCodeConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationSnapshotConfiguration

_Required_: No

_Type_: List of <a href="applicationsnapshotconfigurationdefinition.md">ApplicationSnapshotConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvironmentProperties

_Required_: No

_Type_: List of <a href="environmentpropertiesdefinition.md">EnvironmentPropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlinkApplicationConfiguration

_Required_: No

_Type_: List of <a href="flinkapplicationconfigurationdefinition.md">FlinkApplicationConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunConfiguration

_Required_: No

_Type_: List of <a href="runconfigurationdefinition.md">RunConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SqlApplicationConfiguration

_Required_: No

_Type_: List of <a href="sqlapplicationconfigurationdefinition.md">SqlApplicationConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcConfiguration

_Required_: No

_Type_: List of <a href="vpcconfigurationdefinition.md">VpcConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

