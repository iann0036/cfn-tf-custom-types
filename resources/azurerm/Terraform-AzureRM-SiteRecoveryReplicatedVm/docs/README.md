# Terraform::AzureRM::SiteRecoveryReplicatedVm

CloudFormation equivalent of azurerm_site_recovery_replicated_vm

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::SiteRecoveryReplicatedVm",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#manageddisk" title="ManagedDisk">ManagedDisk</a>" : <i>[ &lt;a href=&#34;manageddisk.md&#34;&gt;ManagedDisk&lt;/a&gt;, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#recoveryreplicationpolicyid" title="RecoveryReplicationPolicyId">RecoveryReplicationPolicyId</a>" : <i>String</i>,
        "<a href="#recoveryvaultname" title="RecoveryVaultName">RecoveryVaultName</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#sourcerecoveryfabricname" title="SourceRecoveryFabricName">SourceRecoveryFabricName</a>" : <i>String</i>,
        "<a href="#sourcerecoveryprotectioncontainername" title="SourceRecoveryProtectionContainerName">SourceRecoveryProtectionContainerName</a>" : <i>String</i>,
        "<a href="#sourcevmid" title="SourceVmId">SourceVmId</a>" : <i>String</i>,
        "<a href="#targetavailabilitysetid" title="TargetAvailabilitySetId">TargetAvailabilitySetId</a>" : <i>String</i>,
        "<a href="#targetrecoveryfabricid" title="TargetRecoveryFabricId">TargetRecoveryFabricId</a>" : <i>String</i>,
        "<a href="#targetrecoveryprotectioncontainerid" title="TargetRecoveryProtectionContainerId">TargetRecoveryProtectionContainerId</a>" : <i>String</i>,
        "<a href="#targetresourcegroupid" title="TargetResourceGroupId">TargetResourceGroupId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::SiteRecoveryReplicatedVm
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#manageddisk" title="ManagedDisk">ManagedDisk</a>: <i>
      - &lt;a href=&#34;manageddisk.md&#34;&gt;ManagedDisk&lt;/a&gt;</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#recoveryreplicationpolicyid" title="RecoveryReplicationPolicyId">RecoveryReplicationPolicyId</a>: <i>String</i>
    <a href="#recoveryvaultname" title="RecoveryVaultName">RecoveryVaultName</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#sourcerecoveryfabricname" title="SourceRecoveryFabricName">SourceRecoveryFabricName</a>: <i>String</i>
    <a href="#sourcerecoveryprotectioncontainername" title="SourceRecoveryProtectionContainerName">SourceRecoveryProtectionContainerName</a>: <i>String</i>
    <a href="#sourcevmid" title="SourceVmId">SourceVmId</a>: <i>String</i>
    <a href="#targetavailabilitysetid" title="TargetAvailabilitySetId">TargetAvailabilitySetId</a>: <i>String</i>
    <a href="#targetrecoveryfabricid" title="TargetRecoveryFabricId">TargetRecoveryFabricId</a>: <i>String</i>
    <a href="#targetrecoveryprotectioncontainerid" title="TargetRecoveryProtectionContainerId">TargetRecoveryProtectionContainerId</a>: <i>String</i>
    <a href="#targetresourcegroupid" title="TargetResourceGroupId">TargetResourceGroupId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedDisk

_Required_: No

_Type_: List of &lt;a href=&#34;manageddisk.md&#34;&gt;ManagedDisk&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecoveryReplicationPolicyId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecoveryVaultName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceRecoveryFabricName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceRecoveryProtectionContainerName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceVmId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetAvailabilitySetId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetRecoveryFabricId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetRecoveryProtectionContainerId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetResourceGroupId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

