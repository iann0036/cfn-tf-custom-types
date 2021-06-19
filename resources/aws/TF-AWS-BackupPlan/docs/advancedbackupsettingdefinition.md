# TF::AWS::BackupPlan AdvancedBackupSettingDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#backupoptions" title="BackupOptions">BackupOptions</a>" : <i>[ <a href="backupoptionsdefinition.md">BackupOptionsDefinition</a>, ... ]</i>,
    "<a href="#resourcetype" title="ResourceType">ResourceType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#backupoptions" title="BackupOptions">BackupOptions</a>: <i>
      - <a href="backupoptionsdefinition.md">BackupOptionsDefinition</a></i>
<a href="#resourcetype" title="ResourceType">ResourceType</a>: <i>String</i>
</pre>

## Properties

#### BackupOptions

_Required_: Yes

_Type_: List of <a href="backupoptionsdefinition.md">BackupOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

