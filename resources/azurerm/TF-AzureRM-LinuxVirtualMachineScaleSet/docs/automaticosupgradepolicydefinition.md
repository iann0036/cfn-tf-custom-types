# TF::AzureRM::LinuxVirtualMachineScaleSet AutomaticOsUpgradePolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#disableautomaticrollback" title="DisableAutomaticRollback">DisableAutomaticRollback</a>" : <i>Boolean</i>,
    "<a href="#enableautomaticosupgrade" title="EnableAutomaticOsUpgrade">EnableAutomaticOsUpgrade</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#disableautomaticrollback" title="DisableAutomaticRollback">DisableAutomaticRollback</a>: <i>Boolean</i>
<a href="#enableautomaticosupgrade" title="EnableAutomaticOsUpgrade">EnableAutomaticOsUpgrade</a>: <i>Boolean</i>
</pre>

## Properties

#### DisableAutomaticRollback

Should automatic rollbacks be disabled?.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableAutomaticOsUpgrade

Should OS Upgrades automatically be applied to Scale Set instances in a rolling fashion when a newer version of the OS Image becomes available?.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

