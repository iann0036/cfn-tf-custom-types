# TF::AzureRM::SiteRecoveryProtectionContainerMapping

Manages a Azure recovery vault protection container mapping. A protection container mapping decides how to translate the protection container when a VM is migrated from one region to another.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::SiteRecoveryProtectionContainerMapping",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#recoveryfabricname" title="RecoveryFabricName">RecoveryFabricName</a>" : <i>String</i>,
        "<a href="#recoveryreplicationpolicyid" title="RecoveryReplicationPolicyId">RecoveryReplicationPolicyId</a>" : <i>String</i>,
        "<a href="#recoverysourceprotectioncontainername" title="RecoverySourceProtectionContainerName">RecoverySourceProtectionContainerName</a>" : <i>String</i>,
        "<a href="#recoverytargetprotectioncontainerid" title="RecoveryTargetProtectionContainerId">RecoveryTargetProtectionContainerId</a>" : <i>String</i>,
        "<a href="#recoveryvaultname" title="RecoveryVaultName">RecoveryVaultName</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::SiteRecoveryProtectionContainerMapping
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#recoveryfabricname" title="RecoveryFabricName">RecoveryFabricName</a>: <i>String</i>
    <a href="#recoveryreplicationpolicyid" title="RecoveryReplicationPolicyId">RecoveryReplicationPolicyId</a>: <i>String</i>
    <a href="#recoverysourceprotectioncontainername" title="RecoverySourceProtectionContainerName">RecoverySourceProtectionContainerName</a>: <i>String</i>
    <a href="#recoverytargetprotectioncontainerid" title="RecoveryTargetProtectionContainerId">RecoveryTargetProtectionContainerId</a>: <i>String</i>
    <a href="#recoveryvaultname" title="RecoveryVaultName">RecoveryVaultName</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Name

The name of the network mapping.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecoveryFabricName

Name of fabric that should contains the protection container to map.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecoveryReplicationPolicyId

Id of the policy to use for this mapping.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecoverySourceProtectionContainerName

Name of the source protection container to map.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecoveryTargetProtectionContainerId

Id of target protection container to map to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecoveryVaultName

The name of the vault that should be updated.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

Name of the resource group where the vault that should be updated is located.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

