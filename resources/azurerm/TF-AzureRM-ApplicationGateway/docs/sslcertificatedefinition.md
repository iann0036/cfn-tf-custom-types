# TF::AzureRM::ApplicationGateway SslCertificateDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#data" title="Data">Data</a>" : <i>String</i>,
    "<a href="#keyvaultsecretid" title="KeyVaultSecretId">KeyVaultSecretId</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#password" title="Password">Password</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#data" title="Data">Data</a>: <i>String</i>
<a href="#keyvaultsecretid" title="KeyVaultSecretId">KeyVaultSecretId</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#password" title="Password">Password</a>: <i>String</i>
</pre>

## Properties

#### Data

PFX certificate. Required if `key_vault_secret_id` is not set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyVaultSecretId

Secret Id of (base-64 encoded unencrypted pfx) `Secret` or `Certificate` object stored in Azure KeyVault. You need to enable soft delete for keyvault to use this feature. Required if `data` is not set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The Name of the SSL certificate that is unique within this Application Gateway.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Password for the pfx file specified in data.  Required if `data` is set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

