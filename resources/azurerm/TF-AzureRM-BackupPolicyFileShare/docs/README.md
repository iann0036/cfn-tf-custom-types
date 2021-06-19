# TF::AzureRM::BackupPolicyFileShare

Manages an Azure File Share Backup Policy within a Recovery Services vault.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::BackupPolicyFileShare",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#recoveryvaultname" title="RecoveryVaultName">RecoveryVaultName</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#timezone" title="Timezone">Timezone</a>" : <i>String</i>,
        "<a href="#backup" title="Backup">Backup</a>" : <i>[ <a href="backupdefinition.md">BackupDefinition</a>, ... ]</i>,
        "<a href="#retentiondaily" title="RetentionDaily">RetentionDaily</a>" : <i>[ <a href="retentiondailydefinition.md">RetentionDailyDefinition</a>, ... ]</i>,
        "<a href="#retentionmonthly" title="RetentionMonthly">RetentionMonthly</a>" : <i>[ <a href="retentionmonthlydefinition.md">RetentionMonthlyDefinition</a>, ... ]</i>,
        "<a href="#retentionweekly" title="RetentionWeekly">RetentionWeekly</a>" : <i>[ <a href="retentionweeklydefinition.md">RetentionWeeklyDefinition</a>, ... ]</i>,
        "<a href="#retentionyearly" title="RetentionYearly">RetentionYearly</a>" : <i>[ <a href="retentionyearlydefinition.md">RetentionYearlyDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::BackupPolicyFileShare
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#recoveryvaultname" title="RecoveryVaultName">RecoveryVaultName</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#timezone" title="Timezone">Timezone</a>: <i>String</i>
    <a href="#backup" title="Backup">Backup</a>: <i>
      - <a href="backupdefinition.md">BackupDefinition</a></i>
    <a href="#retentiondaily" title="RetentionDaily">RetentionDaily</a>: <i>
      - <a href="retentiondailydefinition.md">RetentionDailyDefinition</a></i>
    <a href="#retentionmonthly" title="RetentionMonthly">RetentionMonthly</a>: <i>
      - <a href="retentionmonthlydefinition.md">RetentionMonthlyDefinition</a></i>
    <a href="#retentionweekly" title="RetentionWeekly">RetentionWeekly</a>: <i>
      - <a href="retentionweeklydefinition.md">RetentionWeeklyDefinition</a></i>
    <a href="#retentionyearly" title="RetentionYearly">RetentionYearly</a>: <i>
      - <a href="retentionyearlydefinition.md">RetentionYearlyDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Name

Specifies the name of the policy. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecoveryVaultName

Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to create the policy. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timezone

Specifies the timezone. [the possible values are defined here](http://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/). Defaults to `UTC`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backup

_Required_: No

_Type_: List of <a href="backupdefinition.md">BackupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionDaily

_Required_: No

_Type_: List of <a href="retentiondailydefinition.md">RetentionDailyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionMonthly

_Required_: No

_Type_: List of <a href="retentionmonthlydefinition.md">RetentionMonthlyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionWeekly

_Required_: No

_Type_: List of <a href="retentionweeklydefinition.md">RetentionWeeklyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionYearly

_Required_: No

_Type_: List of <a href="retentionyearlydefinition.md">RetentionYearlyDefinition</a>

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

