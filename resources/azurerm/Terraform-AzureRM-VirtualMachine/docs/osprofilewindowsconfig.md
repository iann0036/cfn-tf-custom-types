# Terraform::AzureRM::VirtualMachine OsProfileWindowsConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enableautomaticupgrades" title="EnableAutomaticUpgrades">EnableAutomaticUpgrades</a>" : <i>Boolean</i>,
    "<a href="#provisionvmagent" title="ProvisionVmAgent">ProvisionVmAgent</a>" : <i>Boolean</i>,
    "<a href="#timezone" title="Timezone">Timezone</a>" : <i>String</i>,
    "<a href="#additionalunattendconfig" title="AdditionalUnattendConfig">AdditionalUnattendConfig</a>" : <i>[ <a href="osprofilewindowsconfig-additionalunattendconfig.md">AdditionalUnattendConfig</a>, ... ]</i>,
    "<a href="#winrm" title="Winrm">Winrm</a>" : <i>[ <a href="osprofilewindowsconfig-winrm.md">Winrm</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enableautomaticupgrades" title="EnableAutomaticUpgrades">EnableAutomaticUpgrades</a>: <i>Boolean</i>
<a href="#provisionvmagent" title="ProvisionVmAgent">ProvisionVmAgent</a>: <i>Boolean</i>
<a href="#timezone" title="Timezone">Timezone</a>: <i>String</i>
<a href="#additionalunattendconfig" title="AdditionalUnattendConfig">AdditionalUnattendConfig</a>: <i>
      - <a href="osprofilewindowsconfig-additionalunattendconfig.md">AdditionalUnattendConfig</a></i>
<a href="#winrm" title="Winrm">Winrm</a>: <i>
      - <a href="osprofilewindowsconfig-winrm.md">Winrm</a></i>
</pre>

## Properties

#### EnableAutomaticUpgrades

Are automatic updates enabled on this Virtual Machine? Defaults to `false.`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProvisionVmAgent

Should the Azure Virtual Machine Guest Agent be installed on this Virtual Machine? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timezone

Specifies the time zone of the virtual machine, [the possible values are defined here](http://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalUnattendConfig

_Required_: No

_Type_: List of <a href="osprofilewindowsconfig-additionalunattendconfig.md">AdditionalUnattendConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Winrm

_Required_: No

_Type_: List of <a href="osprofilewindowsconfig-winrm.md">Winrm</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

