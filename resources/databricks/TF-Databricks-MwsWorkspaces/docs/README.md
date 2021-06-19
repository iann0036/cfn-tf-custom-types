# TF::Databricks::MwsWorkspaces

CloudFormation equivalent of databricks_mws_workspaces

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Databricks::MwsWorkspaces",
    "Properties" : {
        "<a href="#accountid" title="AccountId">AccountId</a>" : <i>String</i>,
        "<a href="#awsregion" title="AwsRegion">AwsRegion</a>" : <i>String</i>,
        "<a href="#creationtime" title="CreationTime">CreationTime</a>" : <i>Double</i>,
        "<a href="#credentialsid" title="CredentialsId">CredentialsId</a>" : <i>String</i>,
        "<a href="#customermanagedkeyid" title="CustomerManagedKeyId">CustomerManagedKeyId</a>" : <i>String</i>,
        "<a href="#deploymentname" title="DeploymentName">DeploymentName</a>" : <i>String</i>,
        "<a href="#isnopublicipenabled" title="IsNoPublicIpEnabled">IsNoPublicIpEnabled</a>" : <i>Boolean</i>,
        "<a href="#managedservicescustomermanagedkeyid" title="ManagedServicesCustomerManagedKeyId">ManagedServicesCustomerManagedKeyId</a>" : <i>String</i>,
        "<a href="#networkid" title="NetworkId">NetworkId</a>" : <i>String</i>,
        "<a href="#pricingtier" title="PricingTier">PricingTier</a>" : <i>String</i>,
        "<a href="#privateaccesssettingsid" title="PrivateAccessSettingsId">PrivateAccessSettingsId</a>" : <i>String</i>,
        "<a href="#storageconfigurationid" title="StorageConfigurationId">StorageConfigurationId</a>" : <i>String</i>,
        "<a href="#storagecustomermanagedkeyid" title="StorageCustomerManagedKeyId">StorageCustomerManagedKeyId</a>" : <i>String</i>,
        "<a href="#workspaceid" title="WorkspaceId">WorkspaceId</a>" : <i>Double</i>,
        "<a href="#workspacename" title="WorkspaceName">WorkspaceName</a>" : <i>String</i>,
        "<a href="#workspacestatus" title="WorkspaceStatus">WorkspaceStatus</a>" : <i>String</i>,
        "<a href="#workspacestatusmessage" title="WorkspaceStatusMessage">WorkspaceStatusMessage</a>" : <i>String</i>,
        "<a href="#workspaceurl" title="WorkspaceUrl">WorkspaceUrl</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Databricks::MwsWorkspaces
Properties:
    <a href="#accountid" title="AccountId">AccountId</a>: <i>String</i>
    <a href="#awsregion" title="AwsRegion">AwsRegion</a>: <i>String</i>
    <a href="#creationtime" title="CreationTime">CreationTime</a>: <i>Double</i>
    <a href="#credentialsid" title="CredentialsId">CredentialsId</a>: <i>String</i>
    <a href="#customermanagedkeyid" title="CustomerManagedKeyId">CustomerManagedKeyId</a>: <i>String</i>
    <a href="#deploymentname" title="DeploymentName">DeploymentName</a>: <i>String</i>
    <a href="#isnopublicipenabled" title="IsNoPublicIpEnabled">IsNoPublicIpEnabled</a>: <i>Boolean</i>
    <a href="#managedservicescustomermanagedkeyid" title="ManagedServicesCustomerManagedKeyId">ManagedServicesCustomerManagedKeyId</a>: <i>String</i>
    <a href="#networkid" title="NetworkId">NetworkId</a>: <i>String</i>
    <a href="#pricingtier" title="PricingTier">PricingTier</a>: <i>String</i>
    <a href="#privateaccesssettingsid" title="PrivateAccessSettingsId">PrivateAccessSettingsId</a>: <i>String</i>
    <a href="#storageconfigurationid" title="StorageConfigurationId">StorageConfigurationId</a>: <i>String</i>
    <a href="#storagecustomermanagedkeyid" title="StorageCustomerManagedKeyId">StorageCustomerManagedKeyId</a>: <i>String</i>
    <a href="#workspaceid" title="WorkspaceId">WorkspaceId</a>: <i>Double</i>
    <a href="#workspacename" title="WorkspaceName">WorkspaceName</a>: <i>String</i>
    <a href="#workspacestatus" title="WorkspaceStatus">WorkspaceStatus</a>: <i>String</i>
    <a href="#workspacestatusmessage" title="WorkspaceStatusMessage">WorkspaceStatusMessage</a>: <i>String</i>
    <a href="#workspaceurl" title="WorkspaceUrl">WorkspaceUrl</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AccountId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsRegion

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreationTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CredentialsId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomerManagedKeyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsNoPublicIpEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedServicesCustomerManagedKeyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PricingTier

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateAccessSettingsId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageConfigurationId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageCustomerManagedKeyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkspaceId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkspaceName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkspaceStatus

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkspaceStatusMessage

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkspaceUrl

_Required_: No

_Type_: String

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

