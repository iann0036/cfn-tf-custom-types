# TF::AzureStack::VirtualMachine OsProfileWindowsConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enableautomaticupgrades" title="EnableAutomaticUpgrades">EnableAutomaticUpgrades</a>" : <i>Boolean</i>,
    "<a href="#provisionvmagent" title="ProvisionVmAgent">ProvisionVmAgent</a>" : <i>Boolean</i>,
    "<a href="#additionalunattendconfig" title="AdditionalUnattendConfig">AdditionalUnattendConfig</a>" : <i>[ <a href="additionalunattendconfigdefinition.md">AdditionalUnattendConfigDefinition</a>, ... ]</i>,
    "<a href="#winrm" title="Winrm">Winrm</a>" : <i>[ <a href="winrmdefinition.md">WinrmDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enableautomaticupgrades" title="EnableAutomaticUpgrades">EnableAutomaticUpgrades</a>: <i>Boolean</i>
<a href="#provisionvmagent" title="ProvisionVmAgent">ProvisionVmAgent</a>: <i>Boolean</i>
<a href="#additionalunattendconfig" title="AdditionalUnattendConfig">AdditionalUnattendConfig</a>: <i>
      - <a href="additionalunattendconfigdefinition.md">AdditionalUnattendConfigDefinition</a></i>
<a href="#winrm" title="Winrm">Winrm</a>: <i>
      - <a href="winrmdefinition.md">WinrmDefinition</a></i>
</pre>

## Properties

#### EnableAutomaticUpgrades

This value defaults to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProvisionVmAgent

This value defaults to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalUnattendConfig

_Required_: No

_Type_: List of <a href="additionalunattendconfigdefinition.md">AdditionalUnattendConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Winrm

_Required_: No

_Type_: List of <a href="winrmdefinition.md">WinrmDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

