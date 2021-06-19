# TF::AzureRM::DataFactoryLinkedServiceAzureSqlDatabase

Manages a Linked Service (connection) between Azure SQL Database and Azure Data Factory.

~> **Note:** All arguments including the connection_string will be stored in the raw state as plain-text. [Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::DataFactoryLinkedServiceAzureSqlDatabase",
    "Properties" : {
        "<a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>" : <i>[ <a href="additionalpropertiesdefinition.md">AdditionalPropertiesDefinition</a>, ... ]</i>,
        "<a href="#annotations" title="Annotations">Annotations</a>" : <i>[ String, ... ]</i>,
        "<a href="#connectionstring" title="ConnectionString">ConnectionString</a>" : <i>String</i>,
        "<a href="#datafactoryname" title="DataFactoryName">DataFactoryName</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#integrationruntimename" title="IntegrationRuntimeName">IntegrationRuntimeName</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#parameters" title="Parameters">Parameters</a>" : <i>[ <a href="parametersdefinition.md">ParametersDefinition</a>, ... ]</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#serviceprincipalid" title="ServicePrincipalId">ServicePrincipalId</a>" : <i>String</i>,
        "<a href="#serviceprincipalkey" title="ServicePrincipalKey">ServicePrincipalKey</a>" : <i>String</i>,
        "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>,
        "<a href="#usemanagedidentity" title="UseManagedIdentity">UseManagedIdentity</a>" : <i>Boolean</i>,
        "<a href="#keyvaultconnectionstring" title="KeyVaultConnectionString">KeyVaultConnectionString</a>" : <i>[ <a href="keyvaultconnectionstringdefinition.md">KeyVaultConnectionStringDefinition</a>, ... ]</i>,
        "<a href="#keyvaultpassword" title="KeyVaultPassword">KeyVaultPassword</a>" : <i>[ <a href="keyvaultpassworddefinition.md">KeyVaultPasswordDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::DataFactoryLinkedServiceAzureSqlDatabase
Properties:
    <a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>: <i>
      - <a href="additionalpropertiesdefinition.md">AdditionalPropertiesDefinition</a></i>
    <a href="#annotations" title="Annotations">Annotations</a>: <i>
      - String</i>
    <a href="#connectionstring" title="ConnectionString">ConnectionString</a>: <i>String</i>
    <a href="#datafactoryname" title="DataFactoryName">DataFactoryName</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#integrationruntimename" title="IntegrationRuntimeName">IntegrationRuntimeName</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#parameters" title="Parameters">Parameters</a>: <i>
      - <a href="parametersdefinition.md">ParametersDefinition</a></i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#serviceprincipalid" title="ServicePrincipalId">ServicePrincipalId</a>: <i>String</i>
    <a href="#serviceprincipalkey" title="ServicePrincipalKey">ServicePrincipalKey</a>: <i>String</i>
    <a href="#tenantid" title="TenantId">TenantId</a>: <i>String</i>
    <a href="#usemanagedidentity" title="UseManagedIdentity">UseManagedIdentity</a>: <i>Boolean</i>
    <a href="#keyvaultconnectionstring" title="KeyVaultConnectionString">KeyVaultConnectionString</a>: <i>
      - <a href="keyvaultconnectionstringdefinition.md">KeyVaultConnectionStringDefinition</a></i>
    <a href="#keyvaultpassword" title="KeyVaultPassword">KeyVaultPassword</a>: <i>
      - <a href="keyvaultpassworddefinition.md">KeyVaultPasswordDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AdditionalProperties

A map of additional properties to associate with the Data Factory Linked Service Azure SQL Database.

_Required_: No

_Type_: List of <a href="additionalpropertiesdefinition.md">AdditionalPropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Annotations

List of tags that can be used for describing the Data Factory Linked Service Azure SQL Database.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionString

The connection string in which to authenticate with Azure SQL Database. Exactly one of either `connection_string` or `key_vault_connection_string` is required.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataFactoryName

The Data Factory name in which to associate the Linked Service with. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description for the Data Factory Linked Service Azure SQL Database.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationRuntimeName

The integration runtime reference to associate with the Data Factory Linked Service Azure SQL Database.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the Data Factory Linked Service Azure SQL Database. Changing this forces a new resource to be created. Must be unique within a data
factory. See the [Microsoft documentation](https://docs.microsoft.com/en-us/azure/data-factory/naming-rules) for all restrictions.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameters

A map of parameters to associate with the Data Factory Linked Service Azure SQL Database.

_Required_: No

_Type_: List of <a href="parametersdefinition.md">ParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to create the Data Factory Linked Service Azure SQL Database. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServicePrincipalId

The service principal id in which to authenticate against the Azure SQL Database. Required if `service_principal_key` is set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServicePrincipalKey

The service principal key in which to authenticate against the Azure SQL Database. Required if `service_principal_id` is set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

The tenant id or name in which to authenticate against the Azure SQL Database.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseManagedIdentity

Whether to use the Data Factory's managed identity to authenticate against the Azure SQL Database. Incompatible with `service_principal_id` and `service_principal_key`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyVaultConnectionString

_Required_: No

_Type_: List of <a href="keyvaultconnectionstringdefinition.md">KeyVaultConnectionStringDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyVaultPassword

_Required_: No

_Type_: List of <a href="keyvaultpassworddefinition.md">KeyVaultPasswordDefinition</a>

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

