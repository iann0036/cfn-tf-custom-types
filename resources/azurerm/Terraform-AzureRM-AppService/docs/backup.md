# Terraform::AzureRM::AppService Backup

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#storageaccounturl" title="StorageAccountUrl">StorageAccountUrl</a>" : <i>String</i>,
    "<a href="#schedule" title="Schedule">Schedule</a>" : <i>[ <a href="backup-schedule.md">Schedule</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#storageaccounturl" title="StorageAccountUrl">StorageAccountUrl</a>: <i>String</i>
<a href="#schedule" title="Schedule">Schedule</a>: <i>
      - <a href="backup-schedule.md">Schedule</a></i>
</pre>

## Properties

#### Enabled

Is this Backup enabled?.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountUrl

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

_Required_: No

_Type_: List of <a href="backup-schedule.md">Schedule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

