# TF::AzureRM::SiteRecoveryNetworkMapping

Manages a site recovery network mapping on Azure. A network mapping decides how to translate connected netwroks when a VM is migrated from one region to another.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::SiteRecoveryNetworkMapping",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#recoveryvaultname" title="RecoveryVaultName">RecoveryVaultName</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#sourcenetworkid" title="SourceNetworkId">SourceNetworkId</a>" : <i>String</i>,
        "<a href="#sourcerecoveryfabricname" title="SourceRecoveryFabricName">SourceRecoveryFabricName</a>" : <i>String</i>,
        "<a href="#targetnetworkid" title="TargetNetworkId">TargetNetworkId</a>" : <i>String</i>,
        "<a href="#targetrecoveryfabricname" title="TargetRecoveryFabricName">TargetRecoveryFabricName</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::SiteRecoveryNetworkMapping
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#recoveryvaultname" title="RecoveryVaultName">RecoveryVaultName</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#sourcenetworkid" title="SourceNetworkId">SourceNetworkId</a>: <i>String</i>
    <a href="#sourcerecoveryfabricname" title="SourceRecoveryFabricName">SourceRecoveryFabricName</a>: <i>String</i>
    <a href="#targetnetworkid" title="TargetNetworkId">TargetNetworkId</a>: <i>String</i>
    <a href="#targetrecoveryfabricname" title="TargetRecoveryFabricName">TargetRecoveryFabricName</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Name

The name of the network mapping.

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

#### SourceNetworkId

The id of the primary network.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceRecoveryFabricName

Specifies the ASR fabric where mapping should be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetNetworkId

The id of the recovery network.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetRecoveryFabricName

The Azure Site Recovery fabric object corresponding to the recovery Azure region.

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

