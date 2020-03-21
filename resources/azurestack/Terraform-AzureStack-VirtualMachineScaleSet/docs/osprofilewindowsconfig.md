# Terraform::AzureStack::VirtualMachineScaleSet OsProfileWindowsConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enableautomaticupgrades" title="EnableAutomaticUpgrades">EnableAutomaticUpgrades</a>" : <i>Boolean</i>,
    "<a href="#provisionvmagent" title="ProvisionVmAgent">ProvisionVmAgent</a>" : <i>Boolean</i>,
    "<a href="#additionalunattendconfig" title="AdditionalUnattendConfig">AdditionalUnattendConfig</a>" : <i>[ &lt;a href=&#34;osprofilewindowsconfig-additionalunattendconfig.md&#34;&gt;AdditionalUnattendConfig&lt;/a&gt;, ... ]</i>,
    "<a href="#winrm" title="Winrm">Winrm</a>" : <i>[ &lt;a href=&#34;osprofilewindowsconfig-winrm.md&#34;&gt;Winrm&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enableautomaticupgrades" title="EnableAutomaticUpgrades">EnableAutomaticUpgrades</a>: <i>Boolean</i>
<a href="#provisionvmagent" title="ProvisionVmAgent">ProvisionVmAgent</a>: <i>Boolean</i>
<a href="#additionalunattendconfig" title="AdditionalUnattendConfig">AdditionalUnattendConfig</a>: <i>
      - &lt;a href=&#34;osprofilewindowsconfig-additionalunattendconfig.md&#34;&gt;AdditionalUnattendConfig&lt;/a&gt;</i>
<a href="#winrm" title="Winrm">Winrm</a>: <i>
      - &lt;a href=&#34;osprofilewindowsconfig-winrm.md&#34;&gt;Winrm&lt;/a&gt;</i>
</pre>

## Properties

#### EnableAutomaticUpgrades

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProvisionVmAgent

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalUnattendConfig

_Required_: No
_Type_: List of &lt;a href=&#34;osprofilewindowsconfig-additionalunattendconfig.md&#34;&gt;AdditionalUnattendConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Winrm

_Required_: No
_Type_: List of &lt;a href=&#34;osprofilewindowsconfig-winrm.md&#34;&gt;Winrm&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

