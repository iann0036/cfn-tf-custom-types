# TF::Aviatrix::ControllerConfig

The **aviatrix_controller_config** resource allows management of an Aviatrix Controller's configurations.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::ControllerConfig",
    "Properties" : {
        "<a href="#awsguarddutyscanninginterval" title="AwsGuardDutyScanningInterval">AwsGuardDutyScanningInterval</a>" : <i>Double</i>,
        "<a href="#backupaccountname" title="BackupAccountName">BackupAccountName</a>" : <i>String</i>,
        "<a href="#backupbucketname" title="BackupBucketName">BackupBucketName</a>" : <i>String</i>,
        "<a href="#backupcloudtype" title="BackupCloudType">BackupCloudType</a>" : <i>Double</i>,
        "<a href="#backupconfiguration" title="BackupConfiguration">BackupConfiguration</a>" : <i>Boolean</i>,
        "<a href="#backupcontainername" title="BackupContainerName">BackupContainerName</a>" : <i>String</i>,
        "<a href="#backupregion" title="BackupRegion">BackupRegion</a>" : <i>String</i>,
        "<a href="#backupstoragename" title="BackupStorageName">BackupStorageName</a>" : <i>String</i>,
        "<a href="#cacertificatefilepath" title="CaCertificateFilePath">CaCertificateFilePath</a>" : <i>String</i>,
        "<a href="#enablevpcdnsserver" title="EnableVpcDnsServer">EnableVpcDnsServer</a>" : <i>Boolean</i>,
        "<a href="#fqdnexceptionrule" title="FqdnExceptionRule">FqdnExceptionRule</a>" : <i>Boolean</i>,
        "<a href="#httpaccess" title="HttpAccess">HttpAccess</a>" : <i>Boolean</i>,
        "<a href="#multiplebackups" title="MultipleBackups">MultipleBackups</a>" : <i>Boolean</i>,
        "<a href="#securitygroupmanagement" title="SecurityGroupManagement">SecurityGroupManagement</a>" : <i>Boolean</i>,
        "<a href="#serverprivatekeyfilepath" title="ServerPrivateKeyFilePath">ServerPrivateKeyFilePath</a>" : <i>String</i>,
        "<a href="#serverpubliccertificatefilepath" title="ServerPublicCertificateFilePath">ServerPublicCertificateFilePath</a>" : <i>String</i>,
        "<a href="#sgmanagementaccountname" title="SgManagementAccountName">SgManagementAccountName</a>" : <i>String</i>,
        "<a href="#targetversion" title="TargetVersion">TargetVersion</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::ControllerConfig
Properties:
    <a href="#awsguarddutyscanninginterval" title="AwsGuardDutyScanningInterval">AwsGuardDutyScanningInterval</a>: <i>Double</i>
    <a href="#backupaccountname" title="BackupAccountName">BackupAccountName</a>: <i>String</i>
    <a href="#backupbucketname" title="BackupBucketName">BackupBucketName</a>: <i>String</i>
    <a href="#backupcloudtype" title="BackupCloudType">BackupCloudType</a>: <i>Double</i>
    <a href="#backupconfiguration" title="BackupConfiguration">BackupConfiguration</a>: <i>Boolean</i>
    <a href="#backupcontainername" title="BackupContainerName">BackupContainerName</a>: <i>String</i>
    <a href="#backupregion" title="BackupRegion">BackupRegion</a>: <i>String</i>
    <a href="#backupstoragename" title="BackupStorageName">BackupStorageName</a>: <i>String</i>
    <a href="#cacertificatefilepath" title="CaCertificateFilePath">CaCertificateFilePath</a>: <i>String</i>
    <a href="#enablevpcdnsserver" title="EnableVpcDnsServer">EnableVpcDnsServer</a>: <i>Boolean</i>
    <a href="#fqdnexceptionrule" title="FqdnExceptionRule">FqdnExceptionRule</a>: <i>Boolean</i>
    <a href="#httpaccess" title="HttpAccess">HttpAccess</a>: <i>Boolean</i>
    <a href="#multiplebackups" title="MultipleBackups">MultipleBackups</a>: <i>Boolean</i>
    <a href="#securitygroupmanagement" title="SecurityGroupManagement">SecurityGroupManagement</a>: <i>Boolean</i>
    <a href="#serverprivatekeyfilepath" title="ServerPrivateKeyFilePath">ServerPrivateKeyFilePath</a>: <i>String</i>
    <a href="#serverpubliccertificatefilepath" title="ServerPublicCertificateFilePath">ServerPublicCertificateFilePath</a>: <i>String</i>
    <a href="#sgmanagementaccountname" title="SgManagementAccountName">SgManagementAccountName</a>: <i>String</i>
    <a href="#targetversion" title="TargetVersion">TargetVersion</a>: <i>String</i>
</pre>

## Properties

#### AwsGuardDutyScanningInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupAccountName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupBucketName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupCloudType

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupConfiguration

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupContainerName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupRegion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupStorageName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaCertificateFilePath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableVpcDnsServer

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FqdnExceptionRule

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpAccess

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MultipleBackups

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupManagement

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerPrivateKeyFilePath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerPublicCertificateFilePath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SgManagementAccountName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetVersion

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

#### Version

Returns the <code>Version</code> value.

