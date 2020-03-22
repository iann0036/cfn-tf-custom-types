# Terraform::AzureStack::StorageAccount

Manages an Azure Storage Account.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureStack::StorageAccount",
    "Properties" : {
        "<a href="#accountencryptionsource" title="AccountEncryptionSource">AccountEncryptionSource</a>" : <i>String</i>,
        "<a href="#accountkind" title="AccountKind">AccountKind</a>" : <i>String</i>,
        "<a href="#accountreplicationtype" title="AccountReplicationType">AccountReplicationType</a>" : <i>String</i>,
        "<a href="#accounttier" title="AccountTier">AccountTier</a>" : <i>String</i>,
        "<a href="#accounttype" title="AccountType">AccountType</a>" : <i>String</i>,
        "<a href="#enableblobencryption" title="EnableBlobEncryption">EnableBlobEncryption</a>" : <i>Boolean</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#customdomain" title="CustomDomain">CustomDomain</a>" : <i>[ <a href="customdomain.md">CustomDomain</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureStack::StorageAccount
Properties:
    <a href="#accountencryptionsource" title="AccountEncryptionSource">AccountEncryptionSource</a>: <i>String</i>
    <a href="#accountkind" title="AccountKind">AccountKind</a>: <i>String</i>
    <a href="#accountreplicationtype" title="AccountReplicationType">AccountReplicationType</a>: <i>String</i>
    <a href="#accounttier" title="AccountTier">AccountTier</a>: <i>String</i>
    <a href="#accounttype" title="AccountType">AccountType</a>: <i>String</i>
    <a href="#enableblobencryption" title="EnableBlobEncryption">EnableBlobEncryption</a>: <i>Boolean</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#customdomain" title="CustomDomain">CustomDomain</a>: <i>
      - <a href="customdomain.md">CustomDomain</a></i>
</pre>

## Properties

#### AccountEncryptionSource

The Encryption Source for this Storage Account. Possible values are `Microsoft.Keyvault` and `Microsoft.Storage`. Defaults to `Microsoft.Storage`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountKind

Defines the Kind of account. Valid option is `Storage`.
. Changing this forces a new resource to be created.
Defaults to `Storage` currently as per [Azure Stack Storage Differences](https://docs.microsoft.com/en-us/azure/azure-stack/user/azure-stack-acs-differences).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountReplicationType

Defines the type of replication to use for this storage account. Valid option is `LRS` currently as per [Azure Stack Storage Differences](https://docs.microsoft.com/en-us/azure/azure-stack/user/azure-stack-acs-differences).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountTier

Defines the Tier to use for this storage account. Valid options are `Standard` and `Premium`. Changing this forces a new resource to be created - **`Can be provisioned, but no performance limit or guarantee.`**.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableBlobEncryption

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

Specifies the supported Azure location where the
resource exists. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the storage account. Changing this forces a
new resource to be created. This must be unique across the entire Azure service,
not just within the resource group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to
create the storage account. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomDomain

_Required_: No

_Type_: List of <a href="customdomain.md">CustomDomain</a>

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

#### PrimaryConnectionString

Returns the <code>PrimaryConnectionString</code> value.

#### PrimaryFileEndpoint

Returns the <code>PrimaryFileEndpoint</code> value.

#### PrimaryLocation

Returns the <code>PrimaryLocation</code> value.

#### PrimaryQueueEndpoint

Returns the <code>PrimaryQueueEndpoint</code> value.

#### PrimaryTableEndpoint

Returns the <code>PrimaryTableEndpoint</code> value.

#### SecondaryAccessKey

Returns the <code>SecondaryAccessKey</code> value.

#### SecondaryBlobConnectionString

Returns the <code>SecondaryBlobConnectionString</code> value.

#### SecondaryBlobEndpoint

Returns the <code>SecondaryBlobEndpoint</code> value.

#### SecondaryConnectionString

Returns the <code>SecondaryConnectionString</code> value.

#### SecondaryLocation

Returns the <code>SecondaryLocation</code> value.

#### SecondaryQueueEndpoint

Returns the <code>SecondaryQueueEndpoint</code> value.

#### SecondaryTableEndpoint

Returns the <code>SecondaryTableEndpoint</code> value.

