# TF::RedisCloud::Subscription

Creates a Subscription within your Redis Enterprise Cloud Account.
This resource is responsible for creating subscriptions and the databases within that subscription. 
This allows Redis Enterprise Cloud to provision your databases in the most efficient way.

~> **Note:** The subscription resource manages changes to its databases by identifying a databases through its name.  This means **database names cannot be changed**, as this resource has no other way of being able to identify the database and would lead to the database to be destroyed.
Due to the limitations mentioned above, the differences shown by Terraform will be different from normal plan.
When an argument has been changed on a nested database - for example changing the `memory_limit_in_gb` from 1 to 2, Terraform
will display the resource as being modified with the database as being removed, and a new one added. As the resource
identifies the database based on the name, the only change that would happen would be to update the database to increas...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::RedisCloud::Subscription",
    "Properties" : {
        "<a href="#memorystorage" title="MemoryStorage">MemoryStorage</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#paymentmethodid" title="PaymentMethodId">PaymentMethodId</a>" : <i>String</i>,
        "<a href="#persistentstorageencryption" title="PersistentStorageEncryption">PersistentStorageEncryption</a>" : <i>Boolean</i>,
        "<a href="#allowlist" title="Allowlist">Allowlist</a>" : <i>[ <a href="allowlistdefinition.md">AllowlistDefinition</a>, ... ]</i>,
        "<a href="#cloudprovider" title="CloudProvider">CloudProvider</a>" : <i>[ <a href="cloudproviderdefinition.md">CloudProviderDefinition</a>, ... ]</i>,
        "<a href="#database" title="Database">Database</a>" : <i>[ <a href="databasedefinition.md">DatabaseDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::RedisCloud::Subscription
Properties:
    <a href="#memorystorage" title="MemoryStorage">MemoryStorage</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#paymentmethodid" title="PaymentMethodId">PaymentMethodId</a>: <i>String</i>
    <a href="#persistentstorageencryption" title="PersistentStorageEncryption">PersistentStorageEncryption</a>: <i>Boolean</i>
    <a href="#allowlist" title="Allowlist">Allowlist</a>: <i>
      - <a href="allowlistdefinition.md">AllowlistDefinition</a></i>
    <a href="#cloudprovider" title="CloudProvider">CloudProvider</a>: <i>
      - <a href="cloudproviderdefinition.md">CloudProviderDefinition</a></i>
    <a href="#database" title="Database">Database</a>: <i>
      - <a href="databasedefinition.md">DatabaseDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### MemoryStorage

Memory storage preference: either ‘ram’ or a combination of 'ram-and-flash’. Default: ‘ram’.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A meaningful name to identify the subscription.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PaymentMethodId

A valid payment method pre-defined in the current account. This value is __Optional__ for AWS/GCP Marketplace accounts, but __Required__ for all other account types.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PersistentStorageEncryption

Encrypt data stored in persistent storage. Required for a GCP subscription. Default: ‘true’.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Allowlist

_Required_: No

_Type_: List of <a href="allowlistdefinition.md">AllowlistDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudProvider

_Required_: No

_Type_: List of <a href="cloudproviderdefinition.md">CloudProviderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Database

_Required_: No

_Type_: List of <a href="databasedefinition.md">DatabaseDefinition</a>

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

