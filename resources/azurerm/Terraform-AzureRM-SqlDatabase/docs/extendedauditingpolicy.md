# Terraform::AzureRM::SqlDatabase ExtendedAuditingPolicy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#retentionindays" title="RetentionInDays">RetentionInDays</a>" : <i>Double</i>,
    "<a href="#storageaccountaccesskey" title="StorageAccountAccessKey">StorageAccountAccessKey</a>" : <i>String</i>,
    "<a href="#storageaccountaccesskeyissecondary" title="StorageAccountAccessKeyIsSecondary">StorageAccountAccessKeyIsSecondary</a>" : <i>Boolean</i>,
    "<a href="#storageendpoint" title="StorageEndpoint">StorageEndpoint</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#retentionindays" title="RetentionInDays">RetentionInDays</a>: <i>Double</i>
<a href="#storageaccountaccesskey" title="StorageAccountAccessKey">StorageAccountAccessKey</a>: <i>String</i>
<a href="#storageaccountaccesskeyissecondary" title="StorageAccountAccessKeyIsSecondary">StorageAccountAccessKeyIsSecondary</a>: <i>Boolean</i>
<a href="#storageendpoint" title="StorageEndpoint">StorageEndpoint</a>: <i>String</i>
</pre>

## Properties

#### RetentionInDays

Specifies the number of days to retain logs for in the storage account.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountAccessKey

Specifies the access key to use for the auditing storage account.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountAccessKeyIsSecondary

Specifies whether `storage_account_access_key` value is the storage's secondary key.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageEndpoint

Specifies the blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

