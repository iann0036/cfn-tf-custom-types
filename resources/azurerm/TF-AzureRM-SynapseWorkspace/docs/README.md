# TF::AzureRM::SynapseWorkspace

Manages a Synapse Workspace.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::SynapseWorkspace",
    "Properties" : {
        "<a href="#aadadmin" title="AadAdmin">AadAdmin</a>" : <i>[ <a href="aadadmindefinition.md">AadAdminDefinition</a>, ... ]</i>,
        "<a href="#customermanagedkeyversionlessid" title="CustomerManagedKeyVersionlessId">CustomerManagedKeyVersionlessId</a>" : <i>String</i>,
        "<a href="#dataexfiltrationprotectionenabled" title="DataExfiltrationProtectionEnabled">DataExfiltrationProtectionEnabled</a>" : <i>Boolean</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#managedresourcegroupname" title="ManagedResourceGroupName">ManagedResourceGroupName</a>" : <i>String</i>,
        "<a href="#managedvirtualnetworkenabled" title="ManagedVirtualNetworkEnabled">ManagedVirtualNetworkEnabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#sqladministratorlogin" title="SqlAdministratorLogin">SqlAdministratorLogin</a>" : <i>String</i>,
        "<a href="#sqladministratorloginpassword" title="SqlAdministratorLoginPassword">SqlAdministratorLoginPassword</a>" : <i>String</i>,
        "<a href="#sqlidentitycontrolenabled" title="SqlIdentityControlEnabled">SqlIdentityControlEnabled</a>" : <i>Boolean</i>,
        "<a href="#storagedatalakegen2filesystemid" title="StorageDataLakeGen2FilesystemId">StorageDataLakeGen2FilesystemId</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#azuredevopsrepo" title="AzureDevopsRepo">AzureDevopsRepo</a>" : <i>[ <a href="azuredevopsrepodefinition.md">AzureDevopsRepoDefinition</a>, ... ]</i>,
        "<a href="#githubrepo" title="GithubRepo">GithubRepo</a>" : <i>[ <a href="githubrepodefinition.md">GithubRepoDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::SynapseWorkspace
Properties:
    <a href="#aadadmin" title="AadAdmin">AadAdmin</a>: <i>
      - <a href="aadadmindefinition.md">AadAdminDefinition</a></i>
    <a href="#customermanagedkeyversionlessid" title="CustomerManagedKeyVersionlessId">CustomerManagedKeyVersionlessId</a>: <i>String</i>
    <a href="#dataexfiltrationprotectionenabled" title="DataExfiltrationProtectionEnabled">DataExfiltrationProtectionEnabled</a>: <i>Boolean</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#managedresourcegroupname" title="ManagedResourceGroupName">ManagedResourceGroupName</a>: <i>String</i>
    <a href="#managedvirtualnetworkenabled" title="ManagedVirtualNetworkEnabled">ManagedVirtualNetworkEnabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#sqladministratorlogin" title="SqlAdministratorLogin">SqlAdministratorLogin</a>: <i>String</i>
    <a href="#sqladministratorloginpassword" title="SqlAdministratorLoginPassword">SqlAdministratorLoginPassword</a>: <i>String</i>
    <a href="#sqlidentitycontrolenabled" title="SqlIdentityControlEnabled">SqlIdentityControlEnabled</a>: <i>Boolean</i>
    <a href="#storagedatalakegen2filesystemid" title="StorageDataLakeGen2FilesystemId">StorageDataLakeGen2FilesystemId</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#azuredevopsrepo" title="AzureDevopsRepo">AzureDevopsRepo</a>: <i>
      - <a href="azuredevopsrepodefinition.md">AzureDevopsRepoDefinition</a></i>
    <a href="#githubrepo" title="GithubRepo">GithubRepo</a>: <i>
      - <a href="githubrepodefinition.md">GithubRepoDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AadAdmin

_Required_: No

_Type_: List of <a href="aadadmindefinition.md">AadAdminDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomerManagedKeyVersionlessId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataExfiltrationProtectionEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedResourceGroupName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedVirtualNetworkEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SqlAdministratorLogin

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SqlAdministratorLoginPassword

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SqlIdentityControlEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageDataLakeGen2FilesystemId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureDevopsRepo

_Required_: No

_Type_: List of <a href="azuredevopsrepodefinition.md">AzureDevopsRepoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GithubRepo

_Required_: No

_Type_: List of <a href="githubrepodefinition.md">GithubRepoDefinition</a>

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

#### ConnectivityEndpoints

Returns the <code>ConnectivityEndpoints</code> value.

#### Id

Returns the <code>Id</code> value.

#### Identity

Returns the <code>Identity</code> value.

