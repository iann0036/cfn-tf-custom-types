# Terraform::AzureRM::KeyVaultAccessPolicy

Manages a Key Vault Access Policy.

~> **NOTE:** It's possible to define Key Vault Access Policies both within [the `azurerm_key_vault` resource](key_vault.html) via the `access_policy` block and by using [the `azurerm_key_vault_access_policy` resource](key_vault_access_policy.html). However it's not possible to use both methods to manage Access Policies within a KeyVault, since there'll be conflicts.

-> **NOTE:** Azure permits a maximum of 1024 Access Policies per Key Vault - [more information can be found in this document](https://docs.microsoft.com/en-us/azure/key-vault/key-vault-secure-your-key-vault#data-plane-access-control).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::KeyVaultAccessPolicy",
    "Properties" : {
        "<a href="#applicationid" title="ApplicationId">ApplicationId</a>" : <i>String</i>,
        "<a href="#certificatepermissions" title="CertificatePermissions">CertificatePermissions</a>" : <i>[ String, ... ]</i>,
        "<a href="#keypermissions" title="KeyPermissions">KeyPermissions</a>" : <i>[ String, ... ]</i>,
        "<a href="#keyvaultid" title="KeyVaultId">KeyVaultId</a>" : <i>String</i>,
        "<a href="#objectid" title="ObjectId">ObjectId</a>" : <i>String</i>,
        "<a href="#secretpermissions" title="SecretPermissions">SecretPermissions</a>" : <i>[ String, ... ]</i>,
        "<a href="#storagepermissions" title="StoragePermissions">StoragePermissions</a>" : <i>[ String, ... ]</i>,
        "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::KeyVaultAccessPolicy
Properties:
    <a href="#applicationid" title="ApplicationId">ApplicationId</a>: <i>String</i>
    <a href="#certificatepermissions" title="CertificatePermissions">CertificatePermissions</a>: <i>
      - String</i>
    <a href="#keypermissions" title="KeyPermissions">KeyPermissions</a>: <i>
      - String</i>
    <a href="#keyvaultid" title="KeyVaultId">KeyVaultId</a>: <i>String</i>
    <a href="#objectid" title="ObjectId">ObjectId</a>: <i>String</i>
    <a href="#secretpermissions" title="SecretPermissions">SecretPermissions</a>: <i>
      - String</i>
    <a href="#storagepermissions" title="StoragePermissions">StoragePermissions</a>: <i>
      - String</i>
    <a href="#tenantid" title="TenantId">TenantId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### ApplicationId

The object ID of an Application in Azure Active Directory.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificatePermissions

List of certificate permissions, must be one or more from
the following: `backup`, `create`, `delete`, `deleteissuers`, `get`, `getissuers`, `import`, `list`, `listissuers`,
`managecontacts`, `manageissuers`, `purge`, `recover`, `restore`, `setissuers` and `update`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyPermissions

List of key permissions, must be one or more from
the following: `backup`, `create`, `decrypt`, `delete`, `encrypt`, `get`, `import`, `list`, `purge`,
`recover`, `restore`, `sign`, `unwrapKey`, `update`, `verify` and `wrapKey`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyVaultId

Specifies the id of the Key Vault resource. Changing this
forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectId

The object ID of a user, service principal or security
group in the Azure Active Directory tenant for the vault. The object ID must
be unique for the list of access policies. Changing this forces a new resource
to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretPermissions

List of secret permissions, must be one or more
from the following: `backup`, `delete`, `get`, `list`, `purge`, `recover`, `restore` and `set`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StoragePermissions

List of storage permissions, must be one or more from the following: `backup`, `delete`, `deletesas`, `get`, `getsas`, `list`, `listsas`, `purge`, `recover`, `regeneratekey`, `restore`, `set`, `setsas` and `update`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

The Azure Active Directory tenant ID that should be used
for authenticating requests to the key vault. Changing this forces a new resource
to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

