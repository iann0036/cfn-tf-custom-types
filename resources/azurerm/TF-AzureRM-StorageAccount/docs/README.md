# TF::AzureRM::StorageAccount

Manages an Azure Storage Account.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::StorageAccount",
    "Properties" : {
        "<a href="#accesstier" title="AccessTier">AccessTier</a>" : <i>String</i>,
        "<a href="#accountkind" title="AccountKind">AccountKind</a>" : <i>String</i>,
        "<a href="#accountreplicationtype" title="AccountReplicationType">AccountReplicationType</a>" : <i>String</i>,
        "<a href="#accounttier" title="AccountTier">AccountTier</a>" : <i>String</i>,
        "<a href="#allowblobpublicaccess" title="AllowBlobPublicAccess">AllowBlobPublicAccess</a>" : <i>Boolean</i>,
        "<a href="#enablehttpstrafficonly" title="EnableHttpsTrafficOnly">EnableHttpsTrafficOnly</a>" : <i>Boolean</i>,
        "<a href="#ishnsenabled" title="IsHnsEnabled">IsHnsEnabled</a>" : <i>Boolean</i>,
        "<a href="#largefileshareenabled" title="LargeFileShareEnabled">LargeFileShareEnabled</a>" : <i>Boolean</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#mintlsversion" title="MinTlsVersion">MinTlsVersion</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nfsv3enabled" title="Nfsv3Enabled">Nfsv3Enabled</a>" : <i>Boolean</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#azurefilesauthentication" title="AzureFilesAuthentication">AzureFilesAuthentication</a>" : <i>[ <a href="azurefilesauthenticationdefinition.md">AzureFilesAuthenticationDefinition</a>, ... ]</i>,
        "<a href="#blobproperties" title="BlobProperties">BlobProperties</a>" : <i>[ <a href="blobpropertiesdefinition.md">BlobPropertiesDefinition</a>, ... ]</i>,
        "<a href="#customdomain" title="CustomDomain">CustomDomain</a>" : <i>[ <a href="customdomaindefinition.md">CustomDomainDefinition</a>, ... ]</i>,
        "<a href="#identity" title="Identity">Identity</a>" : <i>[ <a href="identitydefinition.md">IdentityDefinition</a>, ... ]</i>,
        "<a href="#networkrules" title="NetworkRules">NetworkRules</a>" : <i>[ <a href="networkrulesdefinition.md">NetworkRulesDefinition</a>, ... ]</i>,
        "<a href="#queueproperties" title="QueueProperties">QueueProperties</a>" : <i>[ <a href="queuepropertiesdefinition.md">QueuePropertiesDefinition</a>, ... ]</i>,
        "<a href="#routing" title="Routing">Routing</a>" : <i>[ <a href="routingdefinition.md">RoutingDefinition</a>, ... ]</i>,
        "<a href="#shareproperties" title="ShareProperties">ShareProperties</a>" : <i>[ <a href="sharepropertiesdefinition.md">SharePropertiesDefinition</a>, ... ]</i>,
        "<a href="#staticwebsite" title="StaticWebsite">StaticWebsite</a>" : <i>[ <a href="staticwebsitedefinition.md">StaticWebsiteDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::StorageAccount
Properties:
    <a href="#accesstier" title="AccessTier">AccessTier</a>: <i>String</i>
    <a href="#accountkind" title="AccountKind">AccountKind</a>: <i>String</i>
    <a href="#accountreplicationtype" title="AccountReplicationType">AccountReplicationType</a>: <i>String</i>
    <a href="#accounttier" title="AccountTier">AccountTier</a>: <i>String</i>
    <a href="#allowblobpublicaccess" title="AllowBlobPublicAccess">AllowBlobPublicAccess</a>: <i>Boolean</i>
    <a href="#enablehttpstrafficonly" title="EnableHttpsTrafficOnly">EnableHttpsTrafficOnly</a>: <i>Boolean</i>
    <a href="#ishnsenabled" title="IsHnsEnabled">IsHnsEnabled</a>: <i>Boolean</i>
    <a href="#largefileshareenabled" title="LargeFileShareEnabled">LargeFileShareEnabled</a>: <i>Boolean</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#mintlsversion" title="MinTlsVersion">MinTlsVersion</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nfsv3enabled" title="Nfsv3Enabled">Nfsv3Enabled</a>: <i>Boolean</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#azurefilesauthentication" title="AzureFilesAuthentication">AzureFilesAuthentication</a>: <i>
      - <a href="azurefilesauthenticationdefinition.md">AzureFilesAuthenticationDefinition</a></i>
    <a href="#blobproperties" title="BlobProperties">BlobProperties</a>: <i>
      - <a href="blobpropertiesdefinition.md">BlobPropertiesDefinition</a></i>
    <a href="#customdomain" title="CustomDomain">CustomDomain</a>: <i>
      - <a href="customdomaindefinition.md">CustomDomainDefinition</a></i>
    <a href="#identity" title="Identity">Identity</a>: <i>
      - <a href="identitydefinition.md">IdentityDefinition</a></i>
    <a href="#networkrules" title="NetworkRules">NetworkRules</a>: <i>
      - <a href="networkrulesdefinition.md">NetworkRulesDefinition</a></i>
    <a href="#queueproperties" title="QueueProperties">QueueProperties</a>: <i>
      - <a href="queuepropertiesdefinition.md">QueuePropertiesDefinition</a></i>
    <a href="#routing" title="Routing">Routing</a>: <i>
      - <a href="routingdefinition.md">RoutingDefinition</a></i>
    <a href="#shareproperties" title="ShareProperties">ShareProperties</a>: <i>
      - <a href="sharepropertiesdefinition.md">SharePropertiesDefinition</a></i>
    <a href="#staticwebsite" title="StaticWebsite">StaticWebsite</a>: <i>
      - <a href="staticwebsitedefinition.md">StaticWebsiteDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AccessTier

Defines the access tier for `BlobStorage`, `FileStorage` and `StorageV2` accounts. Valid options are `Hot` and `Cool`, defaults to `Hot`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountKind

Defines the Kind of account. Valid options are `BlobStorage`, `BlockBlobStorage`, `FileStorage`, `Storage` and `StorageV2`. Changing this forces a new resource to be created. Defaults to `StorageV2`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountReplicationType

Defines the type of replication to use for this storage account. Valid options are `LRS`, `GRS`, `RAGRS`, `ZRS`, `GZRS` and `RAGZRS`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountTier

Defines the Tier to use for this storage account. Valid options are `Standard` and `Premium`. For `BlockBlobStorage` and `FileStorage` accounts only `Premium` is valid. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowBlobPublicAccess

Allow or disallow public access to all blobs or containers in the storage account. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableHttpsTrafficOnly

Boolean flag which forces HTTPS if enabled, see [here](https://docs.microsoft.com/en-us/azure/storage/storage-require-secure-transfer/)
for more information. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsHnsEnabled

Is Hierarchical Namespace enabled? This can be used with Azure Data Lake Storage Gen 2 ([see here for more information](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-quickstart-create-account/)). Changing this forces a new resource to be created.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LargeFileShareEnabled

Is Large File Share Enabled?.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinTlsVersion

The minimum supported TLS version for the storage account. Possible values are `TLS1_0`, `TLS1_1`, and `TLS1_2`. Defaults to `TLS1_0` for new storage accounts.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the storage account. Changing this forces a new resource to be created. This must be unique across the entire Azure service, not just within the resource group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nfsv3Enabled

Is NFSv3 protocol enabled? Changing this forces a new resource to be created. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to create the storage account. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureFilesAuthentication

_Required_: No

_Type_: List of <a href="azurefilesauthenticationdefinition.md">AzureFilesAuthenticationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlobProperties

_Required_: No

_Type_: List of <a href="blobpropertiesdefinition.md">BlobPropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomDomain

_Required_: No

_Type_: List of <a href="customdomaindefinition.md">CustomDomainDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identity

_Required_: No

_Type_: List of <a href="identitydefinition.md">IdentityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkRules

_Required_: No

_Type_: List of <a href="networkrulesdefinition.md">NetworkRulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueueProperties

_Required_: No

_Type_: List of <a href="queuepropertiesdefinition.md">QueuePropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Routing

_Required_: No

_Type_: List of <a href="routingdefinition.md">RoutingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShareProperties

_Required_: No

_Type_: List of <a href="sharepropertiesdefinition.md">SharePropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticWebsite

_Required_: No

_Type_: List of <a href="staticwebsitedefinition.md">StaticWebsiteDefinition</a>

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

#### PrimaryAccessKey

Returns the <code>PrimaryAccessKey</code> value.

#### PrimaryBlobConnectionString

Returns the <code>PrimaryBlobConnectionString</code> value.

#### PrimaryBlobEndpoint

Returns the <code>PrimaryBlobEndpoint</code> value.

#### PrimaryBlobHost

Returns the <code>PrimaryBlobHost</code> value.

#### PrimaryConnectionString

Returns the <code>PrimaryConnectionString</code> value.

#### PrimaryDfsEndpoint

Returns the <code>PrimaryDfsEndpoint</code> value.

#### PrimaryDfsHost

Returns the <code>PrimaryDfsHost</code> value.

#### PrimaryFileEndpoint

Returns the <code>PrimaryFileEndpoint</code> value.

#### PrimaryFileHost

Returns the <code>PrimaryFileHost</code> value.

#### PrimaryLocation

Returns the <code>PrimaryLocation</code> value.

#### PrimaryQueueEndpoint

Returns the <code>PrimaryQueueEndpoint</code> value.

#### PrimaryQueueHost

Returns the <code>PrimaryQueueHost</code> value.

#### PrimaryTableEndpoint

Returns the <code>PrimaryTableEndpoint</code> value.

#### PrimaryTableHost

Returns the <code>PrimaryTableHost</code> value.

#### PrimaryWebEndpoint

Returns the <code>PrimaryWebEndpoint</code> value.

#### PrimaryWebHost

Returns the <code>PrimaryWebHost</code> value.

#### SecondaryAccessKey

Returns the <code>SecondaryAccessKey</code> value.

#### SecondaryBlobConnectionString

Returns the <code>SecondaryBlobConnectionString</code> value.

#### SecondaryBlobEndpoint

Returns the <code>SecondaryBlobEndpoint</code> value.

#### SecondaryBlobHost

Returns the <code>SecondaryBlobHost</code> value.

#### SecondaryConnectionString

Returns the <code>SecondaryConnectionString</code> value.

#### SecondaryDfsEndpoint

Returns the <code>SecondaryDfsEndpoint</code> value.

#### SecondaryDfsHost

Returns the <code>SecondaryDfsHost</code> value.

#### SecondaryFileEndpoint

Returns the <code>SecondaryFileEndpoint</code> value.

#### SecondaryFileHost

Returns the <code>SecondaryFileHost</code> value.

#### SecondaryLocation

Returns the <code>SecondaryLocation</code> value.

#### SecondaryQueueEndpoint

Returns the <code>SecondaryQueueEndpoint</code> value.

#### SecondaryQueueHost

Returns the <code>SecondaryQueueHost</code> value.

#### SecondaryTableEndpoint

Returns the <code>SecondaryTableEndpoint</code> value.

#### SecondaryTableHost

Returns the <code>SecondaryTableHost</code> value.

#### SecondaryWebEndpoint

Returns the <code>SecondaryWebEndpoint</code> value.

#### SecondaryWebHost

Returns the <code>SecondaryWebHost</code> value.

