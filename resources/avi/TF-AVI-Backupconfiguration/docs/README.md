# TF::AVI::Backupconfiguration

The BackupConfiguration resource allows the creation and management of Avi BackupConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Backupconfiguration",
    "Properties" : {
        "<a href="#awsaccesskey" title="AwsAccessKey">AwsAccessKey</a>" : <i>String</i>,
        "<a href="#awsbucketid" title="AwsBucketId">AwsBucketId</a>" : <i>String</i>,
        "<a href="#awssecretaccess" title="AwsSecretAccess">AwsSecretAccess</a>" : <i>String</i>,
        "<a href="#backupfileprefix" title="BackupFilePrefix">BackupFilePrefix</a>" : <i>String</i>,
        "<a href="#backuppassphrase" title="BackupPassphrase">BackupPassphrase</a>" : <i>String</i>,
        "<a href="#maximumbackupsstored" title="MaximumBackupsStored">MaximumBackupsStored</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#remotedirectory" title="RemoteDirectory">RemoteDirectory</a>" : <i>String</i>,
        "<a href="#remotehostname" title="RemoteHostname">RemoteHostname</a>" : <i>String</i>,
        "<a href="#savelocal" title="SaveLocal">SaveLocal</a>" : <i>Boolean</i>,
        "<a href="#sshuserref" title="SshUserRef">SshUserRef</a>" : <i>String</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#uploadtoremotehost" title="UploadToRemoteHost">UploadToRemoteHost</a>" : <i>Boolean</i>,
        "<a href="#uploadtos3" title="UploadToS3">UploadToS3</a>" : <i>Boolean</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Backupconfiguration
Properties:
    <a href="#awsaccesskey" title="AwsAccessKey">AwsAccessKey</a>: <i>String</i>
    <a href="#awsbucketid" title="AwsBucketId">AwsBucketId</a>: <i>String</i>
    <a href="#awssecretaccess" title="AwsSecretAccess">AwsSecretAccess</a>: <i>String</i>
    <a href="#backupfileprefix" title="BackupFilePrefix">BackupFilePrefix</a>: <i>String</i>
    <a href="#backuppassphrase" title="BackupPassphrase">BackupPassphrase</a>: <i>String</i>
    <a href="#maximumbackupsstored" title="MaximumBackupsStored">MaximumBackupsStored</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#remotedirectory" title="RemoteDirectory">RemoteDirectory</a>: <i>String</i>
    <a href="#remotehostname" title="RemoteHostname">RemoteHostname</a>: <i>String</i>
    <a href="#savelocal" title="SaveLocal">SaveLocal</a>: <i>Boolean</i>
    <a href="#sshuserref" title="SshUserRef">SshUserRef</a>: <i>String</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#uploadtoremotehost" title="UploadToRemoteHost">UploadToRemoteHost</a>: <i>Boolean</i>
    <a href="#uploadtos3" title="UploadToS3">UploadToS3</a>: <i>Boolean</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
</pre>

## Properties

#### AwsAccessKey

Aws access key id. Field introduced in 18.2.3. Allowed in basic edition, essentials edition, enterprise edition.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsBucketId

Aws bucket. Field introduced in 18.2.3. Allowed in basic edition, essentials edition, enterprise edition.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsSecretAccess

Aws secret access key. Field introduced in 18.2.3. Allowed in basic edition, essentials edition, enterprise edition.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupFilePrefix

Prefix of the exported configuration file. Field introduced in 17.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupPassphrase

Default passphrase for configuration export and periodic backup.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumBackupsStored

Rotate the backup files based on this count. Allowed values are 1-20.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of backup configuration.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteDirectory

Directory at remote destination with write permission for ssh user.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteHostname

Remote destination.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SaveLocal

Local backup.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshUserRef

Access credentials for remote destination. It is a reference to an object of type cloudconnectoruser.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

It is a reference to an object of type tenant.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UploadToRemoteHost

Remote backup.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UploadToS3

Cloud backup. Field introduced in 18.2.3. Allowed in basic edition, essentials edition, enterprise edition.

_Required_: No

_Type_: Boolean

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

