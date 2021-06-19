# TF::GoogleBeta::GoogleOsConfigPatchDeployment PostStepDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#linuxexecstepconfig" title="LinuxExecStepConfig">LinuxExecStepConfig</a>" : <i>[ <a href="linuxexecstepconfigdefinition.md">LinuxExecStepConfigDefinition</a>, ... ]</i>,
    "<a href="#windowsexecstepconfig" title="WindowsExecStepConfig">WindowsExecStepConfig</a>" : <i>[ <a href="windowsexecstepconfigdefinition.md">WindowsExecStepConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#linuxexecstepconfig" title="LinuxExecStepConfig">LinuxExecStepConfig</a>: <i>
      - <a href="linuxexecstepconfigdefinition.md">LinuxExecStepConfigDefinition</a></i>
<a href="#windowsexecstepconfig" title="WindowsExecStepConfig">WindowsExecStepConfig</a>: <i>
      - <a href="windowsexecstepconfigdefinition.md">WindowsExecStepConfigDefinition</a></i>
</pre>

## Properties

#### LinuxExecStepConfig

_Required_: No

_Type_: List of <a href="linuxexecstepconfigdefinition.md">LinuxExecStepConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WindowsExecStepConfig

_Required_: No

_Type_: List of <a href="windowsexecstepconfigdefinition.md">WindowsExecStepConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

