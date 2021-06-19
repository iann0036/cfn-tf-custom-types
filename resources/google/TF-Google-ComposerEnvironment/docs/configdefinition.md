# TF::Google::ComposerEnvironment ConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#nodecount" title="NodeCount">NodeCount</a>" : <i>Double</i>,
    "<a href="#nodeconfig" title="NodeConfig">NodeConfig</a>" : <i>[ <a href="nodeconfigdefinition.md">NodeConfigDefinition</a>, ... ]</i>,
    "<a href="#privateenvironmentconfig" title="PrivateEnvironmentConfig">PrivateEnvironmentConfig</a>" : <i>[ <a href="privateenvironmentconfigdefinition.md">PrivateEnvironmentConfigDefinition</a>, ... ]</i>,
    "<a href="#softwareconfig" title="SoftwareConfig">SoftwareConfig</a>" : <i>[ <a href="softwareconfigdefinition.md">SoftwareConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#nodecount" title="NodeCount">NodeCount</a>: <i>Double</i>
<a href="#nodeconfig" title="NodeConfig">NodeConfig</a>: <i>
      - <a href="nodeconfigdefinition.md">NodeConfigDefinition</a></i>
<a href="#privateenvironmentconfig" title="PrivateEnvironmentConfig">PrivateEnvironmentConfig</a>: <i>
      - <a href="privateenvironmentconfigdefinition.md">PrivateEnvironmentConfigDefinition</a></i>
<a href="#softwareconfig" title="SoftwareConfig">SoftwareConfig</a>: <i>
      - <a href="softwareconfigdefinition.md">SoftwareConfigDefinition</a></i>
</pre>

## Properties

#### NodeCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeConfig

_Required_: No

_Type_: List of <a href="nodeconfigdefinition.md">NodeConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateEnvironmentConfig

_Required_: No

_Type_: List of <a href="privateenvironmentconfigdefinition.md">PrivateEnvironmentConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SoftwareConfig

_Required_: No

_Type_: List of <a href="softwareconfigdefinition.md">SoftwareConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

