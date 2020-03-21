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

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountAccessKey

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountAccessKeyIsSecondary

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageEndpoint

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

