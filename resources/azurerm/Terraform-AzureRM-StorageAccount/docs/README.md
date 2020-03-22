# Terraform::AzureRM::StorageAccount

Manages network rules inside of a Azure Storage Account.

~> **NOTE:** Network Rules can be defined either directly on the `azurerm_storage_account` resource, or using the `azurerm_storage_account_network_rules` resource - but the two cannot be used together. Spurious changes will occur if both are used against the same Storage Account.

~> **NOTE:** Only one `azurerm_storage_account_network_rules` can be tied to an `azurerm_storage_account`. Spurious changes will occur if more than `azurerm_storage_account_network_rules` is tied to the same `azurerm_storage_account`.

~> **NOTE:** Deleting this resource updates the storage account back to the default values it had when the storage account was created.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::StorageAccount",
    "Properties" : {
        "<a href="#accesstier" title="AccessTier">AccessTier</a>" : <i>String</i>,
        "<a href="#accountkind" title="AccountKind">AccountKind</a>" : <i>String</i>,
        "<a href="#accountreplicationtype" title="AccountReplicationType">AccountReplicationType</a>" : <i>String</i>,
        "<a href="#accounttier" title="AccountTier">AccountTier</a>" : <i>String</i>,
        "<a href="#enablehttpstrafficonly" title="EnableHttpsTrafficOnly">EnableHttpsTrafficOnly</a>" : <i>Boolean</i>,
        "<a href="#ishnsenabled" title="IsHnsEnabled">IsHnsEnabled</a>" : <i>Boolean</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#blobproperties" title="BlobProperties">BlobProperties</a>" : <i>[ <a href="blobproperties.md">BlobProperties</a>, ... ]</i>,
        "<a href="#customdomain" title="CustomDomain">CustomDomain</a>" : <i>[ <a href="customdomain.md">CustomDomain</a>, ... ]</i>,
        "<a href="#identity" title="Identity">Identity</a>" : <i>[ <a href="identity.md">Identity</a>, ... ]</i>,
        "<a href="#networkrules" title="NetworkRules">NetworkRules</a>" : <i>[ <a href="networkrules.md">NetworkRules</a>, ... ]</i>,
        "<a href="#queueproperties" title="QueueProperties">QueueProperties</a>" : <i>[ <a href="queueproperties.md">QueueProperties</a>, ... ]</i>,
        "<a href="#staticwebsite" title="StaticWebsite">StaticWebsite</a>" : <i>[ <a href="staticwebsite.md">StaticWebsite</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#corsrule" title="CorsRule">CorsRule</a>" : <i>[ <a href="corsrule.md">CorsRule</a>, ... ]</i>,
        "<a href="#deleteretentionpolicy" title="DeleteRetentionPolicy">DeleteRetentionPolicy</a>" : <i>[ <a href="deleteretentionpolicy.md">DeleteRetentionPolicy</a>, ... ]</i>,
        "<a href="#hourmetrics" title="HourMetrics">HourMetrics</a>" : <i>[ <a href="hourmetrics.md">HourMetrics</a>, ... ]</i>,
        "<a href="#logging" title="Logging">Logging</a>" : <i>[ <a href="logging.md">Logging</a>, ... ]</i>,
        "<a href="#minutemetrics" title="MinuteMetrics">MinuteMetrics</a>" : <i>[ <a href="minutemetrics.md">MinuteMetrics</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::StorageAccount
Properties:
    <a href="#accesstier" title="AccessTier">AccessTier</a>: <i>String</i>
    <a href="#accountkind" title="AccountKind">AccountKind</a>: <i>String</i>
    <a href="#accountreplicationtype" title="AccountReplicationType">AccountReplicationType</a>: <i>String</i>
    <a href="#accounttier" title="AccountTier">AccountTier</a>: <i>String</i>
    <a href="#enablehttpstrafficonly" title="EnableHttpsTrafficOnly">EnableHttpsTrafficOnly</a>: <i>Boolean</i>
    <a href="#ishnsenabled" title="IsHnsEnabled">IsHnsEnabled</a>: <i>Boolean</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#blobproperties" title="BlobProperties">BlobProperties</a>: <i>
      - <a href="blobproperties.md">BlobProperties</a></i>
    <a href="#customdomain" title="CustomDomain">CustomDomain</a>: <i>
      - <a href="customdomain.md">CustomDomain</a></i>
    <a href="#identity" title="Identity">Identity</a>: <i>
      - <a href="identity.md">Identity</a></i>
    <a href="#networkrules" title="NetworkRules">NetworkRules</a>: <i>
      - <a href="networkrules.md">NetworkRules</a></i>
    <a href="#queueproperties" title="QueueProperties">QueueProperties</a>: <i>
      - <a href="queueproperties.md">QueueProperties</a></i>
    <a href="#staticwebsite" title="StaticWebsite">StaticWebsite</a>: <i>
      - <a href="staticwebsite.md">StaticWebsite</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#corsrule" title="CorsRule">CorsRule</a>: <i>
      - <a href="corsrule.md">CorsRule</a></i>
    <a href="#deleteretentionpolicy" title="DeleteRetentionPolicy">DeleteRetentionPolicy</a>: <i>
      - <a href="deleteretentionpolicy.md">DeleteRetentionPolicy</a></i>
    <a href="#hourmetrics" title="HourMetrics">HourMetrics</a>: <i>
      - <a href="hourmetrics.md">HourMetrics</a></i>
    <a href="#logging" title="Logging">Logging</a>: <i>
      - <a href="logging.md">Logging</a></i>
    <a href="#minutemetrics" title="MinuteMetrics">MinuteMetrics</a>: <i>
      - <a href="minutemetrics.md">MinuteMetrics</a></i>
</pre>

## Properties

#### AccessTier

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountKind

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountReplicationType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountTier

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableHttpsTrafficOnly

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsHnsEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to create the storage account. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlobProperties

_Required_: No

_Type_: List of <a href="blobproperties.md">BlobProperties</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomDomain

_Required_: No

_Type_: List of <a href="customdomain.md">CustomDomain</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identity

_Required_: No

_Type_: List of <a href="identity.md">Identity</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkRules

_Required_: No

_Type_: List of <a href="networkrules.md">NetworkRules</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueueProperties

_Required_: No

_Type_: List of <a href="queueproperties.md">QueueProperties</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticWebsite

_Required_: No

_Type_: List of <a href="staticwebsite.md">StaticWebsite</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CorsRule

_Required_: No

_Type_: List of <a href="corsrule.md">CorsRule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteRetentionPolicy

_Required_: No

_Type_: List of <a href="deleteretentionpolicy.md">DeleteRetentionPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HourMetrics

_Required_: No

_Type_: List of <a href="hourmetrics.md">HourMetrics</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logging

_Required_: No

_Type_: List of <a href="logging.md">Logging</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinuteMetrics

_Required_: No

_Type_: List of <a href="minutemetrics.md">MinuteMetrics</a>

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

