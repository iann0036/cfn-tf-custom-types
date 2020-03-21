# Terraform::OCI::DatabaseDbHome Database DbBackupConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autobackupenabled" title="AutoBackupEnabled">AutoBackupEnabled</a>" : <i>Boolean</i>,
    "<a href="#autobackupwindow" title="AutoBackupWindow">AutoBackupWindow</a>" : <i>String</i>,
    "<a href="#recoverywindowindays" title="RecoveryWindowInDays">RecoveryWindowInDays</a>" : <i>Double</i>,
    "<a href="#backupdestinationdetails" title="BackupDestinationDetails">BackupDestinationDetails</a>" : <i>[ <a href="database-dbbackupconfig-backupdestinationdetails.md">BackupDestinationDetails</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#autobackupenabled" title="AutoBackupEnabled">AutoBackupEnabled</a>: <i>Boolean</i>
<a href="#autobackupwindow" title="AutoBackupWindow">AutoBackupWindow</a>: <i>String</i>
<a href="#recoverywindowindays" title="RecoveryWindowInDays">RecoveryWindowInDays</a>: <i>Double</i>
<a href="#backupdestinationdetails" title="BackupDestinationDetails">BackupDestinationDetails</a>: <i>
      - <a href="database-dbbackupconfig-backupdestinationdetails.md">BackupDestinationDetails</a></i>
</pre>

## Properties

#### AutoBackupEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoBackupWindow

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecoveryWindowInDays

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupDestinationDetails

_Required_: No

_Type_: List of <a href="database-dbbackupconfig-backupdestinationdetails.md">BackupDestinationDetails</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

