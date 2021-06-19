# TF::AzureRM::MssqlVirtualMachine KeyVaultCredentialDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#keyvaulturl" title="KeyVaultUrl">KeyVaultUrl</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#serviceprincipalname" title="ServicePrincipalName">ServicePrincipalName</a>" : <i>String</i>,
    "<a href="#serviceprincipalsecret" title="ServicePrincipalSecret">ServicePrincipalSecret</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#keyvaulturl" title="KeyVaultUrl">KeyVaultUrl</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#serviceprincipalname" title="ServicePrincipalName">ServicePrincipalName</a>: <i>String</i>
<a href="#serviceprincipalsecret" title="ServicePrincipalSecret">ServicePrincipalSecret</a>: <i>String</i>
</pre>

## Properties

#### KeyVaultUrl

The azure Key Vault url. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The credential name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServicePrincipalName

The service principal name to access key vault. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServicePrincipalSecret

The service principal name secret to access key vault. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

