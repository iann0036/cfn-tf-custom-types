# Terraform::AzureRM::BackupPolicyVm

CloudFormation equivalent of azurerm_backup_policy_vm

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::BackupPolicyVm",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#recoveryvaultname" title="RecoveryVaultName">RecoveryVaultName</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#timezone" title="Timezone">Timezone</a>" : <i>String</i>,
        "<a href="#backup" title="Backup">Backup</a>" : <i>[ <a href="backup.md">Backup</a>, ... ]</i>,
        "<a href="#retentiondaily" title="RetentionDaily">RetentionDaily</a>" : <i>[ <a href="retentiondaily.md">RetentionDaily</a>, ... ]</i>,
        "<a href="#retentionmonthly" title="RetentionMonthly">RetentionMonthly</a>" : <i>[ <a href="retentionmonthly.md">RetentionMonthly</a>, ... ]</i>,
        "<a href="#retentionweekly" title="RetentionWeekly">RetentionWeekly</a>" : <i>[ <a href="retentionweekly.md">RetentionWeekly</a>, ... ]</i>,
        "<a href="#retentionyearly" title="RetentionYearly">RetentionYearly</a>" : <i>[ <a href="retentionyearly.md">RetentionYearly</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::BackupPolicyVm
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#recoveryvaultname" title="RecoveryVaultName">RecoveryVaultName</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#timezone" title="Timezone">Timezone</a>: <i>String</i>
    <a href="#backup" title="Backup">Backup</a>: <i>
      - <a href="backup.md">Backup</a></i>
    <a href="#retentiondaily" title="RetentionDaily">RetentionDaily</a>: <i>
      - <a href="retentiondaily.md">RetentionDaily</a></i>
    <a href="#retentionmonthly" title="RetentionMonthly">RetentionMonthly</a>: <i>
      - <a href="retentionmonthly.md">RetentionMonthly</a></i>
    <a href="#retentionweekly" title="RetentionWeekly">RetentionWeekly</a>: <i>
      - <a href="retentionweekly.md">RetentionWeekly</a></i>
    <a href="#retentionyearly" title="RetentionYearly">RetentionYearly</a>: <i>
      - <a href="retentionyearly.md">RetentionYearly</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Name

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

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timezone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backup

_Required_: No

_Type_: List of <a href="backup.md">Backup</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionDaily

_Required_: No

_Type_: List of <a href="retentiondaily.md">RetentionDaily</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionMonthly

_Required_: No

_Type_: List of <a href="retentionmonthly.md">RetentionMonthly</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionWeekly

_Required_: No

_Type_: List of <a href="retentionweekly.md">RetentionWeekly</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionYearly

_Required_: No

_Type_: List of <a href="retentionyearly.md">RetentionYearly</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

