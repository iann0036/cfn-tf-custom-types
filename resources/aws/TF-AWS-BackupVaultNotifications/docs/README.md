# TF::AWS::BackupVaultNotifications

Provides an AWS Backup vault notifications resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::BackupVaultNotifications",
    "Properties" : {
        "<a href="#backupvaultevents" title="BackupVaultEvents">BackupVaultEvents</a>" : <i>[ String, ... ]</i>,
        "<a href="#backupvaultname" title="BackupVaultName">BackupVaultName</a>" : <i>String</i>,
        "<a href="#snstopicarn" title="SnsTopicArn">SnsTopicArn</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::BackupVaultNotifications
Properties:
    <a href="#backupvaultevents" title="BackupVaultEvents">BackupVaultEvents</a>: <i>
      - String</i>
    <a href="#backupvaultname" title="BackupVaultName">BackupVaultName</a>: <i>String</i>
    <a href="#snstopicarn" title="SnsTopicArn">SnsTopicArn</a>: <i>String</i>
</pre>

## Properties

#### BackupVaultEvents

An array of events that indicate the status of jobs to back up resources to the backup vault.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupVaultName

Name of the backup vault to add notifications for.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnsTopicArn

The Amazon Resource Name (ARN) that specifies the topic for a backup vault’s events.

_Required_: Yes

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

#### BackupVaultArn

Returns the <code>BackupVaultArn</code> value.

#### Id

Returns the <code>Id</code> value.

