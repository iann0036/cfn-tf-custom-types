# TF::AzureRM::DataFactoryLinkedServiceAzureSqlDatabase KeyVaultPasswordDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#linkedservicename" title="LinkedServiceName">LinkedServiceName</a>" : <i>String</i>,
    "<a href="#secretname" title="SecretName">SecretName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#linkedservicename" title="LinkedServiceName">LinkedServiceName</a>: <i>String</i>
<a href="#secretname" title="SecretName">SecretName</a>: <i>String</i>
</pre>

## Properties

#### LinkedServiceName

Specifies the name of an existing Key Vault Data Factory Linked Service.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretName

Specifies the secret name in Azure Key Vault that stores SQL Server password.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

