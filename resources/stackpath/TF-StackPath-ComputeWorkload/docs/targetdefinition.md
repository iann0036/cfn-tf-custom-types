# TF::StackPath::ComputeWorkload TargetDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#deploymentscope" title="DeploymentScope">DeploymentScope</a>" : <i>String</i>,
    "<a href="#maxreplicas" title="MaxReplicas">MaxReplicas</a>" : <i>Double</i>,
    "<a href="#minreplicas" title="MinReplicas">MinReplicas</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#scalesettings" title="ScaleSettings">ScaleSettings</a>" : <i>[ <a href="scalesettingsdefinition.md">ScaleSettingsDefinition</a>, ... ]</i>,
    "<a href="#selector" title="Selector">Selector</a>" : <i>[ <a href="selectordefinition.md">SelectorDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#deploymentscope" title="DeploymentScope">DeploymentScope</a>: <i>String</i>
<a href="#maxreplicas" title="MaxReplicas">MaxReplicas</a>: <i>Double</i>
<a href="#minreplicas" title="MinReplicas">MinReplicas</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#scalesettings" title="ScaleSettings">ScaleSettings</a>: <i>
      - <a href="scalesettingsdefinition.md">ScaleSettingsDefinition</a></i>
<a href="#selector" title="Selector">Selector</a>: <i>
      - <a href="selectordefinition.md">SelectorDefinition</a></i>
</pre>

## Properties

#### DeploymentScope

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxReplicas

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinReplicas

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleSettings

_Required_: No

_Type_: List of <a href="scalesettingsdefinition.md">ScaleSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Selector

_Required_: No

_Type_: List of <a href="selectordefinition.md">SelectorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

