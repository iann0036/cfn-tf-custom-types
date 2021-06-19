# TF::Aviatrix::Account

The **aviatrix_account** resource allows the creation and management of Aviatrix cloud accounts.

~> **NOTE:** With the release of Controller 5.4 (compatible with Aviatrix provider R2.13), Role-Based Access Control (RBAC) is now integrated into the Accounts workflow. Any **aviatrix_account** created in 5.3 by default will have admin privileges (attached to the 'admin' RBAC permission group). In 5.4, any new accounts created will not be attached to any RBAC group unless otherwise specified through the **aviatrix_rbac_group_access_account_attachment** resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::Account",
    "Properties" : {
        "<a href="#accountname" title="AccountName">AccountName</a>" : <i>String</i>,
        "<a href="#alicloudaccesskey" title="AlicloudAccessKey">AlicloudAccessKey</a>" : <i>String</i>,
        "<a href="#alicloudaccountid" title="AlicloudAccountId">AlicloudAccountId</a>" : <i>String</i>,
        "<a href="#alicloudsecretkey" title="AlicloudSecretKey">AlicloudSecretKey</a>" : <i>String</i>,
        "<a href="#armapplicationid" title="ArmApplicationId">ArmApplicationId</a>" : <i>String</i>,
        "<a href="#armapplicationkey" title="ArmApplicationKey">ArmApplicationKey</a>" : <i>String</i>,
        "<a href="#armdirectoryid" title="ArmDirectoryId">ArmDirectoryId</a>" : <i>String</i>,
        "<a href="#armsubscriptionid" title="ArmSubscriptionId">ArmSubscriptionId</a>" : <i>String</i>,
        "<a href="#auditaccount" title="AuditAccount">AuditAccount</a>" : <i>Boolean</i>,
        "<a href="#awsaccesskey" title="AwsAccessKey">AwsAccessKey</a>" : <i>String</i>,
        "<a href="#awsaccountnumber" title="AwsAccountNumber">AwsAccountNumber</a>" : <i>String</i>,
        "<a href="#awsgatewayroleapp" title="AwsGatewayRoleApp">AwsGatewayRoleApp</a>" : <i>String</i>,
        "<a href="#awsgatewayroleec2" title="AwsGatewayRoleEc2">AwsGatewayRoleEc2</a>" : <i>String</i>,
        "<a href="#awsiam" title="AwsIam">AwsIam</a>" : <i>Boolean</i>,
        "<a href="#awsroleapp" title="AwsRoleApp">AwsRoleApp</a>" : <i>String</i>,
        "<a href="#awsroleec2" title="AwsRoleEc2">AwsRoleEc2</a>" : <i>String</i>,
        "<a href="#awssecretkey" title="AwsSecretKey">AwsSecretKey</a>" : <i>String</i>,
        "<a href="#awschinaaccesskey" title="AwschinaAccessKey">AwschinaAccessKey</a>" : <i>String</i>,
        "<a href="#awschinaaccountnumber" title="AwschinaAccountNumber">AwschinaAccountNumber</a>" : <i>String</i>,
        "<a href="#awschinaiam" title="AwschinaIam">AwschinaIam</a>" : <i>Boolean</i>,
        "<a href="#awschinaroleapp" title="AwschinaRoleApp">AwschinaRoleApp</a>" : <i>String</i>,
        "<a href="#awschinaroleec2" title="AwschinaRoleEc2">AwschinaRoleEc2</a>" : <i>String</i>,
        "<a href="#awschinasecretkey" title="AwschinaSecretKey">AwschinaSecretKey</a>" : <i>String</i>,
        "<a href="#awsgovaccesskey" title="AwsgovAccessKey">AwsgovAccessKey</a>" : <i>String</i>,
        "<a href="#awsgovaccountnumber" title="AwsgovAccountNumber">AwsgovAccountNumber</a>" : <i>String</i>,
        "<a href="#awsgoviam" title="AwsgovIam">AwsgovIam</a>" : <i>Boolean</i>,
        "<a href="#awsgovroleapp" title="AwsgovRoleApp">AwsgovRoleApp</a>" : <i>String</i>,
        "<a href="#awsgovroleec2" title="AwsgovRoleEc2">AwsgovRoleEc2</a>" : <i>String</i>,
        "<a href="#awsgovsecretkey" title="AwsgovSecretKey">AwsgovSecretKey</a>" : <i>String</i>,
        "<a href="#azurechinaapplicationid" title="AzurechinaApplicationId">AzurechinaApplicationId</a>" : <i>String</i>,
        "<a href="#azurechinaapplicationkey" title="AzurechinaApplicationKey">AzurechinaApplicationKey</a>" : <i>String</i>,
        "<a href="#azurechinadirectoryid" title="AzurechinaDirectoryId">AzurechinaDirectoryId</a>" : <i>String</i>,
        "<a href="#azurechinasubscriptionid" title="AzurechinaSubscriptionId">AzurechinaSubscriptionId</a>" : <i>String</i>,
        "<a href="#azuregovapplicationid" title="AzuregovApplicationId">AzuregovApplicationId</a>" : <i>String</i>,
        "<a href="#azuregovapplicationkey" title="AzuregovApplicationKey">AzuregovApplicationKey</a>" : <i>String</i>,
        "<a href="#azuregovdirectoryid" title="AzuregovDirectoryId">AzuregovDirectoryId</a>" : <i>String</i>,
        "<a href="#azuregovsubscriptionid" title="AzuregovSubscriptionId">AzuregovSubscriptionId</a>" : <i>String</i>,
        "<a href="#cloudtype" title="CloudType">CloudType</a>" : <i>Double</i>,
        "<a href="#gcloudprojectcredentialsfilepath" title="GcloudProjectCredentialsFilepath">GcloudProjectCredentialsFilepath</a>" : <i>String</i>,
        "<a href="#gcloudprojectid" title="GcloudProjectId">GcloudProjectId</a>" : <i>String</i>,
        "<a href="#ociapiprivatekeyfilepath" title="OciApiPrivateKeyFilepath">OciApiPrivateKeyFilepath</a>" : <i>String</i>,
        "<a href="#ocicompartmentid" title="OciCompartmentId">OciCompartmentId</a>" : <i>String</i>,
        "<a href="#ocitenancyid" title="OciTenancyId">OciTenancyId</a>" : <i>String</i>,
        "<a href="#ociuserid" title="OciUserId">OciUserId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::Account
Properties:
    <a href="#accountname" title="AccountName">AccountName</a>: <i>String</i>
    <a href="#alicloudaccesskey" title="AlicloudAccessKey">AlicloudAccessKey</a>: <i>String</i>
    <a href="#alicloudaccountid" title="AlicloudAccountId">AlicloudAccountId</a>: <i>String</i>
    <a href="#alicloudsecretkey" title="AlicloudSecretKey">AlicloudSecretKey</a>: <i>String</i>
    <a href="#armapplicationid" title="ArmApplicationId">ArmApplicationId</a>: <i>String</i>
    <a href="#armapplicationkey" title="ArmApplicationKey">ArmApplicationKey</a>: <i>String</i>
    <a href="#armdirectoryid" title="ArmDirectoryId">ArmDirectoryId</a>: <i>String</i>
    <a href="#armsubscriptionid" title="ArmSubscriptionId">ArmSubscriptionId</a>: <i>String</i>
    <a href="#auditaccount" title="AuditAccount">AuditAccount</a>: <i>Boolean</i>
    <a href="#awsaccesskey" title="AwsAccessKey">AwsAccessKey</a>: <i>String</i>
    <a href="#awsaccountnumber" title="AwsAccountNumber">AwsAccountNumber</a>: <i>String</i>
    <a href="#awsgatewayroleapp" title="AwsGatewayRoleApp">AwsGatewayRoleApp</a>: <i>String</i>
    <a href="#awsgatewayroleec2" title="AwsGatewayRoleEc2">AwsGatewayRoleEc2</a>: <i>String</i>
    <a href="#awsiam" title="AwsIam">AwsIam</a>: <i>Boolean</i>
    <a href="#awsroleapp" title="AwsRoleApp">AwsRoleApp</a>: <i>String</i>
    <a href="#awsroleec2" title="AwsRoleEc2">AwsRoleEc2</a>: <i>String</i>
    <a href="#awssecretkey" title="AwsSecretKey">AwsSecretKey</a>: <i>String</i>
    <a href="#awschinaaccesskey" title="AwschinaAccessKey">AwschinaAccessKey</a>: <i>String</i>
    <a href="#awschinaaccountnumber" title="AwschinaAccountNumber">AwschinaAccountNumber</a>: <i>String</i>
    <a href="#awschinaiam" title="AwschinaIam">AwschinaIam</a>: <i>Boolean</i>
    <a href="#awschinaroleapp" title="AwschinaRoleApp">AwschinaRoleApp</a>: <i>String</i>
    <a href="#awschinaroleec2" title="AwschinaRoleEc2">AwschinaRoleEc2</a>: <i>String</i>
    <a href="#awschinasecretkey" title="AwschinaSecretKey">AwschinaSecretKey</a>: <i>String</i>
    <a href="#awsgovaccesskey" title="AwsgovAccessKey">AwsgovAccessKey</a>: <i>String</i>
    <a href="#awsgovaccountnumber" title="AwsgovAccountNumber">AwsgovAccountNumber</a>: <i>String</i>
    <a href="#awsgoviam" title="AwsgovIam">AwsgovIam</a>: <i>Boolean</i>
    <a href="#awsgovroleapp" title="AwsgovRoleApp">AwsgovRoleApp</a>: <i>String</i>
    <a href="#awsgovroleec2" title="AwsgovRoleEc2">AwsgovRoleEc2</a>: <i>String</i>
    <a href="#awsgovsecretkey" title="AwsgovSecretKey">AwsgovSecretKey</a>: <i>String</i>
    <a href="#azurechinaapplicationid" title="AzurechinaApplicationId">AzurechinaApplicationId</a>: <i>String</i>
    <a href="#azurechinaapplicationkey" title="AzurechinaApplicationKey">AzurechinaApplicationKey</a>: <i>String</i>
    <a href="#azurechinadirectoryid" title="AzurechinaDirectoryId">AzurechinaDirectoryId</a>: <i>String</i>
    <a href="#azurechinasubscriptionid" title="AzurechinaSubscriptionId">AzurechinaSubscriptionId</a>: <i>String</i>
    <a href="#azuregovapplicationid" title="AzuregovApplicationId">AzuregovApplicationId</a>: <i>String</i>
    <a href="#azuregovapplicationkey" title="AzuregovApplicationKey">AzuregovApplicationKey</a>: <i>String</i>
    <a href="#azuregovdirectoryid" title="AzuregovDirectoryId">AzuregovDirectoryId</a>: <i>String</i>
    <a href="#azuregovsubscriptionid" title="AzuregovSubscriptionId">AzuregovSubscriptionId</a>: <i>String</i>
    <a href="#cloudtype" title="CloudType">CloudType</a>: <i>Double</i>
    <a href="#gcloudprojectcredentialsfilepath" title="GcloudProjectCredentialsFilepath">GcloudProjectCredentialsFilepath</a>: <i>String</i>
    <a href="#gcloudprojectid" title="GcloudProjectId">GcloudProjectId</a>: <i>String</i>
    <a href="#ociapiprivatekeyfilepath" title="OciApiPrivateKeyFilepath">OciApiPrivateKeyFilepath</a>: <i>String</i>
    <a href="#ocicompartmentid" title="OciCompartmentId">OciCompartmentId</a>: <i>String</i>
    <a href="#ocitenancyid" title="OciTenancyId">OciTenancyId</a>: <i>String</i>
    <a href="#ociuserid" title="OciUserId">OciUserId</a>: <i>String</i>
</pre>

## Properties

#### AccountName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlicloudAccessKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlicloudAccountId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlicloudSecretKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ArmApplicationId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ArmApplicationKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ArmDirectoryId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ArmSubscriptionId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuditAccount

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsAccessKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsAccountNumber

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsGatewayRoleApp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsGatewayRoleEc2

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsIam

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsRoleApp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsRoleEc2

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsSecretKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwschinaAccessKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwschinaAccountNumber

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwschinaIam

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwschinaRoleApp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwschinaRoleEc2

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwschinaSecretKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsgovAccessKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsgovAccountNumber

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsgovIam

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsgovRoleApp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsgovRoleEc2

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsgovSecretKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzurechinaApplicationId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzurechinaApplicationKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzurechinaDirectoryId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzurechinaSubscriptionId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzuregovApplicationId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzuregovApplicationKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzuregovDirectoryId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzuregovSubscriptionId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudType

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcloudProjectCredentialsFilepath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcloudProjectId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OciApiPrivateKeyFilepath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OciCompartmentId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OciTenancyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OciUserId

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

