# TF::AVI::Backup

The Backup resource allows the creation and management of Avi Backup

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Backup",
    "Properties" : {
        "<a href="#backupconfigref" title="BackupConfigRef">BackupConfigRef</a>" : <i>String</i>,
        "<a href="#filename" title="FileName">FileName</a>" : <i>String</i>,
        "<a href="#localfileurl" title="LocalFileUrl">LocalFileUrl</a>" : <i>String</i>,
        "<a href="#remotefileurl" title="RemoteFileUrl">RemoteFileUrl</a>" : <i>String</i>,
        "<a href="#schedulerref" title="SchedulerRef">SchedulerRef</a>" : <i>String</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#timestamp" title="Timestamp">Timestamp</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Backup
Properties:
    <a href="#backupconfigref" title="BackupConfigRef">BackupConfigRef</a>: <i>String</i>
    <a href="#filename" title="FileName">FileName</a>: <i>String</i>
    <a href="#localfileurl" title="LocalFileUrl">LocalFileUrl</a>: <i>String</i>
    <a href="#remotefileurl" title="RemoteFileUrl">RemoteFileUrl</a>: <i>String</i>
    <a href="#schedulerref" title="SchedulerRef">SchedulerRef</a>: <i>String</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#timestamp" title="Timestamp">Timestamp</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
</pre>

## Properties

#### BackupConfigRef

Backupconfiguration information. It is a reference to an object of type backupconfiguration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileName

The file name of backup.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalFileUrl

Url to download the backup file.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteFileUrl

Url to download the backup file.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SchedulerRef

Scheduler information. It is a reference to an object of type scheduler.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

It is a reference to an object of type tenant.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timestamp

Unix timestamp of when the backup file is created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

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

