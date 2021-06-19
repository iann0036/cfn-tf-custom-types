# TF::Rancher2::ClusterTemplate BackupConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#intervalhours" title="IntervalHours">IntervalHours</a>" : <i>Double</i>,
    "<a href="#retention" title="Retention">Retention</a>" : <i>Double</i>,
    "<a href="#safetimestamp" title="SafeTimestamp">SafeTimestamp</a>" : <i>Boolean</i>,
    "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
    "<a href="#s3backupconfig" title="S3BackupConfig">S3BackupConfig</a>" : <i>[ <a href="s3backupconfigdefinition.md">S3BackupConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#intervalhours" title="IntervalHours">IntervalHours</a>: <i>Double</i>
<a href="#retention" title="Retention">Retention</a>: <i>Double</i>
<a href="#safetimestamp" title="SafeTimestamp">SafeTimestamp</a>: <i>Boolean</i>
<a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
<a href="#s3backupconfig" title="S3BackupConfig">S3BackupConfig</a>: <i>
      - <a href="s3backupconfigdefinition.md">S3BackupConfigDefinition</a></i>
</pre>

## Properties

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntervalHours

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Retention

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SafeTimestamp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3BackupConfig

_Required_: No

_Type_: List of <a href="s3backupconfigdefinition.md">S3BackupConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

