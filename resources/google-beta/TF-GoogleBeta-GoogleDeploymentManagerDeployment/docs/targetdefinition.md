# TF::GoogleBeta::GoogleDeploymentManagerDeployment TargetDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#config" title="Config">Config</a>" : <i>[ <a href="configdefinition.md">ConfigDefinition</a>, ... ]</i>,
    "<a href="#imports" title="Imports">Imports</a>" : <i>[ <a href="importsdefinition.md">ImportsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#config" title="Config">Config</a>: <i>
      - <a href="configdefinition.md">ConfigDefinition</a></i>
<a href="#imports" title="Imports">Imports</a>: <i>
      - <a href="importsdefinition.md">ImportsDefinition</a></i>
</pre>

## Properties

#### Config

_Required_: No

_Type_: List of <a href="configdefinition.md">ConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Imports

_Required_: No

_Type_: List of <a href="importsdefinition.md">ImportsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

